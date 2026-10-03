#!/usr/bin/env python3
"""The `md_rows` adapter: one work from Google-Docs Markdown exports of a
row-aligned corpus (format: ../references/md-export-format.md).

Manifest entry (all paths under raw_root unless noted):

    - key: bo-some-commentary
      path: 1-SOURCES/Commentaries/bo-some-commentary.md
      adapter: md_rows
      id_scheme: h2                      # flat for a text with no TOC
      text: commentary.md                # THIS work's rows = its segmentation
      pair:                              # optional: the human row alignment
        own_side: commentary.md          #   this side of the pair (= text, or a letter-identical copy)
        target_side: root-copy.md        #   the other side: the target text cut the way the aligners cut it
      target: bo-root                    # work key the transclusions point at (built earlier)
      min_overlap: 3                     # letters a row needs inside a target segment to transclude it
      pair_corrections:                  # human-decided re-pairings (never invented)
        - {row: 15, target_side_rows: [14], reason: "…", decided_by: "…", date: "…"}
      text_corrections:                  # human-decided text fixes
        - {row: 83, find: "s", replace: "", reason: "…", decided_by: "…", date: "…"}
      toc:                               # where the headings come from
        kind: tree | labels | none
        tree: 2-RAILS/Sections/Raw/toc-tree/<id>.md     # kind: tree (vault path; toc-generate)
        doc: commentary-toc.md                           # kind: labels
        labels: ["༥༽ …།", …]                             # kind: labels, verbatim, in order
        reason: "…"                                      # kind: none

What it guarantees:
  * Every row with letters becomes exactly one block, in row order. Rows are
    never merged or split; a row without letters is not a block (its raw
    text, if any, is kept in the sidecar).
  * A block transcludes exactly the target segments its paired row's letters
    fall in (concordance.py), after any human pair_correction. A row whose
    counterpart is empty transcludes nothing.
  * Headings sit only between rows. Ids come from the headings (h2 scheme),
    so the TOC is applied before ids and transclusions are written.
"""
import hashlib
import pathlib
import re
import sys

from common import raw_path
from concordance import Concordance
from md_export import read_rows, strip_markup
from project import Projector, is_letter
import vault_writer

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "toc-generate" / "scripts"))
from toc_tree_ingest import parse_toc_line          # noqa: E402

ZW = "​﻿"


def has_letters(text):
    return any(is_letter(c) for c in text)


def letters(text):
    return "".join(c for c in text if is_letter(c))


def _rows(ctx, rel):
    return read_rows(raw_path(ctx.raw, rel))


def _shift_runs(runs, pos, removed, added=0):
    out = []
    for r in runs:
        r = dict(r)
        for k in ("start", "end"):
            if r[k] >= pos + removed:
                r[k] += added - removed
            elif r[k] > pos:
                r[k] = pos + min(r[k] - pos, added)
        if r["end"] > r["start"]:
            out.append(r)
    return out


# --------------------------------------------------------------------------
# rows -> blocks
# --------------------------------------------------------------------------

def _blocks(ctx, spec, rep):
    rel = spec["text"]
    corr = {}
    for c in spec.get("text_corrections") or []:
        corr.setdefault(int(c["row"]), []).append(c)
    items, empty_rows = [], []
    for r in _rows(ctx, rel):
        text, runs = r["text"], [dict(x, layer="emphasis") for x in r["runs"]]
        src = {"file": rel, "row": r["row"]}
        for c in corr.pop(r["row"], []):
            if text.count(c["find"]) != 1:
                raise ValueError(f"{spec['key']}: text correction {c} does not match exactly once in row {r['row']}")
            pos = text.index(c["find"])
            text = text[:pos] + c["replace"] + text[pos + len(c["find"]):]
            runs = _shift_runs(runs, pos, len(c["find"]), len(c["replace"]))
            src.setdefault("corrections", []).append(
                {k: c.get(k) for k in ("find", "replace", "reason", "decided_by", "date") if c.get(k) is not None})
        if runs or "\\" in r["raw"]:
            src["raw"] = r["raw"]
        if not has_letters(text):
            if r["raw"].strip() or src.get("corrections"):
                empty_rows.append(src | {"raw": r["raw"]})
            continue
        item = {"kind": "block", "text": text, "row": r["row"], "source": src}
        if runs:
            item["annotations"] = runs
        items.append(item)
    if corr:
        raise ValueError(f"{spec['key']}: text_corrections name rows that do not exist: {sorted(corr)}")
    rep["rows"] = len(items)
    return items, empty_rows


# --------------------------------------------------------------------------
# the human row pairing -> transclusion targets
# --------------------------------------------------------------------------

def _pair(ctx, spec, items, rep):
    pair = spec["pair"]
    own_rel, tgt_rel = pair.get("own_side", spec["text"]), pair["target_side"]
    if own_rel != spec["text"]:
        own = {r["row"]: letters(r["text"]) for r in _rows(ctx, own_rel)}
        mine = {r["row"]: letters(r["text"]) for r in _rows(ctx, spec["text"])}
        bad = sorted(k for k in set(own) | set(mine) if own.get(k, "") != mine.get(k, ""))
        if bad:
            raise ValueError(f"{spec['key']}: pair.own_side differs from text in rows {bad[:10]}")
    tgt_rows = _rows(ctx, tgt_rel)
    tgt_text = {r["row"]: r["text"] for r in tgt_rows}
    target = ctx.works[spec["target"]]
    conc = Concordance(target["blocks"], [(r["row"], r["text"]) for r in tgt_rows if has_letters(r["text"])],
                       min_overlap=spec.get("min_overlap", 3))
    rep["concordance"] = conc.stats
    corrections = {int(c["row"]): c for c in spec.get("pair_corrections") or []}
    used, multi, unaligned, review = set(), [], [], []
    for it in items:
        k = it["row"]
        human = [k] if has_letters(tgt_text.get(k, "")) else []
        rows = human
        al = {"pair_row": k}
        if k in corrections:
            c = corrections.pop(k)
            rows = [int(x) for x in c.get("target_side_rows") or []]
            al["correction"] = {"human_pairing": human, "corrected_to": rows,
                                **{x: c[x] for x in ("reason", "decided_by", "date") if c.get(x)}}
        targets, detail, variants, dropped, flags = [], {}, [], [], []
        for tr in rows:
            x = conc.row(tr)
            for t in x["targets"]:
                if t not in targets:
                    targets.append(t)
            detail.update(x["detail"])
            variants += x["variants"]
            dropped += x["dropped"]
            flags += [f for f in x["flags"] if f not in flags]
            used.add(tr)
        targets.sort(key=conc.pos.get)
        if "correction" in al:
            al["correction"]["human_targets"] = sorted(
                {t for tr in human for t in conc.row(tr)["targets"]}, key=conc.pos.get)
        if rows:
            al["target_side_text"] = "\n".join(tgt_text[r] for r in rows)
            al["targets"] = detail
            if variants:
                al["variants"] = variants
            if dropped:
                al["dropped_overlaps"] = dropped
                review.append({"row": k, "dropped_overlaps": dropped})
            if flags:
                al["flags"] = flags
            if len(targets) > 1:
                multi.append({"row": k, "targets": targets})
            if rows and not targets:
                review.append({"row": k, "issue": "paired row's letters were not found in the target"})
        else:
            al["unaligned"] = True
            unaligned.append(k)
        it["targets"] = targets
        it["alignment"] = al
    if corrections:
        raise ValueError(f"{spec['key']}: pair_corrections name rows that are not blocks: {sorted(corrections)}")
    orphan = [k for k, t in tgt_text.items() if has_letters(t) and k not in used]
    rep.update({"aligned_blocks": sum(1 for it in items if it["targets"]),
                "unaligned_blocks": unaligned, "blocks_spanning_several_targets": multi,
                "target_side_rows_without_counterpart": orphan, "alignment_review": review})
    return {"target_side_rows_without_counterpart": [{"row": k, "text": tgt_text[k]} for k in orphan],
            "concordance": conc.stats}


# --------------------------------------------------------------------------
# headings
# --------------------------------------------------------------------------

def pretoc_layout(title, items):
    """The exact text toc-generate reads (the line numbers its tree pointers
    use): '# title', then one paragraph per block. No frontmatter, so a
    metadata change can never shift a pointer. Returns (text, line -> item)."""
    lines = [f"# {' '.join(vault_writer.clean_lines(title))}", ""]
    where = {}
    for idx, it in enumerate(items):
        if it["kind"] != "block":
            continue
        tl = vault_writer.clean_lines(it["text"])
        for j in range(len(tl)):
            where[len(lines) + 1 + j] = idx
        lines += tl + [""]
    return "\n".join(lines).rstrip() + "\n", where


def sha1_text(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def _frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    import yaml
    return yaml.safe_load(m.group(1)) or {}


def _clean_label(label):
    """toc-generate E2 rule: drop a trailing tsheg, end with a shad."""
    s = label.strip().strip(ZW).strip()
    s = re.sub(r"\[\[[^\]]*\]\]\s*$", "", s).strip()
    s = s.rstrip("་").rstrip()
    if not s.endswith("།"):
        s += "།"
    return s


def _insert(items, placements):
    """placements: [(item_index, 'before'|'after', heading)] in TOC order."""
    before, after = {}, {}
    for idx, where, h in placements:
        (before if where == "before" else after).setdefault(idx, []).append(h)
    out = []
    for idx, it in enumerate(items):
        out += before.get(idx, [])
        out.append(it)
        out += after.get(idx, [])
    return out


def _apply_tree(ctx, spec, items, rep, title):
    toc = spec["toc"]
    tree_path = ctx.vault / toc["tree"]
    tree = tree_path.read_text(encoding="utf-8")
    text, where = pretoc_layout(title, items)
    want = _frontmatter(tree).get("pointer_source_sha1")
    have = sha1_text(text)
    if want != have:
        raise ValueError(f"{spec['key']}: {toc['tree']} pointers were computed against pre-TOC text "
                         f"{want}, the build now produces {have} — rebuild the tree")
    nodes = [n for n in (parse_toc_line(l) for l in tree.splitlines()) if n]
    if not nodes:
        raise ValueError(f"{spec['key']}: no nodes in {toc['tree']}")
    shift = 0
    top = [n for n in nodes if n["depth"] == 1]
    if len(top) == 1 and letters(top[0]["label"]) and letters(top[0]["label"]) == letters(title):
        nodes.remove(top[0])
        shift = 1
        rep["toc_title_node_excluded"] = top[0]["label"]
    anchors = {}
    for a in toc.get("anchors") or []:
        anchors[str(a["decimal"])] = a
    # the placement pass's evidence, kept in the tree file under '## Placement'
    m = re.search(r"^## Placement\s*\n+```[a-z]*\n(.*?)\n```", tree, re.S | re.M)
    if m:
        for line in m.group(1).splitlines():
            parts = line.split("\t")
            if len(parts) >= 4 and parts[0].strip():
                anchors.setdefault(parts[0].strip(), {"decimal": parts[0].strip(), "line": parts[1].strip(),
                                                      "position": parts[2].strip(), "clause": parts[3].strip()})
    nlines = text.count("\n")
    placements = []
    for n in nodes:
        p = n["pointer"]
        if p is None:
            raise ValueError(f"{spec['key']}: tree node {n['decimal_id']} has no line pointer")
        idx = None
        for line in range(p, nlines + 2):
            if line in where:
                idx = where[line]
                break
        if idx is None:
            raise ValueError(f"{spec['key']}: tree node {n['decimal_id']} points past the last block (line {p})")
        h = {"kind": "heading", "path": n["decimal_id"], "level": n["depth"] - shift,
             "title": _clean_label(n["label"]),
             "source": {"origin": "toc-tree", "tree": toc["tree"], "pointer": p, "row": items[idx]["row"],
                        **({"anchor": anchors[n["decimal_id"]]} if n["decimal_id"] in anchors else {})}}
        placements.append((idx, "before", h))
    rep["headings"] = len(placements)
    return _insert(items, placements)


def _find_norm(hay, needle, start=0):
    """Find needle in hay ignoring zero-width spaces; return (s, e) in hay."""
    idx = [i for i, c in enumerate(hay) if c not in ZW]
    h = "".join(hay[i] for i in idx)
    n = "".join(c for c in needle if c not in ZW)
    s0 = next((k for k, i in enumerate(idx) if i >= start), len(idx))
    k = h.find(n, s0)
    if k < 0:
        return None
    return idx[k], idx[k + len(n) - 1] + 1


def _apply_labels(ctx, spec, items, rep):
    """A human TOC given as heading labels in a separate doc (e.g. Dzongsar
    '(toc)' exports). Each label is found verbatim in that doc; its place in
    the commentary is found by projecting the doc onto the commentary's
    letters. A label that is also inside a row is moved out of the row into
    the heading (the row keeps the author's words); a label that exists only
    in the doc is a heading at the row boundary where the doc puts it.
    Headings go at row boundaries only: a label falling inside a row goes
    before the row unless more of the row precedes it than follows it."""
    toc = spec["toc"]
    doc_rel = toc["doc"]
    paras = []
    for i, line in enumerate(open(raw_path(ctx.raw, doc_rel), encoding="utf-8").read().split("\n"), 1):
        clean, _ = strip_markup(line)
        clean = clean.strip()
        if clean:
            paras.append((i, clean))
    doc_text = "\n".join(p for _, p in paras)
    line_of = []
    for i, p in paras:
        line_of += [i] * (len(p) + 1)
    comm, spans = "", []
    for idx, it in enumerate(items):
        s = len(comm)
        comm += it["text"]
        spans.append((s, len(comm), idx))
        comm += "\n"
    proj = Projector(doc_text, comm)

    def locate(pos):
        for s, e, idx in spans:
            if s <= pos < e or pos == e:
                return idx, pos - s
        return None, None

    placements, cursor, moved = [], 0, []
    removals = {}                                  # item idx -> [(start, end, label)]
    for n, label in enumerate(toc["labels"], 1):
        hit = _find_norm(doc_text, label, cursor)
        if hit is None:
            raise ValueError(f"{spec['key']}: TOC label not found (in order) in {doc_rel}: {label!r}")
        s, e = hit
        cursor = e
        lab_letters = sum(1 for c in doc_text[s:e] if is_letter(c))
        mapped = [proj.pos(i) for i in range(s, e) if is_letter(doc_text[i]) and proj.pos(i) is not None]
        h = {"kind": "heading", "path": str(n), "level": 1,
             "title": " ".join(doc_text[s:e].split()).strip(ZW).strip(),
             "source": {"origin": None, "toc_doc": doc_rel, "toc_line": line_of[s]}}
        if lab_letters and len(mapped) >= 0.9 * lab_letters:
            # the label is in the commentary text too: move it out of its row
            idx, off = locate(min(mapped))
            it = items[idx]
            r = _find_norm(it["text"], doc_text[s:e], max(0, off - 2))
            if r is None:
                raise ValueError(f"{spec['key']}: label {label!r} maps into row {it['row']} but is not there verbatim")
            removals.setdefault(idx, []).append((r[0], r[1], doc_text[s:e]))
            before = sum(1 for c in it["text"][:r[0]] if is_letter(c))
            after = sum(1 for c in it["text"][r[1]:] if is_letter(c))
            h["source"].update({"origin": "row", "row": it["row"], "offset_in_row": r[0]})
        else:
            # only in the TOC doc: place it where the doc's next commentary letter falls
            pos = None
            for i in range(e, len(doc_text)):
                if is_letter(doc_text[i]) and proj.pos(i) is not None:
                    pos = proj.pos(i)
                    break
            if pos is None:
                raise ValueError(f"{spec['key']}: cannot place TOC-doc-only label {label!r}")
            idx, off = locate(pos)
            it = items[idx]
            before = sum(1 for c in it["text"][:off] if is_letter(c))
            after = sum(1 for c in it["text"][off:] if is_letter(c))
            h["source"].update({"origin": "toc_doc", "row": it["row"], "offset_in_row": off})
        where = "before" if before == 0 or before <= after else "after"
        if before:
            h["source"]["inside_row"] = {"letters_before": before, "letters_after": after,
                                         "placed": f"{where} row {it['row']}"}
        h["source"]["placement"] = where
        placements.append((idx, where, h))
    # move in-row labels out of their rows (author's words stay)
    for idx, rem in removals.items():
        it = items[idx]
        text, runs = it["text"], it.get("annotations") or []
        for s, e, lab in sorted(rem, reverse=True):
            e2 = e
            while e2 < len(text) and text[e2] in " \t" + ZW:
                e2 += 1
            text = text[:s] + text[e2:]
            runs = _shift_runs(runs, s, e2 - s)
            moved.append({"row": it["row"], "text": lab})
        it["source"]["toc_labels_moved_to_headings"] = [lab for _, _, lab in sorted(rem)]
        it["text"] = text.strip(" \t")
        if runs:
            it["annotations"] = runs
        elif "annotations" in it:
            it.pop("annotations")
    rep["headings"] = len(placements)
    rep["toc_labels_moved_from_rows"] = moved
    out = _insert(items, placements)
    gone = [it["row"] for it in out if it["kind"] == "block" and not has_letters(it["text"])]
    rep["rows_that_were_only_toc_labels"] = gone
    return [it for it in out if it["kind"] != "block" or has_letters(it["text"])], gone


# --------------------------------------------------------------------------
# the adapter
# --------------------------------------------------------------------------

def adapt_md_rows(ctx, spec, rep):
    items, empty_rows = _blocks(ctx, spec, rep)
    extra = {}
    if empty_rows:
        extra["rows_without_letters"] = empty_rows
    if spec.get("pair"):
        extra |= _pair(ctx, spec, items, rep)
    toc = spec.get("toc") or {"kind": "none"}
    title = spec["title"]
    if toc["kind"] == "tree":
        items = _apply_tree(ctx, spec, items, rep, title)
    elif toc["kind"] == "labels":
        items, gone = _apply_labels(ctx, spec, items, rep)
        if gone:
            extra["rows_that_were_only_toc_labels"] = gone
    elif toc["kind"] != "none":
        raise ValueError(f"{spec['key']}: unknown toc kind {toc['kind']!r}")
    extra["toc"] = {k: v for k, v in toc.items() if k != "labels"}
    rep["blocks"] = sum(1 for it in items if it["kind"] == "block")
    flat = spec.get("id_scheme", "flat") == "flat"
    for it in items:
        if it["kind"] == "block":
            row = it.pop("row")
            it["source"]["row"] = row
            if flat:
                # a text with no TOC keeps the human row number as its id
                # (gaps where a row is empty on this side), so ^N is row N of
                # the alignment doc and pairs read across files at a glance
                if row == 0:
                    raise ValueError(f"{spec['key']}: text before the first numbered row cannot take a flat id")
                it["id"] = str(row)
    return items, extra


def pretoc_source(ctx, spec):
    """(text, line map) of the pre-TOC file for a work whose toc is a tree."""
    rep = {}
    items, _ = _blocks(ctx, spec, rep)
    text, where = pretoc_layout(spec["title"], items)
    rows = {line: items[i]["row"] for line, i in where.items()}
    return text, rows

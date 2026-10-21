#!/usr/bin/env python3
"""pdf2ku: books in PDF form -> knowledge units, one per section of the book's outline.

Test scenario for knowledge that a pack carries: the content of a book is not open-licence
documentation, so the units it produces stay local (units/books is git-ignored) and go into a
local pack only, never into the default index or a published pack.

Reads the outline (bookmarks) of each PDF with `pdftohtml -xml` and the page text with
`pdftotext` (poppler). A chapter is an outline entry at the top level whose title starts with
"Chapter N"; its direct children are the sections, each one unit. Deeper entries stay inside
their section; a section longer than SPLIT_CHARS is split at them, or at paragraphs. The text
of a chapter before its first section becomes a unit of its own. Running headers (chapter or
section title at the top of a page) and page numbers are dropped. Front and back matter (cover,
copyright, index, advertising) is skipped; the preface stays, as the book's overview.

Usage: python pdf2ku.py <out-dir> <book.pdf> [<book.pdf> ...] [--domain=cpp] [--publisher=Packt]
  One folder per book under out-dir, named after the book (collection), is removed and rewritten.
"""
import html, re, subprocess, sys
from pathlib import Path
from xml.etree import ElementTree

SPLIT_CHARS = 12_000
MIN_CHARS = 160
SUMMARY_WORDS = 40
ID_MAX = 90
# Outline entries that say nothing about the subject: skipped with everything below them.
SKIP = re.compile(r"(?i)^\s*(cover|title page|copyright( and credits)?|contributors|about the authors?|about the reviewers?|"
                  r"table of contents|contents|index|other books you may enjoy|dedication|foreword|acknowledg?e?ments?|"
                  r"packt is searching for authors like you|share your thoughts|download a free pdf copy( of this book)?|"
                  r"join our (community|book'?s discord)[^\n]*|leave a review[^\n]*|unlock your book'?s exclusive benefits|"
                  r"getting the most out of this book[^\n]*|download the example code files|get in touch|conventions used|"
                  r"get this book[’']s pdf version[^\n]*|how to unlock[^\n]*|unlock your book[^\n]*|free benefits[^\n]*|"
                  r"how to report errata|where to download material about this book|if you like this book|"
                  r"chapter \d+: unlock your book'?s exclusive benefits|part [ivx\d]+\b.*)\s*$")
CHAPTER = re.compile(r"^\s*Chapter\s+(\d+)\s*[:.\-–—]?\s*(.*?)\s*$")
PAGE_NUMBER = re.compile(r"^\s*(\d{1,4}|[ivxlc]{1,6})\s*$", re.I)


def slug(s, n=48):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n].strip("-")


def norm(s):
    s = html.unescape(s).replace("’", "'").replace("–", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


# ── outline ─────────────────────────────────────────────────────────────────

def outline(pdf):
    """[(depth, title, page)] in document order; pdftohtml prints the bookmarks with page 1 alone."""
    xml = subprocess.run(["pdftohtml", "-xml", "-i", "-f", "1", "-l", "1", "-stdout", str(pdf)],
                         capture_output=True, text=True, errors="replace").stdout
    m = re.search(r"<outline>.*</outline>", xml, re.S)
    if not m:
        return []
    root = ElementTree.fromstring(re.sub(r"&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-f]+);)", "&amp;", m.group(0)))
    items = []

    def walk(el, depth):
        for child in el:
            if child.tag == "item":
                items.append((depth, html.unescape((child.text or "").strip()), int(child.get("page", "0") or 0)))
            elif child.tag == "outline":
                walk(child, depth + 1)
    walk(root, 0)
    return items


def pages_of(pdf):
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, errors="replace").stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1)) if m else 0


def book_title(pdf):
    """The title of the PDF's metadata, else the title page: its first lines up to the subtitle (a long line)."""
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, errors="replace").stdout
    m = re.search(r"^Title:\s+(.+)$", info, re.M)
    if m and len(m.group(1).strip()) > 3:
        return m.group(1).strip()
    first = subprocess.run(["pdftotext", "-f", "1", "-l", "2", str(pdf), "-"], capture_output=True, text=True,
                           errors="replace").stdout
    lines = [l.strip() for l in first.split("\n") if l.strip() and l.strip() != "<packt>"]
    title = []
    for l in lines[:4]:
        if title and (len(l.split()) > 4 or l.endswith(",")):
            break
        title.append(l)
    t = re.sub(r"\s+", " ", " ".join(title)).strip() or pdf.stem
    return re.sub(r"(?<=[a-z])(?=C\+\+)", " ", t)


# ── text ────────────────────────────────────────────────────────────────────

# Packt's promotion boxes: a paragraph that advertises the publisher's reader, PDF copy or benefits, with
# the short heading before it and the "Note: ... invoice ..." paragraph after it.
PROMO_WORDS = re.compile(r"packtpub\.com/\s*unlock|Packt Reader|Packt\+|exclusive (benefits|extras)|free PDF copy|PDF/ePub copy|"
                         r"Get [Tt]his [Bb]ook[’']s PDF [Vv]ersion|purchase invoice|invoice handy|Unlock this book[’']s", re.I)
PROMO_HEAD = re.compile(r"PDF|benefit|Packt|Unlock|^\s*Note\s*$", re.I)
PROMO_NOTE = re.compile(r"^Note:? ?(Keep|Have|Did you buy)", re.I)


def strip_promo(text):
    paras = re.split(r"(\n[ \t]*\n)", text)          # paragraphs and the separators between them
    drop = set()
    for i in range(0, len(paras), 2):
        if PROMO_WORDS.search(paras[i]):
            drop.add(i)
            prev = i - 2
            if prev >= 0 and prev not in drop and len(paras[prev]) <= 70 and paras[prev].count("\n") <= 2 \
                    and PROMO_HEAD.search(paras[prev]):
                drop.add(prev)
            nxt = i + 2
            if nxt < len(paras) and PROMO_NOTE.match(paras[nxt].strip()):
                drop.add(nxt)
    out = []
    for i in range(0, len(paras), 2):
        if i not in drop:
            out.append(paras[i])
    return "\n\n".join(x for x in out if x.strip())


def page_texts(pdf, first, last, headers=frozenset()):
    """{page: [lines]} for the pages first..last; index anchors, page numbers and running titles dropped."""
    def header(l):
        return PAGE_NUMBER.match(l) is not None or norm(l) in headers
    txt = subprocess.run(["pdftotext", "-f", str(first), "-l", str(last), "-enc", "UTF-8", str(pdf), "-"],
                         capture_output=True, text=True, errors="replace").stdout
    pages = txt.split("\f")
    out = {}
    for i, p in enumerate(pages[: last - first + 1]):
        lines = [l.rstrip() for l in strip_promo(p).split("\n") if not re.fullmatch(r"idx_[0-9a-f]+", l.strip())]
        for _ in range(2):
            while lines and not lines[0].strip():
                lines.pop(0)
            if lines and header(lines[0]):
                lines.pop(0)
        for _ in range(2):
            while lines and not lines[-1].strip():
                lines.pop()
            if lines and header(lines[-1]):
                lines.pop()
        while lines and not lines[0].strip():
            lines.pop(0)
        out[first + i] = lines
    return out


def drop_running_header(lines, headers):
    """The first line of a page that repeats a chapter or section title is a running header."""
    if lines and norm(lines[0]) in headers:
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return lines


LIST_ITEM = re.compile(r"^\s*([•·▪◦‣\-*]|\d+[.)])\s")


def find_heading(lines, title, start=0, pages=None, min_page=0):
    """Index of the line where `title` begins, allowing a heading wrapped over up to three lines.
    A list item that repeats the title (the chapter's topic list) is not a heading, nor is a line
    on a page before the one the outline names."""
    want = norm(title)
    if not want:
        return None
    for i in range(start, len(lines)):
        if not lines[i].strip() or LIST_ITEM.match(lines[i]) or (pages and pages[i] < min_page):
            continue
        acc = ""
        for j in range(i, min(i + 3, len(lines))):
            if not lines[j].strip():
                break
            acc = (acc + " " + norm(lines[j])).strip()
            if acc == want:
                return (i, j + 1)
            if not want.startswith(acc):
                break
    return None


def paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text) if p.strip()]


def split_long(title, text, sub_titles):
    """Pieces of at most about SPLIT_CHARS: at the sub-headings when they are found, else at paragraphs."""
    if len(text) <= SPLIT_CHARS:
        return [(title, text)]
    lines = text.split("\n")
    cuts = []
    pos = 0
    for st in sub_titles:
        hit = find_heading(lines, st, pos)
        if hit:
            cuts.append((hit[0], hit[1], st))
            pos = hit[1]
    pieces = []
    if cuts:
        prev, prev_title = 0, title
        for (i, j, st) in cuts:
            body = "\n".join(lines[prev:i]).strip()
            if body:
                pieces.append((prev_title, body))
            prev, prev_title = j, f"{title}: {st}"
        pieces.append((prev_title, "\n".join(lines[prev:]).strip()))
    else:
        pieces = [(title, text)]
    out = []
    for t, body in pieces:
        if len(body) <= SPLIT_CHARS:
            out.append((t, body))
            continue
        buf, n = [], 1
        for p in paragraphs(body):
            if sum(len(x) for x in buf) + len(p) > SPLIT_CHARS and buf:
                out.append((f"{t} (part {n})", "\n\n".join(buf)))
                buf, n = [], n + 1
            buf.append(p)
        if buf:
            out.append((f"{t} (part {n})" if n > 1 else t, "\n\n".join(buf)))
    return out


def summary_of(body):
    text = re.sub(r"\s+", " ", re.sub(r"^#+ .*$", "", body, flags=re.M)).strip()
    words = text.split(" ")
    if len(words) <= SUMMARY_WORDS:
        return text
    cut = " ".join(words[:SUMMARY_WORDS - 1])
    m = re.search(r"^(.{40,}?[.!?])\s", cut + " ")
    return (m.group(1) if m else cut.rstrip(",;:") + "…").strip()


# ── units ───────────────────────────────────────────────────────────────────

def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_unit(path, meta, body):
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(yaml_str(str(x)) for x in v)}]")
        elif isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {yaml_str(str(v))}")
    lines += ["---", "", body.strip(), ""]
    path.write_text("\n".join(lines), encoding="utf-8")


PREFIXES = set()


def convert(pdf, out_dir, domain, publisher):
    pdf = Path(pdf)
    items = outline(pdf)
    npages = pages_of(pdf)
    title = book_title(pdf)
    collection = slug(pdf.stem, 40)
    prefix = "".join(w[0] for w in re.findall(r"[a-z0-9]+", title.lower()))[:6] or collection[:6]
    n = 2
    while prefix in PREFIXES:
        prefix = f"{prefix[:5]}{n}"
        n += 1
    PREFIXES.add(prefix)
    folder = out_dir / collection
    if folder.exists():
        for f in folder.glob("*.md"):
            f.unlink()
    folder.mkdir(parents=True, exist_ok=True)
    if not items:
        print(f"{pdf.name}: no outline, skipped", file=sys.stderr)
        return 0

    # Chapters, in the three shapes Packt uses: "Chapter N: Title" with the sections nested below it;
    # the same under a "Part" entry; or a number entry followed by the title entry, with the sections
    # at the same depth and their sub-headings nested (the flat shape). The preface is chapter 0.
    def starts_chapter(k):
        d, t, page = items[k]
        cm = CHAPTER.match(t)
        if cm:
            return int(cm.group(1)), cm.group(2) or t, k + 1
        if re.fullmatch(r"\d{1,2}", t.strip()) and k + 1 < len(items) and items[k + 1][0] == d:
            return int(t), items[k + 1][1], k + 2
        if re.fullmatch(r"(?i)preface", t.strip()):
            return 0, "Preface", k + 1
        return None

    def ends_chapter(k, cd, flat):
        d, t, page = items[k]
        if d < cd or (d == cd and (starts_chapter(k) or re.match(r"(?i)^part\b", t))):
            return True
        if flat:
            return d == cd and re.match(r"(?i)^(index|other books you may enjoy|appendix\b.*)$", t) is not None
        return d == cd

    chapters = []
    i = 0
    while i < len(items):
        st = starts_chapter(i)
        if not st:
            i += 1
            continue
        num, ctitle, j = st
        cd, page = items[i][0], items[i][2]
        flat = j < len(items) and items[j][0] == cd and not ends_chapter(j, cd, True)
        sdepth = cd if flat else cd + 1
        sections = []
        while j < len(items) and not ends_chapter(j, cd, flat):
            d, t, sp = items[j]
            if d == sdepth:
                sections.append({"title": t, "page": sp, "subs": [], "skip": bool(SKIP.match(t))})
            elif d > sdepth and sections:
                sections[-1]["subs"].append(t)
            j += 1
        end_page = items[j][2] if j < len(items) else npages + 1
        chapters.append({"num": num, "title": ctitle.strip(), "page": page, "end": max(page, end_page), "sections": sections})
        i = j

    headers = {norm(c["title"]) for c in chapters} | {norm(s["title"]) for c in chapters for s in c["sections"]}
    headers |= {norm(f"Chapter {c['num']}: {c['title']}") for c in chapters} | {norm(f"Chapter {c['num']}") for c in chapters}
    headers |= {norm(title), norm(title.split(":")[0])}
    count = 0
    seen = set()
    for c in chapters:
        last = min(npages, c["end"] - 1 if c["end"] > c["page"] else c["page"])
        if last < c["page"]:
            continue
        texts = page_texts(pdf, c["page"], last, headers)
        lines = []
        page_at = []            # page number of each line, for the source reference
        for p in range(c["page"], last + 1):
            pl = drop_running_header(texts.get(p, []), headers)
            if lines and lines[-1].strip():
                lines.append("")
                page_at.append(p)
            lines += pl
            page_at += [p] * len(pl)
        # The chapter heading itself at the top of the first page.
        hit = find_heading(lines, c["title"], 0) or find_heading(lines, f"Chapter {c['num']}: {c['title']}", 0)
        if hit and hit[0] < 6:
            del lines[hit[0]:hit[1]]
            del page_at[hit[0]:hit[1]]
        # Section starts in the text; a heading not found starts at its page.
        bounds = []
        pos = 0
        for s in c["sections"]:
            hit = find_heading(lines, s["title"], pos, page_at, s["page"] - 1)
            if hit:
                start, body_start = hit
            else:
                start = next((k for k, p in enumerate(page_at) if p >= s["page"] and k >= pos), len(lines))
                body_start = start
            bounds.append((start, body_start, s))
            pos = body_start
        pieces = []
        intro_end = bounds[0][0] if bounds else len(lines)
        intro = "\n".join(lines[:intro_end]).strip()
        if len(intro) >= MIN_CHARS:
            pieces.append((c["title"], intro, [], page_at[0] if page_at else c["page"]))
        for k, (start, body_start, s) in enumerate(bounds):
            if s["skip"]:
                continue
            end = bounds[k + 1][0] if k + 1 < len(bounds) else len(lines)
            body = "\n".join(lines[body_start:end]).strip()
            if len(body) < MIN_CHARS:
                continue
            pieces.append((f"{c['title']}: {s['title']}", body, s["subs"], page_at[body_start] if body_start < len(page_at) else s["page"]))
        for t, body, subs, page in pieces:
            for pt, pbody in split_long(t, body, subs):
                parts = pt.split(": ")[1:] or [pt]
                part_m = re.search(r" \(part (\d+)\)$", parts[-1])
                if part_m:
                    parts[-1] = parts[-1][: part_m.start()]
                uid = f"{prefix}-ch{c['num']:02d}-" + "-".join(slug(x, 36) for x in parts if slug(x, 36))
                uid = (uid + (f"-p{part_m.group(1)}" if part_m else ""))[:ID_MAX].rstrip("-")
                n = 2
                base = uid
                while uid in seen:
                    uid = f"{base[:ID_MAX - 3]}-{n}"
                    n += 1
                seen.add(uid)
                meta = {
                    "id": uid, "type": "concept", "domain": domain, "title": pt, "summary": summary_of(pbody),
                    "status": "draft", "collection": collection, "book": title, "chapter": c["num"],
                    "source": f"{pdf.name}#page={page}", "page": page,
                    "license": f"Copyright {publisher}; all rights reserved. Local test only, not for distribution.",
                    "mode": "P",
                }
                write_unit(folder / f"{uid}.md", meta, pbody)
                count += 1
    print(f"{pdf.name}: {title!r}, {len(chapters)} chapters, {count} units -> {folder}")
    return count


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    out_dir = Path(args[0])
    total = 0
    for pdf in args[1:]:
        total += convert(pdf, out_dir, opts.get("domain", "cpp"), opts.get("publisher", "Packt Publishing"))
    print(f"{total} units")


if __name__ == "__main__":
    main()

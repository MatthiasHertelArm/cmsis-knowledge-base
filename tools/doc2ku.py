#!/usr/bin/env python3
"""doc2ku: documentation of open-license repositories -> knowledge units, one per section.

Reads the sources listed in a YAML file (sources/docs.yml), each a cloned repository with
documentation in Markdown, doxygen-flavoured Markdown or doxygen comment files (*.txt with
/** \\page ... */ blocks), and writes one concept unit per H2 section of every page. A section
longer than SPLIT_CHARS is split at its H3 headings; the text before the first H2 becomes a
unit of its own when it says something.

Only sources with mode V (full text, open licence) belong in the list: the unit body is the
section text. Every unit records where it came from (source: repo@commit:path), where it is
published (doc_source: URL), its licence and its collection, so a reviewer can trace it.

Usage: python doc2ku.py <sources.yml> <docs-dir> <out-dir> [--only name,name]
  docs-dir holds one clone per source, named like the source's `dir` (default: last part of repo).
"""
import fnmatch, json, re, subprocess, sys
from pathlib import Path
import yaml

SPLIT_CHARS = 12_000
MIN_CHARS = 160
SUMMARY_WORDS = 40
ID_MAX = 90
SKIP_NAMES = re.compile(r"(?i)(changelog|history|revision_history|code_of_conduct|contributing|security|license|third[-_]party|release[-_]notes?|pull_request_template|issue_template)")


def slug(s, n=48):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n].strip("-")


# ── doxygen ─────────────────────────────────────────────────────────────────

def dox_inline(t):
    t = re.sub(r"\\refelem\{(\w+)\}(?:\{[^}]*\})?", r"`<\1>`", t)
    t = re.sub(r'\\(?:ref|subpage)\s+[\w:.]+\s+"([^"]+)"', r"\1", t)
    t = re.sub(r"\\(?:ref|subpage)\s+([\w:.]+)(?:\(\))?", r"\1", t)
    t = re.sub(r"\\(?:b|em)\s+(\S+)", r"**\1**", t)
    t = re.sub(r"\\(?:c|p)\s+(\S+)", r"`\1`", t)
    t = re.sub(r"\\(?:a|e)\s+(\S+)", r"_\1_", t)
    t = re.sub(r"\\token\{([^}]*)\}", r"`\1`", t)
    t = re.sub(r"\\(?:note|remark|remarks)\b", "**Note:**", t)
    t = re.sub(r"\\(?:warning|attention)\b", "**Warning:**", t)
    t = re.sub(r"\\(?:return|returns|retval)\b", "Returns:", t)
    t = re.sub(r"\\param\[(\w+(?:,\w+)?)\]\s+(\w+)", r"- `\2` (\1):", t)
    t = re.sub(r"\\param\s+(\w+)", r"- `\1`:", t)
    t = re.sub(r"\\(?:details|brief|copybrief|copydoc\s+\S+|ingroup\s+\S+|anchor\s+\S+|image\s+\w+\s+\S+(?:\s+\"[^\"]*\")?|tableofcontents|todo|hideinitializer|nosubgrouping|endinternal|internal)\b", "", t)
    t = re.sub(r"\\(?:li)\b", "-", t)
    return t


def html_to_md(text):
    """HTML of the prose as Markdown; code fences and code spans stay as they are (they hold XML such as <sequence>)."""
    parts = re.split(r"(```.*?```|`[^`\n]+`)", text, flags=re.S)
    return "".join(p if p.startswith("`") else html_prose_to_md(p) for p in parts)


def html_prose_to_md(t):
    # doxygen's escaped angle brackets name an XML element: keep it, as code.
    t = re.sub(r"\\<(/?[\w:.-]+)\\>", r"`<\1>`", t)
    t = re.sub(r"(?is)<br\s*/?>", "\n", t)
    t = re.sub(r"(?is)</?(b|strong)>", "**", t)
    t = re.sub(r"(?is)</?(i|em)>", "_", t)
    t = re.sub(r"(?is)</?(code|tt)>", "`", t)
    t = re.sub(r"(?is)<li>", "\n- ", t)
    t = re.sub(r"(?is)</tr>", "\n", t)
    t = re.sub(r"(?is)</t[dh]>", " | ", t)
    t = re.sub(r"(?is)<tr[^>]*>", "| ", t)
    t = re.sub(r"(?is)<(p|div|table|ul|ol|dl|dd|dt)[^>]*>", "\n", t)
    html = r"(?:a|b|i|u|p|em|strong|code|tt|pre|span|div|table|thead|tbody|tr|td|th|ul|ol|li|dl|dt|dd|img|sup|sub|center|h[1-6]|hr|small|big|font|caption|col|colgroup|blockquote|details|summary|kbd|var|samp|cite|abbr|section|figure|figcaption|nobr)"
    t = re.sub(r"(?is)</?" + html + r"(\s[^<>]*)?/?>", "", t)
    # Anything else in angle brackets is an XML element of the specification: keep it, as code.
    t = re.sub(r"(?<![`\w])<(/?[a-zA-Z][\w:.-]*)((?:\s[^<>]*)?)/?>(?!`)", lambda m: f"`<{m.group(1)}{m.group(2)}>`", t)
    t = t.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return t


def comment_blocks(text):
    """The bodies of the /** ... */ blocks. Like doxygen, a /* ... */ inside a block (a code example) nests."""
    out, i = [], 0
    while True:
        start = text.find("/**", i)
        if start < 0:
            return out
        depth, j = 1, start + 3
        while j < len(text) and depth > 0:
            if text.startswith("/*", j):
                depth += 1
                j += 2
            elif text.startswith("*/", j):
                depth -= 1
                j += 2
            else:
                j += 1
        out.append(text[start + 3:j - 2])
        i = j


def doxtxt_to_md(text, default_id="main", default_title=""):
    """doxygen comment file -> list of (page_id, title, markdown)."""
    pages = []
    for block in comment_blocks(text):
        lines = []
        for raw in block.splitlines():
            lines.append(re.sub(r"^\s*\*\s?", "", raw) if re.match(r"^\s*\*(?!\*)", raw) else raw)
        body = "\n".join(lines)
        m = re.search(r"\\(page|defgroup|mainpage|addtogroup)\s+(\S+)?[ \t]*(.*)", body)
        if not m:
            # A \fn, \var or \struct block belongs to the group page before it, or to a page named after the file.
            if re.search(r"\\(fn|var|struct|typedef|def|enum)\s", body):
                if not pages:
                    pages.append([default_id, default_title, ""])
                pages[0][2] += "\n" + body   # the file's main group: sub-groups only define constants
            continue
        title = m.group(3).strip() if m.group(1) != "mainpage" else (m.group(2) or "") + " " + m.group(3)
        if not title:
            title = default_title or (m.group(2) or "").replace("_", " ")
        rest = body[m.end():]
        pages.append([m.group(2) or "main", title.strip(), rest])
    out = []
    for pid, title, body in pages:
        md = []
        in_code = False
        for line in body.splitlines():
            s = line.strip()
            if re.match(r"\\(code|verbatim)\b", s):
                lang = re.search(r"\{\.(\w+)\}", s)
                md.append("```" + (lang.group(1) if lang else ""))
                in_code = True
                continue
            if re.match(r"\\(endcode|endverbatim)\b", s):
                md.append("```")
                in_code = False
                continue
            if in_code:
                md.append(line)
                continue
            h = re.match(r"\\(section|subsection|subsubsection|paragraph)\s+\S+\s*(.*)", s)
            if h:
                level = {"section": 2, "subsection": 3, "subsubsection": 4, "paragraph": 5}[h.group(1)]
                md.append("\n" + "#" * level + " " + dox_inline(h.group(2)).strip() + "\n")
                continue
            other = re.match(r"\\(var|struct|typedef|def|enum)\s+(.*)", s)
            if other:
                name = re.findall(r"\w+", re.sub(r"\(.*", "", other.group(2)))
                md.append(f"\n### {name[-1] if name else other.group(2)}\n\n```c\n{other.group(2).strip()}\n```\n")
                continue
            fn = re.match(r"\\fn\s+(.*)", s)
            if fn:
                name = re.search(r"(\w+)\s*\(", fn.group(1))
                md.append(f"\n### {name.group(1) if name else fn.group(1)}\n\n```c\n{fn.group(1).strip()}\n```\n")
                continue
            if re.match(r"\\(addtogroup|ingroup|defgroup|weakgroup|\{|\})", s) or s in ("@{", "@}"):
                continue
            md.append(dox_inline(line))
        out.append((pid, title, html_to_md("\n".join(md))))
    return out


def doxmd_to_md(text):
    t = re.sub(r"\s*\{#[\w.-]+\}", "", text)
    t = t.replace("[TOC]", "")
    t = re.sub(r"(?m)^\s*\\(?:page|defgroup)\s+\S+\s*(.*)$", r"# \1", t)
    t = re.sub(r"(?m)^\s*\\(?:section)\s+\S+\s*(.*)$", r"## \1", t)
    t = re.sub(r"(?m)^\s*\\(?:subsection)\s+\S+\s*(.*)$", r"### \1", t)
    t = re.sub(r"\\code(?:\{\.(\w+)\})?", lambda m: "```" + (m.group(1) or ""), t)
    t = t.replace("\\endcode", "```")
    return html_to_md(dox_inline(t))


# ── Markdown pages -> sections ──────────────────────────────────────────────

def strip_front_matter(t):
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    return (t[m.end():], yaml.safe_load(m.group(1)) or {}) if m else (t, {})


def headings(md):
    """(level, title, start, end-of-heading-line) of every ATX heading outside code fences."""
    out, fence = [], False
    pos = 0
    for line in md.splitlines(keepends=True):
        if re.match(r"\s*(```|~~~)", line):
            fence = not fence
        elif not fence:
            m = re.match(r"(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if m:
                out.append((len(m.group(1)), m.group(2).strip(), pos, pos + len(line)))
        pos += len(line)
    return out


def prose_chars(md):
    t = re.sub(r"(?s)```.*?```", "", md)
    t = re.sub(r"(?m)^#.*$", "", t)
    return len(re.sub(r"\s+", " ", t).strip())


def summary_of(md, fallback):
    t = re.sub(r"(?s)```.*?```", " ", md)
    for para in re.split(r"\n\s*\n", t):
        p = para.strip()
        if not p or p.startswith(("#", "|", "!", "<", ">", "-", "*", "1.", "```")) or len(p) < 40:
            continue
        p = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", p)
        p = re.sub(r"[`*_]", "", " ".join(p.split()))
        first = re.split(r"(?<=[.!?])\s", p)
        s = ""
        for sent in first:
            if len((s + " " + sent).split()) > SUMMARY_WORDS:
                break
            s = (s + " " + sent).strip()
        if not s:
            s = " ".join(p.split()[:SUMMARY_WORDS - 2]) + " …"
        return s
    return fallback


def rewrite_links(md, page_url):
    """Relative links and images: links become absolute to the published page, images a note."""
    md = re.sub(r"!\[([^\]]*)\]\([^)]*\)", lambda m: f"(figure: {m.group(1)})" if m.group(1) else "", md)

    def fix(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"(?i)^(https?:|mailto:|#)", target) or not page_url:
            return m.group(0)
        base = page_url.rsplit("/", 1)[0] + "/"
        return f"[{label}]({base}{target})"
    return re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", fix, md)


def sections(md):
    """[(path of titles, text)] by H2, an H2 longer than SPLIT_CHARS by H3; the intro first."""
    hs = headings(md)
    h1 = next((h for h in hs if h[0] == 1), None)
    page_title = h1[1] if h1 else ""
    h2 = [h for h in hs if h[0] == 2]
    if not h2 and len(md) > 3_000:
        # An API reference page: no sections, one H3 per function. Each function is a unit of its own.
        h2 = [h for h in hs if h[0] == 3]
    out = []
    intro_end = h2[0][2] if h2 else len(md)
    intro = md[(h1[3] if h1 and h1[2] < intro_end else 0):intro_end]
    out.append(((), intro))
    for i, h in enumerate(h2):
        end = h2[i + 1][2] if i + 1 < len(h2) else len(md)
        text = md[h[3]:end]
        if len(text) > SPLIT_CHARS:
            h3 = [x for x in hs if x[0] == 3 and h[3] <= x[2] < end]
            if h3:
                out.append(((h[1],), md[h[3]:h3[0][2]]))
                for j, s in enumerate(h3):
                    e = h3[j + 1][2] if j + 1 < len(h3) else end
                    out.append(((h[1], s[1]), md[s[3]:e]))
                continue
        out.append(((h[1],), text))
    return page_title, out


# ── one source ──────────────────────────────────────────────────────────────

def git_head(repo):
    return subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip() or "unknown"


def matches(path, globs):
    return any(fnmatch.fnmatch(path, g) for g in globs)


def page_url_of(src, rel, page_id):
    tpl = src.get("url")
    if tpl:
        stem = Path(rel).stem
        if stem.lower() in ("index", "readme"):
            stem = ""
        return re.sub(r"(?<!:)//+", "/", tpl.format(stem=stem, page=page_id, path=rel, dir=str(Path(rel).parent)))
    return f"https://github.com/{src['repo']}/blob/{src['commit']}/{rel}"


def domain_of(src, rel):
    for rule in src.get("domains", []):
        if matches(rel, rule["paths"]):
            return rule["domain"]
    return src["domain"]


def convert(src, repo, out, used):
    src["commit"] = git_head(repo)
    files = sorted(p for p in repo.rglob("*") if p.is_file())
    written = 0
    for f in files:
        rel = f.relative_to(repo).as_posix()
        suffixes = (".md", ".txt", ".c", ".h") if src.get("format") == "doxtxt" else (".md", ".txt")
        if f.suffix.lower() not in suffixes or not matches(rel, src["include"]) or matches(rel, src.get("exclude", [])) \
                or SKIP_NAMES.search(f.stem):
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        fmt = src.get("format", "md")
        if fmt == "doxtxt" and f.suffix in (".txt", ".c", ".h"):
            title = f.stem.replace("ref_", "").replace("cmsis_os2_", "").replace("_", " ").strip()
            pages = [(pid, t, "# " + t + "\n" + md) for pid, t, md in doxtxt_to_md(text, f.stem, title)]
        else:
            body, fm = strip_front_matter(text)
            body = doxmd_to_md(body) if fmt in ("doxmd", "doxtxt") else body
            if fm.get("title") and not re.search(r"(?m)^# ", body):
                body = f"# {fm['title']}\n" + body
            pages = [(f.stem, "", body)]
        for page_id, _title, md in pages:
            page_url = page_url_of(src, rel, page_id)
            page_title, secs = sections(md)
            page_title = page_title or Path(rel).stem.replace("_", " ").replace("-", " ")
            for path, text_ in secs:
                if prose_chars(text_) < MIN_CHARS:
                    continue
                name = path[-1] if path else page_title
                title = f"{page_title}: {' / '.join(path)}" if path else page_title
                # GitHub renders Markdown with heading anchors, not doxygen files; a published site has its own.
                anchored = src.get("anchors", True) and (src.get("url") or f.suffix.lower() == ".md")
                anchor = "#" + slug(path[-1], 80) if path and anchored else ""
                body = rewrite_links(text_.strip(), page_url)
                if len(path) == 2:
                    body = f"_Part of: {path[0]}_\n\n" + body
                base = f"{src['prefix']}-{slug(page_title, 34)}" + (f"-{slug(name, 40)}" if path else "")
                uid = base[:ID_MAX].strip("-")
                n = 1
                while uid in used:
                    n += 1
                    uid = f"{base[:ID_MAX - 4].strip('-')}-{n}"
                used.add(uid)
                meta = dict(id=uid, type="concept", domain=domain_of(src, rel), title=title[:160],
                            summary=summary_of(body, title), status="draft", collection=src["name"],
                            source=f"{src['repo']}@{src['commit']}:{rel}", doc_source=page_url + anchor,
                            license=src["license"], mode="V")
                if src.get("applies_to"):
                    meta["applies_to"] = src["applies_to"]
                p = out / src["name"] / f"{uid}.md"
                p.parent.mkdir(parents=True, exist_ok=True)
                fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
                p.write_text(f"---\n{fm}\n---\n\n{body}\n", encoding="utf-8")
                written += 1
    return written


def main(cfg, docs, out, only=None):
    sources = yaml.safe_load(Path(cfg).read_text(encoding="utf-8"))["sources"]
    out = Path(out)
    used = set()
    total = 0
    for src in sources:
        if only and src["name"] not in only:
            continue
        if src.get("mode", "V") != "V":
            print(f"{src['name']:28s} skipped: mode {src.get('mode')}")
            continue
        repo = Path(docs) / src.get("dir", src["repo"].split("/")[-1])
        if not repo.exists():
            print(f"{src['name']:28s} missing clone {repo}")
            continue
        target = out / src["name"]
        if target.exists():
            for old in target.glob("*.md"):
                old.unlink()
        n = convert(src, repo, out, used)
        total += n
        print(f"{src['name']:28s} {n:4d} units  {src['repo']}@{src['commit']}  {src['license']}")
    print(f"total {total}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--only")]
    only = None
    for a in sys.argv[1:]:
        if a.startswith("--only="):
            only = set(a.split("=", 1)[1].split(","))
    if len(args) != 3:
        sys.exit(__doc__)
    main(*args, only=only)

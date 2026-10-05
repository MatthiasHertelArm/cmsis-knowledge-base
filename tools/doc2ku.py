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

Usage: python doc2ku.py <sources.yml> <docs-dir> <out-dir> [--only=name,name] [--fetch]
  docs-dir holds one clone per source, named like the source's `dir` (default: last part of repo).
  --fetch clones what is missing: shallow, and sparse for a source with `sparse:` paths.
"""
import fnmatch, html, json, re, subprocess, sys
from pathlib import Path
import yaml

SPLIT_CHARS = 12_000
MIN_CHARS = 160
SUMMARY_WORDS = 40
ID_MAX = 90
GENERIC_STEMS = {"readme", "design", "spec", "index", "overview", "introduction", "guide", "docs", "main", "mainpage", "usage"}
PAGE_SKIP = re.compile(r"(?i)^(revision history|release notes|change ?log|history)$")
# Document boilerplate: says nothing about the subject.
SECTION_SKIP = re.compile(r"(?i)^(\d+(\.\d+)*\.?\s+)?(acknowledge?ments?|change control|change history|document history|revision history|"
                          r"release notes|change ?log|licen[cs]e|licensing|copyright|trademark[\w ]*|contributing|contributors|"
                          r"code of conduct|feedback|disclaimer|proprietary notice|confidentiality status|"
                          r"current status and anticipated changes|about the license)$")
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
    text = "".join(p if p.startswith("```") else html_tables(p) for p in re.split(r"(```.*?```)", text, flags=re.S))
    parts = re.split(r"(```.*?```|`[^`\n]+`)", text, flags=re.S)
    return "".join(p if p.startswith("`") else html_prose_to_md(p) for p in parts)


def html_cell(c):
    c = re.sub(r"(?is)<br\s*/?>|</?p[^>]*>", " ", c)
    c = re.sub(r"(?is)</?(code|tt)>", "`", c)
    c = re.sub(r"(?is)</?(b|strong)>", "**", c)
    c = re.sub(r"(?is)<a\s[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"[\2](\1)", c)
    c = re.sub(r"(?is)</?(?:span|div|i|em|sup|sub|small|font|img|ul|ol|li|nobr|center)(\s[^<>]*)?/?>", " ", c)
    return html.unescape(re.sub(r"\s+", " ", c).strip()).replace("|", "\\|")


def html_tables(t):
    """HTML tables as Markdown tables, the first row as the header."""
    def table(m):
        rows = []
        for r in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", m.group(0)):
            cells = [html_cell(c) for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", r)]
            if cells:
                rows.append(cells)
        if not rows:
            return m.group(0)
        n = max(len(r) for r in rows)
        rows = [r + [""] * (n - len(r)) for r in rows]
        lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n] + ["| " + " | ".join(r) + " |" for r in rows[1:]]
        return "\n\n" + "\n".join(lines) + "\n\n"
    return re.sub(r"(?is)<table[^>]*>.*?</table>", table, t)


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
    tags = r"(?:a|b|i|u|p|em|strong|code|tt|pre|span|div|table|thead|tbody|tr|td|th|ul|ol|li|dl|dt|dd|img|sup|sub|center|h[1-6]|hr|small|big|font|caption|col|colgroup|blockquote|details|summary|kbd|var|samp|cite|abbr|section|figure|figcaption|nobr)"
    t = re.sub(r"(?is)</?" + tags + r"(\s[^<>]*)?/?>", "", t)
    # Anything else in angle brackets is an XML element of the specification: keep it, as code.
    t = re.sub(r"(?<![`\w])<(/?[a-zA-Z][\w:.-]*)((?:\s[^<>]*)?)/?>(?!`)", lambda m: f"`<{m.group(1)}{m.group(2)}>`", t)
    return html.unescape(t).replace("\xa0", " ")


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


# ── reStructuredText ────────────────────────────────────────────────────────

RST_ADORN = re.compile(r"^([=\-~^*#+'`\"_:.])\1{2,}\s*$")
RST_DROP = ("toctree", "doxygengroup", "doxygenfunction", "doxygenstruct", "doxygentypedef", "doxygenenum", "doxygendefine",
            "doxygenfile", "contents", "image", "figure", "graphviz", "zephyr-app-commands", "zephyr:code-sample-category",
            "only", "raw", "include", "literalinclude", "kconfig:option", "zephyr:board-catalog", "tabs", "rst-class", "highlight",
            "versionadded", "versionchanged", "index", "uml", "plantuml", "csv-table", "tabularcolumns")


def rst_inline(t):
    t = re.sub(r":(?:c:)?(?:func|macro|type|struct|enum|member|var|data):`~?([^`<]+?)(?:\s*<[^>]+>)?`", r"`\1`", t)
    t = re.sub(r":(?:ref|doc|numref|zephyr:code-sample|zephyr:board)?:`([^`<]+?)\s*<[^>]+>`", r"\1", t)
    t = re.sub(r":(?:ref|doc|numref|zephyr:code-sample|zephyr:board):`([^`]+)`", r"\1", t)
    t = re.sub(r":[\w:+-]+:`([^`]+)`", r"`\1`", t)
    t = re.sub(r"`([^`<]+?)\s*<(https?://[^>]+)>`__?", r"[\1](\2)", t)
    t = re.sub(r"``([^`]+)``", r"`\1`", t)
    t = re.sub(r"(?<![`\w])`([^`]+)`_+", r"\1", t)
    return t


def rst_to_md(text):
    lines = text.replace("\t", "    ").splitlines()
    out, levels, i = [], [], 0
    # A Zephyr board page names its board in a directive, and its first title is "Overview": the board
    # becomes the page title and every section moves one level down.
    board = next((m.group(1) for m in (re.match(r"^\.\.\s+zephyr:board::\s*(\S+)", x) for x in lines) if m), None)
    offset = 1 if board else 0
    if board:
        out += [f"# {board}", ""]
    while i < len(lines):
        line = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        # Title: a line underlined (and maybe overlined) with one adornment character.
        if line.strip() and not RST_ADORN.match(line) and RST_ADORN.match(nxt) and len(nxt.strip()) >= len(line.strip()) - 1:
            over = i > 0 and RST_ADORN.match(lines[i - 1] or "") is not None
            key = (nxt.strip()[0], over)
            if key not in levels:
                levels.append(key)
            if over and out and RST_ADORN.match(out[-1] or ""):
                out.pop()
            out += ["", "#" * min(levels.index(key) + 1 + offset, 6) + " " + rst_inline(line.strip()), ""]
            i += 2
            continue
        if RST_ADORN.match(line) and i + 2 < len(lines) and RST_ADORN.match(lines[i + 2] or ""):
            i += 1            # an overline: the title follows
            continue
        d = re.match(r"^(\s*)\.\.\s+([\w:-]+)::\s*(.*)$", line)
        if d or re.match(r"^\s*\.\.\s+(_[\w -]+:|\|[^|]+\|)", line) or re.match(r"^\s*\.\.\s*$", line):
            indent = len(d.group(1)) if d else len(line) - len(line.lstrip())
            name = d.group(2) if d else ""
            j = i + 1
            block = []
            while j < len(lines) and (not lines[j].strip() or len(lines[j]) - len(lines[j].lstrip()) > indent):
                block.append(lines[j])
                j += 1
            while block and not block[-1].strip():
                block.pop()
            body = [b for b in block if not re.match(r"^\s*:[\w-]+:", b)]
            if name in ("code-block", "code", "sourcecode", "console"):
                lang = d.group(3).strip() if d else ""
                out += ["```" + lang] + dedent(body) + ["```"]
            elif name in ("note", "warning", "important", "tip", "caution", "attention", "hint"):
                text_ = " ".join(x.strip() for x in body if x.strip())
                out += ["", f"**{name.capitalize()}:** {rst_inline((d.group(3) + ' ' + text_).strip())}", ""]
            elif name in ("list-table",):
                out += [rst_inline(x) for x in dedent(body)]
            elif name and name not in RST_DROP and body and not name.startswith(("doxygen", "auto")):
                out += rst_to_md("\n".join(dedent(body))).splitlines()
            i = j
            continue
        if line.rstrip().endswith("::") and not line.strip().startswith(".."):
            # A literal block follows.
            out.append(rst_inline(line.rstrip()[:-1].rstrip() + (":" if line.strip() != "::" else "")))
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            indent = len(line) - len(line.lstrip())
            block = []
            while j < len(lines) and (not lines[j].strip() or len(lines[j]) - len(lines[j].lstrip()) > indent):
                block.append(lines[j])
                j += 1
            while block and not block[-1].strip():
                block.pop()
            out += ["```"] + dedent(block) + ["```"]
            i = j
            continue
        out.append(rst_inline(line))
        i += 1
    return "\n".join(out)


def dedent(block):
    widths = [len(b) - len(b.lstrip()) for b in block if b.strip()]
    cut = min(widths) if widths else 0
    return [b[cut:] for b in block]


# ── Hugo (Arm Learning Paths) ───────────────────────────────────────────────

def hugo_to_md(t):
    """Hugo shortcodes: notices become a bold label, tabs a bold heading, the rest goes."""
    t = re.sub(r"\{\{[<%]\s*notice\s*\"?([^\"%>]*?)\"?\s*[%>]\}\}", lambda m: f"**{(m.group(1) or 'Note').strip()}:**", t)
    t = re.sub(r"\{\{[<%]\s*tab\s+header=\"([^\"]+)\"[^}]*[%>]\}\}", r"**\1:**", t)
    t = re.sub(r"\{\{[<%]\s*/?[\w-]+[^}]*[%>]\}\}", "", t)
    return re.sub(r"(?m)^(#{1,6} .*?)\s*\{#[\w.-]+\}\s*$", r"\1", t)


def liquid_to_md(t):
    """Jekyll pages: Liquid tags and diagram blocks go, a link to another post keeps its slug as text."""
    t = re.sub(r"(?s)\{%\s*blockdiag\s*%\}.*?\{%\s*endblockdiag\s*%\}", "", t)
    t = re.sub(r"(?s)\{%\s*comment\s*%\}.*?\{%\s*endcomment\s*%\}", "", t)
    t = re.sub(r"\{%\s*post_url\s+\d{4}-\d{2}-\d{2}-([\w-]+)\s*%\}", r"https://interrupt.memfault.com/blog/\1", t)
    t = re.sub(r"\{%-?\s*(?:raw|endraw)\s*-?%\}", "", t)
    t = re.sub(r"\{%[^%]*%\}", "", t)
    t = re.sub(r"(?s)<!--.*?-->", "", t)
    return t


def as_list(v):
    return [str(x) for x in v] if isinstance(v, list) else [str(v)] if v else []


def path_overview(fm, steps):
    """The _index.md of a Learning Path keeps its content in the front matter: make it a page."""
    out = [f"# {fm.get('title', '')}", "", str(fm.get("description", "")).strip(), ""]
    for key, label in (("who_is_this_for", "Who is this for"), ("learning_objectives", "Learning objectives"),
                       ("prerequisites", "Prerequisites")):
        items = as_list(fm.get(key))
        if len(items) == 1:
            out += [f"**{label}:** {items[0]}", ""]
        elif items:
            out += [f"**{label}:**", ""] + [f"- {x}" for x in items] + [""]
    if steps:
        out += ["**Steps:**", ""] + [f"{i}. {t}" for i, t in enumerate(steps, 1)] + [""]
    if fm.get("minutes_to_complete"):
        out += [f"Time: about {fm['minutes_to_complete']} minutes."]
    return "\n".join(out)


def path_index(folder):
    """(front matter of the folder's _index.md, step titles in weight order), cached per folder."""
    if folder not in _PATH_INDEX:
        idx = folder / "_index.md"
        fm = strip_front_matter(idx.read_text(encoding="utf-8", errors="replace"))[1] if idx.exists() else {}
        steps = []
        for f in folder.glob("*.md"):
            if f.name.startswith("_"):
                continue
            sfm = strip_front_matter(f.read_text(encoding="utf-8", errors="replace"))[1]
            steps.append((sfm.get("weight", 99), str(sfm.get("title", f.stem))))
        _PATH_INDEX[folder] = (fm, [t for _, t in sorted(steps)])
    return _PATH_INDEX[folder]


_PATH_INDEX = {}


# ── Markdown pages -> sections ──────────────────────────────────────────────

def strip_front_matter(t):
    m = re.match(r"---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n", t, re.S)
    if not m:
        return t, {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return t[m.end():], fm if isinstance(fm, dict) else {}


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
                # A heading that is a link, as in "## [Signing images](#signing-images)": its text.
                title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", m.group(2)).strip()
                out.append((len(m.group(1)), title, pos, pos + len(line)))
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
        # Emphasis marks go; an underscore inside a name such as app_main stays.
        p = re.sub(r"[`*]|(?<!\w)_(?=\S)|(?<=\S)_(?!\w)", "", " ".join(p.split()))
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
        if target.startswith("/"):
            # A site-root link: relative to the host of the published page.
            return f"[{label}]({re.match(r'https?://[^/]+', page_url).group(0)}{target})"
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
        stem = re.sub(src.get("stem_strip", "^$"), "", Path(rel).stem.lstrip("_"))
        if stem.lower() in ("index", "readme"):
            stem = ""
        page_id = "index" if page_id == "mainpage" else page_id
        return re.sub(r"(?<!:)//+", "/", tpl.format(stem=stem, page=page_id, path=rel, dir=str(Path(rel).parent).removeprefix(src.get("dir_strip", "")),
                                                    name=Path(rel).parent.name))
    if src.get("host"):
        return f"{src['host']}/{src['repo']}/-/blob/{src['commit']}/{rel}"
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
        suffixes = (".md", ".txt", ".c", ".h") if src.get("format") == "doxtxt" else (".md", ".txt", ".rst")
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
            if fmt == "hugo":
                body = hugo_to_md(body)
            if fmt == "jekyll":
                body = liquid_to_md(body)
            tags = {str(x).lower() for x in as_list(fm.get("tags"))}
            if (src.get("exclude_tags") and tags & set(src["exclude_tags"])) or \
                    (src.get("include_tags") and not tags & set(src["include_tags"])):
                continue
            body = doxmd_to_md(body) if fmt in ("doxmd", "doxtxt") else rst_to_md(body) if f.suffix == ".rst" else html_to_md(body)
            title = str(fm.get("title", "")).strip()
            if src.get("path_index"):
                pfm, steps = path_index(f.parent)
                if f.name == "_index.md":
                    body = path_overview(fm, steps) + "\n" + body
                elif pfm.get("title") and title:
                    title = f"{pfm['title']}: {title}"
            if title and not any(h[0] == 1 for h in headings(body)):
                body = f"# {title}\n" + body
            pages = [(f.stem, "", body)]
        for page_id, _title, md in pages:
            if PAGE_SKIP.match(_title.strip()) or page_id in ("rev_hist", "revision_history", "changelog"):
                continue
            page_url = page_url_of(src, rel, page_id)
            page_title, secs = sections(md)
            if not page_title:
                # No H1: the file name, and for a generic one (README, DESIGN, SPEC) the source's name in front.
                stem = Path(rel).stem.replace("_", " ").replace("-", " ")
                page_title = f"{src['name']} {stem}" if stem.lower() in GENERIC_STEMS else stem
            for path, text_ in secs:
                if prose_chars(text_) < MIN_CHARS or (path and SECTION_SKIP.match(path[-1].strip())):
                    continue
                name = path[-1] if path else page_title
                title = f"{page_title}: {' / '.join(path)}" if path else page_title
                # GitHub renders Markdown with heading anchors, not doxygen files; a published site has its own.
                anchored = src.get("anchors", True) and (src.get("url") or f.suffix.lower() == ".md")
                anchor = "#" + slug(path[-1], 80) if path and anchored else ""
                body = rewrite_links(text_.strip(), page_url)
                if len(path) == 2:
                    body = f"_Part of: {path[0]}_\n\n" + body
                if src.get("id_from_path"):
                    stem = f.stem.lstrip("_")
                    base = f"{src['prefix']}-{slug(f.parent.name, 34)}" + (f"-{slug(stem, 24)}" if stem != "index" else "") \
                        + (f"-{slug(name, 30)}" if path else "")
                else:
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


def fetch(src, repo):
    url = f"{src.get('host', 'https://github.com')}/{src['repo']}.git"
    sparse = src.get("sparse")
    cmd = ["git", "clone", "-q", "--depth", "1"] + (["--filter=blob:none", "--sparse"] if sparse else []) + [url, str(repo)]
    subprocess.run(cmd, check=True)
    if sparse:
        subprocess.run(["git", "-C", str(repo), "sparse-checkout", "set"] + list(sparse), check=True)


def main(cfg, docs, out, only=None, get=False):
    sources = yaml.safe_load(Path(cfg).read_text(encoding="utf-8"))["sources"]
    out = Path(out)
    used = set()
    total = 0
    expanded = []
    for src in sources:
        # A source with `multi:` is several small repositories under one collection name.
        for part in src.get("multi") or [None]:
            expanded.append({**src, **part, "multi": None, "first": part is src["multi"][0]} if part else src)
    cleared = set()
    for src in expanded:
        if only and src["name"] not in only:
            continue
        if src.get("mode", "V") != "V":
            print(f"{src['name']:28s} skipped: mode {src.get('mode')}")
            continue
        repo = Path(docs) / src.get("dir", src["repo"].split("/")[-1])
        if not repo.exists() and get:
            print(f"{src['name']:28s} cloning {src['repo']}")
            fetch(src, repo)
        elif repo.exists() and get and src.get("sparse"):
            # A second source on the same sparse clone adds its paths.
            subprocess.run(["git", "-C", str(repo), "sparse-checkout", "add"] + list(src["sparse"]), check=False)
        if not repo.exists():
            print(f"{src['name']:28s} missing clone {repo}")
            continue
        target = out / src["name"]
        if target.exists() and src["name"] not in cleared:
            for old in target.glob("*.md"):
                old.unlink()
        cleared.add(src["name"])
        n = convert(src, repo, out, used)
        total += n
        print(f"{src['name']:28s} {n:4d} units  {src['repo']}@{src['commit']}  {src['license']}")
    print(f"total {total}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only = None
    for a in sys.argv[1:]:
        if a.startswith("--only="):
            only = set(a.split("=", 1)[1].split(","))
    if len(args) != 3:
        sys.exit(__doc__)
    main(*args, only=only, get="--fetch" in sys.argv)

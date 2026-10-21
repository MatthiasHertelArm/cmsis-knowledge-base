#!/usr/bin/env python3
"""sources_md: SOURCES.md of an index build, the attribution of everything the index contains.

For the given unit folders it lists every source: the repository, the licence, what was taken (skills,
tool messages, documentation, issue digests in own words) and how many units; then, as the licences
require, the copyright lines and the full licence text of every MIT and BSD-3-Clause source, one
reference block for the Apache-2.0 sources with the copyright lines of their licence files and the text
of every NOTICE file a source ships, and a section on the issue digests with the repositories they
summarise. The units are the authority for what is in the index (their `source`, `license`, `mode` and
`collection`); sources/docs.yml gives the documentation sources their names and hosts.

The licence files themselves are read once with --fetch: from the clone in .work/docs/<dir> when it
exists, else from GitHub (gh when logged in, the public API otherwise) or gitlab.arm.com. The raw files
are cached under .work/licenses/ (git-ignored), and what SOURCES.md needs of them (licence identifier,
licence file, copyright lines, NOTICE text) is written to sources/licenses.yml, which is committed, so a
clean checkout regenerates SOURCES.md without network. The MIT and BSD-3-Clause texts come from the
SPDX templates below with the copyright lines substituted; the Apache-2.0 text is referenced by URL and
identifier, since the LICENSE file of the CMSIS Developer Assistant accompanies the shipped index.

Usage: tools/sources_md.py --units <dir> [--units <dir> ...] [--out build/SOURCES.md] [--recipe core]
                           [--fetch] [--refresh] [--registry sources/licenses.yml] [--cache .work/licenses]
                           [--clones .work/docs]
Run from the repository root. Warnings (a licence that could not be identified, a copyright line that is
missing, a mismatch with what the units declare) go to stderr; the exit code stays 0 so that a build
without network still writes the file.
"""
import argparse, datetime, json, os, re, subprocess, sys, textwrap, urllib.parse, urllib.request
from collections import Counter, OrderedDict
from pathlib import Path

import yaml

GITHUB = "https://github.com"
SKILL_REPOS = {"skills": "Open-CMSIS-Pack/cmsis-skills", "canonical": "Open-CMSIS-Pack/cmsis-skills",
               "cda-skills": "Open-CMSIS-Pack/CMSIS-Developer-Assistant", "cda-routes": "Open-CMSIS-Pack/CMSIS-Developer-Assistant"}
CDA_SKILL_FOLDERS = ("cda-skills", "cda-routes")
# Clones outside .work/docs: fetch_sources.py keeps these two next to it.
EXTRA_CLONES = {"Open-CMSIS-Pack/cmsis-skills": Path(".work/cmsis-skills"), "Open-CMSIS-Pack/devtools": Path(".work/devtools")}
SOURCE_NAMES = {"Open-CMSIS-Pack/cmsis-skills": "cmsis-skills", "Open-CMSIS-Pack/CMSIS-Developer-Assistant": "CMSIS-Developer-Assistant",
                "Open-CMSIS-Pack/devtools": "devtools"}
TAKEN = {"skills": "Agent Skills: procedures, rules, concepts and their files",
         "tool messages": "tool messages (the message tables of packchk, svdconv, csolution); causes and fixes in own words",
         "documentation": "documentation",
         "issue digests": "issue digests in own words, each linked to its thread"}
KIND_ORDER = ("skills", "tool messages", "documentation", "issue digests")
PINNED = re.compile(r"^([\w.-]+(?:/[\w.-]+)+)@[0-9a-f]+:")
ISSUE_URL = re.compile(r"^https://github\.com/([\w.-]+/[\w.-]+)/(?:issues|discussions|pull)/\d+")
LICENSE_FILE = re.compile(r"^(licen[cs]e|copying)", re.I)
NOTICE_FILE = re.compile(r"^notice(\.(txt|md|rst))?$", re.I)
COPYRIGHT_LINE = re.compile(r"\bcopyright\b\s*(\(c\)|©|\d{4})", re.I)
ISSUE_LICENSE = "own summary of a GitHub issue"

MIT_TEXT = """MIT License

{copyright}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and \
associated documentation files (the "Software"), to deal in the Software without restriction, including \
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell \
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the \
following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial \
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT \
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO \
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER \
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR \
THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

BSD3_TEXT = """{copyright}

Redistribution and use in source and binary forms, with or without modification, are permitted provided \
that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and \
the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and \
the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or \
promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED \
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A \
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR \
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED \
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) \
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING \
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE \
POSSIBILITY OF SUCH DAMAGE."""

TEMPLATES = {"MIT": MIT_TEXT, "BSD-3-Clause": BSD3_TEXT}
APACHE_URL = "https://www.apache.org/licenses/LICENSE-2.0"

warnings = []


def warn(msg):
    warnings.append(msg)
    print("sources_md: " + msg, file=sys.stderr)


def frontmatter(p):
    m = re.match(r"---\n(.*?)\n---", p.read_text(encoding="utf-8"), re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


# ── the sources, from the units ─────────────────────────────────────────────────────────────────────

def docs_sources(docs_yml):
    """name -> {host, repos: [repo...], dirs: {repo: clone dir}} in the order of sources/docs.yml."""
    out = OrderedDict()
    for s in yaml.safe_load(Path(docs_yml).read_text(encoding="utf-8"))["sources"]:
        entries = s.get("multi") or [s]
        repos, dirs = [], {}
        for e in entries:
            repo = e.get("repo", s.get("repo"))
            repos.append(repo)
            dirs[repo] = e.get("dir") or s.get("dir") or repo.split("/")[-1]
        out[s["name"]] = {"host": s.get("host", GITHUB), "repos": repos, "dirs": dirs}
    return out


def scan_units(dirs, docs):
    """rows: (kind, name, repo) -> count; repos: repo -> {host, dir, declared: Counter}; issue repos: repo -> count."""
    rows, repos, issues = Counter(), {}, Counter()
    cda_skills = set()
    for d in dirs:
        if Path(d).name in CDA_SKILL_FOLDERS:
            for p in Path(d).rglob("*.md"):
                cda_skills.add(str(frontmatter(p).get("source", "")).split("/")[0])

    def repo_of(meta, folder):
        src = str(meta.get("source", ""))
        m = ISSUE_URL.match(src)
        if m:
            return m.group(1), "issue digests", None
        m = PINNED.match(src)
        if m:
            kind = "tool messages" if meta.get("domain") == "error-catalog" else "documentation"
            return m.group(1), kind, meta.get("collection")
        if folder in SKILL_REPOS:
            return SKILL_REPOS[folder], "skills", None
        if src.split("/")[0] in cda_skills:
            return SKILL_REPOS["cda-skills"], "skills", None
        return SKILL_REPOS["skills"], "skills", None

    for d in dirs:
        folder = Path(d).name
        for p in sorted(Path(d).rglob("*.md")):
            meta = frontmatter(p)
            repo, kind, coll = repo_of(meta, folder)
            if kind == "issue digests":
                issues[repo] += 1
                continue
            if kind == "documentation":
                name = coll if coll in docs else next((n for n, s in docs.items() if repo in s["repos"]), None)
                if name is None:
                    name = coll or repo.split("/")[-1]
                    warn(f"{repo} ({p}) is not a source of sources/docs.yml")
                if len(docs.get(name, {}).get("repos", [])) > 1:
                    name = f"{name} ({repo.split('/')[-1]})"
            else:
                name = SOURCE_NAMES.get(repo, repo.split("/")[-1])
            rows[(kind, name, repo)] += 1
            src = next((s for s in docs.values() if repo in s["repos"]), None)
            r = repos.setdefault(repo, {"host": src["host"] if src else GITHUB,
                                        "dir": src["dirs"][repo] if src else repo.split("/")[-1], "declared": Counter()})
            r["declared"][str(meta.get("license"))] += 1
    return rows, repos, issues


# ── the licence files ───────────────────────────────────────────────────────────────────────────────

def detect_spdx(text):
    t = " ".join(text.split())
    if "Apache License" in t and "Version 2.0" in t:
        return "Apache-2.0"
    if "Permission is hereby granted, free of charge" in t:
        return "MIT"
    if "Redistribution and use in source and binary forms" in t:
        return "BSD-3-Clause" if re.search(r"neither the name|endorse or promote", t, re.I) else "BSD-2-Clause"
    return "unknown"


def copyright_lines(text):
    return [re.sub(r"\s+", " ", ln).strip() for ln in text.splitlines() if COPYRIGHT_LINE.search(ln)]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def pick_license(names, declared):
    cands = [n for n in names if LICENSE_FILE.match(n)]
    if not cands:
        return None
    if len(cands) == 1:
        return cands[0]
    want = norm(declared or "")
    by_id = [n for n in cands if want and want in norm(n)]
    if by_id:
        return sorted(by_id)[0]
    plain = [n for n in cands if norm(n) in ("license", "licensetxt", "licensemd", "licenserst", "licence", "copying")]
    return sorted(plain or cands)[0]


def pick_notice(names):
    cands = sorted(n for n in names if NOTICE_FILE.match(n))
    return cands[0] if cands else None


def gh_api(path, raw=False):
    """GitHub REST: gh when it is logged in, else the public API (GITHUB_TOKEN honoured)."""
    accept = "application/vnd.github.raw" if raw else "application/vnd.github+json"
    try:
        r = subprocess.run(["gh", "api", "-H", f"Accept: {accept}", path], capture_output=True, text=True, timeout=60)
        if r.returncode == 0:
            return r.stdout if raw else json.loads(r.stdout)
        if "HTTP 404" in r.stderr or "Not Found" in r.stderr:
            return None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    req = urllib.request.Request("https://api.github.com/" + path, headers={"Accept": accept, "User-Agent": "sources_md"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read().decode("utf-8")
    except urllib.error.HTTPError as ex:
        if ex.code == 404:
            return None
        raise
    return data if raw else json.loads(data)


def gitlab_api(host, path, raw=False):
    req = urllib.request.Request(f"{host}/api/v4/{path}", headers={"User-Agent": "sources_md"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read().decode("utf-8")
    except urllib.error.HTTPError as ex:
        if ex.code == 404:
            return None
        raise
    return data if raw else json.loads(data)


def remote_files(host, repo):
    """(names, reader) of the repository root on its host."""
    if host == GITHUB:
        listing = gh_api(f"repos/{repo}/contents/") or []
        names = [e["name"] for e in listing if e.get("type") == "file"]
        return names, lambda n: gh_api(f"repos/{repo}/contents/{urllib.parse.quote(n)}", raw=True)
    pid = urllib.parse.quote(repo, safe="")
    branch = (gitlab_api(host, f"projects/{pid}") or {}).get("default_branch", "main")
    listing = gitlab_api(host, f"projects/{pid}/repository/tree?ref={branch}&per_page=100") or []
    names = [e["name"] for e in listing if e.get("type") == "blob"]
    return names, lambda n: gitlab_api(host, f"projects/{pid}/repository/files/{urllib.parse.quote(n, safe='')}/raw?ref={branch}", raw=True)


def fetch_repo(repo, info, clones, cache, declared):
    """The licence and NOTICE files of one repository: from the cache, the clone, or the host. Returns a registry entry."""
    cdir = cache / repo.replace("/", "__")
    meta_file = cdir / "meta.json"
    if meta_file.exists():
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
    else:
        clone = EXTRA_CLONES.get(repo) or (clones / info["dir"]).resolve()
        if clone.is_dir():
            names = [p.name for p in clone.iterdir() if p.is_file()]
            read, origin = (lambda n: (clone / n).read_text(encoding="utf-8", errors="replace")), f"clone {clone}"
        else:
            names, read = remote_files(info["host"], repo)
            origin = info["host"]
        lic, notice = pick_license(names, declared), pick_notice(names)
        meta = {"license_file": lic, "notice_file": notice, "origin": origin, "fetched": datetime.date.today().isoformat()}
        cdir.mkdir(parents=True, exist_ok=True)
        for n in (lic, notice):
            if n:
                (cdir / n).write_text(read(n), encoding="utf-8")
        meta_file.write_text(json.dumps(meta, indent=1), encoding="utf-8")
        print(f"  {repo}: licence {lic or '-'}, notice {notice or '-'} ({origin})")
    entry = OrderedDict(repo=repo, host=info["host"], spdx="unknown", license_file=meta["license_file"], copyright=[],
                        notice_file=meta["notice_file"], notice=None, fetched=meta["fetched"])
    if meta["license_file"]:
        text = (cdir / meta["license_file"]).read_text(encoding="utf-8")
        entry["spdx"], entry["copyright"] = detect_spdx(text), copyright_lines(text)
    if meta["notice_file"]:
        entry["notice"] = (cdir / meta["notice_file"]).read_text(encoding="utf-8").rstrip() + "\n"
    return entry


def load_registry(path):
    if not Path(path).exists():
        return OrderedDict()
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    return OrderedDict((e["repo"], e) for e in data.get("repositories", []))


def save_registry(path, entries):
    class Dumper(yaml.SafeDumper):
        pass

    def str_presenter(dumper, s):
        return dumper.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None)

    Dumper.add_representer(str, str_presenter)
    Dumper.add_representer(OrderedDict, lambda d, data: d.represent_dict(data.items()))
    head = ("# The licence files of the repositories the knowledge units come from, as tools/sources_md.py --fetch read\n"
            "# them: the identifier detected in the licence file, the file's name, its copyright lines and the text of\n"
            "# the repository's NOTICE file. Committed so that SOURCES.md regenerates without network; --refresh reads\n"
            "# the files again. Issue repositories are not listed: their digests are own summaries.\n")
    body = yaml.dump({"repositories": list(entries.values())}, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=110)
    Path(path).write_text(head + body, encoding="utf-8")


# ── SOURCES.md ──────────────────────────────────────────────────────────────────────────────────────

def file_url(entry, name):
    sep = "/-/blob/HEAD/" if entry["host"] != GITHUB else "/blob/HEAD/"
    return f"{entry['host']}/{entry['repo']}{sep}{name}"


def kb_commit():
    try:
        sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "units", "sources", "tools"], capture_output=True, text=True).stdout.strip()
        return sha + (" (with uncommitted changes)" if dirty else "")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def fence(text):
    return "```text\n" + text.rstrip("\n") + "\n```\n"


def wrap(text):
    return "\n".join(textwrap.fill(par, 96, break_on_hyphens=False, break_long_words=False) if par.strip() else ""
                     for par in text.split("\n"))


def render(recipe, dirs, rows, repos, issues, registry):
    total = sum(rows.values()) + sum(issues.values())
    out = []
    out.append("# Sources of the CMSIS knowledge index\n")
    out.append(wrap(
        f"The knowledge index of the CMSIS Developer Assistant (recipe `{recipe}`, `core.db` in the extension) is built from "
        f"{total} knowledge units in Markdown, the folders {', '.join('`' + d + '`' for d in dirs)} of the "
        "cmsis-knowledge-base repository: procedures, rules and concepts converted from Agent Skills; the message tables of "
        "the CMSIS tools with causes and fixes in own words; documentation of repositories under an open licence; and "
        "digests of public GitHub issues written in own words. Every unit names its origin in its frontmatter: `source` "
        "(repository, commit and file, the skill file, or the URL of the issue), `license` (the SPDX identifier of the text, "
        "or the marker of an own summary) and `mode` (`V`, text taken from the source; `S`, an own summary with a link). "
        "This file lists the sources, what was taken from each, their licences, and the copyright lines, licence texts and "
        "NOTICE texts those licences require. It is generated by `tools/sources_md.py` from the units, `sources/docs.yml` and "
        f"`sources/licenses.yml`; the units are those of commit {kb_commit()} of the knowledge base.") + "\n")
    # The table
    out.append("## Sources\n")
    out.append(wrap("One row per source and repository. *Units* counts the units of the folders above; a recipe's drop "
                    "rule (`build_core.sh` leaves out the issue digests of low confidence) can ship fewer.") + "\n")
    out.append("<!-- sources:table:begin -->")
    out.append("| Source | Repository | Licence | What was taken | Units |")
    out.append("| --- | --- | --- | --- | --- |")
    for (kind, name, repo), n in sorted(rows.items(), key=lambda kv: (KIND_ORDER.index(kv[0][0]), row_order(kv[0]))):
        e = registry.get(repo)
        declared = ", ".join(sorted(repos[repo]["declared"]))
        if e and e.get("license_file"):
            lic = f"[{declared}]({file_url(e, e['license_file'])})"
        else:
            lic = declared
        out.append(f"| {name} | [{repo}]({repos[repo]['host']}/{repo}) | {lic} | {TAKEN[kind]} | {n} |")
    for repo, n in sorted(issues.items()):
        out.append(f"| issues of {repo.split('/')[-1]} | [{repo}]({GITHUB}/{repo}/issues) | own summaries | {TAKEN['issue digests']} | {n} |")
    out.append("<!-- sources:table:end -->\n")
    # Licence texts
    out.append("## Licence texts\n")
    by_lic = {}
    for repo, info in repos.items():
        for lic in info["declared"]:
            by_lic.setdefault(lic, []).append(repo)
    for lic in ("MIT", "BSD-3-Clause"):
        if lic not in by_lic:
            continue
        name = "MIT License" if lic == "MIT" else "BSD 3-Clause License"
        out.append(f"### {name} (SPDX `{lic}`)\n")
        out.append(wrap(f"The text taken from these repositories is licensed under the {name}. The licence asks that the "
                        "copyright notice and the licence text accompany it; both follow, the copyright lines as the "
                        "repository's licence file carries them.") + "\n")
        for repo in sorted(by_lic[lic]):
            e = registry.get(repo)
            out.append(f"#### {repo}\n")
            if not e or not e.get("license_file"):
                out.append(wrap(f"The licence file of {repo} has not been recorded in `sources/licenses.yml` "
                                "(run `tools/sources_md.py --fetch`).") + "\n")
                continue
            if e.get("spdx") != lic:
                out.append(wrap(f"Note: the licence file `{e['license_file']}` reads as {e.get('spdx')}, the units declare "
                                f"{lic}; to be reviewed.") + "\n")
            lines = e.get("copyright") or []
            if not lines:
                lines = [f"(no copyright line in {e['license_file']} of {repo})"]
            out.append(f"From [`{e['license_file']}`]({file_url(e, e['license_file'])}):\n")
            out.append(fence(wrap(TEMPLATES[lic].format(copyright="\n".join(lines)))))
    if "Apache-2.0" in by_lic:
        out.append("### Apache License 2.0 (SPDX `Apache-2.0`)\n")
        apache = sorted(by_lic["Apache-2.0"])
        out.append(wrap(f"The text taken from the other {len(apache)} repositories of the table is licensed under the Apache "
                        f"License, Version 2.0: <{APACHE_URL}>. The full licence text is in each repository's licence file, "
                        "linked in the table, and in the `LICENSE` file of the CMSIS Developer Assistant, which accompanies "
                        "the shipped index. The copyright lines their licence files carry, and the NOTICE files the licence "
                        "asks to be passed on (section 4 d), follow.") + "\n")
        out.append("#### Copyright lines\n")
        any_line = False
        for repo in apache:
            e = registry.get(repo)
            if e and e.get("copyright"):
                any_line = True
                for ln in e["copyright"]:
                    out.append(f"- {repo}: {ln}")
        if any_line:
            out.append("")
        without = [r for r in apache if not (registry.get(r) or {}).get("copyright")]
        if without:
            out.append(wrap("The licence files of the other repositories carry no copyright line: " + ", ".join(without) + ".") + "\n")
        notices = [(r, registry[r]) for r in apache if registry.get(r, {}).get("notice")]
        out.append("#### NOTICE files\n")
        if notices:
            for repo, e in notices:
                out.append(f"##### {repo}\n")
                out.append(f"From [`{e['notice_file']}`]({file_url(e, e['notice_file'])}):\n")
                out.append(fence(e["notice"]))
        else:
            out.append("None of these repositories ships a NOTICE file.\n")
        unrecorded = [r for r in apache if r not in registry]
        if unrecorded:
            out.append(wrap("Not yet recorded in `sources/licenses.yml` (run `tools/sources_md.py --fetch`): " + ", ".join(unrecorded) + ".") + "\n")
    odd = sorted(l for l in by_lic if l not in ("MIT", "BSD-3-Clause", "Apache-2.0"))
    for lic in odd:
        out.append(f"### {lic}\n")
        out.append(wrap("Declared by the units of: " + ", ".join(sorted(by_lic[lic])) + ". No licence text is recorded for it.") + "\n")
    # Issue digests
    if issues:
        out.append("## Issue digests\n")
        out.append(wrap(f"The {sum(issues.values())} units of `units/issues` are summaries in our own words of public GitHub "
                        "issues and discussions (`mode: S`, `license: \"" + ISSUE_LICENSE + "\"`): the problem, its cause and "
                        "the fix as the thread established them, with the error message that identifies the problem as the "
                        "symptom. Each unit links to the thread it summarises. The threads are in these repositories:") + "\n")
        for repo, n in sorted(issues.items()):
            out.append(f"- [{repo}]({GITHUB}/{repo}/issues): {n} digest{'s' if n != 1 else ''}")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def row_order(key):
    kind, name, repo = key
    return (ROW_ORDER.get(name.split(" (")[0], 10_000), name, repo)


ROW_ORDER = {}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--units", action="append", required=True, help="a unit folder of the recipe; repeat")
    ap.add_argument("--out", default="build/SOURCES.md")
    ap.add_argument("--recipe", default="core")
    ap.add_argument("--docs", default="sources/docs.yml")
    ap.add_argument("--registry", default="sources/licenses.yml")
    ap.add_argument("--cache", default=".work/licenses")
    ap.add_argument("--clones", default=".work/docs")
    ap.add_argument("--fetch", action="store_true", help="read the licence files of repositories the registry lacks")
    ap.add_argument("--refresh", action="store_true", help="with --fetch: read every repository again")
    a = ap.parse_args()

    docs = docs_sources(a.docs)
    ROW_ORDER.update({name: i for i, name in enumerate(docs)})
    rows, repos, issues = scan_units(a.units, docs)
    registry = load_registry(a.registry)
    if a.fetch:
        cache = Path(a.cache)
        if a.refresh:
            for d in cache.glob("*/meta.json"):
                d.unlink()
            registry = OrderedDict()
        for repo, info in sorted(repos.items()):
            if repo not in registry:
                declared = sorted(info["declared"], key=lambda l: -info["declared"][l])[0]
                try:
                    registry[repo] = fetch_repo(repo, info, Path(a.clones), cache, declared)
                except Exception as ex:  # one unreachable host must not lose the others
                    warn(f"{repo}: fetch failed ({ex})")
        save_registry(a.registry, registry)
    # Checks: every repository recorded, its licence identified, the identifier the units declare.
    for repo, info in sorted(repos.items()):
        e = registry.get(repo)
        declared = set(info["declared"])
        if not e:
            warn(f"{repo}: no licence record (run with --fetch)")
            continue
        if e.get("spdx") == "unknown":
            warn(f"{repo}: licence of {e.get('license_file') or 'no licence file'} not identified")
        elif e.get("spdx") not in declared:
            warn(f"{repo}: licence file says {e['spdx']}, the units declare {', '.join(sorted(declared))}")
        if declared & {"MIT", "BSD-3-Clause"} and not e.get("copyright"):
            warn(f"{repo}: no copyright line in {e.get('license_file')}")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(a.recipe, a.units, rows, repos, issues, registry), encoding="utf-8")
    n_lic = Counter()
    for info in repos.values():
        for l in info["declared"]:
            n_lic[l] += 1
    print(f"{out}: {len(rows)} source rows, {len(repos)} repositories ({', '.join(f'{n} {l}' for l, n in sorted(n_lic.items()))}), "
          f"{len(issues)} issue repositories, {sum(1 for e in registry.values() if e.get('notice'))} NOTICE files, {len(warnings)} warnings")


if __name__ == "__main__":
    main()

"""The CMSIS debug adapter registry -> one concept unit per debug adapter.

Usage: python adapters2ku.py <debug-adapter-registry checkout> <out-dir>

registry/debug-adapters.yml lists every adapter that `debugger: name:` in a csolution project may
name: its aliases, its launch template, the defaults cbuild writes into *.cbuild-run.yml, and the
options the CMSIS Solution extension shows. Each adapter becomes units/.../dbgadapter-<name>.md, so
that "which debugger name for an ST-Link" or "default GDB port of J-Link" finds the answer.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = "Open-CMSIS-Pack/debug-adapter-registry"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def word(v):
    """YAML 1.1 reads on/off as booleans; the registry means the words."""
    return {True: "on", False: "off", None: ""}.get(v, v) if isinstance(v, (bool, type(None))) else v


def option_rows(sections):
    rows = []
    for sec in sections or []:
        base = sec.get("yml-node", "")
        for opt in sec.get("options") or []:
            node = ".".join(x for x in (base, opt.get("yml-node", "")) if x)
            values = ", ".join(f"`{word(v.get('value'))}` ({v.get('name')})" for v in opt.get("values") or [])
            rng = f"{opt['range'][0]} to {opt['range'][1]}" if opt.get("range") else ""
            rows.append(f"| {sec.get('section', '')} | {opt.get('name', '')} | `{node}` | {opt.get('type', '')} | "
                        f"{word(opt.get('default', ''))} | {values or rng} |")
    return rows


def main(repo, out):
    repo, out = Path(repo), Path(out)
    commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    data = yaml.safe_load((repo / "registry/debug-adapters.yml").read_text(encoding="utf-8"))
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()
    for a in data["debug-adapters"]:
        name = a["name"]
        aliases = a.get("alias-name") or []
        names = ", ".join(f"`{n}`" for n in [name] + aliases)
        body = [f"Names accepted in `debugger: name:` of a csolution project: {names}.",
                f"Launch and task template of the CMSIS Solution extension: `{a.get('template', '')}`."]
        if a.get("defaults"):
            body.append("## Defaults\n\nWhat cbuild writes into `*.cbuild-run.yml` when the project sets nothing:\n\n```yaml\n"
                        + yaml.safe_dump(a["defaults"], sort_keys=False).replace(": null", ":").strip() + "\n```")
        rows = option_rows(a.get("user-interface"))
        if rows:
            body.append("## Options\n\nWhat the CMSIS Solution extension offers for this adapter (the YAML node under `debugger:`):\n\n"
                        "| Section | Option | Node | Type | Default | Values |\n|---|---|---|---|---|---|\n" + "\n".join(rows))
        example = f"debugger:\n  name: {aliases[0] if aliases else name}"
        body.append("## Example\n\n```yaml\n" + example + "\n```")
        uid = f"dbgadapter-{slug(name)}"
        summary = f"Debug adapter {name}" + (f" (also {', '.join(aliases)})" if aliases else "") + \
            ": the names csolution accepts, the defaults cbuild writes into cbuild-run.yml, and its options."
        meta = dict(id=uid, type="concept", domain="debug", title=f"Debug adapter {name}: names, defaults and options",
                    summary=summary, status="draft", collection="debug-adapter-registry",
                    source=f"{REPO}@{commit}:registry/debug-adapters.yml",
                    doc_source=f"https://github.com/{REPO}/blob/{commit}/registry/debug-adapters.yml",
                    applies_to={"tool": ["cbuild", "csolution"]}, license="Apache-2.0", mode="V",
                    triggers=[name] + aliases)
        fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
        (out / f"{uid}.md").write_text(f"---\n{fm}\n---\n\n" + "\n\n".join(body) + "\n", encoding="utf-8")
    print(f"{len(data['debug-adapters'])} debug adapters  {REPO}@{commit}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])

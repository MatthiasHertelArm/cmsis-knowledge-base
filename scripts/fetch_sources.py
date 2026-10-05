#!/usr/bin/env python3
"""Fetch the inputs for a full rebuild into a work folder.

  - Keil pack index (index.pidx) and every active PDSC, via the keil.com/pack mirror
    (vendor URLs on github raw are often blocked by proxies; the mirror serves all PDSC files)
  - Open-CMSIS-Pack/cmsis-skills and Open-CMSIS-Pack/devtools (shallow git clones)

Usage: python scripts/fetch_sources.py <work-dir>
"""
import concurrent.futures as cf, subprocess, sys, time, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

INDEX = "https://www.keil.com/pack/index.pidx"
MIRROR = "https://www.keil.com/pack/{}"
REPOS = {"cmsis-skills": "https://github.com/Open-CMSIS-Pack/cmsis-skills",
         "devtools": "https://github.com/Open-CMSIS-Pack/devtools"}


def get(url, dst, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                dst.write_bytes(r.read())
            return True
        except Exception:
            time.sleep(2 * (i + 1))
    return False


def main(work):
    work = Path(work)
    (work / "pdsc").mkdir(parents=True, exist_ok=True)
    print("index.pidx ...")
    if not get(INDEX, work / "index.pidx"):
        sys.exit("cannot download " + INDEX)
    vendor_url = {}
    for p in ET.parse(work / "index.pidx").getroot().iter("pdsc"):
        if "deprecated" not in p.attrib:
            f = f"{p.get('vendor')}.{p.get('name')}.pdsc"
            vendor_url[f] = p.get("url", "").rstrip("/") + "/" + f
    todo = [f for f in vendor_url if not (work / "pdsc" / f).exists()]
    print(f"{len(vendor_url)} active packs, {len(todo)} PDSC to fetch ...")
    # Mirror first, vendor URL as fallback
    fetch = lambda f: get(MIRROR.format(f), work / "pdsc" / f) or get(vendor_url[f], work / "pdsc" / f, tries=1)
    with cf.ThreadPoolExecutor(8) as ex:
        ok = sum(ex.map(fetch, todo))
    missing = [f for f in vendor_url if not (work / "pdsc" / f).exists()]
    print(f"fetched {ok} of {len(todo)}, missing {len(missing)}: {', '.join(missing[:10])}")
    if any(f.startswith("ARM.") for f in missing):
        print("WARNING: ARM packs missing, CMSIS components will not resolve. Run the script again.")
    for name, url in REPOS.items():
        if not (work / name).exists():
            subprocess.run(["git", "clone", "-q", "--depth", "1", url, str(work / name)], check=True)
        print(name, subprocess.run(["git", "-C", str(work / name), "rev-parse", "--short", "HEAD"],
                                   capture_output=True, text=True).stdout.strip())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])

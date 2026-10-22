#!/usr/bin/env python3
"""fetch_issues: the GitHub threads the issue digests are written from, through the GraphQL API.

Writes one JSON list per repository into <out>, in the shape the readers' batches had and
tools/model_run.py reads: {url, title, labels, state, closed, body, comments[str], open}.

  closed issues   stateReason COMPLETED (or none), at least one comment, closed on or after --since
  open issues     at least one comment, updated on or after --since; marked open
  discussions     the Q&A discussions of the repositories in DISCUSSIONS with an accepted answer,
                  updated on or after --since; the answer is the first comment

Usage: python tools/fetch_issues.py <out> [--since YYYY-MM-DD] [--manifest stage2/issues-out.manifest.json]
--manifest reads `since` from the runner's manifest (the newest thread of the last run) when --since
is not given; without either, the last 90 days. Needs GH_TOKEN or GITHUB_TOKEN.
"""
import argparse
import datetime
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

REPOS = ["pyocd/pyOCD", "Open-CMSIS-Pack/devtools", "Open-CMSIS-Pack/cmsis-toolbox", "Open-CMSIS-Pack/cpackget",
         "Open-CMSIS-Pack/vscode-cmsis-debugger", "Open-CMSIS-Pack/vscode-cmsis-solution",
         "ARM-software/CMSIS_6", "ARM-software/CMSIS-RTX", "ARM-software/CMSIS-View"]
DISCUSSIONS = ["pyocd/pyOCD"]
API = "https://api.github.com/graphql"
MAX_COMMENTS = 10          # stored; the runner cuts to the readers' eight
BODY_MAX = 20000

ISSUES = """
query($owner: String!, $name: String!, $since: DateTime!, $states: [IssueState!], $after: String) {
  repository(owner: $owner, name: $name) {
    issues(first: 50, states: $states, filterBy: {since: $since}, orderBy: {field: UPDATED_AT, direction: DESC}, after: $after) {
      pageInfo { hasNextPage endCursor }
      nodes { number url title body state stateReason closedAt updatedAt
              labels(first: 10) { nodes { name } }
              comments(first: %d) { totalCount nodes { body author { login } } } }
    }
  }
}""" % MAX_COMMENTS
DISCUSSION_QUERY = """
query($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 50, orderBy: {field: UPDATED_AT, direction: DESC}, after: $after) {
      pageInfo { hasNextPage endCursor }
      nodes { url title body updatedAt category { name } answer { body }
              comments(first: %d) { nodes { body } } }
    }
  }
}""" % MAX_COMMENTS


def graphql(token, query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(API, data=body, headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
                                                          "User-Agent": "cmsis-knowledge-base fetch_issues"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read())
            if "errors" in data and not data.get("data"):
                raise RuntimeError(json.dumps(data["errors"])[:400])
            return data["data"]
        except Exception as e:
            if attempt == 4:
                raise
            print(f"  retry after {e}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))


def thread(n, open_=False):
    comments = [c["body"] for c in n["comments"]["nodes"] if c.get("body")]
    return {"url": n["url"], "title": n["title"], "labels": [l["name"] for l in n["labels"]["nodes"]],
            "state": n["state"] if not open_ else "OPEN", "closed": (n.get("closedAt") or "")[:10],
            "updated": (n.get("updatedAt") or "")[:10], "body": (n.get("body") or "")[:BODY_MAX], "comments": comments,
            **({"open": True} if open_ else {})}


def fetch_repo(token, repo, since):
    owner, name = repo.split("/")
    out = []
    for states, open_ in (("CLOSED", False), ("OPEN", True)):
        after = None
        while True:
            d = graphql(token, ISSUES, {"owner": owner, "name": name, "since": since + "T00:00:00Z", "states": [states], "after": after})
            conn = d["repository"]["issues"]
            for n in conn["nodes"]:
                if n["comments"]["totalCount"] < 1:
                    continue
                if not open_:
                    if n.get("stateReason") not in (None, "COMPLETED") or (n.get("closedAt") or "")[:10] < since:
                        continue
                out.append(thread(n, open_))
            if not conn["pageInfo"]["hasNextPage"]:
                break
            after = conn["pageInfo"]["endCursor"]
    return out


def fetch_discussions(token, repo, since):
    owner, name = repo.split("/")
    out, after = [], None
    while True:
        d = graphql(token, DISCUSSION_QUERY, {"owner": owner, "name": name, "after": after})
        conn = d["repository"]["discussions"]
        stop = False
        for n in conn["nodes"]:
            if (n.get("updatedAt") or "")[:10] < since:
                stop = True
                break
            if not n.get("answer") or (n.get("category") or {}).get("name") != "Q&A":
                continue
            comments = ["[accepted answer] " + n["answer"]["body"]] + [c["body"] for c in n["comments"]["nodes"] if c.get("body")]
            out.append({"url": n["url"], "title": n["title"], "labels": ["Q&A"], "state": "DISCUSSION", "closed": "",
                        "updated": n["updatedAt"][:10], "body": (n.get("body") or "")[:BODY_MAX], "comments": comments[:MAX_COMMENTS]})
        if stop or not conn["pageInfo"]["hasNextPage"]:
            break
        after = conn["pageInfo"]["endCursor"]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out")
    ap.add_argument("--since")
    ap.add_argument("--manifest")
    a = ap.parse_args()
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GH_TOKEN or GITHUB_TOKEN is not set")
    since = a.since
    if not since and a.manifest and Path(a.manifest).exists():
        since = json.loads(Path(a.manifest).read_text(encoding="utf-8")).get("since") or ""
    if not since:
        since = (datetime.date.today() - datetime.timedelta(days=90)).isoformat()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    total = 0
    for repo in REPOS:
        threads = fetch_repo(token, repo, since)
        if repo in DISCUSSIONS:
            threads += fetch_discussions(token, repo, since)
        (out / (repo.replace("/", "_") + ".json")).write_text(json.dumps(threads, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        total += len(threads)
        print(f"{repo:42s} {len(threads):4d} threads since {since}")
    print(f"total {total} -> {out}")


if __name__ == "__main__":
    main()

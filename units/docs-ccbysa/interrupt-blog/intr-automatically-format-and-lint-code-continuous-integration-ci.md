---
id: "intr-automatically-format-and-lint-code-continuous-integration-ci"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit: Continuous Integration (CI)"
summary: "An article on tooling would hardly be complete without discussing continuous integration 😄"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit#continuous-integration-ci"
license: "CC-BY-SA-4.0"
mode: "V"
---

An article on tooling would hardly be complete without discussing [continuous
integration](https://interrupt.memfault.com/blog/continuous-integration-for-firmware) 😄

Here's a couple of examples of how `pre-commit` could be used in CI:

1. The following command will lint all configured files:

   ```bash
   pre-commit run --all-files
   ```

   It's excellent if you want to keep all files polished in CI.

2. If you want to only lint the _changes_ to files (for example, if you're
   incrementally linting/formatting files rather than in One Big Commit), you
   can set the `${TARGET_BRANCH}` from your CI provider (in GitHub Actions, this
   would be `${{ github.event.pull_request.base.ref }}`

   ```bash
   pre-commit run --from-ref $(git merge-base ${TARGET_BRANCH}) --to-ref HEAD
   ```









{:.no_toc}

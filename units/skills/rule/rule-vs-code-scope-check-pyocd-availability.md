---
type: "rule"
title: "VS Code scope"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-vs-code-scope-check-pyocd-availability"
constrains: ["proc-check-pyocd-availability"]
---

Check the active extension before PATH in a Visual Studio Code environment. Prefer a verified bundled directory and do not perform a redundant PATH check. A bundled directory does not establish that `pyocd` is runnable from the current `PATH`.

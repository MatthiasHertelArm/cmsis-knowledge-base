---
id: "ceed-cppcheck-artifacts"
type: "concept"
domain: "test"
title: "Cppcheck: Artifacts"
summary: "Reports are written to build/artifacts/cppcheck/:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#artifacts"
license: "MIT"
mode: "V"
---

Reports are written to `build/artifacts/cppcheck/`:

| Report | Path |
|--------|------|
| HTML | `build/artifacts/cppcheck/html/index.html` |
| SARIF | `build/artifacts/cppcheck/CppcheckReport.sarif` |
| Text | `build/artifacts/cppcheck/CppcheckReport.txt` |
| XML | `build/artifacts/cppcheck/CppcheckReport.xml` |

Filenames other than the HTML directory are configurable. See the
`*_artifact_filename` settings above.

These artifacts are included in `ceedling clean` targets.

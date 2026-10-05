---
id: "ceed-supported-tool-versions"
type: "concept"
domain: "test"
title: "Supported tool versions"
summary: "At the time of the last major updates to the Gcov plugin, the following notes on version compatibility were known to be accurate."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/tool-versions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/tool-versions/"
license: "MIT"
mode: "V"
---

_**Last updated:**_ May 17, 2026

At the time of the last major updates to the Gcov plugin, the following notes
on version compatibility were known to be accurate.

Keep in mind that for proper functioning, you do not necessarily need to
install all the tooks the Gcov plugin works with. Depending on configuration
options documented in later sections, any of the following tool combinations
may be sufficient for your needs:

1. `gcov`
1. `gcov` + `gcovr`
1. `gcov` + `reportgenerator`
1. `gcov` + `gcovr` + `reportgenerator`

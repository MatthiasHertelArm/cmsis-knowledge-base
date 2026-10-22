---
id: "ceed-supported-tool-versions-reportgenerator"
type: "concept"
domain: "test"
title: "Supported tool versions: `reportgenerator`"
summary: "The Gcov plugin is known to work with reportgenerator 5.2.4. The command line for executing reportgenerator that the Gcov plugin relies on has largely been stable since version 4. We recommend using reportgenerator 5.0 and later."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/gcov/tool-versions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/tool-versions/#reportgenerator"
license: "MIT"
mode: "V"
---

The Gcov plugin is known to work with `reportgenerator` 5.2.4. The command line
for executing `reportgenerator` that the Gcov plugin relies on has largely been
stable since version 4. We recommend using `reportgenerator` 5.0 and later.

Unlike `gcovr`, the plugin does not detect the installed `reportgenerator`
version or gate any option on it.

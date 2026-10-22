---
id: "ceed-release-build-output"
type: "concept"
domain: "test"
title: "`:release_build`: `:output`"
summary: "The name of your release build binary artifact to be found in <build path>/artifacts/release/. Ceedling sets the default artifact file extension to that as is explicitly specified in the :extension section or as is system specific otherwise."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/release-build.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/release-build/#output"
license: "MIT"
mode: "V"
---

The name of your release build binary artifact to be found in 
_<build path>/artifacts/release/_. Ceedling sets the default artifact 
file extension to that as is explicitly specified in the `:extension`
section or as is system specific otherwise.

**Default**: `project.exe` or `project.out`

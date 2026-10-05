---
id: "ceed-cipher-quest-exporting"
type: "concept"
domain: "test"
title: "`cipher_quest`: Exporting"
summary: "After exporting, run ceedling test:all from the project root to execute the full test suite, or ceedling release to produce a release binary. Note that the release build requires configuration from you to provide needed symbols."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/getting-started/example-projects/cipher-quest.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/cipher-quest/#exporting"
license: "MIT"
mode: "V"
---

```shell
ceedling example cipher_quest [destination]
```

After exporting, run `ceedling test:all` from the project root to execute the
full test suite, or `ceedling release` to produce a release binary. Note that
the release build requires configuration from you to provide needed symbols.

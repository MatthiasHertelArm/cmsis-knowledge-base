---
id: "ceed-sanitize-artifacts"
type: "concept"
domain: "test"
title: "Sanitize: Artifacts"
summary: "Each test with findings has a log of its sanitizer reports:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#artifacts"
license: "MIT"
mode: "V"
---

Each test with findings has a log of its sanitizer reports:

```
build/artifacts/sanitize/sanitize/<test_name>.log
```

The configured reports are written beside the logs:

```
build/artifacts/sanitize/sanitize/sanitize.log
build/artifacts/sanitize/sanitize/sanitize.json
build/artifacts/sanitize/sanitize/sanitize.sarif
```

With `:test_builds` enabled, an ordinary `test:` build writes its logs and
reports to `build/artifacts/sanitize/test/`.

The artifacts are included in `ceedling clean` targets.

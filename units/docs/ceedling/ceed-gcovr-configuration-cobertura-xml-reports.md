---
id: "ceed-gcovr-configuration-cobertura-xml-reports"
type: "concept"
domain: "test"
title: "GCovr Configuration: Cobertura XML reports"
summary: "Generation of Cobertura XML reports may be modified with the following configuration items."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#cobertura-xml-reports"
license: "MIT"
mode: "V"
---

Generation of Cobertura XML reports may be modified with the following configuration items.

### `:cobertura_pretty`

Pretty-print the Cobertura XML report. (`gcovr --xml-pretty`)

**Default:** `false`

---

### `:cobertura_artifact_filename`

Override the default Cobertura XML report output filename.

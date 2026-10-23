---
id: "ceed-gcovr-configuration-jacoco-xml-reports"
type: "concept"
domain: "test"
title: "GCovr Configuration: JaCoCo XML reports"
summary: "A JaCoCo XML report is a coverage format that Java-oriented tools and IDEs such as CLion import. Enable it with JaCoCo in :gcov ↳ :reports."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#jacoco-xml-reports"
license: "MIT"
mode: "V"
---

A JaCoCo XML report is a coverage format that Java-oriented tools and IDEs such as
CLion import. Enable it with `JaCoCo` in `:gcov` ↳ `:reports`.

**Requires:** `gcovr` 7.0 or higher. An older `gcovr` stops the build.

Generation of JaCoCo XML reports may be modified with the following configuration items.

### `:jacoco_pretty`

Pretty-print the JaCoCo XML report. (`gcovr --jacoco-pretty`)

**Default:** `false`

---

### `:jacoco_artifact_filename`

Override the default JaCoCo XML report output filename.

**Default:** `GcovCoverageJaCoCo.xml`

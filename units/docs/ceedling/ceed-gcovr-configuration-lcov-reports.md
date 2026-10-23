---
id: "ceed-gcovr-configuration-lcov-reports"
type: "concept"
domain: "test"
title: "GCovr Configuration: LCOV reports"
summary: "An LCOV info file is the coverage format of the lcov toolset that many coverage viewers and services read. Enable it with lcov in :gcov ↳ :reports. ReportGenerator also writes lcov, each utility into its own artifacts folder."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#lcov-reports"
license: "MIT"
mode: "V"
---

An LCOV info file is the coverage format of the `lcov` toolset that many coverage
viewers and services read. Enable it with `lcov` in `:gcov` ↳ `:reports`.
ReportGenerator also writes `lcov`, each utility into its own artifacts folder.

**Requires:** `gcovr` 7.0 or higher. An older `gcovr` stops the build when it is the
only enabled utility. With ReportGenerator also enabled, an older `gcovr` logs a
warning and leaves `lcov` to ReportGenerator.

Generation of LCOV reports may be modified with the following configuration items.

### `:lcov_comment`

Set a comment in the LCOV report. (`gcovr --lcov-comment`)

---

### `:lcov_test_name`

Set the test name recorded in the LCOV report. (`gcovr --lcov-test-name`)

---

### `:lcov_artifact_filename`

Override the default LCOV report output filename.

**Default:** `GcovCoverage.lcov`

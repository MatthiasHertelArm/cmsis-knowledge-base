---
id: "ceed-gcovr-configuration-html-reports"
type: "concept"
domain: "test"
title: "GCovr Configuration: HTML reports"
summary: "Generation of HTML reports may be modified with the following configuration items."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#html-reports"
license: "MIT"
mode: "V"
---

Generation of HTML reports may be modified with the following configuration items.

### `:html_artifact_filename`

Override the default HTML report output filename.

---

### `:html_title`

Use `title` as the title for the HTML report. (`gcovr --html-title`)

**Default:** `Head`

---

### `:html_medium_threshold`

If the coverage is below this value, it is marked as low coverage in the HTML
report. Must be lower than or equal to `:html_high_threshold`. If equal to
`:html_high_threshold`, the report has only high and low coverage.
(`gcovr --html-medium-threshold`)

**Default:** `75.0`

---

### `:html_high_threshold`

If the coverage is below this value, it is marked as medium coverage in the
HTML report. Must be greater than or equal to `:html_medium_threshold`. If
equal to `:html_medium_threshold`, the report has only high and low coverage.
(`gcovr --html-high-threshold`)

**Default:** `90.0`

---

### `:html_absolute_paths`

Use absolute paths to link the "detailed" reports. Defaults to relative
links. (`gcovr --html-absolute-paths`)

---

### `:html_encoding`

Override the declared HTML report encoding. (`gcovr --html-encoding`)

**Default:** `UTF-8`

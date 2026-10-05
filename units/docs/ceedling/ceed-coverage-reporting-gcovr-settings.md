---
id: "ceed-coverage-reporting-gcovr-settings"
type: "concept"
domain: "test"
title: "Coverage Reporting: GCovr Settings"
summary: "All options below live under :gcov: ↳ :gcovr:. Reports are written to <build root>/artifacts/gcov/gcovr/."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/gcov-plugin.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/gcov-plugin/#gcovr-settings"
license: "MIT"
mode: "V"
---

All options below live under `:gcov:` ↳ `:gcovr:`. Reports are written to
`<build root>/artifacts/gcov/gcovr/`.

### `:report_root`

Root directory of your source files; file names in reports are relative to
this path.

**Default:** `"."` (current directory)

---

### `:config_file`

Load a `gcovr` configuration file. (`gcovr --config`)

**Default:** `gcovr.cfg` in the `:report_root` directory, if present.

---

### `:fail_under_line`

Exit with status 2 if total line coverage is below this percentage.
(`gcovr --fail-under-line`)

**Values:** `1`–`100`

---

### `:fail_under_branch`

Exit with status 4 if total branch coverage is below this percentage.
(`gcovr --fail-under-branch`)

**Values:** `1`–`100`

---

### `:fail_under_decision`

Exit with status 8 if total decision coverage is below this percentage.
(`gcovr --fail-under-decision`)

`gcovr` treats `--fail-under-decision` as a no-op without `--decisions` also
present — setting this option implies `:decisions` (below) automatically.

**Values:** `1`–`100`

**Requires:** `gcovr` 7.0 or higher

---

### `:decisions`

Report the decision coverage. For HTML, JSON, and the summary report.
(`gcovr --decisions`)

Implied automatically whenever `:fail_under_decision` is set.

**Requires:** `gcovr` 5.1 or higher

---

### `:fail_under_function`

Exit with status 16 if total function coverage is below this percentage.
(`gcovr --fail-under-function`)

**Values:** `1`–`100`

---

### `:exception_on_fail`

When any `:fail_under_*` threshold is set, raise a build-breaking exception
instead of only logging a warning.

**Default:** `FALSE`

---

### `:source_encoding`

Source file character encoding. (`gcovr --source-encoding`)

**Default:** system default (typically `UTF-8`)

---

### `:branches`

Report branch coverage instead of line coverage. Applies to text reports only.
Uses `gcovr --txt-metric branch` on `gcovr` 7.0+ (`--branches` is deprecated as
of 7.0, though still functional); `gcovr --branches` below it.

---

### `:sort_uncovered`

Sort report entries by increasing number of uncovered lines. Applies to text
and HTML reports. Uses `gcovr --sort uncovered-number` on `gcovr` 7.0+
(`--sort-uncovered` is deprecated as of 7.0, though still functional);
`gcovr --sort-uncovered` below it.

---

### `:sort_percentage`

Sort report entries by increasing percentage of uncovered lines. Applies to
text and HTML reports. Uses `gcovr --sort uncovered-percent` on `gcovr` 7.0+
(`--sort-percentage` is deprecated as of 7.0, though still functional);
`gcovr --sort-percentage` below it.

---

### `:print_summary`

Print a brief line- and branch-coverage summary to stdout in addition to any
other reports. (`gcovr --print-summary`)

---

### `:report_include`

Keep only source files matching this regular expression filter.
(`gcovr --filter`)

**Example:** `"^src"`

---

### `:report_exclude`

Exclude source files matching this regular expression filter.
(`gcovr --exclude`)

**Example:** `"^vendor.*|^build.*|^test.*|^lib.*"`

---

### `:gcov_filter`

Keep only `.gcov` data files matching this regular expression filter.
(`gcovr --gcov-filter`)

---

### `:gcov_exclude`

Exclude `.gcov` data files matching this regular expression filter.
(`gcovr --gcov-exclude`)

---

### `:exclude_directories`

Exclude directories matching this regular expression filter when searching for
raw coverage files. (`gcovr --exclude-directories`)

---

### `:gcov_executable`

Use a specific `gcov` executable instead of the one on `PATH`.
(`gcovr --gcov-executable`)

---

### `:exclude_unreachable_branches`

Exclude branch coverage from lines without useful source code.
(`gcovr --exclude-unreachable-branches`)

---

### `:exclude_throw_branches`

Exclude compiler-generated exception-handling branches from branch coverage.
(`gcovr --exclude-throw-branches`)

---

### `:merge_mode_function`

Controls how `gcovr` handles multiple coverage entries for the same function
(e.g. when Ceedling tests the same source under multiple build configurations).

**Default:** `merge-use-line-max`

See the [gcovr merging docs](https://gcovr.com/en/stable/guide/merging.html)
for all valid values.

---

### `:use_gcov_files`

Use existing `.gcov` files on disk instead of running `gcov` again.
(`gcovr --use-gcov-files`)

**Default:** `FALSE`

---

### `:gcov_ignore_parse_errors`

Skip lines with parse errors in `.gcov` files rather than exiting with an
error. (`gcovr --gcov-ignore-parse-errors`)

---

### `:object_directory`

Override normal working-directory detection for `.gcda` / `.gcno` files.
(`gcovr --object-directory`)

---

### `:keep`

Retain intermediate `.gcov` files after processing. (`gcovr --keep`)

---

### `:delete`

Delete `.gcda` files after processing. (`gcovr --delete`)

---

### `:threads`

Number of parallel threads to use during report generation. (`gcovr -j`)

---

### `:html_artifact_filename`

Override the default HTML report output filename.

---

### `:html_title`

Title text for the HTML report. (`gcovr --html-title`)

**Default:** `Head`

---

### `:html_medium_threshold`

Coverage percentage below which a value is marked as low coverage in the HTML
report. Must be ≤ `:html_high_threshold`. (`gcovr --html-medium-threshold`)

**Default:** `75.0`

---

### `:html_high_threshold`

Coverage percentage below which a value is marked as medium coverage in the
HTML report. Must be ≥ `:html_medium_threshold`. (`gcovr --html-high-threshold`)

**Default:** `90.0`

---

### `:html_absolute_paths`

Use absolute paths when linking to detailed reports in the HTML output.
(`gcovr --html-absolute-paths`)

**Default:** relative links

---

### `:html_encoding`

Override the declared character encoding in the HTML report.
(`gcovr --html-encoding`)

**Default:** `UTF-8`

---

### `:cobertura_pretty`

Pretty-print the Cobertura XML report. (`gcovr --xml-pretty`)

**Default:** `FALSE`

---

### `:cobertura_artifact_filename`

Override the default Cobertura XML report output filename.

---

### `:sonarqube_artifact_filename`

Override the default SonarQube XML report output filename.

---

### `:json_pretty`

Pretty-print the JSON report. (`gcovr --json-pretty`)

**Default:** `FALSE`

---

### `:json_artifact_filename`

Override the default JSON report output filename.

---

### `:text_artifact_filename`

Override the default text report output filename. When unset the text report
is printed to the console.

---

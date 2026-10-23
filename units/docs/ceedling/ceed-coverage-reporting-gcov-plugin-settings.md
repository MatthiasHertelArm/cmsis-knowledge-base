---
id: "ceed-coverage-reporting-gcov-plugin-settings"
type: "concept"
domain: "test"
title: "Coverage Reporting: `gcov` Plugin Settings"
summary: "Options avialable directly beneath :gcov."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/reference/gcov-plugin.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/gcov-plugin/#gcov-plugin-settings"
license: "MIT"
mode: "V"
---

Options avialable directly beneath `:gcov`.

### `:summaries`

Enable or disable automatic console coverage summaries printed after each
`gcov:` task.

**Default:** `TRUE`

```yaml
:gcov:
  :summaries: FALSE
```

---

### `:mcdc`

Enable or disable Modified Condition / Decision Coverage in coverage results.
This feature is dependent on minimum tool versions.

**Default:** `FALSE`

```yaml
:gcov:
  :mcdc: TRUE
```

---

### `:untested_sources`

!!! warning
    **Compiling all untested sources for 0% coverage reporting (`:compile`) will likely require additional work.**

    Successful compilation of untested source files may require certain symbols 
    to be defined, certain flags to be set, or entire stand-in shims for platform 
    headers and code.
    
    Ceedling’s 
    [`:defines`](https://throwtheswitch.github.io/Ceedling/reference/gcov-plugin/../configuration/reference/defines.md)
    and 
    [`:flags`](https://throwtheswitch.github.io/Ceedling/reference/gcov-plugin/../configuration/reference/flags.md)
    matchers can provide these. For GCov tasks, symbols and flags are extracted from
    the `:test` context beneath the `:defines` and `:flags` configuration sections 
    by default. If you need something special for coverage builds, use the `:gcov` 
    context for these matchers instead.

Controls handling of source files not exercised by any test. Valid values:

* `:ignore` — Skip untested sources entirely (no logging, no compilation).
* `:list` — Log the filepaths of untested sources as a warning; do not compile them.
* `:compile` — Compile all untested sources with coverage so they appear in
  the report at 0% coverage. On compilation failure, Ceedling logs
  guidance and fails the build.

**Default:** `:list`

```yaml
:gcov:
  :untested_sources: :list
```

When `:untested_sources` is set to `:compile`, a `gcov:untested_sources` task is
also available, letting you re-run just the untested-source compilation step
on its own — without a full `gcov:` test suite run — while iterating on source
compilation fixes.

---

### `:utilities`

List of report generation utilities to enable. Valid values are `gcovr` and
`ReportGenerator`. Either or both may be specified.

**Default:** `[gcovr]` (when `:reports:` is configured and `:utilities:` is absent)

```yaml
:gcov:
  :utilities:
    - gcovr
    - ReportGenerator
```

---

### `:report_task`

When `TRUE`, disables automatic report generation after `gcov:` tasks and
instead enables a separate `report:gcov` Ceedling task for on-demand report
generation.

**Default:** `FALSE`

```yaml
:gcov:
  :report_task: TRUE
```

---

### `:reports`

List of report types to generate. When empty or absent, report generation
(but not coverage summaries) is disabled.

```yaml
:gcov:
  :reports:
    - HtmlBasic
    - HtmlDetailed
    - ...
```

| Report option | gcovr | ReportGenerator |
|---|:---:|:---:|
| `HtmlBasic` | ✓ | ✓ |
| `HtmlDetailed` | ✓ | ✓ |
| `Text` | ✓ | ✓ |
| `Cobertura` | ✓ | ✓ |
| `SonarQube` | ✓ | ✓ |
| `JSON` | ✓ | |
| `HtmlInline` | | ✓ |
| `HtmlInlineAzure` | | ✓ |
| `HtmlInlineAzureDark` | | ✓ |
| `HtmlChart` | | ✓ |
| `MHtml` | | ✓ |
| `Badges` | | ✓ |
| `CsvSummary` | | ✓ |
| `Latex` | | ✓ |
| `LatexSummary` | | ✓ |
| `PngChart` | | ✓ |
| `TeamCitySummary` | | ✓ |
| `lcov` | | ✓ |
| `Xml` | | ✓ |
| `XmlSummary` | | ✓ |

---

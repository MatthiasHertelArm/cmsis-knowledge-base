---
id: "ceed-coverage-reporting-reportgenerator-settings"
type: "concept"
domain: "test"
title: "Coverage Reporting: ReportGenerator Settings"
summary: "All options below live under :gcov: ↳ :report_generator:. Reports are written to <build root>/artifacts/gcov/ReportGenerator/."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/gcov-plugin.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/gcov-plugin/#reportgenerator-settings"
license: "MIT"
mode: "V"
---

All options below live under `:gcov:` ↳ `:report_generator:`. Reports are
written to `<build root>/artifacts/gcov/ReportGenerator/`.

### `:history_directory`

Optional directory for storing persistent coverage history, enabling
coverage-trend charts across builds.

---

### `:plugins`

Optional semicolon-separated list of plugin DLL files for custom report types
or custom history storage.

**Example:** `plugin.dll;*.dll`

---

### `:assembly_filters`

Optional semicolon-separated list of assembly inclusion/exclusion filters.
Prefix `+` to include, `-` to exclude. Exclusions take precedence. Wildcards
allowed (not regular expressions).

**Example:** `+MyLib;-ThirdParty`

---

### `:class_filters`

Optional semicolon-separated list of class inclusion/exclusion filters. Same
prefix and wildcard rules as `:assembly_filters`.

---

### `:file_filters`

Optional semicolon-separated list of file inclusion/exclusion filters. Same
prefix and wildcard rules as `:assembly_filters`.

**Example:** `"-./vendor/*;-./build/*;-./test/*;+./src/*"`

---

### `:verbosity`

Verbosity level for ReportGenerator log output.

**Values:** `Verbose`, `Info`, `Warning`, `Error`, `Off`

**Default:** `Warning`

---

### `:tag`

Optional build tag or version label embedded in the report.

---

### `:gcov_exclude`

Optional list of regular expressions; `.gcov` notes files whose paths match
are excluded from report generation.

```yaml
:gcov:
  :report_generator:
    :gcov_exclude:
      - <regex>
```

---

### `:num_parallel_threads`

Number of parallel threads to use during report generation. Drives both
ReportGenerator's own `numberOfReportsParsedInParallel` and
`numberOfReportsMergedInParallel` settings together.

**Default:** unset (ReportGenerator's own default applies)

---

### `:custom_args`

Optional list of additional command-line arguments passed directly to
ReportGenerator. Useful for configuring Risk Hotspots and other settings not
covered by the options above. See the
[ReportGenerator settings wiki](https://github.com/danielpalme/ReportGenerator/wiki/Settings).

```yaml
:gcov:
  :report_generator:
    :custom_args:
      - <argument>
```

---
id: "ceed-reportgenerator-configuration-plugin-configuration"
type: "concept"
domain: "test"
title: "ReportGenerator Configuration: Plugin configuration"
summary: "Optional directory for storing persistent coverage information. Can be used in future reports to show coverage evolution."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/reportgenerator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/reportgenerator/#plugin-configuration"
license: "MIT"
mode: "V"
---

### `:history_directory`

Optional directory for storing persistent coverage information. Can be used
in future reports to show coverage evolution.

---

### `:plugins`

Optional plugin files for custom reports or custom history storage (separated
by semicolon).

**Example:** `plugin.dll;*.dll`

---

### `:assembly_filters`

Optional list of assemblies that should be included or excluded in the
report (separated by semicolon). Exclusion filters take precedence over
inclusion filters. Wildcards are allowed, but not regular expressions.

**Example:** `+<included>;-<excluded>`

---

### `:class_filters`

Optional list of classes that should be included or excluded in the report
(separated by semicolon). Exclusion filters take precedence over inclusion
filters. Wildcards are allowed, but not regular expressions.

**Example:** `+<included>;-<excluded>`

---

### `:file_filters`

Optional list of files that should be included or excluded in the report
(separated by semicolon). Exclusion filters take precedence over inclusion
filters regardless of order. Wildcards are allowed, but not regular
expressions.

This plugin places your own patterns first, ahead of the exclusions it
generates automatically for test paths, the build root, and (when Partials
are in use) Partial-generated files (see
[Report filtering](#report-filtering) above for exactly what those defaults
cover). Because exclusions always win, your patterns can add further
exclusions or includes but cannot override or remove one of those defaults;
see [Overriding the defaults](#overriding-the-defaults) above.

**Example:** `"-./vendor/*;-./build/*;-./test/*;-./lib/*;+./src/*"`

---

### `:verbosity`

The verbosity level of the log messages.

**Values:** `Verbose`, `Info`, `Warning`, `Error`, `Off`

**Default:** `Warning`

---

### `:tag`

Optional tag or build version.

---

### `:gcov_exclude`

Optional list of one or more regular expressions to exclude gcov notes
(`.gcno`) files that match these filters from coverage processing — these
files are never run through `gcov` at all. A trailing `.gcov` or `.gcno`
suffix on a pattern is stripped automatically, so either form works.

Ceedling combines your patterns with exclusions it generates automatically
for test files, mocks, test runners, and vendored Unity/CMock sources (see
[Coverage generation filtering](#coverage-generation-filtering) above for
exactly what these cover). Your patterns can only add further exclusions;
there's no way to override or remove one of the defaults — see
[Overriding the defaults](#overriding-the-defaults) above.

```yaml
:gcov:
  :report_generator:
    :gcov_exclude:
      - <regex>
      - ...
```

**Default:** `[]`

---

### `:num_parallel_threads`

Optionally set the number of threads ReportGenerator uses in parallel. Drives
both of ReportGenerator's own `numberOfReportsParsedInParallel` and
`numberOfReportsMergedInParallel` settings together.

**Default:** unset (ReportGenerator's own default applies)

---

### `:custom_args`

Optional list of one or more command line arguments to pass to Report
Generator. Useful for configuring Risk Hotspots and other settings not
covered by the options above. See the
[ReportGenerator settings wiki](https://github.com/danielpalme/ReportGenerator/wiki/Settings).

Note: This can be accomplished with Ceedling's tool configuration options
outside of plugin configuration but is supported here to collect
configuration options in one place.

```yaml
:gcov:
  :report_generator:
    :custom_args:
      - <argument>
      - ...
```

**Default:** `[]`

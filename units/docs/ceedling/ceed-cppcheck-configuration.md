---
id: "ceed-cppcheck-configuration"
type: "concept"
domain: "test"
title: "Cppcheck: Configuration"
summary: "All settings live in a top-level :cppcheck section of your project file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#configuration"
license: "MIT"
mode: "V"
---

All settings live in a top-level `:cppcheck` section of your project file.

```yaml
:cppcheck:
  :reports:
    - html
  :addons:
    - misra
```

### `:reports:`

The report formats to produce. Each entry costs its own analysis pass.

* `html` — Browsable HTML. Requires `cppcheck-htmlreport` and implies `xml`.
* `sarif` — SARIF, consumed by many code-scanning dashboards.
* `text` — Plain text.
* `xml` — Cppcheck's own XML schema.

```yaml
:cppcheck:
  :reports:
    - text
    - html
```

**Default:** `[]` (no reports, so `cppcheck:all` analyzes nothing and says so)

### `:fail_build:`

When `true`, findings matching [`:fail_build_severities:`](#fail_build_severities)
fail the build. Enabling this implies the `xml` report, because findings are
counted from Cppcheck's own XML output.

```yaml
:cppcheck:
  :fail_build: true
```

**Default:** `false`

Cppcheck exits successfully even when it finds defects, so without this setting
a `cppcheck:all` run can never fail a CI build.

### `:fail_build_severities:`

Which finding severities fail the build when
[`:fail_build:`](#fail_build) is enabled. Valid values are `error`, `warning`,
`style`, `performance`, `portability`, and `information`. An unrecognized value
is rejected when the plugin loads.

```yaml
:cppcheck:
  :fail_build_severities:
    - error
    - warning
```

**Default:** `[error]`

!!! tip "Why not every severity by default"
    Whole project analysis always runs with `--enable=all`, so a typical run
    reports many `style` and `information` findings. Failing on all of them
    would make this setting impractical on most projects.

### `:html_title:`

Title shown in the HTML report.

```yaml
:cppcheck:
  :html_title: Awesome Project
```

**Default:** unset

### `:sarif_artifact_filename:`

Filename for the SARIF report.

```yaml
:cppcheck:
  :sarif_artifact_filename: CppcheckResults.sarif
```

**Default:** `CppcheckReport.sarif`

### `:text_artifact_filename:`

Filename for the text report.

```yaml
:cppcheck:
  :text_artifact_filename: CppcheckResults.txt
```

**Default:** `CppcheckReport.txt`

### `:template:`

Output format for the text report. Accepts any template name Cppcheck ships
with, such as `gcc`, or a custom format string.

```yaml
:cppcheck:
  :template: gcc
```

**Default:** unset (Cppcheck's own default)

### `:xml_artifact_filename:`

Filename for the XML report.

```yaml
:cppcheck:
  :xml_artifact_filename: CppcheckResults.xml
```

**Default:** `CppcheckReport.xml`

### `:xml_report_version:`

Cppcheck XML schema version. Accepts `2` or `3`.

```yaml
:cppcheck:
  :xml_report_version: 3
```

**Default:** `2`

!!! warning "Version 3 requires a newer Cppcheck"
    Older Cppcheck releases reject `--xml-version=3` outright and fail the
    build. Version 2 is accepted by every release. Both versions carry the same
    severity information, so this plugin's finding counts work with either.

### `:project:`

Import a project file and let Cppcheck discover sources and include paths
itself. Compatible files include Cppcheck GUI projects (`*.cppcheck`),
compilation databases (`compile_commands.json`), and Visual Studio projects
(`*.vcxproj`, `*.sln`).

```yaml
:cppcheck:
  :project: path/to/compile_commands.json
```

**Default:** unset

!!! note "What `:project:` does and does not replace"
    Setting this stops the plugin passing Ceedling's own source and include
    path collections. Every other setting in this section still applies.
    `:defines:`, `:includes:`, `:excludes:`, `:suppressions:`, `:addons:`, and
    the rest are all still added to the command line.

### `:defines:`

Preprocessor symbols to define.

```yaml
:cppcheck:
  :defines:
    - A
    - B
    - C=1
```

**Default:** `[]`

### `:undefines:`

Preprocessor symbols to undefine.

```yaml
:cppcheck:
  :undefines:
    - A
    - B
```

**Default:** `[TEST]`

`TEST` is undefined by default so analysis runs against production code rather
than test builds.

### `:includes:`

Files force-included ahead of each analyzed file.

```yaml
:cppcheck:
  :includes:
    - file1.h
    - file2.h
```

**Default:** `[]`

### `:excludes:`

Files excluded from analysis.

```yaml
:cppcheck:
  :excludes:
    - file1.c
    - file2.c
```

**Default:** `[]`

### `:platform:`

Platform to analyze for. Accepts any platform Cppcheck ships with, such as
`unix64`, or the path to a platform XML file.

```yaml
:cppcheck:
  :platform: unix64
```

**Default:** unset

### `:standard:`

C or C++ language standard.

```yaml
:cppcheck:
  :standard: c99
```

**Default:** unset

### `:check_level:`

Analysis depth. Accepts the levels your Cppcheck supports, commonly `normal`
and `exhaustive`.

```yaml
:cppcheck:
  :check_level: exhaustive
```

**Default:** unset

### `:addons:`

Addons to run. Entries may be built-in addon names or paths to addon scripts
and JSON addon configurations.

```yaml
:cppcheck:
  :addons:
    - misra
    - path/to/addon.py
```

**Default:** `[]`

MISRA needs a rule texts file, which is not distributed with Cppcheck. Place
your copy in the project, for example at `misra.txt`, then create an addon
configuration naming it:

```json
{
	"script": "misra",
	"args": ["--rule-texts=misra.txt"]
}
```

Enable that configuration rather than the bare addon name:

```yaml
:cppcheck:
  :addons:
    - misra.json
```

### `:enable_checks:`

Additional checks enabled for single file analysis.

```yaml
:cppcheck:
  :enable_checks:
    - performance
    - portability
```

**Default:** `[style]`

!!! note "Single file analysis only"
    Whole project analysis always enables every check with `--enable=all`, so
    this setting does not affect `cppcheck:all`.

### `:disable_checks:`

Checks to disable. Applies to both analysis modes.

```yaml
:cppcheck:
  :disable_checks:
    - style
    - information
```

**Default:** `[]`

### `:inline_suppressions:`

Honor suppression comments written inline in source.

```yaml
:cppcheck:
  :inline_suppressions: true
```

**Default:** `false`

### `:suppressions:`

Suppressions given directly on the command line.

```yaml
:cppcheck:
  :suppressions:
    - memleak:src/file1.c
    - exceptNew:src/file1.c
```

**Default:** `[]`

Suppression *files* are collected separately, through Ceedling's path and file
collections rather than this list:

```yaml
:paths:
  :cppcheck:
    - suppressions/
    - source/*/suppressions/

:files:
  :cppcheck:
    - suppressions.xml
```

Both XML and text suppression files are supported. The extension used to find
text suppression files is configurable:

```yaml
:extension:
  :cppcheck: .txt
```

Confirm which files were collected with the
[`files:cppcheck`](#list-suppression-files) task.

### `:libraries:`

Library configuration files.

```yaml
:cppcheck:
  :libraries:
    - lib1.cfg
    - lib2.cfg
```

**Default:** `[]`

### `:rules:`

Regular expression rules.

```yaml
:cppcheck:
  :rules:
    - if \( p \) { free \( p \) ; }
```

**Default:** `[]`

### `:options:`

Raw command line arguments passed straight through to Cppcheck. This is the
escape hatch for anything the settings above do not cover.

```yaml
:cppcheck:
  :options:
    - --max-configs=<limit>
    - --suppressions-list=<file>
```

**Default:** `[]`

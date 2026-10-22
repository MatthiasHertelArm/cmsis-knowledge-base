---
id: "ceed-set-up-configuration-report-generation"
type: "concept"
domain: "test"
title: "Set up & Configuration: Report generation"
summary: "The next sections explain each of these steps."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/gcov/setup.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/setup/#report-generation"
license: "MIT"
mode: "V"
---

To generate reports:

1. GCovr and / or ReportGenerator must installed or otherwise ready to run in
   Ceedling’s environment.
1. Reporting options must be configured in your project file beneath a `:gcov:`
   entry.

The next sections explain each of these steps.

### Modified Condition / Decision Coverage

As of version 14, the GNU Compiler Collection supports MC/DC. If your environment
contains a minimum of GCC 14 you can enable MC/DC in coverage summaries.

If your environment contains a minimum of GCC 14 and GCovr 8, you can enable MC/DC 
in your generated coverage reports.

NOTE: ReportGenerator does not support MC/DC reporting.

```yaml
:plugins:
  :enabled:
    - gcov

:gcov:
  :mcdc: TRUE
```
**Default:** `FALSE`

### Coverage for untested sources

This setting controls how the GCov plugin handles project source files that
are not exercised by any test. It takes one of three values:

* `:ignore` — Untested source files are not processed at all. Nothing is
  logged, nothing is compiled, and these files are simply absent from the
  coverage report.
* `:list` — Untested source files are not compiled with coverage, but their
  filepaths are logged as a warning so you know which files will not appear
  in the coverage report.
* `:compile` — All untested source files are compiled with coverage so they
  appear in the final report with 0% coverage (since no test exercises
  them). This causes all source files to appear in any generated reporting.
  If a source file fails to compile, Ceedling logs guidance at the console,
  and the build fails.

```yaml
:plugins:
  :enabled:
    - gcov

:gcov:
  :untested_sources: :list
```
**Default:** `:list`

!!! warning
    **Compiling all untested sources for 0% coverage reporting (`:compile`) will likely require additional work.**

    Successful compilation of untested source files may require certain symbols 
    to be defined, certain flags to be set, or entire stand-in shims for platform 
    headers and code.
    
    Ceedling’s 
    [`:defines`](https://throwtheswitch.github.io/Ceedling/plugins/gcov/setup/../../configuration/reference/defines.md)
    and 
    [`:flags`](https://throwtheswitch.github.io/Ceedling/plugins/gcov/setup/../../configuration/reference/flags.md)
    matchers can provide these. For GCov tasks, symbols and flags are extracted from
    the `:test` context beneath the `:defines` and `:flags` configuration sections 
    by default. If you need something special for coverage builds, use the `:gcov` 
    context for these matchers instead. For an untested source, matchers match
    against the source file's own path.

Notes:

* Versions of GCovr before 7.0 do not include the necessary options to produce 
  0% coverage results for source files only compiled (but never executed).

---

When `:untested_sources` is `:compile`, an additional `gcov:untested_sources`
build task becomes available:

```shell
 > ceedling gcov:untested_sources
```

This task exists to let you work through the compilation problems described
in the warning above — missing symbols, flags, or platform header/code
stand-ins — by re-running just the untested-source compilation step
directly. No test suite build is needed while iterating on source compilation 
fixes.

### Reporting utilities installation

!!! tip "Variants of the `madsciencelab` Docker images come with these tools preinstalled"
    See [the Docker image options](https://throwtheswitch.github.io/Ceedling/plugins/gcov/setup/../../getting-started/installation.md#madsciencelab-docker-images)
    for running Ceedling.

[gcovr] is available on any platform supported by Python.

`gcovr` can be installed via pip like this:

```shell
 > pip install gcovr
```

[ReportGenerator] is available on any platform supported by .Net.

`ReportGenerator` can be installed via .NET Core like so:

```shell
 > dotnet tool install -g dotnet-reportgenerator-globaltool
```

Either or both of `gcovr` or `ReportGenerator` may be used. Only one must 
be installed for advanced report generation.

[gcovr]: https://www.gcovr.com/
[ReportGenerator]: https://reportgenerator.io

### Enabling reporting utilities

If reports are configured (see next sections) but no `:utilities:` subsection 
exists, this plugin defaults to using `gcovr` for report generation.

Otherwise, enable Gcovr and / or ReportGenerator to create coverage reports.

```yaml
:gcov:
  :utilities:
    - gcovr           # Use `gcovr` to create reports (default if no :utilities set).
    - ReportGenerator # Use `ReportGenerator` to create reports.
```

### Automatic and manual report generation

By default, if reports are specified, this plugin automatically generates 
reports after any `gcov:` task is executed. To disable this behavior, add
`:report_task: TRUE` to your project file’s `:gcov:` configuration.

With this setting enabled, an additional Ceedling task `report:gcov` is enabled.
It may be executed after `gcov:` tasks to generate the configured reports.

For small projects, the default behavior is likely preferred. This alernative 
setting allows large or complex projects to execute potentially time intensive 
report generation only when desired.

Enabling the manual report generation task looks like this:

```yaml
:gcov:
  :report_task: TRUE
```

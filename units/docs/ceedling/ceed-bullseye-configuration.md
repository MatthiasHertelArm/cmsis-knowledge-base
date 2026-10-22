---
id: "ceed-bullseye-configuration"
type: "concept"
domain: "test"
title: "Bullseye: Configuration"
summary: "All settings live in a top-level :bullseye section of your project file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/bullseye/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/#configuration"
license: "MIT"
mode: "V"
---

All settings live in a top-level `:bullseye` section of your project file.

### `:summaries:`

Controls the coverage summaries printed to the console after `bullseye:` tasks.
Set it to `FALSE` to suppress them.

```yaml
:bullseye:
  :summaries: FALSE
```

**Default:** `TRUE`

### `:untested_sources:`

Controls how the plugin handles source files that no test exercises. It takes
one of three values.

* `:ignore` — Untested sources are not processed. Nothing is logged. Nothing
  is compiled. These files are absent from coverage reports.
* `:list` — Untested sources are not compiled. Their filepaths are logged as a
  warning so you know what is missing from reports.
* `:compile` — All untested sources are compiled with coverage. They appear in
  reports at 0% coverage. A source that fails to compile fails the build.

```yaml
:bullseye:
  :untested_sources: :list
```

**Default:** `:list`

!!! warning
    **Compiling all untested sources for 0% coverage reporting will likely require additional work.**

    Successful compilation of untested source files may require certain
    symbols to be defined, certain flags to be set, or entire stand-in shims
    for platform headers and code.

    Ceedling's
    [`:defines`](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/../../configuration/reference/defines.md)
    and
    [`:flags`](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/../../configuration/reference/flags.md)
    matchers can provide these. Bullseye tasks extract symbols and flags from
    the `:test` context by default. Use the `:bullseye` context in those
    matchers to supply anything specific to coverage builds. For an untested
    source, matchers match against the source file's own path.

`:compile` also enables a standalone `bullseye:untested_sources` task.

```shell
 > ceedling bullseye:untested_sources
```

This task recompiles only the untested sources. It exists so you can work
through the compilation problems above without rebuilding the whole test suite
each time.

### `:branch_detail:`

Prints an annotated source listing identifying individual uncovered branches.
Console summaries report branch coverage only as a percentage. This setting is
the only console report that shows which branches account for that number.

It takes one of three values.

* `:none` — No annotated listing.
* `:uncovered` — Annotate only probes that are not fully covered.
* `:all` — Annotate every source line.

```yaml
:bullseye:
  :branch_detail: :uncovered
```

**Default:** `:none`

See [Branch coverage detail](#branch-coverage-detail) for how to read the
output.

### `:xml_report:`

Generates a machine-readable coverage report for CI tooling. It takes one of
three values.

* `:none` — No XML report.
* `:native` — Bullseye's own XML schema.
* `:cobertura` — Cobertura format (a popular format across coverage reporting
    tools and CI dashboards).

```yaml
:bullseye:
  :xml_report: :cobertura
```

**Default:** `:none`

The report is written to `build/artifacts/bullseye/coverage.xml`.

### `:fail_under:`

Fails the build when coverage falls below a minimum percentage. Each metric is
configured separately. A value of `0` disables that check.

```yaml
:bullseye:
  :fail_under:
    :functions: 90
    :branches: 75
```

**Default:** `0` for both metrics

Reports are still generated when a threshold is unmet. The failure is reported
last so you see the coverage numbers first.

```
------------------------
❌ BUILD FAILURE SUMMARY
------------------------
 • [BULLSEYE] Function coverage 50% is below the configured minimum of 90%.
 • [BULLSEYE] Branch coverage 10% is below the configured minimum of 75%.
```

### `:report_task:`

Controls whether reports generate automatically. By default, HTML and XML
reports are generated after every `bullseye:` task. Set this to `TRUE` to
generate them on demand instead.

```yaml
:bullseye:
  :report_task: TRUE
```

**Default:** `FALSE`

This setting enables a `report:bullseye` task.

```shell
 > ceedling bullseye:all
 > ceedling report:bullseye
```

Large projects may prefer this. Report generation can be time intensive.

### `:license_manager_file:`

Points the plugin at a shared Bullseye license manager file. This applies only
to floating and evaluation licenses. See
[Licensing](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing.md#floating-and-evaluation-licenses).

```yaml
:bullseye:
  :license_manager_file: /path/to/shared/bullseye.lmgr
```

**Default:** unset

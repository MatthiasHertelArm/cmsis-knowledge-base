---
id: "ceed-ide-test-suite-console-report-configuration"
type: "concept"
domain: "test"
title: "IDE Test Suite Console Report: Configuration"
summary: "Two settings shape the report. Neither is required."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-ide-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout/#configuration"
license: "MIT"
mode: "V"
---

Two settings shape the report. Neither is required.

```YAML
:report_tests_ide_stdout:
  :format: :gcc            # Default
  :absolute_paths: TRUE    # No default. Each format sets its own path form.
```

### `:format`

`:format` chooses how each failed and ignored test is listed.

| `:format` | Lines | Paths unless `:absolute_paths` is set |
|---|---|---|
| `:gcc` | GCC diagnostic shape (default) | Relative |
| `:legacy` | The shape before Ceedling 1.2.0 | Relative |
| `:vscode` | Same as `:gcc` | Relative |
| `:eclipse` | Same as `:gcc` | Relative |
| `:clion` | Same as `:gcc` | Absolute and required |

Use `:gcc` with any tool that reads GCC output.

The IDE names are shortcuts (other settings are not required when these aliases
are used). Each stands for the `:gcc` settings that IDE needs. More names may be 
added later.

A format may be written as a symbol or a string, in any letter case.

`:legacy` restores the lines this plugin printed before Ceedling 1.2.0. Every line
of a message repeats the file, line, and test case, and the message is quoted.

```
test/TestModel.c:21:testInitShouldCallSchedulerAndTemperatureFilterInit: "Function TaskScheduler_Init() called more times than expected."
```

Few IDEs read `:legacy` lines as problems without extra configuration.

### `:absolute_paths`

Paths are relative to your project’s root unless a format says otherwise. Set
`:absolute_paths` to `TRUE` for full paths. Set it to `FALSE` for relative paths.

When `:absolute_paths` is not set, each format’s own path form applies. When it is
set, it overrides that path form, unless the named IDE cannot read the result.
CLion’s output filters find only absolute paths. So `:clion` with
`:absolute_paths: FALSE` stops the build with a configuration error.

```YAML
:report_tests_ide_stdout:
  :format: :eclipse
  :absolute_paths: TRUE
```

### Multi-line messages

The first line of a message goes on the test’s line. The remaining lines follow,
indented four spaces. Your IDE shows one problem for the test, and the console
keeps the whole message.

```
test/TestModel.c:30:1: error: testFilterShouldReset: Expected 5 Was 4
    Filter state at failure: RESET_PENDING
```

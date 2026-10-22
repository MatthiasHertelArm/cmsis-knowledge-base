---
id: "ceed-sanitize-configuration"
type: "concept"
domain: "test"
title: "Sanitize: Configuration"
summary: "The plugin’s defaults turn on ASan and UBSan, stop a test at its first finding, check for leaks where supported, and fail the build on any finding. Change any of these under an optional :sanitize section in your project configuration."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#configuration"
license: "MIT"
mode: "V"
---

The plugin’s defaults turn on ASan and UBSan, stop a test at its first finding,
check for leaks where supported, and fail the build on any finding. Change any
of these under an optional `:sanitize` section in your project configuration.

### Default configuration

```yaml
:sanitize:
  :sanitizers:
    - :address
    - :undefined
  :recover: FALSE
  :detect_leaks: TRUE
  :test_builds: FALSE
  :fail_build: TRUE
  :reports: []
  :runtime_options:
    :asan: []
    :ubsan: []
    :lsan: []
  :flags:
    :compile: []
    :link: []
```

### `:sanitizers:`

The sanitizers to build with. Any of `:address`, `:undefined`, and `:leak`.
Names written as strings, such as `address`, work too.

```yaml
:sanitize:
  :sanitizers:
    - :undefined
```

ASan’s runtime includes leak detection, so `:leak` adds nothing beside
`:address`. List `:leak` alone for leak detection without ASan.

**Default:** `[:address, :undefined]`

### `:recover:`

When `false` (the default), a sanitizer stops a test at its first finding.
When `true`, the test keeps running and each finding is reported.

```yaml
:sanitize:
  :recover: true
```

**Default:** `false`

### `:detect_leaks:`

When `true` (the default), ASan checks for leaks as each test executable exits.
Leak detection is not supported on macOS. There, the plugin disables it with a
notice.

**Default:** `true`

### `:test_builds:`

When `true`, ordinary `test:` builds are built with the sanitizers too. A
`sanitize:` build is always instrumented.

```yaml
:sanitize:
  :test_builds: true
```

**Default:** `false`

### `:fail_build:`

When `true` (the default), any sanitizer finding fails the build. When `false`,
findings are still logged and saved, but the build is not failed for them.

A test a sanitizer stopped is still a failing test either way.

**Default:** `true`

### `:reports:`

Reports of a build’s findings, written for each instrumented build. Any of
`:text`, `:json`, and `:sarif`.

- **`:text`** collects each finding’s report as the sanitizer printed it.
- **`:json`** lists each finding’s test, sanitizer, kind, file, line, and
  message.
- **`:sarif`** writes [SARIF] 2.1.0 for code scanning services such as GitHub
  code scanning. Each finding is an error.

```yaml
:sanitize:
  :reports:
    - :text
    - :sarif
```

The JSON and SARIF reports are written even for a build without findings, so a
CI step always finds its file. An empty SARIF run tells a code scanning service
that earlier findings are gone.

**Default:** `[]` (the text report alone)

### `:runtime_options:`

Extra runtime options for each sanitizer, appended to the plugin’s own. Each
entry is one `name=value` option.

```yaml
:sanitize:
  :runtime_options:
    :asan:
      - strict_string_checks=1
    :ubsan:
      - report_error_type=1
```

The plugin sets these options itself:

| Variable | Options |
|---|---|
| `ASAN_OPTIONS` | `halt_on_error`, `exitcode=0`, and `detect_leaks` (Linux) |
| `UBSAN_OPTIONS` | `halt_on_error`, `print_stacktrace=1`, and `exitcode=0` |
| `LSAN_OPTIONS` | `exitcode=0`, when the leak sanitizer runs without ASan |

`exitcode=0` lets the plugin judge each run by what the sanitizers report rather
than by their exit codes. See [How findings are reported](#how-findings-are-reported).

**Default:** none

### `:flags:`

Extra compile and link flags for instrumented builds. They follow the plugin’s
own `-fsanitize`, `-fno-omit-frame-pointer`, and `-g`, plus
`-fno-sanitize-recover=all` unless [`:recover:`](#recover) is on.

```yaml
:sanitize:
  :flags:
    :compile:
      - -O1
    :link:
      - -static-libasan
```

**Default:** none

### Flags and defines for the `sanitize:` build

A `sanitize:` build is a build context of its own. Like `:test`, it accepts
[`:flags`](https://throwtheswitch.github.io/Ceedling/plugins/sanitize/../configuration/reference/flags.md) and
[`:defines`](https://throwtheswitch.github.io/Ceedling/plugins/sanitize/../configuration/reference/defines.md) entries, matchers included.
Without its own entries for an operation, a `sanitize:` build uses `:test`’s.

```yaml
:defines:
  :sanitize:
    - SANITIZED_BUILD
```

---
id: "ceed-reportgenerator-configuration-results-filtering"
type: "concept"
domain: "test"
title: "ReportGenerator Configuration: Results filtering"
summary: "This plugin filters coverage results for reportgenerator coverage reporting in two separate stages, each with its own defaults."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/reportgenerator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/reportgenerator/#results-filtering"
license: "MIT"
mode: "V"
---

This plugin filters coverage results for `reportgenerator` coverage reporting
in two separate stages, each with its own defaults.

### Coverage generation filtering

Before `reportgenerator` ever runs, this plugin runs `gcov` itself against each
`.gcno` file produced by the coverage test build, skipping any that match an 
exclusion pattern — no `.gcov` data is ever produced for a skipped file, so 
nothing downstream can put it back into a report.

By default this skips:

- **Test files** — matched by `:test_file_prefix`.
- **Mocks** — matched by `:mock_prefix`.
- **Test runners** — any filename containing `_runner`.
- **Vendored Unity and CMock sources** — `unity.gcno` and `cmock.gcno` by
  name.

Given `:test_file_prefix` ⇒ `test_` and CMock's default `:mock_prefix` ⇒
`Mock`, the equivalent filename-fragment patterns are:

```
test_[^\/\\]*
Mock[^\/\\]*
[^\/\\]*_runner[^\/\\]*
unity
cmock
```

These combine with whatever you add via [`:gcov_exclude`](#gcov_exclude)
below. Your patterns extend this list, they don't replace it.

### Report filtering

Separately, once `.gcov` files exist, ReportGenerator's own `-filefilters:`
argument controls which of them actually appear in the generated report(s).
By default this excludes:

1.  **Test paths** — every file anywhere under each of your configured
    `:paths` ↳ `:test` directories, not only files matching
    `:test_file_prefix`. A support subdirectory nested under a test path
    (e.g. `test/support/`) is excluded as a side effect of this — the whole
    tree goes, not just prefixed test files.

    Given a `:paths` ↳ `:test` entry of `test/`:
    ```
    -./test/**/*
    ```

1.  **The build root** — every generated and vendored file: mocks, test
    runners, Partials output, Unity, CMock, CException.

    Given `:build_root` ⇒ `build/`:
    ```
    -./build/**/*
    ```

1.  **Partial-generated files** — only when `:use_partials` is enabled, any
    file whose name starts with Ceedling's Partial filename prefix, wherever
    it's found (not only under the build root).

    ```
    -ceedling_partial_*
    ```

These patterns are generated automatically and placed ahead of whatever you
provide via [`:file_filters`](#file_filters) below.

### Overriding the defaults

Neither filtering stage above can be overridden or narrowed by plugin
configuration — only added to.

For [coverage generation filtering](#coverage-generation-filtering),
[`:gcov_exclude`](#gcov_exclude) only ever adds more exclusion patterns; there
is no plugin option to disable one of the built-in exclusions, and no way to
resurrect `.gcov` data for a file `gcov` was never run against in the first
place.

For [report filtering](#report-filtering), the natural instinct is to reach
for [`:custom_args`](#custom_args) to pass a second, conflicting
`-filefilters:` argument, but this is not an option because of ReportGenerator's
rules and the order in which the filters are provided by the plugin.

In short, there's no supported way to broaden what this plugin reports
beyond its defaults. If you need to override coverage reporting filtering, 
use the [Gcovr option for this pluing](https://throwtheswitch.github.io/Ceedling/plugins/gcov/reportgenerator/gcovr.md) instead. Its
`:config_file` option hands full control to a `gcovr` configuration file,
bypassing Ceedling's generated exclusions entirely (see
[Gcovr's Results filtering](https://throwtheswitch.github.io/Ceedling/plugins/gcov/reportgenerator/gcovr.md#results-filtering)).

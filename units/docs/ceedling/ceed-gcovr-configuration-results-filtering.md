---
id: "ceed-gcovr-configuration-results-filtering"
type: "concept"
domain: "test"
title: "GCovr Configuration: Results filtering"
summary: "By default, this plugin configures gcovr to excludes three categories of .c files from coverage results. These defaults exist because a coverage percentage is typically only meaningful over the production code you're actually trying to exercise with test coverage."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#results-filtering"
license: "MIT"
mode: "V"
---

By default, this plugin configures `gcovr` to excludes three categories of 
`.c` files from coverage results. These defaults exist because a
coverage percentage is typically only meaningful over the production code 
you're actually trying to exercise with test coverage. Test code, test 
support code, and every file Ceedling itself generates as part of a build 
will skew that number if left in coverage reporting.

The list that follows details the filtering this plugin injects into 
Gcovr coverage report generation. The examples are usable regular 
expressions that mirror the defaults in use. The plugin dynamically 
generates these regular expressions from your project configuration.
When creating them youself, you will need to match your project 
configuration settings with static strings.

1.  **Test files** — matched by `:test_file_prefix` within your configured
    `:paths` ↳ `:test` directories.

    Given `:test_file_prefix` ⇒ `test_` and a `:paths` ↳ `:test` entry of
    `test/`:

    ```
    .*test/.*/test_.+\.c$
    ```

2.  **Test support files** — any `.c` file within your configured `:paths` ↳
    `:support` directories, regardless of name. Helpers, stubs, and fixtures
    living there are no more production code than the test files themselves.

    Given a `:paths` ↳ `:support` entry of `test/support/`:

    ```
    .*test/support/.+\.c$
    ```

3.  **Generated and vendored files** — any `.c` file anywhere below your
    `:build_root`: generated mocks, test runners, Partials output, and the
    vendored Unity/CMock/CException framework sources Ceedling copies in to
    build against. This pattern always matches a literal `.c` extension
    regardless of your project's own `:extension` ↳ `:source` setting, since
    every file it catches is one Ceedling itself writes in plain C.

    Given `:build_root` ⇒ `build/`:

    ```
    .*build/.+\.c$
    ```

These patterns are generated automatically and combined with whatever you
provide via [`:report_exclude`](#report_exclude) below.

!!! warning "Not applied when using a Gcovr configuration file"
    These defaults are only generated when Ceedling builds `gcovr`'s command
    line directly. As covered in
    [Gcovr configuration file](#gcovr-configuration-file) above, setting
    `:config_file` bypasses this entirely — none of the three patterns above
    are applied, and you must supply equivalent exclusions in the config file
    yourself.

### Overriding the defaults

[`:report_exclude`](#report_exclude) can only add exclusions on top of the
three defaults above — `gcovr --exclude` is a deny-list with no way to
"un-exclude" a pattern already passed to it, and this plugin always passes its
own three patterns ahead of anything you configure there. Setting
[`:report_include`](#report_include) doesn't help either; it narrows which
files are considered at all, but an exclude pattern still wins over it for
any file matching both.

The only way to actually remove or replace one of these defaults — for
example, to include test files in coverage results so you can confirm a
conditional test build compiled the branches you expect — is a
[Gcovr configuration file](#gcovr-configuration-file). Setting `:config_file`
stops Ceedling from generating any of the three patterns at all, handing you
full control:

```ini
; gcovr.cfg — omits the test-file exclude pattern so test files remain in
; coverage results, while still keeping generated/vendored build output out.
exclude = .*build/.+\.c$
```

```yaml
:gcov:
  :gcovr:
    :config_file: gcovr.cfg
```

Note that this isn't scoped per category. Once a default is dropped, any
file it would have excluded is folded into the same combined report as your
production code, not broken out separately.

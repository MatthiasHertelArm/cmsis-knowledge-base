---
id: "ceed-gcovr-configuration-results-filtering"
type: "concept"
domain: "test"
title: "GCovr Configuration: Results filtering"
summary: "By default, gcovr excludes three categories of .c files from coverage results, on top of whatever gcov itself already limits reporting to (the sources your test build actually compiled)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#results-filtering"
license: "MIT"
mode: "V"
---

By default, `gcovr` excludes three categories of `.c` files from coverage
results, on top of whatever `gcov` itself already limits reporting to (the
sources your test build actually compiled). These defaults exist because a
coverage percentage is only meaningful over the production code you're
actually trying to cover — test code, test support code, and every file
Ceedling itself generates as part of a build all skew that number if left in.

1.  **Test files** — matched by `:test_file_prefix` within your configured
    `:paths` ↳ `:test` directories.

    Given `:test_file_prefix` ⇒ `test_` and a `:paths` ↳ `:test` entry of
    `test/`:

    ```
    .*(?:^|/)test/(?:.*/)?test_[^/]+(?:\.c)$
    ```

    A project's `:extension` ↳ `:source` can list more than one source
    extension; every configured extension is joined into this same
    alternation. Given `:extension` ↳ `:source` ⇒ `['.c', '.C']`:

    ```
    .*(?:^|/)test/(?:.*/)?test_[^/]+(?:\.c|\.C)$
    ```

2.  **Test support files** — any file matching one of your configured source
    extensions within your configured `:paths` ↳ `:support` directories,
    regardless of name. Helpers, stubs, and fixtures living there are no more
    production code than the test files themselves.

    Given a `:paths` ↳ `:support` entry of `test/support/`:

    ```
    .*(?:^|/)test/support/.+(?:\.c)$
    ```

    Again, every configured `:extension` ↳ `:source` value is included in
    the alternation. Given `:extension` ↳ `:source` ⇒ `['.c', '.C']`:

    ```
    .*(?:^|/)test/support/.+(?:\.c|\.C)$
    ```

3.  **Generated and vendored files** — any `.c` file anywhere below your
    `:build_root`: generated mocks, test runners, Partials output, and the
    vendored Unity/CMock/CException framework sources Ceedling copies in to
    build against. Unlike the two patterns above, this one always matches a
    literal `.c` extension regardless of your project's own `:extension` ↳
    `:source` setting, since every file it catches is one Ceedling itself
    writes in plain C.

    Given `:build_root` ⇒ `build/`:

    ```
    .*(?:^|/)build/.+\.c$
    ```

These patterns are generated automatically and combined with whatever you
provide via [`:report_exclude`](#report_exclude) below — you don't need to
(and normally shouldn't) duplicate them yourself.

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
"un-exclude" a pattern already passed to it, and Ceedling always passes its
own three patterns ahead of anything you configure there. Neither
[`:report_include`](#report_include) nor [`:custom_args`](#custom_args) helps
either: `:report_include` narrows which files are considered at all, but an
exclude pattern still wins over it for any file matching both; `:custom_args`
lets you pass additional raw `gcovr` flags, but a raw `--filter`/`--exclude`
of your own is just as additive as `:report_exclude` — there's no `gcovr`
flag that removes or replaces an exclusion already given, only ones that add
more.

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

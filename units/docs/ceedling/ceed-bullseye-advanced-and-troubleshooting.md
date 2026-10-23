---
id: "ceed-bullseye-advanced-and-troubleshooting"
type: "concept"
domain: "test"
title: "Bullseye: Advanced and troubleshooting"
summary: "This plugin's tool definitions and defaults are contained in defaults_bullseye.rb and defaults.yml. Both are useful references for overriding plugin behavior with Ceedling's advanced features."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/bullseye/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/#advanced-and-troubleshooting"
license: "MIT"
mode: "V"
---

### Advanced usage

This plugin's tool definitions and defaults are contained in
[defaults_bullseye.rb](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/../../snapshot/plugins/bullseye/config/defaults_bullseye.rb)
and [defaults.yml](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/../../snapshot/plugins/bullseye/config/defaults.yml). Both
are useful references for overriding plugin behavior with Ceedling's advanced
features.

### Tool wrapping and custom flags

This plugin's compiler and linker tools wrap `gcc` with Bullseye's `covc`.
`covc` parses everything before the wrapped compiler's name as its own option.
Anything after that name is passed through to the compiler.

The wrapped compiler name is therefore folded into each tool's `:executable`
setting as `covc -q gcc`. It is not left as a leading argument.

Keep this ordering in mind when overriding `:bullseye_compiler` or
`:bullseye_linker`. Your own `:arguments:` entries must land after the wrapped
compiler's name. So must any flags Ceedling injects through `:defines` and
`:flags` matchers.

### "unknown option" errors from `covc`

A flag that belongs to `gcc` landed before the wrapped compiler's name. See
[Tool wrapping and custom flags](#tool-wrapping-and-custom-flags).

### `bullseye:browser` fails to launch `CoverageBrowser`

`CoverageBrowser` is a GUI application with its own runtime dependencies. GTK
is one example on Linux. Install your platform's GUI toolkit dependencies
alongside Bullseye.

Headless environments rarely have these libraries. Console summaries, HTML
reports, and XML reports have no GUI dependencies at all.

### Relocating the coverage data file

Region-based exclusions may stop matching if you relocate the coverage data
file through your own `:tools` overrides. See
[The coverage data file](#the-coverage-data-file) for why its location
matters.

[bullseye]:                  https://www.bullseye.com
[bullseye-coverage]:         https://www.bullseye.com/coverage.html
[bullseye-coverage-file]:    https://www.bullseye.com/help/build-coverageFile.html
[bullseye-download]:         https://www.bullseye.com/cgi-bin/download
[bullseye-regions]:          https://www.bullseye.com/help/ref-regions.html

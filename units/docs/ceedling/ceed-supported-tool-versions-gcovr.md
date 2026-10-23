---
id: "ceed-supported-tool-versions-gcovr"
type: "concept"
domain: "test"
title: "Supported tool versions: `gcovr`"
summary: "The Gcov plugin is known to work with gcovr 5.2 through gcovr 8.x. The Gcov plugin supports gcovr command line conventions since version 4.2 and attempts to support gcovr command lines before version 4.2."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/tool-versions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/tool-versions/#gcovr"
license: "MIT"
mode: "V"
---

The Gcov plugin is known to work with `gcovr` 5.2 through `gcovr` 8.x. The
Gcov plugin supports `gcovr` command line conventions since version 4.2 and
attempts to support `gcovr` command lines before version 4.2. We recommend 
using `gcovr` 5 and later.

Several `:gcovr` options and report types depend on a minimum `gcovr` version, checked and
enforced by this plugin (see [GCovr Configuration](https://throwtheswitch.github.io/Ceedling/plugins/gcov/tool-versions/gcovr.md) for each
option's own details):

| Option | Minimum `gcovr` version |
|---|---|
| `:decisions` | 5.1 |
| `:merge_mode_function` | 6.0 (ignored for earlier versions) |
| `:fail_under_decision` | 7.0 |
| `JaCoCo` report | 7.0 |
| `lcov` report | 7.0 (gcovr only; ReportGenerator has no minimum) |
| `:mcdc` | 8.0 |

`gcovr` 7.0 also deprecated `:branches`, `:sort_uncovered`, and
`:sort_percentage`'s underlying flags in favor of renamed equivalents; the
plugin automatically uses whichever form of arguments your installed `gcovr` 
expects but each is enabled with the [keys documented](https://throwtheswitch.github.io/Ceedling/plugins/gcov/tool-versions/gcovr.md).

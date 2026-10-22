---
id: "ceed-supported-tool-versions-gcov"
type: "concept"
domain: "test"
title: "Supported tool versions: `gcov`"
summary: "The Gcov plugin is known to work with gcov packaged with GNU Compiler Collection 12 through at least 15."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/gcov/tool-versions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/tool-versions/#gcov"
license: "MIT"
mode: "V"
---

The Gcov plugin is known to work with `gcov` packaged with GNU Compiler
Collection 12 through at least 15.

The maintainers of `gcov` introduced significant behavioral changes for
version 12. Previous versions of `gcov` had a simple exit code scheme with only a
single non-zero exit code upon fatal errors. Since version 12 `gcov` emits a
variety of exit codes even if the noted issue is a non-fatal error. The Gcov
plugin's logic assumes version 12 behavior and processes failure messages and
exit codes appropriately, taking into account plugin configuration options.

The Gcov plugin should be compatible with versions of `gcov` before version 12.
That is, its improved `gcov` exit handling should not be broken by the prior
simpler behavior. The Gcov plugin dependes on the `gcov` command line and has
been compatible with it as far back as `gcov` version 7.

Because long file paths are quite common in software development scenarios, by
default, the Gcov plugin depends on the `gcov` `-x` flag. This flag hashes long
file paths to ensure they are not a problem for certain platforms' file
systems. This flag became available with `gcov` version 7. We do not recommend 
using `gcov` version 6 and earlier. And, in fact, because of the Gcov plugin's 
dependence on the `gcov` `-x` flag, attempting to use it will fail.

GNU Compiler Collection 14 introduced support for Modified Condition/Decision
Coverage (MC/DC). For this reason, the Gcov plugin's own `:mcdc` option (see
[Setup](https://throwtheswitch.github.io/Ceedling/plugins/gcov/tool-versions/setup.md)) explicitly checks for GCC 14+. The plugin raises a clear 
error if running against an older GCC with `:mcdc` enabled. This GCC-version 
dependency is specific to `:mcdc`; it does not otherwise affect how the 
plugin processes coverage.

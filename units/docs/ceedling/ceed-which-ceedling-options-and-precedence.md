---
id: "ceed-which-ceedling-options-and-precedence"
type: "concept"
domain: "test"
title: "Which Ceedling: Options and precedence"
summary: "When Ceedling starts up, it evaluates a handful of conditions to determine which Ceedling location to launch."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/which-ceedling.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/which-ceedling/#options-and-precedence"
license: "MIT"
mode: "V"
---

When Ceedling starts up, it evaluates a handful of conditions to determine
which Ceedling location to launch.

The following are evaluated in order:

1. Environment variable `WHICH_CEEDLING`. If this environment variable is
   set, its value is used.
1. Configuration entry `:project` ↳ `:which_ceedling`. If this is set,
   its value is used.
1. The path `vendor/ceedling`. If this path exists in your working 
   directory — typically because of a `--local` vendored installation at
   project creation — its contents are used to launch Ceedling.
1. If none of the above exist, the `ceedling` launcher defaults to using
   the `lib/` directory next to the `bin/` directory from which the 
   `ceedling` launcher is running. In the typical case this is the default 
   gem installation.

!!! note "Configuration entry (2) does not make sense in some scenarios"
    When running `ceedling new`, `ceedling examples`, or `ceedling example` 
    there is no project file to read. Similarly, `ceedling upgrade` does not 
    load a project file; it merely works with the directory structure and 
    contents of a project. In these cases, the environment variable is your
    only option to set which Ceedling to launch.

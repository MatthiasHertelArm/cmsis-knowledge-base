---
id: "ceed-gcovr-configuration-gcovr-options"
type: "concept"
domain: "test"
title: "GCovr Configuration: GCovr options"
summary: "A Gcovr config file replaces Ceedling's own automatically generated exclusion patterns (see Results filtering below) entirely — it is the only way to override or remove one of those defaults, since the project-configuration :report_exclude option can only add …"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/gcovr.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/gcovr/#gcovr-options"
license: "MIT"
mode: "V"
---

### Project config vs. GCovr config file

GCovr can be configured in two ways:

1. Using one or more of the options documented below in the `:gcov` section
   of your project configuration.
1. Through a Gcovr configuration file (.ini format) provided to Gcovr via
   the speciial `:config_file` value in the `:gcov` section of your project
   configuration.

### Gcovr configuration file

!!! warning "Using a gcovr configuration file"
    When `:config_file` is set, Ceedling passes only `--root` (`:report_root`), 
    `--config` (`:config_file`), and any `:custom_args:` to `gcovr` at the command 
    line from your plugin configuration. This prevents overriding config file 
    settings with other CLI arguments derived from plugin configuration. You must 
    provide any settings that would have been provided by the Gcov plugin, either 
    in the config file itself or via `:custom_args:`.

A Gcovr config file replaces Ceedling's own automatically generated exclusion
patterns (see [Results filtering](#results-filtering) below) entirely — it is
the only way to override or remove one of those defaults, since the
project-configuration `:report_exclude` option can only add further
exclusions on top of them, never take one away. To preserve the same
filtering of test and build files when switching to a Gcovr config file, you
must provide equivalent explicit exclusion patterns matching your project
layout yourself (example below).

```ini
; You will need to revise these example exclude patterns to match your
; project directories and file naming as they cannot be automatically 
; provided to Gcovr when a Gcovr configuration file is in use.
;
; Note: Format is flat `key = value` lines with no `[section]` header.

; Test path(s) exclusions for 'test_' files with .c extensions. 
exclude = .*test.*/test_.+\.c$

; Build path exlcude for all generated C files (runners, mocks, partials).
exclude = .*build/.+\.c$
```

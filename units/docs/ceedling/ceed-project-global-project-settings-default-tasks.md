---
id: "ceed-project-global-project-settings-default-tasks"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:default_tasks`"
summary: "A list of default build / plugin tasks Ceedling should execute if none are provided at the command line."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#default-tasks"
license: "MIT"
mode: "V"
---

A list of default build / plugin tasks Ceedling should execute if none are
provided at the command line.

!!! note "Build & plugin tasks only"
    Build & plugin tasks include tasks such as `test:all` and `clobber`. 
    `:default_tasks` does not support application commands (e.g. `dumpconfig`) 
    or command line flags (e.g. `--verbosity`).
    
    See the documentation [on using the command line][command-line]
    to understand the distinction between application commands and build & 
    plugin tasks.

[command-line]: ../../getting-started/command-line.md

Example YAML:
```yaml
:project:
  :default_tasks:
    - clobber
    - test:all
    - release
```
**Default**: `['test:all']`

---
id: "ceed-project-global-project-settings-build-root"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:build_root`"
summary: "Top level directory into which generated path structure and files are placed."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#build-root"
license: "MIT"
mode: "V"
---

Top level directory into which generated path structure and files are placed.

!!! note "Build configuration requirement"
    This is one of the handful of configuration values that must be set for 
    any project. `:project` ↳ `:build_root` must be set for any build — release 
    build or test suite — to run.

**Default**: (none)

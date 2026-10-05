---
id: "ceed-bullseye"
type: "concept"
domain: "test"
title: "Bullseye"
summary: "Plugin for integrating Bullseye code coverage tool into Ceedling projects. This plugin requires a working license to Bullseye code coverage tools."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/bullseye.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/"
license: "MIT"
mode: "V"
---

Plugin for integrating Bullseye code coverage tool into Ceedling projects.
This plugin requires a working license to Bullseye code coverage tools. The tools
must be within the path or the path should be added to the environment in the 
project configuration.

!!! warning "Bullseye Plugin Disabled"
    [June 1, 2024] Until the Bullseye Plugin can be updated for compatibility 
    with Ceedling >= 1.0.0, it has been disabled.

!!! note
    The Bullseye plugin creates a duplicate test build with `bullseye:` 
    command line plugin tasks. [This is intentional and needed](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/index.md#understanding-plugin-build-duplication).

---

---
id: "cact-arm-software-cmsis-actions-action-setup-vcpkg"
type: "concept"
domain: "devops"
title: "ARM-software/cmsis-actions: Action: setup-vcpkg"
summary: "This action can be used to install vcpkg into the current runner environment."
status: "draft"
collection: "cmsis-actions"
source: "ARM-software/cmsis-actions@f248cd4:README.md"
doc_source: "https://github.com/ARM-software/cmsis-actions/blob/f248cd4/README.md#action-setup-vcpkg"
license: "Apache-2.0"
mode: "V"
---

This action can be used to install vcpkg into the current runner environment.

```yaml
- name: Install vcpkg
  uses: ARM-software/cmsis-actions/setup-vcpkg@v1
  with:
    version: 2026.04.27
```

inputs              | default value  | description
--------------------|----------------|--------------
`version:`          | 2026.04.27     | The version of vcpkg to install.

**NOTE:** The required vcpkg-artifacts is dropped after July 1st 2026. Assure the version installed has still support for artifacts.

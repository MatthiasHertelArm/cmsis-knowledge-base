---
id: "tbx-csolution-project-structure-context"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Context"
summary: "A context is defined in the .csolution.yml file by projects:, target-types:, and build-types:. It identifies a configuration with project-name, build-type, and target-type and is used on various places in the CMSIS-Toolbox."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#context"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

A [context](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#context-name-conventions) is defined in the `*.csolution.yml` file by `projects:`, `target-types:`, and `build-types:`. It identifies a configuration with `project-name`, `build-type`, and `target-type` and is used on various places in the CMSIS-Toolbox.

The following [context](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#context-name-conventions) refers to the example above and selects the `project: Sample.cproject.yml` with `build-type: Debug` and `target-type: FRDM-K32L3A6`:

```txt
Sample.Debug+FRDM-K32L3A6
```

The [context](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#context-name-conventions) allows you to refer to each possible build combination that, by default, uses a different [output directory](#output-directory-structure). A context may be partly specified in many places.

The [target-set](#working-with-target-set) defines a combination of projects (that belong to the same target type) along with debug configuration and is useful when an application is composed of [multiple related projects](#configure-related-projects).

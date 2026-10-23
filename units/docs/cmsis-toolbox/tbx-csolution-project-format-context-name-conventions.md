---
id: "tbx-csolution-project-format-context-name-conventions"
type: "concept"
domain: "project"
title: "CSolution Project Format: Name Conventions / `context:` Name Conventions"
summary: "A context: name combines project-name, built-type, and target-type and is used in various places in the CMSIS-Toolbox. The following syntax is used to specify a context: name."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#context-name-conventions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Name Conventions_

A `context:` name combines `project-name`, `built-type`, and `target-type` and is used in various places in the CMSIS-Toolbox.  The following syntax is used to specify a `context:` name.

```yml
[project-name][.build-type][+target-type]
```

Element             |              | Description
:-------------------|:-------------|:---------------------
`project-name`      |   Optional   | Project name of a project (base name of the *.cproject.yml file).
`.build-type`       |   Optional   | The [`build-type`](#build-types) name that is currently processed (specified with `- type: name`).
`+target-type`      |   Optional   | The [`target-type`](#target-types) name that is currently processed (specified with `- type: name`).

!!! Note
    The `.build-type` and `+target-type` names allow letters (A-Z, a-z), digits (0-9), dash ('-'), and underscore ('_'); the maximum length is 32 characters.

- When `project-name` is omitted, the `project-name` is the base name of the `*.cproject.yml` file.
- When `.build-type` is omitted, it matches with any possible `.build-type`.
- When `+target-type` is omitted, it matches with any possible `+target-type`.

By default, the specified `- type: name` of [`build-types:`](#build-types) and [`target-types:`](#target-types) nodes in the `*.csolution.yml` file are directly mapped to the `context` name.
Using the [`context-map:`](#context-map) node, it is possible to assign a different `.build-type` and/or `+target-type` mapping for a specific `project-name`.

**Example:**

Show the different possible context settings of a `*.csolution.yml` file.

```txt
AWS_MQTT_MutualAuth_SW_Framework>csolution list contexts -s Demo.csolution.yml
Demo.Debug+FVP
Demo.Debug+IP-Stack
Demo.Debug+WiFi
Demo.Release+FVP
Demo.Release+IP-Stack
Demo.Release+WiFi
```

The `context` name is also used in [`for-context:`](#for-context) and [`not-for-context:`](#not-for-context) nodes that allow to include or exclude items depending on the `context`. In many cases, the `project-name` can be omitted as the `context` name is within a specific `*.cproject.yml` file or applied to a specific `*.cproject.yml` file.

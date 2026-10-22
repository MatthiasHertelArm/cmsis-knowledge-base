---
id: "tbx-csolution-project-format-target-selection"
type: "concept"
domain: "project"
title: "CSolution Project Format: Target Selection"
summary: "Specifies a unique board name, optionally with vendor that must be defined in software packs. This information is used to define the device: along with basic toolchain settings."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#target-selection"
license: "Apache-2.0"
mode: "V"
---

### `board:`

Specifies a [unique board name](#board-name-conventions), optionally with vendor that must be defined in software packs.
This information is used to define the `device:` along with basic toolchain settings.

### `device:`

Specifies a [unique device name](#device-name-conventions), optionally with the vendor that must be defined in software
packs. This information is used to define the `device:` along with basic toolchain settings.

A `device:` is derived from the `board:` setting, but an explicit `device:` setting overrules the `board:` device.

If `device:` specifies a device with a multi-core processor, and no explicit `pname` for the processor core selection is specified, the default `pname` of the device is used.

At the level of a `cproject.yml` file, only the `pname` can be specified as the device itself is selected at the level of a `csolution.yml` file.

**Example:**

The following assumes that the csolution is based on NXP's `K32L3A60VPJ1A` which has two `pnames`: `cm4` and `cm0plus`. Here are the corresponding entries in the `*.cproject.yml` files:

*CM4.cproject.yml:*

```yml
project:
  device: :cm4
```

*CM0Plus.cproject.yml:*

```yml
project:
  device: :cm0plus
```

---
id: "tbx-csolution-project-format-cdefault"
type: "concept"
domain: "project"
title: "CSolution Project Format: Project File Structure / `cdefault:`"
summary: "When cdefault: is specified in the .csolution.yml file, the csolution Project Manager uses a file with the name cdefault.yml to setup the compiler with specific default controls. The search order for this file is:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#cdefault"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project File Structure_

When [`cdefault:`](#solution) is specified in the `*.csolution.yml` file, the **`csolution` Project Manager** uses a file with the name [`cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#cdefaultyml) to setup
the compiler with specific default controls. The search order for this file is:

- A [`cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#cdefaultyml) file in the same directory as the `<solution-name>.csolution.yml` file.
- A [`cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#cdefaultyml) file in the directory [`<cmsis-toolbox-installation-dir>/etc`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/installation.md#environment-variables).

The `default:` node is the start of a [`cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#cdefaultyml) file and contains the following.

`default:`                                                |            | Content
:---------------------------------------------------------|:-----------|:------------------------------------
&nbsp;&nbsp; [`misc:`](#misc)                             |  Optional  | Literal tool-specific controls. Refer to [CSolution Project Structure: `cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#cdefaultyml) for an example.

!!! Note
    The [`compiler:`](#compiler) selection in `cdefault.yml` has been deprecated in CMSIS-Toolbox 2.6.0.

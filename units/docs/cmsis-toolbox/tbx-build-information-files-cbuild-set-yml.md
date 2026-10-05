---
id: "tbx-build-information-files-cbuild-set-yml"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / `*.cbuild-set.yml`"
summary: "The <solution-name>.cbuild-set.yml file stores a legacy context selection for the csolution project. New projects should define a target-set: and select it with --active. The legacy file structure is outlined below."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#cbuild-set-yml"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

The `<solution-name>.cbuild-set.yml` file stores a legacy [context selection](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-tools.md#legacy-context-set) for the *csolution project*. New projects should define a [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#target-set) and select it with `--active`. The legacy file structure is outlined below.

`cbuild-set:`                                                      | Content
:------------------------------------------------------------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `generated-by:`                                 | Reference to tool along with version information that generated this file.
&nbsp;&nbsp;&nbsp; `contexts:`                                     | List of [context](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#context-name-conventions) names for the legacy [`--context-set`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-tools.md#legacy-context-set) option.

**Example:**

```yml
cbuild-set:
  generated-by: csolution version 2.2.0
  contexts:
    - context: CM33_s.Release+FVP
    - context: CM33_ns.Debug+FVP
```

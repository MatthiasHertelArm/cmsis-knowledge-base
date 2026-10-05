---
id: "tbx-troubleshooting-layer-search-fails"
type: "concept"
domain: "project"
title: "Troubleshooting: Layer Search Fails"
summary: "The cbuild setup command does not find compatible layers."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Troubleshooting.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Troubleshooting/#layer-search-fails"
license: "Apache-2.0"
mode: "V"
---

The `cbuild setup` command does not find compatible layers.

```txt
>cbuild setup xxx.csolution.yml
error csolution: undefined variables in xxx.csolution.yml:
  - $SDS-Layer$
```

The layer search of `cbuild setup` requires that the packs are defined in the `xxx.csolution.yml` file.  Ensure that the packs that define compatible layers are part of the software packs list, for example:

```yml
solution:

  # This is a CMSIS-Toolbox Reference Application that requires a compatible board layer
  # Refer to https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/ for more information

  packs:
    - pack: ARM::SDS          # search SDS pack for layers
```

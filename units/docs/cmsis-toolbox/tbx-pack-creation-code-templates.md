---
id: "tbx-pack-creation-code-templates"
type: "concept"
domain: "pack"
title: "Pack Creation: Code Templates"
summary: "Code Templates are part of a software component and published using the <components> element using attr=\"template\" in the PDSC file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#code-templates"
license: "Apache-2.0"
mode: "V"
---

*Code templates* are part of the [components files](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#Component_Files) in the PDSC file and can be manually added by the user to a software project. *Code templates* show how a software component is used, and the source code can be directly adapted to the requirements of the application program.

**Register *Code Templates* in PDSC File:**

[*Code Templates*](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#software-layers) are part of a software component and published using the [`<components>` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html) using `attr="template"` in the PDSC file.

```xml
  <component Cgroup="Socket" Csub="UDP" condition="Network Interface">
    :
    <files>
      <file category="doc"    name="Documentation/html/Network/group__netUDP__Func.html"/>
      <file category="header" name="Components/Network/Config/Net_Config_UDP.h" attr="config" version="5.1.1"/>
      <file category="source" name="Components/Network/Template/UDP_Socket.c" attr="template" select="UDP Socket"/>
      <!-- Library source files -->
      <file category="source" name="Components/Network/Source/net_udp.c"/>
    </files>
```

!!! Note
    The [CMSIS-RTX](https://github.com/ARM-software/CMSIS-RTX) and [MDK-Middleware](https://github.com/ARM-software/MDK-Middleware) packs contain several *code templates* that exemplify the overall structure.

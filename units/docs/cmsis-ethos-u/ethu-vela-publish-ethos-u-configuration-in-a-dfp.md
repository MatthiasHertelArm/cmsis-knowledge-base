---
id: "ethu-vela-publish-ethos-u-configuration-in-a-dfp"
type: "concept"
domain: "edge-ai"
title: "Vela: Create device-specific vela.ini file / Publish Ethos-U configuration in a DFP"
summary: "Part of: Create device-specific vela.ini file"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/vela/src/main.md#publish-ethos-u-configuration-in-a-dfp"
license: "Apache-2.0"
mode: "V"
---

_Part of: Create device-specific vela.ini file_

A CMSIS Device Family Pack (DFP) can publish the NPU capabilities, `vela.ini` file, and matching linker scripts in its DFP description. The CMSIS-Toolbox can then select these resources for the device, processor, and toolchain used by a project.

Declare each integrated NPU with a device `feature`. The `n` attribute identifies
the Ethos-U variant, `m` identifies its MAC configuration, and `Pname` associates
it with a processor when the device contains more than one:

```xml
<feature type="NPU" n="Ethos-U55" m="256MACs" Pname="M55_P0"/>
<feature type="NPU" n="Ethos-U55" m="128MACs" Pname="M55_P1"/>
```

Publish the device-specific Vela configuration through the `VELA` environment:

```xml
<environment name="VELA">
  <file name="Device/scripts/vela/device_vela.ini" type="ini"/>
</environment>
```

Add linker scripts as component files. Conditions can select the script that
matches a processor and toolchain:

```xml
<file category="linkerScript" name="Device/linker/linker_ac6.sct"    attr="config" condition="AC6"/>
<file category="linkerScript" name="Device/linker/linker_gnu.ld.src" attr="config" condition="GCC"/>
```

Keep the NPU feature, Vela environment, `My_vela.ini`, linker scripts, and their
conditions consistent. A project that selects a different processor or toolchain
must resolve to the corresponding NPU configuration and linker script.

For the complete pack structure and element rules, see:

- [DFP Pack Hands-On](https://github.com/Open-CMSIS-Pack/DFP-Pack-HandsOn);
- [`feature` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature);
- [`environment` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_environment); and
- [component `file` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

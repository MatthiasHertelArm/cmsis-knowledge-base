---
id: "spec-package-devices-family-element-package-devices-family-sequences"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../sequences"
summary: "Container for debug access sequences for this device."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Container for debug access sequences for this device.

**Example**
```
<family Dfamily="LPC4300 Series" Dvendor="NXP:11">
  ...
  <sequences traceSetup="legacy">
    ...
    <sequence name="DebugCoreStart" Pname="Cortex-M0">
      ...
    </sequence>
    ...
    <sequence name="ResetSystem" Pname="Cortex-M4">
      ...
    </sequence>
    ...
    <sequence name="TraceStart" Pname="Cortex-M4">
      ...
    </sequence>
    ...
  </sequences>
  ...
</family>
```

 		



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| device | element_device |  |  |
| Attributes | Description | Type | Use |
| traceSetup | If **full**, all trace sink and trace data path setup is done by debug access sequences. In this case, a debugger is not expected to configure trace sinks or the CoreSight trace data path using a priori knowledge of CoreSight trace components. If **legacy**, a debugger is expected to have knowledge of CoreSight trace components. In this case, the **TraceStart** and **TraceStop** sequences are intended only for device-specific trace setup and teardown steps. Default value is `legacy`. However, the expectation is that future DFPs set it to `full` and provide the full trace setup in sequences. The default value will change with the next major version update of this specification. | xs:boolean | optional |
| Child Elements | Description | Type | Occurrence |
| sequence | Describe a debug access sequence. | SequenceType | 1..* |

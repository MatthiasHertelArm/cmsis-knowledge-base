---
id: "spec-package-devices-family-element-package-devices-family-trace-tracebuffer"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../trace/tracebuffer"
summary: "Indicates on-device trace buffer capabilities of the specified processor. This element describes possible configuration settings for capturing trace and reading it from the buffer."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Indicates on-device trace buffer capabilities of the specified processor.
This element describes possible configuration settings for capturing trace
and reading it from the buffer. The optional **name** attribute identifies
the trace buffer for use with the `BufferStreamOut` and `TraceBufferSelected` debug access functions.
If more than one **tracebuffer** element is specified for a **trace**
element, every trace buffer shall have a unique **name** attribute. A single
trace buffer may omit the attribute.

**Example** for an LPC812 device. The MTB uses a configurable region of RAM; this example reserves its complete
4 KB SRAM region for trace capture.
```
<family Dfamily="LPC800" Dvendor="NXP:11">
  ...
  <trace>
    ...
    <tracebuffer name="MTB" start="0x10000000" size="0x1000"/>
    ...
  </trace>
  ...
</family>
```


 		



| Parents | Element Chain |  |  |
|---|---|---|---|
| trace | element_trace |  |  |
| Attributes | Description | Type | Use |
| name | Identifier of the trace buffer. This attribute is required and shall be unique when the parent **trace** element contains multiple **tracebuffer** elements. | RestrictedString | optional |
| start | Start address of the on-chip memory used as trace buffer for a supported configuration. | NonNegativeInteger | optional |
| size | Size of the on-chip memory used as trace buffer in bytes for a supported configuration. | NonNegativeInteger | optional |

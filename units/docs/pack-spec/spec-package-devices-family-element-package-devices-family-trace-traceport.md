---
id: "spec-package-devices-family-element-package-devices-family-trace-traceport"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../trace/traceport"
summary: "Indicates parallel trace port output capabilities of the specified processor. This element describes possible configuration settings for capturing trace. A trace element is expected to contain only one traceport element."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Indicates parallel trace port output capabilities of the specified processor.
This element describes possible configuration settings for capturing trace. A
**trace** element is expected to contain only one **traceport** element.

**Example**
```
<family Dfamily="LPC4300 Series" Dvendor="NXP:11">
  ...
  <trace>
    ...
    <traceport width="0x0000000B"/> <!-- support for port widths 1, 2, and 4 -->
    ...
  </trace>
  ...
</family>
```


 



| Parents | Element Chain |  |  |
|---|---|---|---|
| trace | element_trace |  |  |
| Attributes | Description | Type | Use |
| width | Parallel trace port widths supported for the processor connection (see table below). | NonNegativeInteger | optional |




The attribute **width** specifies the available trace port width that is supported by the device.
Each bit of this value represents an available trace port size. If bit `n` is set a trace port width of `n+1` is supported.
The value **width=0x00008088** (as shown in the table) indicates that three port sizes (16-bit, 8-bit, and 4-bit) are supported by the device.



| Bit | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| width | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| Value | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

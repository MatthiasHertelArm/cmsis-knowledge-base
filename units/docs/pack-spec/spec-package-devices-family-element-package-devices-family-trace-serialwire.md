---
id: "spec-package-devices-family-element-package-devices-family-trace-serialwire"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../trace/serialwire"
summary: "Indicates serial wire trace output capabilities of the specified processor. A trace element is expected to contain only one serialwire element."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Indicates serial wire trace output capabilities of the specified processor.
A **trace** element is expected to contain only one **serialwire** element.

**Example**
```
<family Dfamily="LPC4300 Series" Dvendor="NXP:11">
  ...
  <trace>
    ...
    <serialwire/>
    ...
  </trace>
  ...
</family>
```


 		



| Parents | Element Chain |
|---|---|
| trace | element_trace |

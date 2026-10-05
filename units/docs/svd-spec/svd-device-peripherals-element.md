---
id: "svd-device-peripherals-element"
type: "concept"
domain: "pack"
title: "/device/peripherals element"
summary: "All peripherals of a device are enclosed within the tag \\tagem{peripherals}."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_peripherals.html"
license: "Apache-2.0"
mode: "V"
---

All peripherals of a device are enclosed within the tag \tagem{peripherals}.


**Example:**
```
<device>
  ...
  <peripherals>
     ...
  </peripherals>
<device>
```


**/device/peripherals**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| device | elem_device |  |  |
| Child Elements | Description | Type | Occurrence |
| peripheral | Define the sequence of peripherals. | peripheralType | 1..* |



\delim_sec

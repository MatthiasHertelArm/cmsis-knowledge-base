---
id: "svd-device-peripherals-peripheral-regi"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element"
summary: "All registers of a peripheral are enclosed between the \\tagem{registers} opening and closing tags. Clusters define a set of registers. You can either use the \\tagem{cluster} or the \\tagem{register} element."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

All registers of a peripheral are enclosed between the \tagem{registers} opening and closing tags.
Clusters define a set of registers. You can either use the \tagem{cluster} or the \tagem{register} element.

**Example:**
```
...
<peripheral>
  <registers>
    ...
  </registers>
</peripheral>
...
```


**/device/peripherals/peripheral/registers**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| peripheral | elem_peripheral |  |  |
| Child Elements | Description | Type | Occurrence |
| cluster | Define the sequence of register clusters. | clusterType | 0..* |
| register | Define the sequence of registers. | registerType | 1..* |



\delim_sec

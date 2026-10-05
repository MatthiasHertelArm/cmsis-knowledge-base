---
id: "svd-device-peripherals-peripheral-regi-device-peripherals-peripheral-registers-2"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element: /device/peripherals/peripheral/registers/.../register/.../writeConstraint element"
summary: "Define constraints for writing values to a field. You can choose between three options, which are mutualy exclusive."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

Define constraints for writing values to a field. You can choose between three options, which are mutualy exclusive.

**Example:**
```
<register>
  ...
  <writeConstraint>
    <useEnumeratedValues>true</useEnumeratedValues>
  </writeConstraint>
  ...
  <field>
    <name>F_ONE</name>
    ...
    <writeConstraint>
      <range>
        <minimum>2</minimum>
        <maximum>4</maximum>
      </range>
    </writeConstraint>
    ...
  <field>
  <field>
    <name>F_TWO</name>
    ...
    <writeConstraint>
      <writeAsRead>true</writeAsRead>
    </writeConstraint>
    ...
  <field>
  <field>
    <name>F_N</name>
    ...
  <field>
  ...
<register>
```

The example shows write constraints defined on different levels. The write constrains on \tagem{register} level are propagated as default
to all subsequent fields, especially to field **F_N.** Field **F_ONE** overwrites the default and sets the write range between `2..4`.
Other values cannot be written to this field. Field **F_TWO** overwrites the default and allows to write only the last read value.


**/device/peripherals/peripheral/registers/.../register/.../writeConstraint**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<register>` | elem_register |  |  |
| `<field>` | elem_field |  |  |
| Child Elements | Description | Type | Occurrence |
| writeAsRead | If `true`, only the last read value can be written. | xs:boolean | 0..1 |
| useEnumeratedValues | If `true`, only the values listed in the `<enumeratedValues>` list can be written. xs:boolean | 0..1 |  |
| range | Contains the following two elements: |   | 0..1 |
| minimum | Specify the smallest number to be written to the field. | scaledNonNegativeInteger | 1..1 |
| maximum | Specify the largest number to be written to the field. | scaledNonNegativeInteger | 1..1 |



\delim_sec

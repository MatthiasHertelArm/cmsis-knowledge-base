---
id: "svd-device-peripherals-peripheral-regi-device-peripherals-peripheral-registers-3"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element: /device/peripherals/peripheral/registers/.../register/fields element"
summary: "Grouping element to define bit-field properties of a register."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

Grouping element to define bit-field properties of a register.

**Example:**
```
...
<fields>
  ...
  <field>
    <name>TimerCtrl0_IntSel</name>
    <description>Select interrupt line that is triggered by timer overflow.</description>
    <bitOffset>1</bitOffset>
    <bitWidth>3</bitWidth>
    <access>read-write</access>
    <modifiedWriteValues>oneToSet</modifiedWriteValues>
    <writeConstraint>
      <range>
        <minimum>0</minimum>
        <maximum>5</maximum>
      </range>
    </writeConstraint>
    <readAction>clear</readAction>
  <field>
  ...
  <field>
    <name>BIT1</name>
    <description>test</description>
    <bitRange>[7:0]</bitRange>
    <access>read-write</access>
  </field>
  ...
</fields>
...
```

The example creates two bit-files **TimerCtrl0_IntSel** and **BIT1.** The bit-field **TimerCtrl0_IntSel** has an bit offset of `1` and a depth
of `3` bits, with unrestricted read and write access, a reset value of `0` and a write constraint of `oneToSet`, which means that only the written bit is changed. The value allowed to be written to the field range between `0-5`. After a read operation, all bits are set to `zero`.

The bit-field **BIT1,** described as a test field, has the size of `8` bits and can be unlimited read and written.


**/device/peripherals/peripheral/registers/.../register/fields**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<register>` | elem_register |  |  |
| Child Elements | Description | Type | Occurrence |
| `<field>` | Define the bit-field properties of a register. | fieldType | 1..* |



\delim_sec

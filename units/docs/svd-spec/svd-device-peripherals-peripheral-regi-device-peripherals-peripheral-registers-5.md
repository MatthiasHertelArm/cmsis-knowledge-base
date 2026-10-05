---
id: "svd-device-peripherals-peripheral-regi-device-peripherals-peripheral-registers-5"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element: /device/peripherals/peripheral/registers/.../field/enumeratedValues element"
summary: "The concept of enumerated values creates a map between unsigned integers and an identifier string. In addition, a description string can be associated with each entry in the map."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

The concept of enumerated values creates a map between unsigned integers and an identifier string.
In addition, a description string can be associated with each entry in the map.



  0 <-> disabled -> "The clock source clk0 is turned off."
  1 <-> enabled  -> "The clock source clk1 is running."
  2 <-> reserved -> "Reserved values. Do not use."
  3 <-> reserved -> "Reserved values. Do not use."


This information generates an _enum_ in the device header file. The debugger may use
this information to display the identifier string as well as the description. Just like symbolic constants
making source code more readable, the system view in the debugger becomes more instructive. The detailed description
can provide reference manual level details within the debugger.

**Example:**

```
<enumeratedValues>

    <name>TimerIntSelect</name>
    <usage>read-write</usage>

    <enumeratedValue>
        <name>disabled</name>
        <description>The clock source clk0 is turned off.</description>
        <value>0</value>
    </enumeratedValue>

    <enumeratedValue>
        <name>enabled</name>
        <description>The clock source clk1 is running.</description>
        <value>1</value>
    </enumeratedValue>

    <enumeratedValue>
        <name>reserved</name>
        <description>Reserved values. Do not use.</description>
        <isDefault>true</isDefault>
    </enumeratedValue>

</enumeratedValues>
```



**/device/peripherals/peripheral/registers/.../field/enumeratedValues**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<field>` | elem_field |  |  |
| Attributes | Description | Type | Occurrence |
| derivedFrom | Makes a copy from a previously defined **enumeratedValues** section. No modifications are allowed. An **enumeratedValues** entry is referenced by its name. If the name is not unique throughout the description, it needs to be further qualified by specifying the associated field, register, and peripheral as required. For example: field: clk.dis_en_enum register + field: ctrl.clk.dis_en_enum peripheral + register + field: timer0.ctrl.clk.dis_en_enum | referenceIdentifierType | 0..1 |
| Child Elements | Description | Type | Occurrence |
| name | Identifier for the whole enumeration section. | xs:Name | 0..1 |
| headerEnumName | Identifier for the enumeration section. Overwrites the hierarchical enumeration type in the device header file. User is responsible for uniqueness across description. | identifierType | 0..1 |
| usage | Possible values are `read , write , or read-write`. This allows specifying two different enumerated values depending whether it is to be used for a read or a write access. If not specified, the default value `read-write` is used. | enumUsageType | 0..1 |
| `<enumeratedValue>` | Describes a single entry in the enumeration. The number of required items depends on the bit-width of the associated field. If derived from a previously defined **enumeratedValues** section, don't specify, else required. | enumeratedValueType | 0/1..* |



\delim_sec

---
id: "svd-device-peripherals-peripheral-regi-device-peripherals-peripheral-registers-4"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element: /device/peripherals/peripheral/registers/.../fields/field element"
summary: "All fields of a register are enclosed between the \\tagem{fields} opening and closing tags."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

All fields of a register are enclosed between the \tagem{fields} opening and closing tags.

A bit-field has a name that is unique within the register. The
position and size within the register can be decsribed in two ways:
 - by the combination of the least significant bit's position (lsb) and the most significant bit's position (msb), or
 - the lsb and the bit-width of the field.

A field may define an **enumeratedValue** in order to make the display more intuitive to read.



**/device/peripherals/peripheral/registers/.../fields/field**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<fields>` | elem_fields |  |  |
| Attributes | Description | Type | Occurrence |
| derivedFrom | Specify the field name from which to inherit data. Elements specified subsequently override inherited values. **Usage:** - Always use the full qualifying path, which must start with the peripheral \tagem{name}, when deriving from another scope. (for example, in periperhal `A` and `registerX`, derive from `peripheralA.registerYY.fieldYY`. - You can use the field \tagem{name} only when both fields are in the same scope. - No relative paths will work. **Remarks:** When deriving, it is mandatory to specify at least the \tagem{name} and \tagem{description}. | referenceIdentifierType | 0..1 |
| Child Elements | Description | Type | Occurrence |
|   | Refer to dimElementGroup_gr for details. |  |  |
| dim | Defines the number of elements in a list. | scaledNonNegativeInteger | 1..1 |
| dimIncrement | Specify the address increment, in `bits`, between two neighboring list members in the address map. | scaledNonNegativeInteger | 1..1 |
| dimIndex | Specify the strings that substitue the placeholder %%s within \tagem{name} and \tagem{displayName}. | dimIndexType | 0..1 |
| dimName | Specify the name of the C-type structure. If not defined, then the entry in the \tagem{name} element is used. | identifierType | 0..1 |
| `<dimArrayIndex>` | Grouping element to create enumerations in the header file. | dimArrayIndexType | 0..1 |
| name | Name string used to identify the field. Field names must be unique within a register. | dimableIdentifierType | 1..1 |
| description | String describing the details of the register. | stringType | 0..1 |
| Choice of | Three mutually exclusive options exist to describe the bit-range: | 1..1 |  |
| 1. bitRangeOffsetWidthStyle |  |  |  |
| bitOffset | Value defining the position of the least significant bit of the field within the register. | scaledNonNegativeInteger | 1..1 |
| bitWidth | Value defining the bit-width of the bitfield within the register. | scaledNonNegativeInteger | 1..1 |
| 2. bitRangeLsbMsbStyle |  |  |  |
| lsb | Value defining the bit position of the least significant bit within the register. | scaledNonNegativeInteger | 1..1 |
| msb | Value defining the bit position of the most significant bit within the register. | scaledNonNegativeInteger | 1..1 |
| 3. bitRangePattern |  |  |  |
| bitRange | A string in the format: "[`<msb>`:`<lsb>`]" | bitRangeType | 1..1 |
| access | Predefined strings set the access type. The element can be omitted if access rights get inherited from parent elements. | accessType | 0..1 |
| modifiedWriteValues | Describe the manipulation of data written to a field. If not specified, the value written to the field is the value stored in the field. The other options are bitwise operations: - `oneToClear`: write data bit of one shall clear (set to zero) the corresponding bit in the field. - `oneToSet`: write data bit of one shall set (set to one) the corresponding bit in the field. - `oneToToggle`: write data bit of one shall toggle (invert) the corresponding bit in the field. - `zeroToClear`: write data bit of zero shall clear (set to zero) the corresponding bit in the field. - `zeroToSet`: write data bit of zero shall set (set to one) the corresponding bit in the field. - `zeroToToggle`: write data bit of zero shall toggle (invert) the corresponding bit in the field. - `clear`: after a write operation all bits in the field are cleared (set to zero). - `set`: after a write operation all bits in the field are set (set to one). - `modify`: after a write operation all bit in the field may be modified (default). | modifiedWriteValuesType | 0..1 |
| `<writeConstraint>` | Three mutually exclusive options exist to set write-constraints. | writeConstraintType | 0..1 |
| readAction | If set, it specifies the side effect following a read operation. If not set, the field is not modified after a read. The defined side effects are: - `clear`: The field is cleared (set to zero) following a read operation. - `set`: The field is set (set to ones) following a read operation. - `modify`: The field is modified in some way after a read operation. - `modifyExternal`: One or more dependent resources other than the current field are immediately affected by a read operation (it is recommended that the field description specifies these dependencies). Debuggers are not expected to read this field location unless explicitly instructed by the user. | readActionType | 0..1 |
| `<enumeratedValues>` | Next lower level of description. | enumerationType | 0..2 |



\delim_sec

---
id: "svd-device-peripherals-peripheral-regi-device-peripherals-peripheral-registers"
type: "concept"
domain: "pack"
title: "/device/peripherals/peripheral/registers element: /device/peripherals/peripheral/registers/.../register element"
summary: "The description of registers is the most essential part of SVD. If the elements \\tagem{size}, \\tagem{access}, \\tagem{resetValue}, and \\tagem{resetMask} have not been specified on a higher level, then these elements are mandatory on register level."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"
license: "Apache-2.0"
mode: "V"
---

The description of registers is the most essential part of SVD. If the elements \tagem{size}, \tagem{access}, \tagem{resetValue}, and \tagem{resetMask}
have not been specified on a higher level, then these elements are mandatory on register level.

A register can represent a single value or can be subdivided into individual bit-fields of specific functionality and semantics.
From a schema perspective, the element \tagem{fields} is optional, however, from a specification perspective,
\tagem{fields} are mandatory when they are described in the device documentation.

You can define register arrays where the single description gets duplicated automatically.
The size of the array is specified by the \tagem{dim} element. Register names get composed by the element \tagem{name} and
the index-specific string defined in \tagem{dimIndex}. The element \tagem{dimIncrement} specifies the address offset between two registers.

**Example:**
```
...
<register>
  <name>TimerCtrl0</name>
  <description>Timer Control Register</description>
  <addressOffset>0x0</addressOffset>
  <access>read-write</access>
  <resetValue>0x00008001</resetValue>
  <resetMask>0x0000ffff</resetMask>
  <size>32</size>
</register>

<register derivedFrom="TimerCtrl0">
  <name>TimerCtrl1</name>
  <description>Derived Timer</description>
  <addressOffset>0x4</addressOffset>
</register>
...
```

This example describes two registers, **TimerCtrl0** and **TimerCtrl1.** The values defined for **TimerCtrl0** are inherited by the derived register
**TimerCtrl1,** except for the value in \tagem{addressOffset}.

**Example:**
```
...
<register>
    <name>TIM_MODEA</name>
    <description>In mode A this register acts as a reload value</description>
    <addressOffset>0xC</addressOffset>
</register>
<register>
    <name>TIM_MODEB</name>
    <description>In mode B this register acts as the compare value</description>
    <alternateRegister>TIM_MODEA</alternateRegister>
    <addressOffset>0xC</addressOffset>
</register>
<register>
    <name>DMA_DATA</name>
    <description>This register contains the address of the data being transferred</description>
    <dataType>uint32_t *</dataType>
    <addressOffset>0xf0</addressOffset>
</register>
...
```

This example describes two registers, **TIM_MODEA** and **TIM_MODEB.** Both have the same address offset. Based on the configured operation
model being A or B, the register acts as reload or compare value. The register DMA_DATA is specified as a pointer to unsigned word data.
The code generated for the device header file is:

```
typedef struct {
  union {
    __IO   uint32_t TIM_MODEA;
    __IO   uint32_t TIM_MODEB;
    };
  __IO uint32_t * DMA_DATA;
  ...
} <peripheral:name>_Type;

```



**/device/peripherals/peripheral/registers/.../register**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<cluster>` | elem_cluster |  |  |
| `<registers>` | elem_registers |  |  |
| Attributes | Description | Type | Occurrence |
| derivedFrom | Specify the register name from which to inherit data. Elements specified subsequently override inherited values. **Usage:** - Always use the full qualifying path, which must start with the peripheral \tagem{name}, when deriving from another scope. (for example, in periperhal `B`, derive from `peripheralA.registerX`. - You can use the register \tagem{name} only when both registers are in the same scope. - No relative paths will work. **Remarks:** When deriving, it is mandatory to specify at least the \tagem{name}, the \tagem{description}, and the \tagem{addressOffset}. | referenceIdentifierType | 0..1 |
| Child Elements | Description | Type | Occurrence |
|   | Refer to dimElementGroup_gr for details. |  |  |
| dim | Define the number of elements in an array of registers. If \tagem{dimIncrement} is specified, this element becomes mandatory. | scaledNonNegativeInteger | 1..1 |
| dimIncrement | Specify the address increment, in `Bytes`, between two neighboring registers. | scaledNonNegativeInteger | 1..1 |
| dimIndex | Specify the substrings that replaces the %%s placeholder within **name** and **displayName.** By default, the index is a decimal value starting with 0 for the first register. **dimIndex** should not be used together with the placeholder [%%s] , but rather with %%s . | dimIndexType | 0..1 |
| dimName | Specify the name of the C-type structure. If not defined, then the entry of the \tagem{name} element is used. | identifyerType | 0..1 |
| `<dimArrayIndex>` | Grouping element to create enumerations in the header file. | dimArrayIndexType | 0..1 |
| name | String to identify the register. Register names are required to be unique within the scope of a peripheral. You can use the placeholder %%s , which is replaced by the **dimIndex** substring. Use the placeholder [%%s] only at the end of the identifier to generate arrays in the header file. The placeholder [%%s] cannot be used together with **dimIndex. | registerNameType | 1..1 |
| displayName | When specified, then this string can be used by a graphical frontend to visualize the register. Otherwise the **name** element is displayed. **displayName** may contain special characters and white spaces. You can use the placeholder %%s , which is replaced by the **dimIndex** substring. Use the placeholder [%%s] only at the end of the identifier. The placeholder [%%s] cannot be used together with **dimIndex. | xs:string | 0..1 |
| description | String describing the details of the register. | xs:string | 0..1 |
| alternateGroup | Specifies a group name associated with all alternate register that have the same name. At the same time, it indicates that there is a register definition allocating the same absolute address in the address space. | xs:Name | 0..1 |
| alternateRegister | This tag can reference a register that has been defined above to current location in the description and that describes the memory location already. This tells the SVDConv's address checker that the redefinition of this particular register is intentional. The register name needs to be unique within the scope of the current peripheral. A register description is defined either for a unique address location or could be a redefinition of an already described address. In the latter case, the register can be either marked alternateRegister and needs to have a unique name, or it can have the same register name but is assigned to a register subgroup through the tag alternateGroup (specified in version 1.0). | identifierType | 0..1 |
| addressOffset | Define the address offset relative to the enclosing element. | scaledNonNegativeInteger | 1..1 |
|   | Refer to registerPropertiesGroup_gr for details about the colored elements. |  |  |
| size | Defines the default bit-width of any register contained in the device (implicit inheritance). | scaledNonNegativeInteger | 0..1 |
| access | Defines the default access rights for all registers. | accessType | 0..1 |
| protection | Defines the protection rights for all registers. | protectionStringType | 0..1 |
| resetValue | Defines the default value for all registers at RESET. | scaledNonNegativeInteger | 0..1 |
| resetMask | Identifies which register bits have a defined reset value. | scaledNonNegativeInteger | 0..1 |
| dataType | It can be useful to assign a specific native C datatype to a register. This helps avoiding type casts. For example, if a 32 bit register shall act as a pointer to a 32 bit unsigned data item, then dataType can be set to "uint32_t *". The following simple data types are predefined: - `uint8_t`: unsigned byte - `uint16_t`: unsigned half word - `uint32_t`: unsigned word - `uint64_t`: unsigned double word - `int8_t`: signed byte - `int16_t`: signed half word - `int32_t`: signed world - `int64_t`: signed double word - `uint8_t *`: pointer to unsigned byte - `uint16_t *`: pointer to unsigned half word - `uint32_t *`: pointer to unsigned word - `uint64_t *`: pointer to unsigned double word - `int8_t *`: pointer to signed byte - `int16_t *`: pointer to signed half word - `int32_t *`: pointer to signed world - `int64_t *`: pointer to signed double word dataTypeType | 0..1 |  |
| modifiedWriteValues | Element to describe the manipulation of data written to a register. If not specified, the value written to the field is the value stored in the field. The other options define bitwise operations: - `oneToClear`: write data bits of one shall clear (set to zero) the corresponding bit in the register. - `oneToSet`: write data bits of one shall set (set to one) the corresponding bit in the register. - `oneToToggle`: write data bits of one shall toggle (invert) the corresponding bit in the register. - `zeroToClear`: write data bits of zero shall clear (set to zero) the corresponding bit in the register. - `zeroToSet`: write data bits of zero shall set (set to one) the corresponding bit in the register. - `zeroToToggle`: write data bits of zero shall toggle (invert) the corresponding bit in the register. - `clear`: after a write operation all bits in the field are cleared (set to zero). - `set`: after a write operation all bits in the field are set (set to one). - `modify`: after a write operation all bit in the field may be modified (default). | modifiedWriteValuesType | 0..1 |
| `<writeConstraint>` | Three mutually exclusive options exist to set write-constraints. | writeConstraintType | 0..1 |
| readAction | If set, it specifies the side effect following a read operation. If not set, the register is not modified. The defined side effects are: - `clear`: The register is cleared (set to zero) following a read operation. - `set`: The register is set (set to ones) following a read operation. - `modify`: The register is modified in some way after a read operation. - `modifyExternal`: One or more dependent resources other than the current register are immediately affected by a read operation (it is recommended that the register description specifies these dependencies). Debuggers are not expected to read this register location unless explicitly instructed by the user. | readActionType | 0..1 |
| `<fields>` | In case a register is subdivided into bit fields, it should be reflected in the SVD description file to create bit-access macros and bit-field structures in the header file. | fieldsType | 0..1 |



\delim_sec

---
id: "svd-special-elements-registerpropertiesgroup"
type: "concept"
domain: "pack"
title: "Special Elements: registerPropertiesGroup"
summary: "The following elements are available on various levels. Element values defined on a lower level overwrite element values defined on a more general level. For example, \\tagem{register}.\\tagem{size} overwrites \\tagem{peripheral}.\\tagem{size}."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_special.html"
license: "Apache-2.0"
mode: "V"
---

The following elements are available on various levels.
Element values defined on a lower level overwrite element values defined on a more general level.
For example, \tagem{register}.\tagem{size} overwrites \tagem{peripheral}.\tagem{size}.
Elements not defined on a more general level, must be defined at \tagem{register} level at the latest.

Special requirements are described on the level where the element occurs. Click on the parent element in the table below for details.

**Example:**
```
<device schemaVersion="1.3" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="CMSIS-SVD.xsd">
  <name>ARM_Cortex_M3</name>
  <version>0.1</version>
  <description>Arm Cortex-M3 based Microcontroller demonstration device</description>
  <addressUnitBits>8</addressUnitBits>
  <width>32</width>
  <size>32</size>
  <access>read-write</access>
  <protection>s</protection>
  ...
  <peripherals>
    ...
  </peripherals>
</device>
```

Default settings have been defined for \tagem{width}, \tagem{size}, \tagem{access}, and \tagem{protection} on device level.
These settings can be refined on subsequent levels.


**Register Properties**


| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<device>` | elem_device |  |  |
| ` ` | elem_peripheral |  |  |
| `<register>` | elem_register |  |  |
| `<cluster>` | elem_cluster |  |  |
|   | `Below: Parent elements that have a reference to a single element of this block` |  |  |
| `<field>` | elem_field (only for element \tagem{access}) |  |  |
| `<sauRegionsConfig>` | elem_sauRegionsConfig (element \tagem{protection} for attribute \tagem{protectionWhenDisabled}) |  |  |
| `<addressBlock>` | elem_addressBlock (only for element \tagem{protection}) |  |  |
| Elements | Description | Type | Occurrence |
| size | Define the default bit-width of any device register (implicit inheritance). The value can be redefined on any lower level using the \tagem{size} element there. | scaledNonNegativeInteger | 0..1 |
| access | Define access rights. Access rights can be redefined at any lower level. Use one of the following predefined values: - `read-only`: Read access is permitted. Write operations have an undefined result. - `write-only`: Read operations have an undefined result. Write access is permitted. - `read-write`: Read and write accesses are permitted. Writes affect the state of the register and reads return the register value. - `writeOnce`: Read operations have an undefined results. Only the first write after reset has an effect. - `read-writeOnce`: Read access is always permitted. Only the first write access after a reset will have an effect on the content. Other write operations have an undefined result. | accessType | 0..1 |
| protection | Specify the security privilege to access an address region. This information is relevant for the programmer as well as the debugger when no universal access permissions have been granted. If no specific information is provided, an address region is accessible in any mode. The following values can be used to protect accesses by the programmer or debugger: - `"s"` - secure permission required for access - `"n"` - non-secure or secure permission required for access - `"p"` - privileged permission required for access | protectionStringType | 0..1 |
| resetValue | Define the default value for all registers at RESET. The value can be redefined on any lower level using the \tagem{resetValue} element there. The actual reset value is calculated from the \tagem{resetValue} and the \tagem{resetMask}. The mask is used to specify bits with an undefined reset value. | scaledNonNegativeInteger | 0..1 |
| resetMask | Identify register bits that have a defined reset value. These bit positions are set to `1`. Bit positions with an undefined reset value are set to `0`. | scaledNonNegativeInteger | 0..1 |

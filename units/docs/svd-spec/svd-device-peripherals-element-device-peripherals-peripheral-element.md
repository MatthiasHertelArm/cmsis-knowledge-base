---
id: "svd-device-peripherals-element-device-peripherals-peripheral-element"
type: "concept"
domain: "pack"
title: "/device/peripherals element: /device/peripherals/peripheral element"
summary: "At least one peripheral has to be defined. - Each peripheral describes all registers belonging to that peripheral. - The address range allocated by a peripheral is defined through one or more address blocks."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_peripherals.html"
license: "Apache-2.0"
mode: "V"
---

At least one peripheral has to be defined.
- Each peripheral describes all registers belonging to that peripheral.
- The address range allocated by a peripheral is defined through one or more address blocks.
- An address block and register addresses are specified relative to the base address of a peripheral.
The address block information can be used for constructing a memory map for the device peripherals.

Starting version 1.3 of the SVD specification, arrays of peripherals can be specified.
The single peripheral description gets duplicated automatically into an array.
The number of array elements is specified by the \tagem{dim} element. To define arrays, the \tagem{name} needs
the format _myPeripheral[%%s]_. The tag \tagem{dimIncrement} specifies the address offset between two
peripherals. To create copies of a peripheral using different names, you must use the **derivedFrom** attribute.

**Note:**  The memory map does not contain any information about physical memory. The memory of a
device is described as part of the CMSIS-Pack device description.

**Example:**
```
<peripherals>
  <peripheral>
    <name>Timer1</name>
    <version>1.0</version>
    <description>Timer 1 is a standard timer ... </description>
    <baseAddress>0x40002000</baseAddress>
    <addressBlock>
      <offset>0x0</offset>
      <size>0x400</size>
      <usage>registers</usage>
      <protection>s</protection>
    </addressBlock>
    <interrupt><name>TIM0_INT</name><value>34</value></interrupt>
    <registers>
      ...
    </registers>
  </peripheral>

  <peripheral>
    <name>Timer1_Alt</name>
    <version>1.0</version>
    <description>Alternate Timer 1 is a special timer execution mode ... </description>
    <baseAddress>0x40002000</baseAddress>
    <alternatePeripheral>Timer1</alternatePeripheral>
    ...
  </peripheral>
</peripherals>
```

Two timer peripheral descriptions are specified for the same memory block. No redefined addresses will be reported for both peripherals.


**/device/peripherals/peripheral**


  | 
    Parent Element | 
    Element Chain | 
  

  | 
    peripherals | 
    elem_peripherals | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    derivedFrom | 
    Specify the peripheral name from which to inherit data.
        Elements specified subsequently override inherited values.  | 
    dimableIdentifierType | 
    0..1 | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
      | 
    Refer to dimElementGroup_gr for details about the colored elements. | 
  

  | 
    dim | 
    Define the number of elements in an array. | 
    scaledNonNegativeInteger | 
    0..1  | 
  

  | 
    dimIncrement | 
    Specify the address increment, in `Bytes`, between two neighboring array members in the address map. | 
    scaledNonNegativeInteger | 
    0..1  | 
  

  | 
    dimIndex | 
    Do not define on peripheral level. By default, \tagem{dimIndex} is an integer value starting at `0`. | 
    dimIndexType | 
    0..1  | 
  

  | 
    dimName | 
    Specify the name of the C-type structure. If not defined, then the entry of the \tagem{name} element is used. | 
    idnetifierType | 
    0..1  | 
  

  | 
    `<dimArrayIndex>` | 
    Grouping element to create enumerations in the header file. | 
    dimArrayIndexType | 
    0..1  | 
  

  | 
    name  | 
    The string identifies the peripheral. Peripheral names are required to be unique for a device.
        The name needs to be an ANSI C identifier to generate the header file.
        You can use the placeholder _[%%s]_ to create arrays. | 
    dimableIdentifierType | 
    1..1  | 
  

  | 
    version  | 
    The string specifies the version of this peripheral description.  | 
    xs:string  | 
    0..1  | 
  

  | 
    description  | 
    The string provides an overview of the purpose and functionality of the peripheral. | 
    xs:string  | 
    0..1  | 
  

  | 
    alternatePeripheral | 
    All address blocks in the memory space of a device are assigned to a unique peripheral by default. If multiple
		peripherals describe the same address blocks, then this needs to be specified explicitly. A peripheral redefining an address block needs to
		specify the name of the peripheral that is listed first in the description. | 
    dimaleIdentifierType  | 
    0..1  | 
  

  | 
    groupName  | 
    Define a name under which the System Viewer is showing this peripheral. | 
    xs:Name  | 
    0..1  | 
  

  | 
    prependToName  | 
    Define a string as prefix. All register names of this peripheral get this prefix. | 
    identifierType  | 
    0..1  | 
  

  | 
    appendToName  | 
    Define a string as suffix. All register names of this peripheral get this suffix. | 
    identifierType  | 
    0..1  | 
  

  | 
    headerStructName | 
    Specify the base name of C structures. The headerfile generator uses the name of a peripheral as the base name for the C structure type.
        If \tagem{headerStructName} element is specfied, then this string is used instead of the peripheral name; useful when multiple peripherals get derived and a generic type name should be used. | 
    dimableIdentifierType  | 
    0..1  | 
  

  | 
    disableCondition  | 
    Define a C-language compliant logical expression returning a TRUE or FALSE result.
        If TRUE, refreshing the display for this peripheral is disabled and related accesses by the debugger are suppressed.
        \n \n Only constants and references to other registers contained in the description are allowed:
        \tagem{peripheral}->\tagem{register}->\tagem{field}, for example, (System->ClockControl->apbEnable == 0).
        The following operators are allowed in the expression [&&,||, ==, !=, >>, <<, &, |].
        **Warning:**
        Use this feature only in cases where accesses from the debugger to registers of
        un-clocked peripherals result in severe debugging failures. SVD is intended to provide
        static information and does not include any run-time computation or functions.
        Such capabilities can be added by the tools, and is beyond the scope of this
        description language. | 
    stringType  | 
    0..1  | 
  

  | 
    baseAddress  | 
    Lowest address reserved or used by the peripheral. | 
    scaledNonNegativeInteger  | 
    1..1  | 
  

  | 
      | 
    Refer to registerPropertiesGroup_gr for details about the colored elements. | 
  

  | 
    size | 
    Define the default bit-width of any register contained in the device (implicit inheritance). | 
    scaledNonNegativeInteger | 
    0..1 | 
  

  | 
    access | 
    Define default access rights for all registers. | 
    accessType | 
    0..1 | 
  

  | 
    protection | 
    Define default protection rights for all registers. | 
    protectionStringType | 
    0..1  | 
  

  | 
    resetValue  | 
    Define the default value for all registers at RESET. | 
    scaledNonNegativeInteger  | 
    0..1  | 
  

  | 
    resetMask | 
    Identify which register bits have a defined reset value. | 
    scaledNonNegativeInteger | 
    0..1 | 
  

  | 
    `<addressBlock>` | 
    Specify an address range uniquely mapped to this peripheral. A peripheral must
        have at least one address block, but can allocate multiple distinct address ranges.
        If a peripheral is derived from another peripheral, the addressBlock is not mandatory. | 
    addressBlockType | 
    0/1..* | 
  

  | 
    `<interrupt>` | 
    A peripheral can have multiple associated interrupts. This entry allows the debugger
        to show interrupt names instead of interrupt numbers. | 
    interruptType  | 
    0..*  | 
  

  | 
    `<registers>`  | 
    Group to enclose register definitions. | 
    registersType | 
    0..1  | 
  



\delim_sec

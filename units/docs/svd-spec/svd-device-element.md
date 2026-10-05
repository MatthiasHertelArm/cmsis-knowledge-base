---
id: "svd-device-element"
type: "concept"
domain: "pack"
title: "/device element"
summary: "The element \\tagem{device} provides the outermost frame of the description. - Only one \\tagem{device} section is allowed per file. All other elements are described within this scope. - A \\tagem{device} contains one or more peripherals, but one \\tagem{cpu} description."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/elem_device.html"
license: "Apache-2.0"
mode: "V"
---

The element \tagem{device} provides the outermost frame of the description.
    - Only one \tagem{device} section is allowed per file. All other elements are described within this scope.
    - A \tagem{device} contains one or more peripherals, but one \tagem{cpu} description.
    - Optional elements such as \tagem{size}, \tagem{access}, or \tagem{resetValue} defined on this level
      represent default values for registers and can be refined at lower levels.

**Example**
```
<device schemaVersion="1.3" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="CMSIS-SVD.xsd">
  <vendor>ARM Ltd.</vendor>
  <vendorID>ARM</vendorID>
  <name>ARM_Cortex_M4</name>
  <series>ARMCM4</series>
  <version>0.1</version>
  <description>Arm Cortex-M4 based Microcontroller demonstration device</description>
  <licenseText>
    Arm Limited (Arm) is supplying this software for use with Cortex-M \n
    processor based microcontrollers.  This file can be freely distributed \n
    within development tools that are supporting such Arm based processors. \n
    \n
    THIS SOFTWARE IS PROVIDED "AS IS".  NO WARRANTIES, WHETHER EXPRESS, IMPLIED \n
    OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF \n
    MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE. \n
    ARM SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL, OR \n
    CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.
  </licenseText>
  ...
  <headerSystemFilename>system_ARMCM4</headeSystemFilename>
  <headerDefinitionsPrefix>ARM_</headerDefinitionsPrefix>
  <addressUnitBits>8</addressUnitBits>
  <width>32</width>
  <size>32</size>
  <access>read-write</access>
  <resetValue>0</resetValue>
  <resetMask>0xffffffff</resetMask>
  <peripherals>
    ...
  </peripherals>
</device>
```

This example describes a device from the vendor `ARM Ltd.` using `ARM` as short name.
The device belongs to the device family `ARMCM4`. The device description is at version `0.1` and uniquely identifies the device by the name `ARM_Cortex_M4`. The legal disclaimer in the header files generated from
this description is captured and formatted in accordance to the standard Arm CMSIS disclaimer. The CMSIS system file included by the
generated device header file is named `system_ARMCM4.h` and all type definitions will be prepended with `ARM_`.

The peripherals are memory mapped in a byte-addressable address space with a bus width of `32` bits.
The default size of the registers contained in the peripherals is set to `32` bits.
Unless redefined for specific peripherals, all registers or fields are `read-write` accessible.
A reset value of `0`, valid for all `32` bits as specified by the reset mask,
is set for all registers unless redefined at a lower level.


**/device**


  | 
    Parent Level | 
    Element Chain | 
  

  | 
    root | 
    None; Document root | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    xmlns:xs | 
    Specify the underlying XML schema to which the CMSIS-SVD schema is compliant.
    Has to be set to: `"http://www.w3.org/2001/XMLSchema-instance"`. | 
    xs:string | 
    required | 
  

  | 
    xs:noNamespaceSchemaLocation | 
    Specify the file path and file name of the CMSIS-SVD Schema. For example, `CMSIS-SVD.xsd`. | 
    xs:string | 
    required | 
  

  | 
    schemaVersion | 
    Specify the compliant CMSIS-SVD schema version (for example, `1.1`). | 
    xs:decimal | 
    required | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    vendor | 
    Specify the vendor of the device using the full name.  | 
    xs:string  | 
    0..1  | 
  

  | 
    vendorID | 
    Specify the vendor abbreviation without spaces or special characters. This information is used
        to define the directory.  | 
    xs:string  | 
    0..1  | 
  

  | 
    name | 
    The string identifies the device or device series. Device names are required to be unique. | 
    xs:string  | 
    1..1  | 
  

  | 
    series | 
    Specify the name of the device series.  | 
    xs:string  | 
    0..1  | 
  

  | 
    version | 
    Define the version of the SVD file. Silicon vendors maintain the description
    throughout the life-cycle of the device and ensure that all updated and released copies
    have a unique version string. Higher numbers indicate a more recent version.  | 
  

    xs:string  | 
    1..1  | 
  | 
    description  | 
    Describe the main features of the device (for example CPU, clock frequency, peripheral overview). | 
    xs:string  | 
    1..1  | 
  

  | 
    licenseText  | 
    The text will be copied into the header section of the generated device header file and shall contain the legal disclaimer.
        New lines can be inserted by using `\\n`. This section is mandatory if the SVD file is used for generating the device header file. | 
    xs:string  | 
    0..1  | 
  

  | 
    `<cpu>`  | 
    Describe the processor included in the device. | 
    xs:string  | 
    0..1  | 
  

  | 
    headerSystemFilename  | 
    Specify the file name (without extension) of the device-specific system include file (system_<device>.h; See CMSIS-Core description).
        The header file generator customizes the include statement referencing the CMSIS system file within the CMSIS device header file.
        By default, the filename is system__device-name_.h. In cases where a device series shares a single system header file,
        the name of the series shall be used instead of the individual device name.  | 
    xs:string  | 
    0..1  | 
  

  | 
    headerDefinitionsPrefix  | 
    This string is prepended to all type definition names generated in the CMSIS-Core device header file.
        This is used if the vendor's software requires vendor-specific types in order to avoid name clashes with other definied types. | 
    xs:string  | 
    0..1  | 
  

  | 
    addressUnitBits  | 
    Define the number of data bits uniquely selected by each address.
    The value for Cortex-M-based devices is  `8` (byte-addressable).
     | 
    scaledNonNegativeInteger  | 
    1..1  | 
  

  | 
    width  | 
    Define the number of data bit-width of the maximum single data transfer supported
    by the bus infrastructure. This information is relevant for debuggers when accessing
    registers, because it might be required to issue multiple accesses for resources of a bigger size.
    The expected value for Cortex-M-based devices is `32`. | 
    scaledNonNegativeInteger  | 
    1..1  | 
  

  | 
       | 
     Refer to registerPropertiesGroup_gr for details about the colored elements listed below. | 
  

  | 
    size | 
    Default bit-width of any register contained in the device. | 
    scaledNonNegativeInteger | 
    0..1 | 
  

  | 
    access | 
    Default access rights for all registers. | 
    accessType | 
    0..1  | 
  

  | 
    protection | 
    Default access protection for all registers. | 
    protectionStringType | 
    0..1  | 
  

  | 
    resetValue  | 
    Default value for all registers at RESET. | 
    scaledNonNegativeInteger | 
    0..1  | 
  

  | 
    resetMask | 
    Define which register bits have a defined reset value. | 
    scaledNonNegativeInteger | 
    0..1 | 
  

  | 
    `<peripherals>` | 
    Group to define peripherals.  | 
      | 
    1..1  | 
  

  | 
    vendorExtensions  | 
    The content and format of this section is unspecified.
    Silicon vendors may choose to provide additional information. By default, this section
    is ignored when constructing CMSIS files. It is up to the silicon vendor to specify
    a schema for this section.
     | 
    xs:anyType (restriction)  | 
    0..1  |

---
id: "spec-package-conditions-element-package-conditions-condition-deny"
type: "concept"
domain: "pack"
title: "/package/conditions element: /package/conditions/condition/deny"
summary: "All attributes set in an accept, require, or deny must resolve to true for the element to become true."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/conditions_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html"
license: "Apache-2.0"
mode: "V"
---

All attributes set in an accept, require, or deny must resolve to true for the element to become true.
A condition becomes `true` when:
  - At least one accept element is true, AND
  - all require elements are true, AND
  - no deny element is true.



| Parent | Chain |  |  |
|---|---|---|---|
| condition /package/conditions/condition |  |  |  |
| Attributes | Description | Type | Use |
| Dvendor | Specifies the silicon vendor of the device. Use predefined values as listed in the table Device Vendor. | DeviceVendorEnum | optional |
| Dfamily***** | **DEPRECATED**** Specifies the device family name (for example: STM32F2 Series). | xs:string | optional |
| DsubFamily***** | **DEPRECATED****Specifies the device sub-family name (for example: STM32F205 Series). | xs:string | optional |
| Dname***** | Specifies the name of the device. | xs:string | optional |
| Dvariant***** | **DEPRECATED****Specifies the variant name of a device (for example: Step A). | xs:string | optional |
| Pname | Specifies the processor instance in case of multi processor devices. This allows to describe distinct conditions for a specific processor. | xs:string | optional |
| Dcore | Specifies a processor core. Use predefined values as listed in the table Device Cores. | DcoreEnum | optional |
| Dfpu | Specifies whether a Floating Point Unit (FPU) must be present or not. Predefined values can be used as listed in the table Device FPU. | DfpuEnum | optional |
| Dmpu | Specifies whether a Memory Protection Unit (MPU) must be present or not. Predefined values can be used as listed in the table Device MPU. | DmpuEnum | optional |
| Dtz | Specifies whether TrustZone (TZ) must be supported by the device or not. Predefined values can be used as listed in the table Device TrustZone. | DtzEnum | optional |
| Dsecure | Specifies whether the application is configured to run in secure or non-secure mode. Predefined values can be used as listed in the table Software Model Secure. | DsecureEnum | optional |
| Ddsp | Specifies whether Digital Signal Processing (DSP) instruction set must be supported by the device or not. Predefined values can be uses as listed in the table Device DSP. | DdspEnum | optional |
| Dmve | Specifies whether the M-Profile Vector instruction set extension must be supported by the device or not. Predefined values can be used as listed in the table Device MVE. | DmveEnum | optional |
| Dcdecp | Specifies whether [Custom Datapath Extension](https://support.arm.com/documentation/ddi0607/ab) Coprocessors and which coprocessor interfaces must be supported by the device. Possible values are explained in Custom Datapath Extensions. | DcdecpEnum | optional |
| Dpacbti | Specifies whether a device implements Pointer Authentication/Branch Target Identification (PAC/BTI) instructions. Possible values are explained in Device PAC/BTI. | DpacbtiEnum | required for ARMv8.1-M based devices with PAC/BTI support |
| Dendian | Specifies the endianess of a device. Use predefined values as listed in the table Endianess. | DendianEnum | optional |
| Cvendor***** | Specifies a component vendor name. | xs:string | optional |
| Cbundle***** | Specifies a component class bundle name. Requires that Cclass is also specified. | xs:string | optional |
| Cclass***** | Specifies a component class name. Predefined values can be used as listed in the table Component Classes. | CclassType | optional |
| Cgroup***** | Specifies a software Component Group. Predefined values can be used as listed in the table Component Groups. Requires that Cclass is also specified. | CgroupType | optional |
| Csub***** | Specifies a software component subgroup. The type is described in Component Subgroups. Requires that Cclass and Cgroup is also specified. | CsubType | optional |
| Cvariant***** | Specifies a software component variant. Requires that Cclass, Cgroup, and Csub (if part of the component definition) is also specified. | xs:string | optional |
| Cversion | Specifies a software component's version. Requires that Cclass, Cgroup, and Csub (if part of the component definition) is also specified. - **require Cversion:**condition is true if version of component is equal or higher than requested and compatible. According to [**SemanticVersioning**](https://semver.org/#spec-item-8) compatibility requires the **major version** to remain unchanged. - **deny Cversion:** condition is true if version of component is lower than requested. - Version ranges are specified with min_version **:** max_version . The condition is true if the version of the component is equal or higher than min_version and lower or equal than max_version . If min_version and max_version are equal the version must match exactly. Note: Specifying the min_version e.g Cversion="4.1.0" is identical to the version range Cversion="4.1.0:5.0.0-0" . VersionType | optional |  |
| Capiversion | Specifies an API version. - **require Capiversion:**condition is true if version of API is equal or higher than requested and compatible. According to [**SemanticVersioning**](https://semver.org/#spec-item-8) compatibility requires the **major version** to remain unchanged. - **deny Capiversion:** condition is true if version of API is lower than requested. - Version ranges are specified with min_version **:** max_version . The condition is true if the version of the API is equal or higher than min_version and lower or equal than max_version . If min_version and max_version are equal the version must match exactly. Note: Specifying the min_version e.g Capiversion="4.1.0" is identical to the version range Capiversion="4.1.0:5.0.0-0" . VersionType | optional |  |
| Bvendor***** | Specifies a board vendor name that refers to a `<board>` element in a PDSC file. | xs:string | optional |
| Bname***** | Specifies a board name that refers to a `<board>` element in a PDSC file. | xs:string | optional |
| Brevision***** | Specifies a board revision that refers to a `<board>` element in a PDSC file. | xs:string | optional |
| Hvendor | Specifies a part vendor name that refers to a \ element in a PDSC file. | xs:string | optional |
| Hname***** | Specifies a part name that refers to a \ element in a PDSC file. | xs:string | optional |
| Tcompiler | Specifies a compiler toolchain (ARMCC, GCC, IAR, Tasking, ...). Use predefined values as listed in table Compiler Types. | CompilerEnumType | optional |
| Toptions | Specifies compiler specific options being active. For Tcompiler="ARMCC" available Toptions are: - **AC5**: Arm Compiler Version 5 is in used - **AC6**: Arm Compiler Version 6 (armclang) is in use - **AC6LTO**: Arm Compiler Version 6 with Link Time Optimization (LTO) is in use This attribute can be used to select compatible libraries for the selected compiler version or optimization mode. Note: can only be used in combination with **Tcompiler.** | "AC5", "AC6", "AC6LTO" | optional |
| Toutput | Specifies the compiler output type. Use predefined values `exe` or `lib`. | "exe", "lib" | optional |
| condition | Refers to another condition identified through the attribute **\b** id. | xs:string | optional |



***)** Wild-cards can be used to match names with the following definitions:
       - '*'  matches any substring
       - '?'  matches any single character
       - [abc] matches any character in the set (a,b,c)

****)** These attributes must not be used in conditions because
           - 'Dfamily' and 'DsubFamily' turn out to be volatile, meaning that silicon vendors have a trend to change the grouping of devices.
           - conditions shall only filter for selectable devices. 'Dvariant'effectively is just an alias for 'Dname'.
             Once a \`<variant>` tag exists, the \`<device>` tag no longer represents a selectable device.


 

 **Table: Compiler Types**

The tale list values representing a C/C++ compiler toolchains from a specific tool vendor.
The tokens can be used in the elements:
- element_accept
- element_require
- element_deny



| Tcompiler= | Description |
|---|---|
| GCC | GNU Tools for Arm Embedded Processors. Refer to [Arm GCC](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain). |
| G++ | Code Sourcery GCC compiler for C and C++ (is now Mentor Graphics CodeBench). |
| ARMCC | Arm Compiler for C and C++. Refer to [ Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded). |
| IAR | IAR compiler for C and C++. |
| Tasking | TASKING compiler for C and C++. |
| GHS | Green Hills Software compiler for C, C++, and EC++. |
| XC | Microchip MPLAB XC32 Compiler. |
| Cosmic | Cosmic compiler for C and C++. |
| CLANG | CLANG: a C language family frontend for LLVM for 32-bit Arm embedded targets. Refer to [ CLANG](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm) |
| Renesas | Renesas compiler for C and C++. |
| CLANG_TI | CLANG-based TI compiler for C and C++. |

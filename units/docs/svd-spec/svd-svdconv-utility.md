---
id: "svd-svdconv-utility"
type: "concept"
domain: "pack"
title: "SVDConv utility"
summary: "Operation --------- SVDConv is invoked form the command line. The general command format is:"
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/svd_SVDConv_pg.html"
license: "Apache-2.0"
mode: "V"
---

**SVDConv** is a command-line utility to validate CMSIS-SVD files and to generate CMSIS-compliant device header files.
**SVDConv** is distributed with the **ARM::CMSIS** Pack (in the CMSIS\\Utilities directory) together with the **CMSIS-SVD.xsd** schema file.
**SVDConv** is available for Windows and Linux operating systems.

**SVDConv** performs the following operations:
  - Checks the syntactical and structural compliance with the specified CMSIS-SVD format.
  - Checks the consistency, correctness, and completeness of the CMSIS-SVD file against the CMSIS-SVD schema file.
  - Generates CMSIS-compliant device header files, which can be used for software development.

**Note:** Consider using \-\-strict option to receive all pedantic warnings. Some rules are skipped by default due to
  backward compatibility reasons. All newly developed/updated SVD files should rather respect all rules.


Operation
---------
**SVDConv** is invoked form the command line. The general command format is:
```
SVDConv.exe <SVD_file> <options>
```


 



| \`<options>` | Short Name | Description |
|---|---|---|
| none | Validation | Perform a validation check of the SVD file. Errors and warnings are printed on screen. |
| -b | Log File | Specify the log file name for writing messages. Default: screen. |
| -o | Output Path | Specify an output path for the generated device header file or log file. Default: current directory. |
| \-\-generate=header | Generate Device Header File | Generates the device header file. The name of the generated file is derived from the value of the tag `<devicename>` in the CMSIS-SVD file. Refer to `<device>`. |
| \-\-generate=partition | Generate Partition file for Cortex-M Security Extensions (Armv8-M) | Generates the device partition file. The name of the generated file is composed of partition_ and the value of the device `<name>` (for example, partition_CMSDK_ARMv8MBL.h ). Refer to elem_device. The content of the file uses Configuration Wizard annotations and is derived from the SAU-specific information of the elem_sauRegionsConfig and the interrupts specified in the elem_peripherals. |
| \-\-fields=enum | Bit-field Enums | Generates enum lists for each field value description contained in the CMSIS-SVD input file. Must be used in combination with \-\-generate=header . |
| \-\-fields=macro | Bit-field Macros | Generates position and mask C-Macros for each field description contained in the CMSIS-SVD input file. Must be used in combination with \-\-generate=header . |
| \-\-fields=struct | Bit-field Structs | Generates bit fields for each field description contained in the CMSIS-SVD input file. Must be used in combination with \-\-generate=header . |
| \-\-fields=struct-ansic | ANSI Bit-field Structs | Generates MISRA-compliant structures for each bitfield. The generated code **is not CMSIS-compliant**! Must be used in combination with \-\-generate=header . |
| \-\-strict | Strict error checking | **RECOMMENDED!** Applies strict error checking and generates a lot more messages. |



Return Codes
-------------

**SVDConv** returns the following codes:
\n
Code | Description             | Action
:---:|:------------------------|:--------------------
  0  | OK                      | No action required. Validation and conversion performed without errors.
  1  | WARNINGS                | Warnings should be checked an possibly removed. The header file is created and could be used.
  2  | ERRORS                  | Errors in the SVD description file. Important elements are missing and must be corrected.
  3  | Error in command line   | Check and correct the command line arguments.

**Examples** \n
-# Retrieve help information on screen.
```
     SVDConv
```
   \n
-# Perform a consistency check by passing only the SVD file name. Errors and warnings are printed on screen.
```
     SVDConv ARM_Example.svd
```
   \n
   The result is printed on screen:
```
   MVCM3110.svd(1688) : info
   <description> missing for value '2 : MODE2'
   MVCM3110.svd(1692) : info
   <description> missing for value '3 : MODE3'
   MVCM3110.svd(1696) : info
   <description> missing for value '4 : MODE4'
   Area of improvements:
Description contains 267 <fields> defined without associated <enumeratedValues>
   Found 0 Errors and 1 Warnings
   Return Code: 1 (WARNINGS)
```
   \n
-# Generate the header file. Performs a consistency check. Errors and warnings are printed on screen.
```
     SVDConv ARM_Example.svd --generate=header
```
   \n
   Code snippet from the generated header file showing the structure for **TIMER0.**
   \n
   \include "ARM_ExampleT0.h"
   \n
-# Generate the header file containing bit fields. Performs a consistency check. Errors and warnings are printed on screen.
```
     SVDConv ARM_Example.svd --generate=header --fields=struct
```
   \n
   Code snippet from the generated header file showing the structure for **TIMER0.**
   \n Compare to the code snippet above.
   \include "ARM_ExampleT0Struct.h"

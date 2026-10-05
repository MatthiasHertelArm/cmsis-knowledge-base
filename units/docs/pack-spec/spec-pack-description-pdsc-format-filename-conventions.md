---
id: "spec-pack-description-pdsc-format-filename-conventions"
type: "concept"
domain: "pack"
title: "Pack Description (*.pdsc) Format: Filename Conventions"
summary: "A software pack must have a unique filename which uses the following format: <vendor>.<name>.<version>.pack."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/packFormat.html"
license: "Apache-2.0"
mode: "V"
---

A software pack must have a unique filename which uses the following format:
**`<vendor>`.`<name>`.`<version>`.pack**.

**Where:**
 - **`<vendor>`**: name of the supplier or vendor of the software pack.
 - **`<name>`**: name of the software pack. It is the vendor's responsibility to ensure unique
   package names.
 - **\`<release version="X.Y.Z"\>`**: version number of the software pack.
 - **.pack**: file extension identifying a software pack.

**Note:** `<vendor>` and `<name>` **must** **not** contain spaces.

\n
The **Pack Description** (*.pdsc) file belonging to such a software pack file (`<vendor>`.`<name>`.`<version>`.pack)
is version independent and has the format:
**`<vendor>`.`<name>`.pdsc**.

**Where:**
 - **`<vendor>`**: name of the supplier or vendor of the software pack.
 - **`<name>`**: name of the software pack that is described by this *.pdsc file.
 - **.pack**: file extension identifying a software pack.

**Note:** `<vendor>` and `<name>` **must** **not** contain spaces.

Example filenames for software packs:

Software Pack for CMSIS Version 4.0 released by Arm.
 - **ARM.CMSIS.4.0.0.pack**: filename of the software pack.
 - **ARM.CMSIS.pdsc**: filename of the **Pack Description** (*.pdsc) file.

Device Family Pack for STM32F4 Version 1.0.0 released by ST Microelectronics.
 - **ST.STM32F4xx_DFP.1.0.0.pack**: filename of the software pack.
 - **ST.STM32F4xx.pdsc**: filename of the **Pack Description** (*.pdsc) file.

**Note:** All elements are case sensitive and must be consistently spelled in all places, i.e. the definition in the PDSC
file must match the filenames of the *.pdsc and *.pack files. The file extensions (*.pdsc and *.pack) must be lower case.

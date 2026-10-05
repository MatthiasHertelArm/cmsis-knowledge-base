---
id: "spec-technical-background-pack-conventions"
type: "concept"
domain: "pack"
title: "Technical background: Pack Conventions"
summary: "A software pack is a collection of files located in directories that are archived in a file with the extension .pack using the standard ZIP file format."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

A software pack is a collection of files located in directories that are archived in a file with the extension *.pack using the standard
ZIP file format.
The Pack Description file (PDSC) with the file extension *.pdsc contains the meta information, describing the content of a pack based on 
XML. The PDSC file must be:
- included in the software pack
- located in the base folder of the archive
- compliant with the software pack file naming convention

**Note:**
- The _base folder_ is defined to be the root folder './' of a zip archive and it is imperative that the whole
  software pack only contains a single PDSC file.
- Future tools shall support this case: if the PDSC file is located in an immediate subdirectory, then the subdirectory
  becomes the base folder. The software pack is installed as if the subdirectory does not exist. All
  files and directories located in the root folder are ignored and do not get installed.


### Pack File Name


A software pack must have a unique filename. Therefore it is constructed from vendor, packname and version and the file extension *.pack.

**`<vendor>`.`<name>`.`<version>`.pack**.

Where:
 - **`<vendor>`** is the name of the supplier or vendor of the software pack.
 - **`<name>`** is the name of the software pack. All packs that are published by a vendor must have a unique pack name.
 - **\`<release version="X.Y.Z"\>`**specifies the version number of the release for the software pack.
 - **.pack** is the file extension identifying a software pack.

**Note:**
- The XML elements \elem{vendor}, \elem{name}, and the version attribute of the \elem{release} are specified in the PDSC file. 
  PDSC, Pack filenames are case sensitive and need to match exactly.
- \elem{vendor} and \elem{name} **must** **not** contain spaces.
- The PDSC file needs to reside in the base folder of the Pack. All file references are relative to the location of the PDSC file.


### Software Component Cclasses


If you add a software component in the PDSC file, you have to specify a component class (CClass), component group (Cgroup),
and the component's version number (Cversion). For more information refer to cp_Components.

If applicable, try to map the **Cclass** of your software component to one of the following predefined or already well
established classes listed below.  These **Cclass** names are pre-defined in the CMSIS pack using the taxonomy element.

Cclass            | Description
:-----------------|:------------------------------------------------------------------
Audio             | Software components for audio processing
Board Support     | Generic interfaces for evaluation and development boards
Board Part *      | Drivers that support an external component available on an evaluation board
CMSIS             | _Common Microcontroller Software Interface Standard_ components
CMSIS Driver      | Unified device drivers compliant to the CMSIS-Driver specification
Compiler          | Arm Compiler software extensions
Data Exchange     | Data exchange components or data formatter, for example JSON
Device            | Startup and system setup components
Extension Board * | Drivers that support an extension boards or shield
File System*      | File drive support and file system
Graphics*         | Graphical libraries for user interfaces
IoT Client        | IoT cloud client connectors
IoT Service       | IoT specific services, i.e. device on-boarding
IoT Utility       | IoT specific utilities, i.e. a socket interface
Network*          | Network stack using Internet protocols
RTOS*             | Real-time operating systems
Security*         | Encryption for secure communication or storage
USB*              | Universal Serial Bus stack
Utility           | Generic software utility components

Classes with a * should always be used together with a bundle to avoid conflicts with other software
components.

If you wish to standardize a new Cclass, please send an inquiry to cmsis@arm.com or raise an issue on the public 
CMSIS GitHub development repository.

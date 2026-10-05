---
id: "svd-system-view-description"
type: "concept"
domain: "pack"
title: "System View Description"
summary: "Introduction ------------ The CMSIS System View Description format(CMSIS-SVD) formalizes the description of the system contained in Arm Cortex processor-based devices, in particular, the memory mapped registers of peripherals."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/System.html"
license: "Apache-2.0"
mode: "V"
---

Introduction
------------
The CMSIS System View Description format(CMSIS-SVD) formalizes the description of the system
contained in Arm Cortex processor-based devices, in particular, the memory mapped
registers of peripherals.
The detail contained in system view descriptions is comparable to the data in device
reference manuals. The information ranges from high level functional
descriptions of a peripheral all the way down to the definition and purpose of an individual bit
field in a memory mapped register.

CMSIS-SVD files are developed and maintained by silicon vendors.
Silicon vendors distribute their descriptions as part of CMSIS Device Family Packs.
Tool vendors use CMSIS-SVD files for providing device-specific debug views of peripherals in
their debugger. Last but not least, CMSIS-compliant device header files are generated from CMSIS-SVD
files.

CMSIS-SVD Benefits
------------------
- For Software Developers:
  - Consistency between device header file and what is being displayed by the debugger.
  - Detailed information about peripherals, registers, fields, and bit values as well as named
    interrupts from within the debugger, without the need to reference device documentation.
  - Convenient access to new and updated descriptions as part of the silicon vendor's CMSIS Device
    Family Packs as the packs are made available by silicon vendors.
  - Improved software development efficiency.

- For Silicon Vendors:
  - A tool vendor independent file format enables early device support by a wide range of toolchains
    with limited effort.
  - The XML-based format helps ease the integration into in-house design flows.
  - Automated generation of CMSIS compliant device header files.
  - Full control throughout the life cycle of the CMSIS-SVD files from creation to maintenance.

- For Tool Vendors:
  - Unified file format across silicon vendors helps the efficiency of supporting a wide range of
    devices in a timely manner.
  - Silicon vendors can provide early review access to the device support via restricted access to
    CMSIS Device Family Packs.
  - Updated descriptions are available over the web simplifying the maintenance of device support.

Language Specification and Conventions
---------------------------------------
- svd_Format_pg


CMSIS-SVD in ARM::CMSIS Pack
----------------------------

The following files relevant to CMSIS-SVD are present in the **ARM::CMSIS** Pack directories:

|File/Folder                   |Content
|------------------------------|-----------------------------------------------------------------------
|**CMSIS\\Documentation\\SVD**  | This documentation
|**CMSIS\\Utilities**           | Exemplary SVD file (ARM_Example.svd) and generated header file (ARM_Example.h).

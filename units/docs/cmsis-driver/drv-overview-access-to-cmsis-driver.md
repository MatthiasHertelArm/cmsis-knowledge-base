---
id: "drv-overview-access-to-cmsis-driver"
type: "concept"
domain: "drivers"
title: "Overview: Access to CMSIS-Driver"
summary: "CMSIS-Driver intefaces are actively maintained in the CMSIS 6 GitHub repository and released as part of the CMSIS Software Pack."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/mainpage.md#access-to-cmsis-driver"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Driver intefaces are actively maintained in the [**CMSIS 6 GitHub repository**](https://github.com/ARM-software/CMSIS_6) and released as part of the [**CMSIS Software Pack**](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/../General/cmsis_pack.html).

The CMSIS Software Pack publishes the API Interface under the Component Class **CMSIS Driver** with header files and a documentation. These header files are the reference for the implementation of the standardized peripheral driver interfaces.

These implementations are published typically in the Device Family Pack of a related microcontroller family under the Component Class **CMSIS Driver**. A Device Family Pack may contain additional interfaces in the Component Class **Device** to extend the standard Peripheral Drivers covered by this CMSIS-Driver specification with additional device specific interfaces for example for Memory BUS, GPIO, or DMA.

The following directories and files relevant to CMSIS-Driver are present in the **ARM::CMSIS** Pack:

 Directory                        | Content
:---------------------------------|:------------------------------------------------------------------------
📂 CMSIS                          | CMSIS Base software components folder
 ┣ 📂 Documentation/html/Driver   | A local copy of this CMSIS-Driver documentation
 ┣ 📂 Driver                      | Directory with CMSIS-Driver component, see cmsis_driver_files
   ┣ 📂 DriverTemplates | Driver Template files (Driver__interface_.c)
   ┣ 📂 Include         | API header files (Driver__interface_.h, %Driver_Common.h)
   ┗ 📂 VIO             | Implementation of virtual Input/Output interface (vio_interface_gr)

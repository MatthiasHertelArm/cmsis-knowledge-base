---
id: "sds-sds-with-sdsio-via-file-system-sd"
type: "concept"
domain: "test"
title: "SDS with SDSIO via File System (SD Card)"
summary: "This layer provides SDS with SDSIO using the SD card as storage media. It is implemented with the MDK-Middleware File System component. It is based on the following components:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:layer/sdsio/filesystem/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/layer/sdsio/filesystem/README.md"
license: "Apache-2.0"
mode: "V"
---

This layer provides SDS with SDSIO using the SD card as storage media.
It is implemented with the MDK-Middleware File System component.
It is based on the following components:

- [SDS](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDS__Stream__Interface.html) data streaming,
- [SDSIO](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDSIO__Interface.html) SDSIO interface,
- [CMSIS-Compiler](https://arm-software.github.io/CMSIS-Compiler/latest/index.html) retargeting standard C run-time library file operations,
- [MDK-Middleware File System](https://arm-software.github.io/MDK-Middleware/latest/FileSystem/index.html) file system interface,
- [CMSIS-Driver MCI](https://arm-software.github.io/CMSIS_6/latest/Driver/group__mci__interface__gr.html) physical interface.

---
id: "sds-sds-with-sdsio-via-network-etherne"
type: "concept"
domain: "test"
title: "SDS with SDSIO via Network (Ethernet)"
summary: "This layer provides SDS with SDSIO using the Ethernet-based IoT Socket communication. It is implemented with the MDK-Middleware Network component. It is based on the following components:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:layer/sdsio/network/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/layer/sdsio/network/README.md"
license: "Apache-2.0"
mode: "V"
---

This layer provides SDS with SDSIO using the Ethernet-based IoT Socket communication.
It is implemented with the MDK-Middleware Network component.
It is based on the following components:

- [SDS](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDS__Stream__Interface.html) data streaming,
- [SDSIO](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDSIO__Interface.html) SDSIO interface,
- [IoT Socket](https://mdk-packs.github.io/IoT_Socket/latest/index.html) communication interface,
- [MDK-Middleware Network](https://arm-software.github.io/MDK-Middleware/latest/Network/index.html) protocol stack,
- [CMSIS-Driver Ethernet](https://arm-software.github.io/CMSIS_6/latest/Driver/group__eth__interface__gr.html) physical interface.

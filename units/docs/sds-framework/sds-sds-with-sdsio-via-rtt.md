---
id: "sds-sds-with-sdsio-via-rtt"
type: "concept"
domain: "test"
title: "SDS with SDSIO via RTT"
summary: "This layer provides SDS with SDSIO using the RTT (Real Time Transfer) communication. It is implemented with the SEGGER RTT component. It is based on the following components:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:layer/sdsio/rtt/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/layer/sdsio/rtt/README.md"
license: "Apache-2.0"
mode: "V"
---

This layer provides SDS with SDSIO using the RTT (Real Time Transfer) communication.
It is implemented with the SEGGER RTT component.
It is based on the following components:

- [SDS](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDS__Stream__Interface.html) data streaming,
- [SDSIO](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDSIO__Interface.html) SDSIO interface,
- [RTT](https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/) communication channel.

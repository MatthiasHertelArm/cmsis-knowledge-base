---
id: "sds-utilities-sdsio-server"
type: "concept"
domain: "test"
title: "Utilities: SDSIO-Server"
summary: "The Python utility SDSIO-Server enables recording and playback of SDS data files via USB, socket (TCP/IP) or serial (UART) connection. It communicates with the target using a SDSIO-Client interface. Refer to the following sections for using the different client interfaces:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-server"
license: "Apache-2.0"
mode: "V"
---

The Python utility [**SDSIO-Server**](https://github.com/ARM-software/SDS-Framework/tree/main/utilities) enables recording and playback of SDS data files via USB, socket (TCP/IP) or serial (UART) connection.
It communicates with the target using a [SDSIO-Client interface](https://github.com/ARM-software/SDS-Framework/tree/main/sds/sdsio/client). Refer to the following sections for using the different client interfaces:

- [USB](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#using-usb-interface) for communication via USB using MDK-Middleware.
- [RTT](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#using-rtt-interface) for communication via the RTT interface of a debug adapter (J-Link or pyOCD).
- [Network](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/sdsio.md#using-network-interface) for TCP/IP communication via IoT Socket using MDK-Middleware, LwIP, or CMSIS-Driver WiFi.

SDS data streams are stored in file that use the format `<stream-name>.<label>[.p].sds`. See [Filenames](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#filenames) for details. The contents of SDS data files are described by the [YAML metadata](https://github.com/ARM-software/SDS-Framework/tree/main/schema) file that use the format `<stream-name>.sds.yml`.

---
id: "sds-theory-sdsio-server-protocols"
type: "concept"
domain: "test"
title: "theory: SDSIO-Server Protocols"
summary: "The SDSIO-Server communicates with the firmware using the SDSIO-Server Firmware Protocol over supported physical interfaces, including Ethernet, Wi-Fi, USB, debugger, and serial (USART) connections."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#sdsio-server-protocols"
license: "Apache-2.0"
mode: "V"
---

The SDSIO-Server communicates with the firmware using the [SDSIO-Server Firmware Protocol](#sdsio-server-firmware-protocol) over supported physical interfaces,
including Ethernet, Wi-Fi, USB, debugger, and serial (USART) connections.
It communicates with the monitor program through the [Monitor Interface](#sdsio-server-monitor-interface) over a network connection,
typically via the loopback (localhost) interface.

(figure: SDSIO-Server Protocols)

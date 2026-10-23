---
id: "drv-wifi-bypass-mode"
type: "concept"
domain: "drivers"
title: "WiFi Bypass Mode"
summary: "Transfer Ethernet frames by WiFi module. The wifi_bypass_gr functions are an optional interface and enable the transmission of Ethernet frames with WiFi modules."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

Transfer Ethernet frames by WiFi module.
 The wifi_bypass_gr functions are an optional interface and enable the transmission of
Ethernet frames with WiFi modules. The use of this interface requires that the TCP/IP stack is running
on the microcontroller (usually a third-party or open-source networking component). The internal TCP/IP
stack of the WiFi module is therefore not used, and this usually means that the wifi_socket_gr
functions can not be used.

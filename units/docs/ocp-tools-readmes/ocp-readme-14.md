---
id: "ocp-readme-14"
type: "concept"
domain: "project"
title: "README"
summary: "IoT Socket interface using WiFi module via CMSIS-Driver WiFi."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/Socket/WiFi/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/Socket/WiFi/README.md"
license: "Apache-2.0"
mode: "V"
---

Socket: WiFi
------------

[IoT Socket](https://mdk-packs.github.io/IoT_Socket/html/index.html) interface using WiFi module via 
[CMSIS-Driver WiFi](https://arm-software.github.io/CMSIS_6/latest/Driver/index.html).

The file `socket_startup.c` configures the WiFi connection with these settings:
 - SSID:          network identifier
 - PASSWORD:      network password
 - SECURITY_TYPE: network security

Note: These settings need to be configured by the user!

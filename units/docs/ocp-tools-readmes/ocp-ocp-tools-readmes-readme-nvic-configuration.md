---
id: "ocp-ocp-tools-readmes-readme-nvic-configuration"
type: "concept"
domain: "project"
title: "ocp-tools-readmes README: NVIC Configuration"
summary: "ocp-tools-readmes README: NVIC Configuration"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/Board/IMXRT1050-EVKB/IoT/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/Board/IMXRT1050-EVKB/IoT/README.md#nvic-configuration"
license: "Apache-2.0"
mode: "V"
---

| NVIC Interrupt      | Priority
|:--------------------|:--------
| ENET                | 8
| USDHC1              | 8
| LPUART3             | 8

**STDIO** is routed to debug console through Virtual COM port (DAP-Link, peripheral = LPUART1, baudrate = 115200)

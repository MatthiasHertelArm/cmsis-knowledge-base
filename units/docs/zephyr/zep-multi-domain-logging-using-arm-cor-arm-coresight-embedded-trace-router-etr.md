---
id: "zep-multi-domain-logging-using-arm-cor-arm-coresight-embedded-trace-router-etr"
type: "concept"
domain: "debug"
title: "Multi-domain logging using ARM Coresight STM: ARM Coresight Embedded Trace Router (ETR)"
summary: "ETR is a circular RAM buffer to which tracing data is saved. Since it may contain data from various sources additional wrapping protocol is used to multiplex them. Coresight Trace Formatter is used for that."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/logging/cs_stm.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/logging/cs_stm.rst"
license: "Apache-2.0"
mode: "V"
---

ETR is a circular RAM buffer to which tracing data is saved. Since it may contain data from
various sources additional wrapping protocol is used to multiplex them. ``Coresight Trace
Formatter`` is used for that. Data is encoded into 16 bytes frames which holds up to 15 byte
of data. Circular RAM buffer size is limited to 4k thus there is a risk of data overflow. If
overflow occurs then data is lost but due to presence of synchronization opcodes in the STPv2
data stream synchronization can be restored.

Data from ETR is handled on the device. It can be forwarded as-is to the host (e.g. using UART),
where a host tool is decoding the data or data can be decoded on-chip to output the data in human readable format.

Nordic Semiconductor NRF54H20 implementation instead of using ETR peripheral for getting
buffer busyness is using own wrapper: Trace Buffer Monitor (TBM).

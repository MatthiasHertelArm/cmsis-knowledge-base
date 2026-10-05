---
id: "zep-mipi-stp-decoder-limitations"
type: "concept"
domain: "debug"
title: "MIPI STP Decoder: Limitations"
summary: "MIPI STP Decoder: Limitations"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/mipi_stp_decoder.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/mipi_stp_decoder.rst"
license: "Apache-2.0"
mode: "V"
---

There are following limitations:

* Decoder supports only little endian architectures.
* When decoding nibbles, it is more efficient when core supports unaligned memory access.
  Implementation supports optimized version with unaligned memory access and generic one.
  Optimized version is used for ARM Cortex-M (expect for M0).
* Limited set of the most common opcodes is implemented.

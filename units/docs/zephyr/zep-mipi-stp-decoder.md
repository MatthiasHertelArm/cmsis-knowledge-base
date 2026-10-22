---
id: "zep-mipi-stp-decoder"
type: "concept"
domain: "debug"
title: "MIPI STP Decoder"
summary: "The MIPI System Trace Protocol (MIPI STP) was developed as a generic base protocol that can be shared by multiple application-specific trace protocols."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/mipi_stp_decoder.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/mipi_stp_decoder.rst"
license: "Apache-2.0"
mode: "V"
---

The MIPI System Trace Protocol (MIPI STP) was developed as a generic base protocol that can
be shared by multiple application-specific trace protocols. It serves as a wrapper protocol
that merges disparate streams that typically contain different trace protocols from different
trace sources. Stream consists of opcode (shortest is 4 bit long) followed by optional data and
optional timestamp. There are opcodes for data (8, 16, 32, 64 bit data marked/not marked, with or
without timestamp), stream recognition (master and channel), synchronization (ASYNC opcode) and
others.

One example where protocol is used is ARM Coresight STM (System Trace Macrocell) where data
written to Stimulus Port registers maps directly to STP stream.

This module can be used to perform on-chip decoding of the data stream. STP v2 is used.

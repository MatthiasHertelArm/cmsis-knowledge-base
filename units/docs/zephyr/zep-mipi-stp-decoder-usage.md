---
id: "zep-mipi-stp-decoder-usage"
type: "concept"
domain: "debug"
title: "MIPI STP Decoder: Usage"
summary: "Decoder is initialized with a callback. A callback is called on each decoded opcode. Decoder has internal state since there are dependency between opcodes (e.g. timestamp can be relative). Decoder can be in synchronization or not. Initial state is configurable."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/mipi_stp_decoder.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/mipi_stp_decoder.rst"
license: "Apache-2.0"
mode: "V"
---

Decoder is initialized with a callback. A callback is called on each decoded opcode.
Decoder has internal state since there are dependency between opcodes (e.g. timestamp can be
relative). Decoder can be in synchronization or not. Initial state is configurable.
If decoder is not synchronized to the stream then it decodes each nibble in search for ASYNC opcode.
Loss of synchronization can be indicated to the decoder by calling
`mipi_stp_decoder_sync_loss`. `mipi_stp_decoder_decode` is used to decode the data.

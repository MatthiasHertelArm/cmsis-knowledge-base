---
id: "zep-arm-coresight-trace-deformatter-usage"
type: "concept"
domain: "debug"
title: "ARM Coresight Trace Deformatter: Usage"
summary: "Deformatter is initialized with a user callback. Data is decoded using cs_trace_defmt_process in 16 bytes chunks. Callback is called whenever stream changes or end of chunk is reached. Callback contains stream ID and the data."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/cs_trace_defmt.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/cs_trace_defmt.rst"
license: "Apache-2.0"
mode: "V"
---

Deformatter is initialized with a user callback. Data is decoded using
`cs_trace_defmt_process` in 16 bytes chunks. Callback is called whenever stream changes or
end of chunk is reached. Callback contains stream ID and the data.

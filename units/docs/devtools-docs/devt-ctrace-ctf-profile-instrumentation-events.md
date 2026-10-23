---
id: "devt-ctrace-ctf-profile-instrumentation-events"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Instrumentation events"
summary: "The channel enumeration covers ITM stimulus ports 1 through 31. Labels from ctrace-run.yml replace the fallback names ITM1 through ITM31; duplicate labels receive a unique fallback."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/ctf-format.md#instrumentation-events"
license: "Apache-2.0"
mode: "V"
---

### ITM (event ID 0)

```text
cmsis_itm_channel_t cmsis_itm_channel
value tag and selected value variant
uint8_t             cmsis_sample_flags
uint32_t            cmsis_overflow_count
```

The channel enumeration covers ITM stimulus ports 1 through 31. Labels from `ctrace-run.yml` replace the fallback
names `ITM1` through `ITM31`; duplicate labels receive a unique fallback. Port 0 is decoded for stream integrity but
is intentionally excluded from CTF payload output.

Trace Compass exposes ITM as point events through its standard CTF event table. The generated XML does not invent a
time graph for these values.

---
id: "mlek-implementing-custom-ml-application-printing-to-console"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Printing to console"
summary: "The preceding examples used some function to print messages to the console. To use them, include mlek/log/log_macros.h header."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md#printing-to-console"
license: "Apache-2.0"
mode: "V"
---

The preceding examples used some function to print messages to the console. To use them, include `mlek/log/log_macros.h` header.

However, for clarity, here is the full list of available functions:

- `printf`
- `trace` - printf wrapper for tracing messages.
- `debug` - printf wrapper for debug messages.
- `info` - printf wrapper for informational messages.
- `warn` - printf wrapper for warning messages.
- `printf_err` - printf wrapper for error messages.

`printf` wrappers can be switched off with `MLEK_LOG_LEVEL` define:

`trace (0) < debug (1) < info (2) < warn (3) < error (4)`.

> **Note:** The default output level is `info = level 2`.

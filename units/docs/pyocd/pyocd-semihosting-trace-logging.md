---
id: "pyocd-semihosting-trace-logging"
type: "concept"
domain: "debug"
title: "Semihosting: Trace logging"
summary: "The semihosting agent supports a trace logger, pyocd.debug.semihost.trace that will output a log message every time a semihosting request is processed. This can be enabled on the command line with -Lpyocd.debug.semihost.trace=debug."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/semihosting.md#trace-logging"
license: "Apache-2.0"
mode: "V"
---

The semihosting agent supports a trace logger, `pyocd.debug.semihost.trace` that will output a log message every time a
semihosting request is processed. This can be enabled on the command line with `-Lpyocd.debug.semihost.trace=debug`.

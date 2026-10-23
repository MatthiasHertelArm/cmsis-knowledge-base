---
id: "zep-tracing-percepio-view-for-zephyr"
type: "concept"
domain: "debug"
title: "Tracing: Tracing Tools / Percepio View for Zephyr"
summary: "Percepio View is a free-of-charge tracing tool based on Percepio Tracealyzer, intended for debugging and verification of Zephyr applications."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tracing Tools_

Percepio View is a free-of-charge tracing tool based on Percepio Tracealyzer, intended for
debugging and verification of Zephyr applications.

Percepio View can be used side-by-side with a traditional debugger and complements your debugger
by visualising the real-time execution of threads, ISRs, syscalls and your own “User Events”.

To learn more about Percepio View, how to get started and upgrade options, check out
`Percepio's product page
<https://traceviewer.io/get-view/?target=zephyr>`_.

Percepio View provides snapshot tracing, meaning the data is stored to a ring-buffer in target RAM
and is saved to host using the regular debugger connection.
For trace streaming support, Percepio offers (paid-for) upgrades to Percepio Profile or
Percepio Tracealyzer. No modifications of the Zephyr source code are needed, only enabling the
TraceRecorder library in Kconfig. Percepio View runs on Windows and Linux hosts.

---
id: "zep-tracing-segger-systemview-support"
type: "concept"
domain: "debug"
title: "Tracing: Tracing Tools / SEGGER SystemView Support"
summary: "Zephyr provides built-in support for SEGGER SystemView that can be enabled in any application for platforms that have the required hardware support."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tracing Tools_

Zephyr provides built-in support for SEGGER SystemView that can be enabled in
any application for platforms that have the required hardware support.

The payload and format used with SystemView is custom to the application and
relies on RTT as a transport. Newer versions of SystemView support other
transports, for example UART or using snapshot mode (both still not
supported in Zephyr).

To enable tracing support with SEGGER SystemView add the
snippet-rtt-tracing to your build command:

SystemView can also be used for post-mortem tracing, which can be enabled with
`CONFIG_SEGGER_SYSVIEW_POST_MORTEM_MODE`. In this mode, a debugger can
be attached after the system has crashed using `west attach` after which the
latest data from the internal RAM buffer can be loaded into SystemView.

Recent versions of SEGGER SystemView come with an API translation table for
Zephyr which is incomplete and does not match the current level of support
available in Zephyr. To use the latest Zephyr API description table, copy the
file available in the tree to your local configuration directory to override the
builtin table::
```
# On Linux and MacOS
cp $ZEPHYR_BASE/subsys/tracing/sysview/SYSVIEW_Zephyr.txt ~/.config/SEGGER/
```

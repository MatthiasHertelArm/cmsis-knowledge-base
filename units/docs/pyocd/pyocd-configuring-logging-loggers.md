---
id: "pyocd-configuring-logging-loggers"
type: "concept"
domain: "debug"
title: "Configuring logging: Loggers"
summary: "Each module in pyOCD uses its own module-specific logger with a name matching the dotted module name, for instance pyocd.coresight.fpb. This lets you control verbosity at the module level."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/configuring_logging.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/configuring_logging.md#loggers"
license: "Apache-2.0"
mode: "V"
---

Each module in pyOCD uses its own module-specific logger with a name matching the dotted module
name, for instance `pyocd.coresight.fpb`. This lets you control verbosity at the module level. Even
more advanced configurations, such as routing a particular module's log output to a separate file,
are also possible.

The best way to see which loggers are available is simply to look at the pyOCD source code to see
its package structure.


### Trace loggers

Certain modules define additional sub-module loggers that output debug trace logs. These loggers always have the
suffix ".trace" and are disabled by default. This ensures the trace messages won't be seen unless explicitly enabled by the `--log-level` / `-L` argument described in the following section.

Currently defined trace loggers:

Trace logger                                            | Trace output
--------------------------------------------------------|----------------------------------------------
`pyocd.coresight.ap.trace`                              | AP memory transfers
`pyocd.coresight.dap.trace`                             | AP and DP register accesses
`pyocd.debug.semihost.trace`                            | Semihost file operations
`pyocd.debug.sequences.scope.trace`                     | Open-CMSIS-Pack debug sequence variable read/write
`pyocd.debug.sequences.sequences.trace`                 | Open-CMSIS-Pack debug sequence statements
`pyocd.flash.flash.trace`                               | Flash algorithm operations
`pyocd.probe.cmsis_dap_probe.trace`                     | CMSIS-DAP probe API calls
`pyocd.probe.jlink_probe.trace`                         | Log output from JLink library
`pyocd.probe.pydapaccess.dap_access_cmsis_dap.trace`    | CMSIS-DAP packet building
`pyocd.probe.pydapaccess.interface.hidapi_backend.trace` | CMSIS-DAP v1 hidapi backend USB transfers
`pyocd.probe.pydapaccess.interface.pyusb_backend.trace` | CMSIS-DAP v1 pyusb backend USB transfers
`pyocd.probe.pydapaccess.interface.pyusb_v2_backend.trace` | CMSIS-DAP v2 pyusb backend USB transfers
`pyocd.probe.pydapaccess.interface.pywinusb_backend.trace` | CMSIS-DAP v1 pywinusb backend USB transfers
`pyocd.probe.stlink.usb.trace`                          | STLink USB transfers
`pyocd.probe.tcp_client_probe.trace`                    | Remote probe client requests and responses
`pyocd.probe.tcp_probe_server.trace`                    | Remote probe server requests and responses
`pyocd.utility.notification.trace`                      | Sent notifications

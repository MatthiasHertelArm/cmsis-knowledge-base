---
id: "zep-tracing-out-of-tree-tracing-formats"
type: "concept"
domain: "debug"
title: "Tracing: Tracing Tools / Out-of-tree Tracing Formats"
summary: "A downstream module can supply its own tracing format without editing the Zephyr tree."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tracing Tools_

A downstream module can supply its own tracing format without editing the Zephyr
tree. Set `CONFIG_TRACING_FORMAT_HEADER` (a promptless Kconfig
string, assigned from the module's `Kconfig` with a `default`) to the name of
a header on the include path; `include/zephyr/tracing/tracing.h`
pulls it in with a computed `#include` when no in-tree format is selected.

The format header defines the `sys_port_trace_*` hooks it records and ends with:

```c

/* default no-ops for the scheduler/idle/init/named function layer */
#include <zephyr/tracing/tracing_default_hooks.h>
/* no-op for every sys_port_trace_* hook this header does not define */
#include <zephyr/tracing/tracing_hooks.h>
```
so a format only has to implement the hooks it cares about. A tracing transport
is added independently with `TRACING_BACKEND_DEFINE()` (see
`subsys/tracing/include/tracing_backend.h`), so neither a custom
format nor a custom backend requires changes to the core tree.
`tests/subsys/tracing/tracing_format_module` is a complete worked
example.

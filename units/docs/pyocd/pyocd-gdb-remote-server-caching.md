---
id: "pyocd-gdb-remote-server-caching"
type: "concept"
domain: "debug"
title: "gdb remote server: Caching"
summary: "Several forms of caching are supported to improve performance when communicating with gdb."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/gdbserver.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/gdbserver.md#caching"
license: "Apache-2.0"
mode: "V"
---

Several forms of caching are supported to improve performance when communicating with gdb.

Note that these caches are currently only used with gdb, not for pyOCD's commander interface or the `Target` Python API. (But they will be used for the `DebugContext` objects return from `SoCTarget.get_target_context()`, if that is used through the Python API.)

### Reading memory from the ELF

If provided the firmware's ELF executable file with the `--elf` argument, pyOCD will read target memory contents present in the ELF from that file instead of reading from the target via SWD/JTAG. This can be faster, especially with slower debug probe connections or wire protocol speeds.

The `cache.read_code_from_elf` session option (bool) controls whether this feature is enabled. It's turned on by default, but of course requires the ELF to be passed to pyOCD. (Unfortunately, there is no way to access the executable through gdb.)

### Memory and register cache

Caches for target memory and core register values are present and enabled by default. Both caches are invalidated every time the core is resumed or stepped.

The memory cache will cache any memory region marked as cacheable (all are by default). To disable caching for a memory region, a user script can be used to set its `is_cacheable` property to False.

For example, to disable caching of the "iram" region:

```py
def will_connect():
    target.memory_map.get_first_matching_region(name="iram").is_cacheable = False
```

(Use the `show map` command to see the list of memory regions.)

These session options allow control over the memory and register caches. Both are enabled by default.

- `cache.enable_memory` (bool)
- `cache.enable_register` (bool)

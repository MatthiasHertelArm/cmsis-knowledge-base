---
id: "pyocd-memory-transfer-attributes-controlling-attributes"
type: "concept"
domain: "debug"
title: "Memory transfer attributes: Controlling attributes"
summary: "In pyOCD, the HPROT value for memory transactions is set using the set hprot <value> command, and show hprot to view the current setting."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/memory_attributes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/memory_attributes.md#controlling-attributes"
license: "Apache-2.0"
mode: "V"
---

In pyOCD, the HPROT value for memory transactions is set using the `set hprot <value>` command, and `show hprot` to view the current setting. These modify/view the currently selected MEM-AP (`set/show mem-ap`), which is independent of the gdbserver's core (not something to worry about if you are only debugging core #0).

As a reminder, these commands can be executed from gdb by prefixing them with the gdb `monitor` command. For example, to enable cacheable transfers from gdb, you'd run `monitor set hprot 0xb`. This can be placed in a connect script if you want cacheable transfers all the time.

To configure the used attributes in a pyOCD [user script]({% link _docs/user_scripts.md %}), a snippet such as this is can be used:

```py
def did_connect():
    target.aps[0].hprot = 0xb
```

And if using pyOCD via a Python script, mirror the statement inside `did_connect()` above using your target object.

In the above commands, 0xb == data (hprot[0]) | privileged (hprot[1]) | cacheable (hprot[3]).

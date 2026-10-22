---
id: "zep-troubleshooting-devicetree-validate-properties"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Validate properties"
summary: "If you're getting a compile error reading a node property, check your node identifier and property. For example, if you get a build error on a line that looks like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

If you're getting a compile error reading a node property, check your node
identifier and property. For example, if you get a build error on a line that
looks like this:

```c

int baud_rate = DT_PROP(DT_NODELABEL(my_serial), current_speed);
```
Try checking the node by adding this to the file and recompiling:

```c

#if !DT_NODE_EXISTS(DT_NODELABEL(my_serial))
#error "whoops"
#endif
```
If you see the "whoops" error message when you rebuild, the node identifier
isn't referring to a valid node. get-devicetree-outputs and debug from
there.

Some hints for what to check next if you don't see the "whoops" error message:

- did you dt-use-the-right-names?
- does the property exist?
- does the node have a matching binding?
- does the binding define the property?

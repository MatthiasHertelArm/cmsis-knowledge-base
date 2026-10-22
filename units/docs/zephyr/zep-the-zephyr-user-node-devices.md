---
id: "zep-the-zephyr-user-node-devices"
type: "concept"
domain: "project"
title: "The `/zephyr,user` node: Devices"
summary: "You can store phandles in /zephyr,user if you want to be able to reconfigure which devices your application uses in simple cases using devicetree overlays."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/zephyr-user-node.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/zephyr-user-node.rst"
license: "Apache-2.0"
mode: "V"
---

You can store phandles in `/zephyr,user` if you want to
be able to reconfigure which devices your application uses in simple cases
using devicetree overlays.

For example, with this devicetree overlay:

```devicetree

/ {
 zephyr,user {
     handle = <&gpio0>;
     handles = <&gpio0>, <&gpio1>;
     };
};
```
You can convert the phandles in the `handle` and `handles` properties to
device pointers like this:

```C

/*
 * Same thing as:
 *
 * ... my_dev = DEVICE_DT_GET(DT_NODELABEL(gpio0));
 */
const struct device *my_device =
    DEVICE_DT_GET(DT_PROP(ZEPHYR_USER_NODE, handle));

/*
 * Same thing as:
 *
 * ... *my_devices[] = {
 *         DEVICE_DT_GET(DT_NODELABEL(gpio0)),
 *         DEVICE_DT_GET(DT_NODELABEL(gpio1))
 * };
 */
const struct device *my_devices[] = {
     DT_FOREACH_PROP_ELEM_SEP(ZEPHYR_USER_NODE, handles, DEVICE_DT_GET_BY_IDX, (,))
};
```

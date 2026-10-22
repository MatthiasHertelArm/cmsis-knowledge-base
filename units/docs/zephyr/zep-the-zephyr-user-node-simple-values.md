---
id: "zep-the-zephyr-user-node-simple-values"
type: "concept"
domain: "project"
title: "The `/zephyr,user` node: Simple values"
summary: "You can store numeric or array values in /zephyr,user if you want them to be configurable at build time via devicetree."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/zephyr-user-node.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/zephyr-user-node.rst"
license: "Apache-2.0"
mode: "V"
---

You can store numeric or array values in `/zephyr,user` if you want them to
be configurable at build time via devicetree.

For example, with this devicetree overlay:

```devicetree

/ {
 zephyr,user {
     boolean;
     bytes = [81 82 83];
     number = <23>;
     numbers = <1>, <2>, <3>;
     string = "text";
     strings = "a", "b", "c";
 };
};
```
You can get the above property values in C/C++ code like this:

```C

#define ZEPHYR_USER_NODE DT_PATH(zephyr_user)

DT_PROP(ZEPHYR_USER_NODE, boolean) // 1
DT_PROP(ZEPHYR_USER_NODE, bytes)   // {0x81, 0x82, 0x83}
DT_PROP(ZEPHYR_USER_NODE, number)  // 23
DT_PROP(ZEPHYR_USER_NODE, numbers) // {1, 2, 3}
DT_PROP(ZEPHYR_USER_NODE, string)  // "text"
DT_PROP(ZEPHYR_USER_NODE, strings) // {"a", "b", "c"}
```

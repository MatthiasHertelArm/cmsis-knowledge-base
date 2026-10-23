---
id: "zep-troubleshooting-devicetree-make-sure-you-re-using-the-right-names"
type: "concept"
domain: "project"
title: "Troubleshooting devicetree: Make sure you're using the right names"
summary: "For example, if you're trying to get the clock-frequency property of a node with path /soc/i2c@12340000 in a C/C++ file:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

Remember that:

- In C/C++, devicetree names must be lowercased and special characters must be
  converted to underscores. Zephyr's generated devicetree header has DTS names
  converted in this way into the C tokens used by the preprocessor-based
  `<devicetree.h>` API.
- In overlays, use devicetree node and property names the same way they
  would appear in any DTS file. Zephyr overlays are just DTS fragments.

For example, if you're trying to **get** the `clock-frequency` property of a
node with path `/soc/i2c@12340000` in a C/C++ file:

```c

/*
 * foo.c: lowercase-and-underscores names
 */

/* Don't do this: */
#define MY_CLOCK_FREQ DT_PROP(DT_PATH(soc, i2c@1234000), clock-frequency)
/*                                           ^               ^
 *                                        @ should be _     - should be _  */

/* Do this instead: */
#define MY_CLOCK_FREQ DT_PROP(DT_PATH(soc, i2c_1234000), clock_frequency)
/*                                           ^               ^           */
```
And if you're trying to **set** that property in a devicetree overlay:

```none

/*
 * foo.overlay: DTS names with special characters, etc.
 */

/* Don't do this; you'll get devicetree errors. */
&{/soc/i2c_12340000/} {
    clock_frequency = <115200>;
};

/* Do this instead. Overlays are just DTS fragments. */
&{/soc/i2c@12340000/} {
    clock-frequency = <115200>;
};
```

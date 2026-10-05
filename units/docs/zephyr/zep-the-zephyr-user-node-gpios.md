---
id: "zep-the-zephyr-user-node-gpios"
type: "concept"
domain: "project"
title: "The `/zephyr,user` node: GPIOs"
summary: "The /zephyr,user node is a convenient place to store application-specific GPIOs that you want to be able to reconfigure with a devicetree overlay."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/zephyr-user-node.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/zephyr-user-node.rst"
license: "Apache-2.0"
mode: "V"
---

The `/zephyr,user` node is a convenient place to store application-specific
GPIOs that you want to be able to reconfigure with a devicetree overlay.


**Note:** All properties with a value containing at least one phandle and a number will be inferred as a phandle-array. example `<&adc0 1>`.

For example, with this devicetree overlay:

```devicetree

#include <zephyr/dt-bindings/gpio/gpio.h>

/ {
 zephyr,user {
     signal-gpios = <&gpio0 1 GPIO_ACTIVE_HIGH>;
     };
};
```
You can convert the pin defined in `signal-gpios` to a ``struct
gpio_dt_spec`` in your source code, then use it like this:

```C

#include <zephyr/drivers/gpio.h>

#define ZEPHYR_USER_NODE DT_PATH(zephyr_user)

const struct gpio_dt_spec signal =
        GPIO_DT_SPEC_GET(ZEPHYR_USER_NODE, signal_gpios);

/* Configure the pin */
gpio_pin_configure_dt(&signal, GPIO_OUTPUT_INACTIVE);

/* Set the pin to its active level */
gpio_pin_set_dt(&signal, 1);
```
(See `gpio_dt_spec`, `GPIO_DT_SPEC_GET`, and
`gpio_pin_configure_dt` for details on these APIs.)

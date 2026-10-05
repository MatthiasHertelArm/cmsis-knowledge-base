---
id: "intr-practical-zephyr-devicetree-practi-device-driver-function-calls"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Device driver function calls"
summary: "Even though we still won't write an instance-based device driver in this article series it is worth quickly (and this time I mean really quickly) reviewing how Zephyr's API function calls map to the function tables provided by …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#device-driver-function-calls"
license: "CC-BY-SA-4.0"
mode: "V"
---

Even though we still won't write an instance-based device driver in this article series it is worth quickly (and this time I mean _really quickly_) reviewing how Zephyr's API function calls map to the function tables provided by the device drivers.

Let's first have a look at an overly simplified Devicetree driver function call tree for `gpio_pin_configure_dt`, which looks approximately as follows:

```
gpio_pin_configure_dt(
  │     spec, extra_flags)
  └── gpio_pin_configure(
        │     spec->port, spec->pin, spec->dt_flags | extra_flags)
        └── z_impl_gpio_pin_configure(
              │     spec->port, spec->pin, spec->dt_flags | extra_flags)
              └── spec->port->api->pin_configure(
                        spec->port, spec->pin, flags)
```

A call to `gpio_pin_configure_dt` thus maps to the function call `spec->port->api->pin_configure`. When we dissected the GPIO pin information type, we've already seen that `spec->port` is assigned the [device object `__device_dts_ord_<N>`](#macrobatics-resolving-device-objects-with-device_dt_get). Knowing already that our device object is created in `zephyr/drivers/gpio/gpio_nrfx.c`, we can immediately see that the API function table is the last parameter passed to the macro `DEVICE_DT_INST_DEFINE`:

`zephyr/drivers/gpio/gpio_nrfx.c`

```c
static const struct gpio_driver_api gpio_nrfx_drv_api_funcs = {
  .pin_configure = gpio_nrfx_pin_configure,
  // --snip--
};

// --snip--
#define GPIO_NRF_DEVICE(id)                 \
  /* --snip-- */                            \
  DEVICE_DT_INST_DEFINE(id, gpio_nrfx_init, \
      /* --snip-- */                        \
      &gpio_nrfx_drv_api_funcs);

DT_INST_FOREACH_STATUS_OKAY(GPIO_NRF_DEVICE)
```

That's it, as promised I was quick about that one. That's the magic behind the device driver abstractions in Zephyr. With that, you'll have an easy time diving into the [device driver model](https://docs.zephyrproject.org/latest/kernel/drivers/index.html) and [instance-based APIs](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-inst-apis).

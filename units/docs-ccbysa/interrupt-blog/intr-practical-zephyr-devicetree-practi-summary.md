---
id: "intr-practical-zephyr-devicetree-practi-summary"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting the GPIO pin information type / Summary"
summary: "Part of: Dissecting the GPIO pin information type"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#summary"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting the GPIO pin information type_

We now not only know how the GPIO subsystem uses the macros from `devicetree.h` to get the _specifiers_ for `gpio` properties of type `phandle-array`, but we also know what the device objects are and how they're resolved:

```c
static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED_NODE, gpios);
// =  {
//    .port = (&__device_dts_ord_11),
//    .pin = 13 /* DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_pin */,
//    .dt_flags = 1 /* DT_N_S_leds_S_led_0_P_gpios_IDX_0_VAL_flags */,
//  }
```

Zephyr's Devicetree generator provides much more than just macros for accessing property values in the Devicetree. It also creates the necessary macros to _associate_ driver instances with nodes, and to _create_ the corresponding instances in the device driver itself. And then some ...

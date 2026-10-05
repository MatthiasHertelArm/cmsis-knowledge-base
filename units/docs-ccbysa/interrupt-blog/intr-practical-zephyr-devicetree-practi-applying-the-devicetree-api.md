---
id: "intr-practical-zephyr-devicetree-practi-applying-the-devicetree-api"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting the GPIO pin information type / Applying the Devicetree API"
summary: "Part of: Dissecting the GPIO pin information type"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#applying-the-devicetree-api"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting the GPIO pin information type_

Let's ignore the `gpio_dt_spec` structure's contents for now. Instead, let's see how `GPIO_DT_SPEC_GET` is used to populate the structure and how it compares with what we've learned about the Devicetree API in the previous articles:

So far, we've only used the macros from the Devicetree API `zephyr/include/zephyr/devicetree.h`. Now we see how Zephyr's drivers create their own Devicetree macros on top of this basic API. We can find the macro declaration in Zephyr's `gpio.h` header file.

`zephyr/include/zephyr/drivers/gpio.h`

```c
#define GPIO_DT_SPEC_GET(node_id, prop) GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, 0)
// At some other location ...
#define GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, idx)                 \
  {                                                                 \
    .port = DEVICE_DT_GET(DT_GPIO_CTLR_BY_IDX(node_id, prop, idx)), \
    .pin = DT_GPIO_PIN_BY_IDX(node_id, prop, idx),                  \
    .dt_flags = DT_GPIO_FLAGS_BY_IDX(node_id, prop, idx),           \
  }
```

Similar to what we've seen for our own example in the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics), Zephyr uses Devicetree macros to create an initializer expression for the matching type that should be used with the corresponding macro. The macros `DT_GPIO_PIN_BY_IDX` and `DT_GPIO_FLAGS_BY_IDX` simply expand to the `DT_PHA_<x>` macros that we used when accessing `phandle-array`s:

```c
#define DT_GPIO_PIN_BY_IDX(node_id, gpio_pha, idx) \
  DT_PHA_BY_IDX(node_id, gpio_pha, idx, pin)
#define DT_GPIO_FLAGS_BY_IDX(node_id, gpio_pha, idx) \
  DT_PHA_BY_IDX_OR(node_id, gpio_pha, idx, flags, 0)
```

Ignoring the `.port` field (we'll get to that, don't worry), `GPIO_DT_SPEC_GET` expands to a very familiar format, where `.pin` and `.dt_flags` are initialized using the `pin` and `flags` _specifier cells_ from our Devicetree:

```c
#define GPIO_DT_SPEC_GET(node_id, prop)                              \
  {                                                                  \
    .port = DEVICE_DT_GET(/* --snip-- */),                           \
    .pin = DT_PHA_BY_IDX(node_id, prop, /*idx*/0, pin),              \
    .dt_flags = DT_PHA_BY_IDX_OR(node_id, prop, /*idx*/0, flags, 0), \
  }
```

> **Note:** The downside of using C macros is that, well, they're macros. Macros are expanded by the preprocessor, and the preprocessor doesn't care about types. It therefore also doesn't care if you use `GPIO_DT_SPEC_GET` as an initializer for an incompatible type. This _typically_ fails during compile time in case the assigned variable or constant doesn't have a compatible type.

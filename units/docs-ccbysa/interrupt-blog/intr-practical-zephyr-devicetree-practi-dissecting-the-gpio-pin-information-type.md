---
id: "intr-practical-zephyr-devicetree-practi-dissecting-the-gpio-pin-information-type"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting the GPIO pin information type"
summary: "Looking through the function prototypes of gpio_is_ready_dt, gpio_pin_configure_dt, and gpio_pin_toggle_dt, you'll notice that they take a \"GPIO specification\" const struct gpio_dt_spec spec as a parameter. We find the matching declaration in Zephyr's gpio.h:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#dissecting-the-gpio-pin-information-type"
license: "CC-BY-SA-4.0"
mode: "V"
---

Looking through the function prototypes of `gpio_is_ready_dt`, `gpio_pin_configure_dt`, and `gpio_pin_toggle_dt`,  you'll notice that they take a "_GPIO specification_" `const struct gpio_dt_spec *spec` as a parameter. We find the matching declaration in Zephyr's `gpio.h`:

`zephyr/include/zephyr/drivers/gpio.h`

```c
struct gpio_dt_spec {
  /** GPIO device controlling the pin */
  const struct device *port;
  /** The pin's number on the device */
  gpio_pin_t pin;
  /** The pin's configuration flags as specified in devicetree */
  gpio_dt_flags_t dt_flags;
};
```

> **Disclaimer:** This section is a nose dive deep into Zephyr's use of the generated Devicetree files. In case you don't want - or don't need - to know about the inner workings, I highly recommend sticking to [Zephyr's samples and demos](https://docs.zephyrproject.org/latest/samples/index.html) or the official documentation in general. Skip ahead to the [next section about the `status` property](#the-status-property) instead. In case I couldn't talk you out of it, hold on tight!

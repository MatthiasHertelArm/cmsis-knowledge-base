---
id: "intr-practical-zephyr-devicetree-practi-devicetree-with-gpio"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Devicetree with `gpio`"
summary: "Let's start with a classic: The blinking LED. The easiest way to control a low-power LED is using a GPIO, and one obvious way to approach this problem is to jump straight to the gpio API documentation."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#devicetree-with-gpio"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's start with a classic: The blinking LED. The easiest way to control a low-power LED is using a GPIO, and one obvious way to approach this problem is to jump straight to the [`gpio` API](https://docs.zephyrproject.org/latest/hardware/peripherals/gpio.html#gpio-api) documentation. In contrast to [Zephyr's OS service documentation](https://docs.zephyrproject.org/latest/services/index.html), however, the documentation for [peripherals](https://docs.zephyrproject.org/latest/hardware/peripherals/index.html) is typically restricted to the API, without further explaining the subsystem.

Instead, Zephyr's chosen approach is to provide a list of related **code samples** for each subsystem, showing the API in action. And Zephyr comes with _hundreds_ of [samples and demos](https://docs.zephyrproject.org/latest/samples/index.html)! In the list of related samples for the `gpio` subsystem, we also find the good old [blinky example](https://docs.zephyrproject.org/latest/samples/basic/blinky/README.html).

> **Note:** [Blinky](https://docs.zephyrproject.org/latest/samples/basic/blinky/README.html) is an example for a [Zephyr _repository_ application](https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-repo-app). We continue using a [_freestanding_ application](https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-freestanding-app), and in the next article, we'll finally create a [_workspace_ application](https://docs.zephyrproject.org/latest/develop/application/index.html#zephyr-workspace-app).

Straight from the documentation, we follow the _"Open in GitHub"_ link to find the application in Zephyr's repository and simply copy the contents from [`main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/basic/blinky/src/main.c) into our own application. We'll now compare the `gpio` Devicetree API with the "plain" API in `zephyr/include/zephyr/devicetree.h` that we've seen in the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics).


### Blinky with a `/chosen` LED node

The *Blinky* example chooses the LED Devicetree node using the _alias_ `led0`. Zephyr keeps its Devicetrees clean and we've seen that aliases, including `led0` are usually consistent throughout supported boards. Thus, if there's a board supported by Zephyr that has at least one light on it that works like LED, you can be sure that there's also a matching `led0` alias:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`

```dts
/ {
  leds {
    compatible = "gpio-leds";
    led0: led_0 {
      gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;
      label = "Green LED 0";
    };
  };
  aliases {
    led0 = &led0;
  };
};
```

Since we're practicing, however, we'll use a `/chosen` node called `app-led` instead. We add this node using a new board overlay file `boards/nrf52840dk_nrf52840.overlay` for the nRF52840 development kit:

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── boards
│   └── nrf52840dk_nrf52840.overlay
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

`boards/nrf52840dk_nrf52840.overlay`

```dts
/ {
    chosen {
        app-led = &led0;
    };
};
```

In the example application, we use `DT_CHOSEN(app_led)` instead of `DT_ALIAS(led0)`, but that's about the only change for the original *Blinky* sources that we need. Notice that again we specify the chosen node's name using its "lowercase-and-underscore" form `app_led` instead of the node's name `app-led` in the Devicetree. With a few minor adaptions, our application looks as follows:

```c
/** \file main.c */

#include <zephyr/drivers/gpio.h>
#include <zephyr/kernel.h>

#define SLEEP_TIME_MS 1000U
#define LED_NODE      DT_CHOSEN(app_led)

static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED_NODE, gpios);

int main(void)
{
    int err = 0;

    if (!gpio_is_ready_dt(&led)) { return -EIO; }

    err = gpio_pin_configure_dt(&led, GPIO_OUTPUT_ACTIVE);
    if (err < 0) { return -EIO; }

    while (1)
    {
        (void) gpio_pin_toggle_dt(&led);
        k_msleep(SLEEP_TIME_MS);
    }
}
```

Building and flashing the application we indeed end up with a blinking LED.

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build
$ west flash --build-dir ../build
```



I don't know about you, but even after all those years a blinking LED still puts a smile on my face.

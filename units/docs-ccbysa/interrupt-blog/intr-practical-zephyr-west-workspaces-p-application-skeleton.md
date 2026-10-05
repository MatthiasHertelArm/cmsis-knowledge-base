---
id: "intr-practical-zephyr-west-workspaces-p-application-skeleton"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Zephyr with West / Application skeleton"
summary: "Let's zoom through the usual warm-up to create our application. Go ahead and create the following file tree:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#application-skeleton"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr with West_

Let's zoom through the usual warm-up to create our application. Go ahead and create the following file tree:

```bash
$ tree --dirsfirst -a -L 3
.
└── app
    ├── boards
    │   └── nrf52840dk_nrf52840.overlay
    ├── src
    │   └── main.c
    ├── CMakeLists.txt
    └── prj.conf
```

As an application, we're using a modified version of the *Blinky* sample, where we select the LED node via a newly created `/chosen` node, and output "Tick" and "Tock" each time the LED is turned on or off:

`app/main.c`

```c
/** \file main.c */

#include <zephyr/drivers/gpio.h>
#include <zephyr/kernel.h>

#define SLEEP_TIME_MS 1000U
#define LED_NODE      DT_CHOSEN(app_led)

static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED_NODE, gpios);

int main(void)
{
    int err   = 0;
    bool tick = true;

    if (!gpio_is_ready_dt(&led))
    {
        printk("Error: LED pin is not available.\n");
        return -EIO;
    }

    err = gpio_pin_configure_dt(&led, GPIO_OUTPUT_ACTIVE);
    if (err != 0)
    {
        printk("Error %d: failed to configure LED pin.\n", err);
        return -EIO;
    }

    while (1)
    {
        (void) gpio_pin_toggle_dt(&led);
        k_msleep(SLEEP_TIME_MS);

        if (tick != false) { printk("Tick\n"); }
        else { printk("Tock\n"); }
        tick = !tick;
    }
}
```

I'll again build the application for my [nRF52840 Development Kit from Nordic](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk) and will only later switch to the [STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-f411re.html), so, for now, all I need is the matching `nrf52840dk_nrf52840.overlay` that specifies the chosen LED node:

`app/boards/nrf52840dk_nrf52840.overlay`

```dts
/ {
    chosen {
        app-led = &led0;
    };
};
```

The `prj.conf` remains empty, and the `CMakeLists.txt` only includes the same old boilerplate to create a Zephyr application with a single `main.c` source file:

`app/CMakeLists.txt`

```cmake
cmake_minimum_required(VERSION 3.20.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(
    EmptyApp
    VERSION 0.1
    DESCRIPTION "Modified Blinky application."
    LANGUAGES C
)

target_sources(
    app
    PRIVATE
    src/main.c
)
```

Trying to run `west build` shows us that we're not just missing the Zephyr source code, but we're also still lacking the Zephyr-specific [extension commands](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html), e.g., `build`:

```bash
workspace-m $ west build
usage: west [-h] [-z ZEPHYR_BASE] [-v] [-V] <command> ...
west: unknown command "build"; workspace /path/to/workspace-m does not define this extension command -- try "west help"
```

As we've seen in previous articles, e.g., `build` and `flash` are Zephyr-specific [extension commands](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html) that are not included by a plain _West_ installation. We'll resolve this in the following sections.

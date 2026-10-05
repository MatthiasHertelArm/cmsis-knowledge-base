---
id: "intr-practical-zephyr-devicetree-practi-warm-up"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Warm-up"
summary: "If you've been following along, you know the drill by now: Let's create a new freestanding application with the files listed below:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#warm-up"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you've been following along, you know the drill by now: Let's create a new freestanding application with the files listed below:

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

The `prj.conf` remains empty for now, and the `CMakeLists.txt` only includes the necessary boilerplate to create a Zephyr application with a single `main.c` source file. As an application, we have a `main` function that simply puts the MCU back to sleep at fixed intervals:

```c
#include <zephyr/kernel.h>
#define SLEEP_TIME_MS 100U

int main(void)
{
    printk("Message in a bottle.\n");
    while (1)
    {
        k_msleep(SLEEP_TIME_MS);
    }
}
```

As usual, I'll build the application for my [nRF52840 Development Kit from Nordic](https://www.nordicsemi.com/), but you can use any of [Zephyr's long list of supported boards](https://docs.zephyrproject.org/latest/boards/index.html) - or an emulation target.

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build
```

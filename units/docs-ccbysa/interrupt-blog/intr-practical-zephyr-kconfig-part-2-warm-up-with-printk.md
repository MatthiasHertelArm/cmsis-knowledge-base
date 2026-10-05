---
id: "intr-practical-zephyr-kconfig-part-2-warm-up-with-printk"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Warm up with `printk`"
summary: "Go ahead and create a new, empty freestanding application, e.g., using the application from the previous article."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#warm-up-with-printk"
license: "CC-BY-SA-4.0"
mode: "V"
---

Go ahead and create a new, empty freestanding application, e.g., using the application from the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_basics).

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

The simplest way to log text in Zephyr is the `printk` function. `printk` can take multiple arguments and format strings, but that's not what we want to show here, so we'll just modify the application's `main` function to output the string _"Message in a bottle."_ each time it is called - and thus after each reset:

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

But where does our output end up?

As mentioned in the previous article, we're using a development kit from [Nordic](https://www.nordicsemi.com/); in my case, the [development kit for the nRF52840](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk). For most development kits, the logging output is available via its UART interface and the following settings:

* Baud rate: _115200_ bits/s
* Data bits: _8_
* No parity, one stop bit

The connection settings for the UART interface are configured using [devicetree](https://docs.zephyrproject.org/latest/build/dts/index.html) - which we'll explore in a later article. Since these default settings are all we need for now, let's focus on Kconfig. We build and flash the project as follows:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build
$ west flash --build-dir ../build
```

When connecting the development kit to my computer, it shows up as TTY device `/dev/tty.usbmodem<some-serial-number>`. The format may vary depending on your development kit and operating system, e.g., on Windows, it'll show up as a `COM` port.

Open your serial monitor of choice, e.g., using the `screen` command, by launching [PuTTY](https://www.putty.org/) or - in case you're using _macOS_ - maybe you're also a fan of [Serial](https://www.decisivetactics.com/products/serial/), and reboot or reflash your device. You should see the following output each time your device starts:

```
$ screen /dev/tty.usbmodem<some-serial-number> 115200
*** Booting Zephyr OS build v3.3.99-ncs1 ***
Message in a bottle.

$ # use CTRL+A+k to quit the screen command.
```

Great! But what if we'd like to get rid of this feature entirely without changing our code? We all know that string processing is expensive and slow on an embedded system. Let's assume that in a production build, we want to get rid of any logging output to reduce our image size and speed up our application. How do we achieve this? This is where the [kernel configuration system _"Kconfig"_](https://docs.zephyrproject.org/latest/build/kconfig/index.html#configuration-system-kconfig) comes into play.

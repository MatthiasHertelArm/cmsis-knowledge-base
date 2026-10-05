---
id: "intr-practical-zephyr-devicetree-basics-devicetree-and-zephyr"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Devicetree and Zephyr"
summary: "We create a new freestanding application with the files listed below to get started. If you're not familiar with the required files, the installation, or the build process, have a look at the previous articles or the official documentation."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#devicetree-and-zephyr"
license: "CC-BY-SA-4.0"
mode: "V"
---

We create a new freestanding application with the files listed below to get started. If you're not familiar with the required files, the installation, or the build process, have a look at the previous articles or the official documentation. As mentioned in the [prerequisites](#prerequisites), you should be familiar with creating, building, and running a Zephr application.

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

The `prj.conf` can remain empty for now, and the `CMakeLists.txt` only includes the necessary boilerplate to create a Zephyr application with a single `main.c` source file. As an application, we'll use the same old `main` function that outputs the string _"Message in a bottle."_ each time it is called, and thus each time the device starts.

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

As usual, we can now build this application for the development kit of choice, in my case, the [nRF52840 Development Kit from Nordic](https://www.nordicsemi.com/).

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build
```

But wait, we didn't "do anything Devicetree" yet, did we? That's right, someone else already did it for us! After our first look into Zephyr and exploring Kconfig, we're familiar with the build output of our Zephyr application, so let's have a look! You should find a similar output right at the start of your build:

```
-- Found Dtc: /opt/nordic/ncs/toolchains/322ac893fe/bin/dtc (found suitable version "1.6.1", minimum required is "1.4.6")
-- Found BOARD.dts: /opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts
-- Generated zephyr.dts: /path/to/build/zephyr/zephyr.dts
-- Generated devicetree_generated.h: /path/to/build/zephyr/include/generated/devicetree_generated.h
-- Including generated dts.cmake file: /path/to/build/zephyr/dts.cmake
```

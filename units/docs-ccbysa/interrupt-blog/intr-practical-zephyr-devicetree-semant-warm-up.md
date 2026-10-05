---
id: "intr-practical-zephyr-devicetree-semant-warm-up"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Warm-up"
summary: "Before we get started, let's quickly review what we've seen when we had a look at the UART nodes of the nRF52840 Development Kit from Nordic."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#warm-up"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before we get started, let's quickly review what we've seen when we had a look at the UART nodes of the [nRF52840 Development Kit from Nordic](https://www.nordicsemi.com/). We're using the same old freestanding application with an empty `prj.conf` and the following file tree:

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

The `CMakeLists.txt` only includes the necessary boilerplate to create a freestanding Zephyr application. As an application, we'll again use the same old `main` function that outputs the string _"Message in a bottle."_ each time it is called, and thus each time the device starts.

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

The following command builds this application for the [nRF52840 Development Kit from Nordic](https://www.nordicsemi.com/) that we're using as a reference. As usual, you can follow along with any board (or emulation target) and you should see a similar output.

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build
```

Using the `--board` parameter, Zephyr selects the matching Devicetree source file `zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`, which specifies the properties `status` and `current-speed` for the node with the label `uart0`, as follows:

`zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`
```dts
&uart0 {
  compatible = "nordic,nrf-uarte";
  status = "okay";
  current-speed = <115200>;
  /* other properties */
};
```

Zephyr's DTS generator script produces the matching output in `devicetree_generated.h` for the specified properties:

`build/zephyr/include/generated/devicetree_generated.h`
```c
#define DT_N_S_soc_S_uart_40002000_P_current_speed 115200
#define DT_N_S_soc_S_uart_40002000_P_status "okay"
```

Can we get a similar output for Devicetree nodes that we define from scratch? In the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_dt), we've been using _overlay_ files to define custom nodes with their own properties to showcase Zephyr's Devicetree types. We'll see if we can get some output for the nodes and properties in these overlays, but before we go ahead and make blind use of _overlays_ yet again, let's finally have a look and learn how they work.

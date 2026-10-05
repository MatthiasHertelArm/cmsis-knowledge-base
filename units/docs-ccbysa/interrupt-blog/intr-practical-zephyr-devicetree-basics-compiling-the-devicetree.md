---
id: "intr-practical-zephyr-devicetree-basics-compiling-the-devicetree"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Devicetree and Zephyr / Compiling the Devicetree"
summary: "At the beginning of this article, we mentioned that Zephyr uses the dtc Devicetree compiler to generate the corresponding source code."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#compiling-the-devicetree"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Devicetree and Zephyr_

At the beginning of this article, we mentioned that Zephyr uses the `dtc` Devicetree compiler to generate the corresponding source code. That is, however, not entirely true: While the official Devicetree compiler `dtc` is definitely invoked during the build process, it is not used to generate any source code. Instead, Zephyr feeds the generated `build/zephyr/zephyr.dts.pre` into its own `GEN_DEFINES_SCRIPT` Python script, located at `zephyr/scripts/dts/gen_defines.py`.

Now, why would you want to do that? The Devicetree compiler `dtc` is typically used to compile Devicetree sources into a _binary_ format called the Devicetree blob `dtb`. The Linux kernel parses the DTB and uses the information to configure and initialize the hardware components described in the DTB. This allows the kernel to know how to communicate with the hardware without hardcoding this information in the kernel code. Thus, in Linux, the Devicetree is parsed and loaded during _runtime_ and thus can be _changed_ without modifying the application.

Zephyr, however, is designed to run on resource-constrained, embedded systems. It is simply not feasible to load a Devicetree blob during runtime: Any such structure would take up too many resources in both the Zephyr drivers and storing the Devicetree blob. Instead, the Devicetree is resolved during _compile time_.

> **Note:** In case this article is too slow for you but you still want to know more about Devicetree, there is a [brilliant video of the Zephyr Development Summit 2022 by Martí Bolívar on Devicetree](https://www.youtube.com/watch?v=w8GgP3h0M8M&list=PLzRQULb6-ipFDwFONbHu-Qb305hJR7ICe).

So, if not a binary, what's the output of this `gen_defines.py` generator? Let's have another peek at the output of our build process:

```
-- Generated zephyr.dts: /path/to/build/zephyr/zephyr.dts
-- Generated devicetree_generated.h: /path/to/build/zephyr/include/generated/devicetree_generated.h
-- Including generated dts.cmake file: /path/to/build/zephyr/dts.cmake
```

The build process creates three important output files: The `zephyr.dts` that has been generated out of the preprocessed `zephyr.dts.pre`, a `devicetree_generated.h` header file, and a CMake file `dts.cmake`.

As promised, the original Devicetree `dtc` compiler _is_ invoked during the build, and that's where it comes into play: The `zephyr.dts` Devicetree source file is fed into `dtc`, but not to generate any binaries or source code: Instead, it is only used to generate warnings and errors; the output itself is discarded. This helps to reduce the complexity of the Python Devicetree script `gen_defines.py` and ensures that the generated Devicetree source file used in Zephyr is at least still compatible with the original specification.

The `devicetree_generated.h` header file replaces the Devicetree blob `dtb`. It contains _macros_ for "all things Devicetree" and is included by the drivers and our application thereby strips all unnecessary or unused parts. **"Macrobatics"** is the term that Martí Bolívar used in his [talk about the Zephyr Devicetree at the June 2022 developer summit](https://www.youtube.com/watch?v=w8GgP3h0M8M&list=PLzRQULb6-ipFDwFONbHu-Qb305hJR7ICe), and it fits. Even for our tiny application, the generated header is over 15000 lines of code! In the next article, we'll see what these macros look like and how they are used with the Zephyr Devicetree API. If you're curious, have a look at `zephyr/include/zephyr/devicetree.h` already. In fact, let's have a glimpse:

`build/zephyr/include/generated/devicetree_generated.h`

```c
#define DT_CHOSEN_zephyr_console DT_N_S_soc_S_uart_40002000
// --snip---
#define DT_N_S_soc_S_uart_40002000_P_current_speed 115200
#define DT_N_S_soc_S_uart_40002000_P_status "okay"
```

Looks cryptic? With just a few hints, this becomes readable. Know that:
- `DT_` is just the common prefix for Devicetree macros,
- `_S_` is a forward slash `/`,
- `_N_` refers to a _node_,
- `_P_` is a _property_.

Thus, e.g., `DT_N_S_soc_S_uart_40002000_P_current_speed` simply refers to the _property_ `current_speed` of the _node_ `/soc/uart_40002000`. In Zephyr, this configuration value is set during _compile time_. You'll need to recompile your application in case you want to change this property. The approach in Linux would be different: There, the (UART speed) property is read from the Devicetree blob `dtb` during runtime. You could change the property, recompile the Devicetree, exchange the Devicetree blob, and wouldn't need to touch your application or the Kernel at all.

But let's leave it at that for now, we'll have a proper look at this later. For now, it is just important to know that we'll resolve our Devicetree at _compile time_ using lots of generated macros.

Finally, the generated `dts.cmake` is a file that basically allows to access the entire Devicetree from within CMake, using CMake target properties, e.g., we'll find the _current speed_ of our UART peripheral also within CMake:

`dts.cmake`

```cmake
set_target_properties(
    devicetree_target
    PROPERTIES
    "DT_PROP|/soc/uart@40002000|current-speed" "115200"
)
```

That's it for a peek into the Zephyr build. Let's wrap it up:
- Zephyr uses a so-called Devicetree to describe hardware.
- Most of the Devicetree sources are already available within Zephyr, e.g., MCUs and boards.
- We'll use Devicetree source files mostly to override or extend existing DTS files.
- In Zephyr, the Devicetree is resolved at _compile time_, using [macrobatics](https://www.youtube.com/watch?v=w8GgP3h0M8M&list=PLzRQULb6-ipFDwFONbHu-Qb305hJR7ICe).

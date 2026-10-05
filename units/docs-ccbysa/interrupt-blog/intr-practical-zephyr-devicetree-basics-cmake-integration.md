---
id: "intr-practical-zephyr-devicetree-basics-cmake-integration"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Devicetree and Zephyr / CMake integration"
summary: "The build output shows us that Devicetree - just like Kconfig - is a central part of any application build. It is added to your build via the CMake module zephyr/cmake/modules/dts.cmake."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#cmake-integration"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Devicetree and Zephyr_

The build output shows us that Devicetree - just like Kconfig - is a central part of any application build. It is added to your build via the CMake module `zephyr/cmake/modules/dts.cmake`. The first thing that Zephyr is looking for, is the _Devicetree compiler_ `dtc` (see, `zephyr/cmake/modules/FindDtc.cmake`). Typically, this tool is in your `$PATH` after installing Zephyr or loading your Zephyr environment:

```bash
$ where dtc
/opt/nordic/ncs/toolchains/322ac893fe/bin/dtc
```

Since we didn't specify any so-called _Devicetree overlay file_ (bear with me for now, we'll see how to modify our Devicetree using _overlay_ files in a later section), Zephyr then looks for a Devicetree source file that matches the specified _board_. In my case, that's the nRF52840 development kit, which is supported in the current Zephyr version: The board and thus its Devicetree is fully described by the file `zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`.

> **Note:** If you're using a custom board not supported by Zephyr, you'd have to provide your own DTS file for it. We won't go into details about adding support for a custom board in this article (and maybe the next one), but at the end of it, you should have all the knowledge to do that - or to understand any other article showing you how to do it.

Let's not dive into the file's contents for now; instead, look at the build. Somehow, the build ends up with a generated `zephyr.dts` file. A couple of interesting things are happening in this process that are worth mentioning, so we'll have a closer look.

> **Note:** In this section, we're really just brushing over the files to get a bit of a feeling for the syntax and how nodes are used. We'll cover all of this in great detail still!

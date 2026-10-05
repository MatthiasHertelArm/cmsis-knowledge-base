---
id: "intr-practical-zephyr-kconfig-part-2-kconfig-search"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Navigating Kconfig / Kconfig search"
summary: "In case you don't like menuconfig or guiconfig, or just want to browse available configuration options, Zephyr's documentation also includes a dedicated Kconfig search. E.g., when searching for our PRINTK configuration we'll be presented with the following output:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#kconfig-search"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Navigating Kconfig_

In case you don't like `menuconfig` or `guiconfig`, or just want to browse available configuration options, Zephyr's documentation also includes a dedicated [Kconfig search](https://docs.zephyrproject.org/latest/kconfig.html). E.g., when [searching for our `PRINTK` configuration](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRINTK) we'll be presented with the following output:



While this search does point out that there is a dependency on the `BOOT_BANNER` symbol, it cannot know our current configuration and therefore can't tell us that disabling `PRINTK` won't have any effect since `BOOT_BANNER` is also still enabled by default.

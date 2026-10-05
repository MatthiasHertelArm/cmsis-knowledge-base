---
id: "intr-practical-zephyr-kconfig-part-2-navigating-kconfig"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Navigating Kconfig"
summary: "As mentioned before, Kconfig uses an entire hierarchy of Kconfig files. The initial configuration is merged from several Kconfig files, including the Kconfig file of the specified board."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#navigating-kconfig"
license: "CC-BY-SA-4.0"
mode: "V"
---

As mentioned before, _Kconfig_ uses an entire _hierarchy_ of `Kconfig` files. The initial configuration is merged from several `Kconfig` files, including the `Kconfig` file of the specified board. The exact procedure used by Zephyr for merging the configuration file is explained in great detail in a [dedicated section of the official documentation](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#the-initial-configuration) but is not worth repeating here.

> **Notice:** The command line output of `west build` also shows the order in which _Kconfig_ merges the configuration files. We'll see this in the section about [build types and alternative Kconfig files](#build-types-and-alternative-kconfig-files).

When debugging _Kconfig_ settings, it can be helpful to have a look at the generated output. All _Kconfig_ symbols are merged into a single `zephyr/.config` file located in the build directory, in our case, `build/zephyr/.config`. There, we find the following setting:

`build/zephyr/.config`

```conf
#
# Debugging Options
#
# CONFIG_DEBUG is not set
# CONFIG_STACK_USAGE is not set
# CONFIG_STACK_SENTINEL is not set
CONFIG_PRINTK=y
```

It seems that our `CONFIG_PRINTK` setting was not accepted. Why?

The reason is that `Kconfig` files can have _dependencies_: Enabling one option can automatically also enable other options. Sadly, at the time of writing, _Kconfig_ does not seem to warn about conflicting values for symbols, e.g., from the application configuration file: It'd be great if Kconfig would tell me that some other option overwrites my `CONFIG_PRINTK=n` setting and has no effect!

Zephyr contains _hundreds_ of so-called Kconfig _fragments_. It is therefore almost impossible to navigate these files without tool support. Thankfully, _West_ integrates two graphical tools to explore available _Kconfig_ options and their current setting: `menuconfig` and `guiconfig`.

---
id: "intr-practical-zephyr-kconfig-part-2-using-different-configuration-files"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Using different configuration files"
summary: "Until now, we've only used the application configuration file prj.conf for setting Kconfig symbols. In addition to this configuration file, Zephyr's build system automatically picks up additional Kconfig fragments, if provided, and also allows explicitly specifying additional or alternative fragments."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#using-different-configuration-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

Until now, we've only used the _application configuration file_ [prj.conf](https://github.com/lmapii/practical-zephyr/blob/main/00_basics/prj.conf) for setting _Kconfig_ symbols. In addition to this configuration file, Zephyr's build system automatically picks up additional _Kconfig_ _fragments_, if provided, and also allows explicitly specifying additional or alternative fragments.

We'll quickly glance through the most common practices here.

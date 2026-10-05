---
id: "intr-practical-zephyr-zephyr-basics-par-series-outline"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Series outline"
summary: "As mentioned, this series covers \"Zephyr's basics\", so what is it that we'll explore in detail?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#series-outline"
license: "CC-BY-SA-4.0"
mode: "V"
---

As mentioned, this series covers "_Zephyr's basics_", so what is it that we'll explore in detail?

__Setup__

First, we walk through the basics of installing Zephyr and creating a minimal skeleton application. We'll see how to compile, flash, and debug an application skeleton and how Zephyr's _West_ tool fits into this. We'll improve this setup in a later article, leveraging the true potential of _West_.

__Kconfig__

In our skeleton application, we'll already stumble upon the configuration tool [Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html). We'll now see how it works and how to explore, modify, and persist so-called _Kconfig symbols_, and will create our application-specific symbol. Since _Kconfig_ is also used to configure build settings, we'll see how to use _Kconfig_ for specifying _build types_.

__Devicetree basics__

Zephyr uses a tree data structure called _devicetree_ to describe hardware: All supported microcontrollers and boards are represented by a set of _devicetree sources_, which use their syntax. First, we'll skim through some device tree files in Zephyr and then create our files to explore the devicetree _syntax_.

__Devicetree bindings__

After understanding the _devicetree_ syntax, we'll now use so-called _bindings_ to add _semantics_ and, therefore _meaning_ to our devicetree. Only via devicetree _bindings_, Zephyr knows how to translate the provided devicetree into source code. Creating bindings for our nodes, we'll look at the generated output, and finally how we can access it via the Zephyr devicetree API.

__Workspaces__

Throughout this article series, for the sake of simplicity, we'll mostly use so-called _freestanding_ applications. Such applications require Zephyr's sources to be installed outside of your application. For professional applications, Zephyr's _West_ tool supports so-called _workspaces_: In workspaces, _all_ sources, their location, and their versions are specified in a _manifest_ file that is used by _West_ to populate the workspace, eliminating references to files outside of the workspace. We'll see how to create a _minimal_ workspace application using _West_.

This is where the journey **ends**. After this series, you should find it easy - or at least easier - to explore, understand, and apply advanced concepts such as:

- [application version management](https://docs.zephyrproject.org/latest/build/version/index.html)
- using the actual [Zephyr operating system and its communication primitives](https://docs.zephyrproject.org/latest/services/index.html),
- creating custom [device drivers](https://docs.zephyrproject.org/latest/kernel/drivers/index.html) or integrating a [custom board](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html),
- using integrated bootloaders such as [Mcuboot](https://docs.zephyrproject.org/latest/services/device_mgmt/dfu.html#mcuboot),
- [testing Zephyr](https://docs.zephyrproject.org/latest/develop/test/index.html) applications, e.g., using its [Twister](https://docs.zephyrproject.org/latest/develop/test/twister.html) test runner,
- running [static code analysis](https://docs.zephyrproject.org/latest/develop/sca/index.html) with the integrated [code checker](https://docs.zephyrproject.org/latest/develop/sca/codechecker.html),
- and many more ...

... but we won't cover any of the above. All example code used throughout the articles is available in the [_practical-zephyr_ GitHub repository](https://github.com/lmapii/practical-zephyr).

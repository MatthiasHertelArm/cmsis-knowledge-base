---
id: "intr-practical-zephyr-zephyr-basics-par-installation"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Installation"
summary: "Let's get started - with a shortcut. Installation and toolchain management is - and probably always will be - a very biased topic. This article series is about something other than solving that problem."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's get started - with a shortcut. Installation and toolchain management is - and probably always will be - a very biased topic. This article series is about something other than solving that problem. Therefore, I'm deliberately choosing a shortcut: We'll download "all things Zephyr" using Nordic's [`nrfutil`](https://docs.nordicsemi.com/bundle/nrfutil/page/README.html) command line tool instead of following the complete installation procedure. This is optional but convenient.

> **Note:** Those of you who are coming back to this series might notice that I'm no longer referring to Nordic's [toolchain manager](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/installation/assistant.html#install-toolchain-manager). The toolchain manager is deprecated and is replaced by `nrfutil`. Also, Zephyr's _West_ tool got a brand new `sdk-install` extension command to install the Zephyr SDK toolchain. This extension command, however, is not available in Nordic's _nRF Connect SDK_. Refer to [Zephyr's Getting Started][[zephyr-getting-started](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)] guide for details.

Instead of using Nordic's full-blown IDE solution, we'll create a shell script to set up our terminal. This demonstrates some of the environment variables used by Zephyr and allows you to use a plain terminal to follow along.

> **Note:** In case you want a "Zephyr only" installation without downloading Nordic's software, feel free to follow the installation procedure in the [official documentation](https://docs.zephyrproject.org/latest/develop/getting_started/index.html) - and I'll meet you again in the [next section](#creating-an-empty-application-skeleton)!

As mentioned in the introduction, later in this series, we'll see a much better approach where Zephyr's sources will be pulled into our _workspace_ rather than separately installed: The only thing you'll need are the host tools documented in Zephyr's [getting started guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-dependencies). For now, I'm using Nordic's toolchain installer simply to have a running setup that we can use to explore Zephyr's sources and tools.

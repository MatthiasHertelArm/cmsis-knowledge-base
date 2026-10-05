---
id: "intr-practical-zephyr-west-workspaces-p-zephyr-with-west"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Zephyr with West"
summary: "Having covered the West basics, let's get back to creating Zephyr applications and put this knowledge into practice."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#zephyr-with-west"
license: "CC-BY-SA-4.0"
mode: "V"
---

Having covered the _West_ basics, let's get back to creating _Zephyr_ applications and put this knowledge into practice.

In this section, we recreate the modified **Blinky** application that we've seen in the previous article, where we failed to compile the application for the [STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-f411re.html) since we relied upon the sources from a globally installed [nRF Connect SDK](https://www.nordicsemi.com/Products/Development-software/nrf-connect-sdk) - which doesn't include [STM32 HAL](https://github.com/zephyrproject-rtos/hal_stm32).

> **Note:** You can find the complete _manifest repositories_ on GitHub: [practical-zephyr-manifest-repository](https://github.com/lmapii/practical-zephyr-manifest-repository).

---
id: "intr-practical-zephyr-zephyr-basics-par-setup-using-nordic-s-nrfutil"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Installation / Setup using Nordic's `nrfutil`"
summary: "Nordic provides the nRF Connect SDK for its microcontrollers. This SDK is based on Zephyr and, therefore, its version of it (plus some vendor-specific extras)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#setup-using-nordic-s-nrfutil"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Installation_

Nordic provides the [nRF Connect SDK](https://www.nordicsemi.com/Products/Development-software/nrf-connect-sdk) for its microcontrollers. This SDK is based on Zephyr and, therefore, its version of it (plus some vendor-specific extras). Still, instead of having to go through all the installation steps of the [getting started guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html), it comes with its own very handy command line tool [`nrfutil`](https://docs.nordicsemi.com/bundle/nrfutil/page/README.html) to manage different versions of the SDK and thus also Zephyr. We'll also use it as a reference when checking the necessary steps to set up a Zephyr environment.

The nRF Connect SDK also comes with a [`VS Code` extension pack](https://nrfconnect.github.io/vscode-nrf-connect/): We'll see several of the extensions throughout this series but won't use the fully integrated solution since we want to understand what's going on underneath the hood. Go ahead and:

- Follow [`nrfutil`'s instructions](https://docs.nordicsemi.com/bundle/nrfutil/page/guides/installing.html) to install the current toolchain,
- _[optional]_ install the [nRF Kconfig extension for `VS Code`](https://marketplace.visualstudio.com/items?itemName=nordic-semiconductor.nrf-kconfig),
- _[optional]_ install the [nRF DeviceTree extension for `VS Code`](https://marketplace.visualstudio.com/items?itemName=nordic-semiconductor.nrf-kconfig).

> **Note:** If you like Nordic's [nRF Connect for `VS Code` extension pack](https://nrfconnect.github.io/vscode-nrf-connect/), you can now also skip the _nrfutil_ installation step and install the toolchain straight from within `VS Code`.

If you're not convinced and want to install the SDK manually, you can also have a look at the steps performed in the [Dockerfile](https://github.com/lmapii/practical-zephyr/blob/main/builder.Dockerfile) in the [accompanying GitHub repository](https://github.com/lmapii/practical-zephyr). Notice that this _Dockerfile_ is tailored to the needs of this article series and is _not_ a generic solution. If you want something more generic, look at [Zephyr's docker-image repository](https://github.com/zephyrproject-rtos/docker-image).

---
id: "intr-practical-zephyr-kconfig-part-2-nordic-s-kconfig-extension-for-vs-code"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Navigating Kconfig / Nordic's Kconfig extension for VS Code"
summary: "Another graphical user interface for Kconfig is the nRF Kconfig extension for VS Code."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#nordic-s-kconfig-extension-for-vs-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Navigating Kconfig_

Another graphical user interface for _Kconfig_ is the [nRF Kconfig](https://marketplace.visualstudio.com/items?itemName=nordic-semiconductor.nrf-kconfig) extension for VS Code. This is an extension tailored for use with the [nRF Connect SDK](https://www.nordicsemi.com/Products/Development-software/nrf-connect-sdk) and with Nordic's [complete VS Code extension pack](https://nrfconnect.github.io/vscode-nrf-connect/), but to some extent, this extension can also be used for a generic Zephyr project and might therefore also be useful if you're not developing for a target from [Nordic](https://www.nordicsemi.com/):



At the time of writing and for this repository, the following configuration options were necessary to use the extension in a workspace that does not rely on the entire extension set:

```json
{
  "nrf-connect.toolchain.path": "${nrf-connect.toolchain:3.2.1}",
  "nrf-connect.topdir": "${nrf-connect.sdk:3.2.1}",
  "kconfig.zephyr.base": "${nrf-connect.sdk:3.2.1}",
  "nrf-connect.applications": ["${workspaceFolder}/path/to/app"]
}
```

> **Note:** Let's hope that the good people at Nordic find the time to change this extension so that it is easily usable for any Zephyr project!

However, as visible in the above screenshot, at the time of writing the extension fails to inform the user about the dependency to `BOOT_BANNER`, and in contrast to `menuconfig` and `guiconfig` it is therefore not visible why the configuration option cannot be disabled. Aside from that, this extension has two major benefits:

* The _Save minimal config_ option seems to recognize options coming from a `_defconfig` file and therefore really only exports the configuration options set within the extension.
* The extension adds auto-completion to your `.conf` files.

With this last tool to explore _Kconfig_, let's have a look at a couple of more options.

---
id: "intr-practical-zephyr-kconfig-part-2-kconfig-hardening"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Kconfig hardening"
summary: "Another tool worth mentioning when talking about Kconfig is the hardening tool. Just like menuconfig and guiconfig, this tool is a target for west build. It is executed using the -t hardenconfig target in the call to west build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#kconfig-hardening"
license: "CC-BY-SA-4.0"
mode: "V"
---

Another tool worth mentioning when talking about _Kconfig_ is the [hardening tool](https://docs.zephyrproject.org/latest/security/hardening-tool.html). Just like `menuconfig` and `guiconfig`, this tool is a target for `west build`. It is executed using the `-t hardenconfig` target in the call to `west build`. The hardening tool checks the _Kconfig_ symbols against a set of known configuration options that should be used for a secure Zephyr application. It then lists all differences found in the application.

We can use this tool to check our normal and _release_ configurations:

```bash
$ # test normal build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 \
  -d ../build \
  --pristine \
  -t hardenconfig

$ # test release build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 \
  -d ../build \
  --pristine \
  -t hardenconfig \
  -- -DCONF_FILE=prj_release.conf
```

For the normal build using `prj.conf`, the hardening tool displays a table of all symbols whose current values do not match the recommended, secure configuration value. E.g., at the time of writing, this is the output for the normal build in my demo application:

```
-- west build: running target hardenconfig
[0/1] cd /path/to/zephyr/kconfig/hardenconfig.py /opt/nordic/ncs/v3.2.1/zephyr/Kconfig
                 name                 | current | recommended || check result
==============================================================================
CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT |    n    |      y      ||     FAIL
CONFIG_USE_SEGGER_RTT                 |    y    |      n      ||     FAIL
CONFIG_BUILD_OUTPUT_STRIPPED          |    n    |      y      ||     FAIL
CONFIG_FAULT_DUMP                     |    2    |      0      ||     FAIL
CONFIG_STACK_SENTINEL                 |    n    |      y      ||     FAIL
```

The symbols in `prj_release.conf` have been chosen such that at the time of writing all hardening options are fulfilled and the above table is empty.

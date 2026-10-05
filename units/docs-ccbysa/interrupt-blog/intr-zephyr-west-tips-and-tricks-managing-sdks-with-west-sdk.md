---
id: "intr-zephyr-west-tips-and-tricks-managing-sdks-with-west-sdk"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: Managing SDKs with `west sdk`"
summary: "West has a built-in command for managing Zephyr SDKs:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#managing-sdks-with-west-sdk"
license: "CC-BY-SA-4.0"
mode: "V"
---

West has a built-in command for managing Zephyr SDKs:

```bash
# install a specific SDK version and target toolchain
west sdk install --version 0.17.4 -t arm-zephyr-eabi
```

You can install just the toolchain(s) you actually need, rather than pulling
down the full SDK bundle. Some other useful targets:

- `riscv64-zephyr-elf`
- `xtensa-espressif_esp32_zephyr-elf`

Run `west sdk list` to see what's available, and `west sdk install --help` for
the full set of options.

What's awesome is if you run this from a west workspace containing a `zephyr`
project, `west sdk install` will match the `zephyr/SDK_VERSION` value, so you'll
get a matching SDK version, ezpz!

```plaintext
  --version [SDK_VER]   version of the Zephyr SDK to install. If not specified,
                        the install version is detected from
                        ${ZEPHYR_BASE}/SDK_VERSION file.
```

This is covered in more depth in [Practical Zephyr - West workspaces (Part
6)](https://interrupt.memfault.com/blog/practical_zephyr_west), definitely worth a read if
you haven't already.

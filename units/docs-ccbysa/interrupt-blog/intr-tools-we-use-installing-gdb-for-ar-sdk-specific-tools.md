---
id: "intr-tools-we-use-installing-gdb-for-ar-sdk-specific-tools"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / SDK-specific tools"
summary: "SDK Vendors (and IDE vendors too!) will often package copies of GDB, along with other toolchain components, to make it easy to get started with their platform."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#sdk-specific-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

SDK Vendors (and IDE vendors too!) will often package copies of GDB, along with
other toolchain components, to make it easy to get started with their platform.

For example, Zephyr RTOS provides pre-built toolchains, that include the
appropriate GDB versions:

- <https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.14.2>

ESP-IDF from Espressif provides similar tool packages:

- <https://github.com/espressif/binutils-gdb/releases/esp-gdb-v11.2_20220715>

Advantages:

- these packages are often well-tested by the vendors, and you may even be able
  to get support if you encounter issues!
- generally support all Linux/Mac/Windows these days

Disadvantages:

- often these packages are very tailored to the particular environment (which
  usually is just fine), including custom patches for example
- Python support can be pretty variable- some packages won't have Python support
  at all, or it will only be for a specific version.
- external dependencies may not be provided (eg libpython), and you'll have to
  bring your own
- can be based on pretty old GDB/binutils releases, so there might be
  long-resolved bugs present, or missing newer optimizations + features

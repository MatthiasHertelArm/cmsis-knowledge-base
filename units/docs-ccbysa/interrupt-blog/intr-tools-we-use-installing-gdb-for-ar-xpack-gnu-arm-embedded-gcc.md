---
id: "intr-tools-we-use-installing-gdb-for-ar-xpack-gnu-arm-embedded-gcc"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / xPack GNU Arm Embedded GCC"
summary: "The xPack Project provides a prebuilt gcc-arm toolchain:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#xpack-gnu-arm-embedded-gcc"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

The [xPack Project](https://xpack.github.io/) provides a prebuilt gcc-arm
toolchain:

- <https://github.com/xpack-dev-tools/arm-none-eabi-gcc-xpack/releases/>

They tend to be pretty up-to-date, and more reliably include Python support.

There's also build documentation, if you'd like to tweak the package:

- <https://github.com/xpack-dev-tools/arm-none-eabi-gcc-xpack/blob/xpack/README-BUILD.md>

Overall pretty simple and easy to use, and make a very good alternative to the
official ARM GCC toolchains! I've used it as a drop-in replacement for the ARM
GCC toolchains, and it's working very well.

Advantages:

- wider host support (`darwin-arm64`) than the official releases
- more consistent Python support across host platform versions
- documented + reproducible build instructions

Disadvantages:

- only a single Python version supported per release
- similarly non-customizable as the official ARM GCC packages. _you get what you
  get and you don't get upset!_

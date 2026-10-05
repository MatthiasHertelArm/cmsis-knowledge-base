---
id: "intr-practical-zephyr-zephyr-basics-par-prerequisites"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Prerequisites"
summary: "You should be familiar with embedded software since we won't cover the basics. Some knowledge in using build systems such CMake doesn't hurt but is not required."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

You should be familiar with embedded software since we won't cover the basics. Some knowledge in using build systems such _CMake_ doesn't hurt but is not required. If you don't know what Zephyr is, look briefly at the [introduction in the official documentation](https://docs.zephyrproject.org/latest/introduction/index.html).

The practical examples in this series use [Nordic's](https://www.nordicsemi.com/) [nRF52840 development kit](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk). If you don't have such a board, don't worry. You should be able to follow along using most of the boards in [Zephyr's long list of supported boards](https://docs.zephyrproject.org/latest/boards/index.html) - or using an emulation target. However, we won't cover using emulation targets in this article series. Most of the content of this series does not require any hardware; we'll just _compile_ the project for a specific board for simplicity.

Whenever relevant, we'll use [Visual Studio Code](https://code.visualstudio.com/) as the editor of choice. However, **using `VS Code` is, of course, entirely optional** and not required at all. Only in certain sections, e.g., debugging, we'll show how using `VS Code` and some plugins can make your life easier - and we won't cover any other editor.

We won't assume any operating system, but - for the sake of simplicity - we'll be exclusively using _Linux_ shell commands. Windows users should have a "`bash`-compatible" environment - or _WSL_ - installed. We won't jump through the hoops of creating Windows-compatible shell scripts, batch files, or other atrocities.

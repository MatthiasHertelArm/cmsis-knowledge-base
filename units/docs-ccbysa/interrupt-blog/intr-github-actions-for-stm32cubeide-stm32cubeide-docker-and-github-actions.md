---
id: "intr-github-actions-for-stm32cubeide-stm32cubeide-docker-and-github-actions"
type: "concept"
domain: "debug"
title: "GitHub Actions for STM32CubeIDE: STM32CubeIDE, Docker, and GitHub Actions"
summary: "(figure: Picture of GitHub Actions calling STM32CubeIDE in a Docker container)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-01-github-actions-for-stm32cubeide.md"
doc_source: "https://interrupt.memfault.com/blog/github-actions-for-stm32cubeide#stm32cubeide-docker-and-github-actions"
license: "CC-BY-SA-4.0"
mode: "V"
---

(figure: Picture of GitHub Actions calling STM32CubeIDE in a Docker container)

The STM32 series of microcontrollers from STMicroelectronics are very popular in
the embedded industry. ST provides an in-house Eclipse-based IDE,
[STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html), for
developing projects using these chips.

The STM32CubeIDE provides an all-in-one starting point for STM32-based projects,
with example code, drivers, and middleware, and tools for configuring
peripherals and generating code.

This IDE comes with both the graphical frontend (using Eclipse) and the
necessary tools for building, flashing, and debugging STM32 projects (it bundles
a pretty standard GCC ARM toolchain and the ST-Link tools for flashing and
debugging).

Typically, developers install the STM32CubeIDE on their local machines and build
projects using the GUI, but that manual and UI-based workflow doesn't fit well
with modern CI systems- we want to build our projects automatically, without
clicking through a UI, and in a reproducible way.

To accomplish this, we'll use Docker to create a containerized environment with
STM32CubeIDE and its dependencies, and GitHub Actions to automate the build
process!

---
id: "alp-zephyr-vsworkbench-1-installation-set-up-the-workbench-for-zephy"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Set up the Workbench for Zephyr development environment: Set up the Workbench for Zephyr development"
summary: "Getting started with Zephyr RTOS development can be challenging. You often need to install SDKs, set up toolchains, and organize workspace directories by hand."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation/#set-up-the-workbench-for-zephyr-development-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Getting started with [Zephyr](https://zephyrproject.org/) RTOS development can be challenging. You often need to install SDKs, set up toolchains, and organize workspace directories by hand. 

[Workbench for Zephyr](https://z-workbench.com/) is an open-source [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=Ac6.zephyr-workbench) that transforms Zephyr RTOS development into a streamlined IDE experience. Created by [Ac6](https://www.ac6.fr/en/), it automates toolchain setup, project management, and debugging, making Zephyr projects faster to start and easier to scale.

In this Learning Path, you'll set up Workbench for Zephyr and configure a complete development environment on your computer. By the end, you can create, build, and debug applications for Arm Cortex-M boards using Zephyr RTOS.

Workbench for Zephyr makes it easy to set up your development environment with a single click. It automatically installs all the tools you need, such as Python, CMake, Ninja, and Git. You can import and manage different versions of the Zephyr SDK, choose the right architecture, and quickly initialize West workspaces. The extension lets you create board-specific applications from sample projects, build and flash them to your hardware, and debug your code, all within Visual Studio Code. You also get features like breakpoint debugging and memory usage insights when using a supported hardware probe.

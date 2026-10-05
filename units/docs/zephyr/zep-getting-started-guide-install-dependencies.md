---
id: "zep-getting-started-guide-install-dependencies"
type: "concept"
domain: "project"
title: "Getting Started Guide: Install dependencies"
summary: "Next, install the host tools Zephyr needs to configure and build applications. The instructions below use the recommended package manager for each operating system so the tools are available from your terminal."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/getting_started/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/getting_started/index.rst"
license: "Apache-2.0"
mode: "V"
---

Next, install the host tools Zephyr needs to configure and build applications.
The instructions below use the recommended package manager for each operating
system so the tools are available from your terminal.

The current minimum required versions for the main dependencies are:


* - Tool
  - Min. Version

* - [CMake](https://cmake.org/)
  - 3.28.0

* - [Python](https://www.python.org/)
  - 3.12

* - [Devicetree compiler](https://www.devicetree.org/)
  - 1.4.6

**Note:** Python 3.12 is strongly recommended. Using a newer Python release may fail on some systems, for example when installing the required packages on Windows.

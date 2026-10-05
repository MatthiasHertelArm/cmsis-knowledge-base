---
id: "intr-how-to-build-drivers-for-zephyr-example-walkthrough"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Example Walkthrough"
summary: "In this example, you'll learn about what it takes to create a driver for the PCF85063A real-time clock and counter. I've chosen to use the counter API for reasons we'll discuss in a bit."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#example-walkthrough"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this example, you'll learn about what it takes to create a driver for the PCF85063A real-time clock and counter. I've chosen to use the counter API for reasons we'll discuss in a bit. There are some prerequisites to getting started though. Let's begin with SDK Setup.

### SDK Setup

I'll be referencing Nordic's nRF Connect SDK a bunch throughout this post. I've been building and testing nRF9160 Feather on v1.3.0. I won't be going into detail on how to set up the SDK though. Nordic has [great documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/getting_started.html) you can check out to get started. I've also discussed [my experience here](https://www.jaredwolff.com/zephyr-on-nrf9160-feather/).

### What `west` can do for you

The Zephyr project uses a CLI tool, `west`, for project management, compilation, and flashing. `west` replaces the idea of a top-level Makefile and project dependency management like Git submodules. For the most part, it accomplishes that goal well.

You’ll need to install `west` if you haven't already. Follow the SDK setup links above for more information.

**Building**

To build a project, navigate to the directory for the application in question and run `west build`. For example:

```terminal
$ cd ncs/nrf/samples/nrf9160/nrf_cloud_agps
$ west build -b circuitdojo_feather_nrf9160ns -p
```

This builds in the current folder for the `circuitdojo_feather_nrf9160ns` board. You can find all the possible `arm` based boards in `ncs/zephyr/boards/arm/` The `-p` flag tells `west` to clean before building.

A ton of things happen in the background to build a project. We'll discuss more how things compile in the next section.

**Flashing**

Flashing code is as simple as running `west flash` from your project directory. You can use the `-r` parameter to choose which programming method you'd like to use. Common options are `jlink`, `nrfjprog` (for Nordic projects), `pyocd`, `openocd`, `dfu-util`, etc.

These "runners" are set in the board configuration. Here's the `board.cmake` for the nRF9160 Feather located in `zephyr/boards/arm/circuitdojo_feather_nrf9160/board.cmake`:

```cmake
board_runner_args(nrfjprog "--nrf-family=NRF91")
board_runner_args(jlink "--device=cortex-m33" "--speed=4000")
include(${ZEPHYR_BASE}/boards/common/nrfjprog.board.cmake)
include(${ZEPHYR_BASE}/boards/common/jlink.board.cmake)
```

([Original Github code here](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/arm/circuitdojo_feather_nrf9160/board.cmake))

As you can see, the nRF9160 Feather supports the `nrfjprog` and `jlink` options.

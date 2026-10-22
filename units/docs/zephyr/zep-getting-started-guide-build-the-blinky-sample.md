---
id: "zep-getting-started-guide-build-the-blinky-sample"
type: "concept"
domain: "project"
title: "Getting Started Guide: Build the Blinky Sample"
summary: "Build the blinky with west build. Replace <your-board-name> with the name of your board:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/getting_started/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/getting_started/index.rst"
license: "Apache-2.0"
mode: "V"
---

**Note:** does not meet Blinky's blinky-sample-requirements, then If you are unsure what name west uses for your board, use `west boards` to list all boards Zephyr supports. Your board's `documentation page` also shows the exact board target name to pass to `west build`.

Build the blinky with west build.
Replace `<your-board-name>` with the name of your board:

The `-p always` option forces a pristine build, which removes build output
from any previous configuration. This avoids stale files when you are getting
started. Later, you can use `-p auto` to let `west build` heuristics decide
when a pristine build may be needed. See `west build -h` for details.


**Note:** A board may contain one or multiple SoCs and each SoC may contain one or more CPU clusters. When building for such boards, specify the SoC or CPU cluster for which the sample must be built. For example to build blinky for the `cpuapp` core on the nrf5340dk the board must be provided as: `nrf5340dk/nrf5340/cpuapp`. See also board_terminology for more details.

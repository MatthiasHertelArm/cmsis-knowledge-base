---
id: "zep-devicetree-howtos-applications-that-depend-on-board-specif"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Applications that depend on board-specific devices"
summary: "One way to allow application code to run unmodified on multiple boards is by supporting a devicetree alias to specify the hardware specific portions, as is done in the blinky sample."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

One way to allow application code to run unmodified on multiple boards is by
supporting a devicetree alias to specify the hardware specific portions, as is
done in the blinky sample. The application can then be configured in
BOARD.dts files or via :ref:`devicetree
overlays <use-dt-overlays>`.

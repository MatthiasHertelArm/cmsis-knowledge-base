---
id: "zep-design-goals-single-source-for-hardware-information"
type: "concept"
domain: "project"
title: "Design goals: Single source for hardware information"
summary: "Zephyr's built-in device drivers and sample applications shall obtain configurable hardware descriptions from devicetree."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/design.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/design.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr's built-in device drivers and sample applications shall obtain
configurable hardware descriptions from devicetree.


### Examples


- New device drivers shall use devicetree APIs to determine which :ref:`devices
  to create <dt-create-devices>`.

- In-tree sample applications shall use aliases to
  determine which of multiple possible generic devices of a given type will be
  used in the current build. For example, the blinky sample uses this to
  determine the LED to blink.

- Boot-time pin muxing and pin control for new SoCs shall be accomplished via a
  devicetree-based pinctrl driver


### Example remaining work


- Zephyr's twister_script currently use `board.yaml` files to
  determine the hardware supported by a board. This should be obtained from
  devicetree instead.

- Legacy device drivers currently use Kconfig to determine which instances of a
  particular compatible are enabled. This can and should be done with devicetree
  overlays instead.

- Board-level documentation still contains tables of hardware support which are
  generated and maintained by hand. This can and should be obtained from the
  board level devicetree instead.

- Runtime determination of `struct device` relationships should be done using
  information obtained from devicetree, e.g. for device power management.

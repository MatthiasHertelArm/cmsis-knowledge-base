---
id: "zep-board-porting-guide-general-recommendations"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: General recommendations"
summary: "For consistency and to make it easier for users to build applications which remain board agnostic, please follow these guidelines when porting a board you intend to contribute to Zephyr:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

For consistency and to make it easier for users to build applications which remain board agnostic,
please follow these guidelines when porting a board you intend to contribute to Zephyr:

Enable valuable components in Devicetree
  Devicetree nodes for valuable onboard components (LEDs, buttons, sensors, onboard
  USB/Ethernet/BLE/Wi-Fi, etc.) must be **enabled by default** and have correct pin control and
  driver configuration so that they work out of the box.

Keep subsystems disabled by default (Kconfig)
  Do not enable subsystems in the board defconfig unless they are strictly required for basic board
  operation, or are explicitly listed as exceptions in these recommendations.

Configure system clock and tick source
  Set up a functioning system clock and tick source.

Provide a default console
  Use the `zephyr,console` chosen node to point to the UART controller used for console output.

  Boards with built-in debug or a USB-to-UART adapter should set the console to the UART controller
  connected to that adapter.

  USB-only boards without any debug adapter must include the common USB CDC-ACM
  `Kconfig <boards/common/usb/Kconfig.cdc_acm_serial.defconfig>` and :zephyr_file:`DTS
  <boards/common/usb/cdc_acm_serial.dtsi>` fragments to enable CDC-ACM UART as a default backend
  for logging and shell.

Add shield interface definitions
  For boards exposing standard expansion headers, add connector nodes and pin-muxing. Enable only
  the peripherals needed for the expected/standard connector functionality.

Configure pins and peripheral instances
  Map peripherals to the correct pins (e.g., SPI on Arduino SPI pins) and provide default pinmux
  entries supporting the board's features.

Enable networking interfaces
  If networking hardware is present, configure default interfaces for each supported technology so
  that networking samples work out of the box.

Enable GPIO controllers
  All GPIO ports connected to onboard components or expansion headers should be enabled.

Enable MPU and stack protection
  It is recommended to enable the MPU when available (unless memory resources are too limited).
  When the MPU is enabled, it is recommended to also enable hardware stack protection
  (`CONFIG_HW_STACK_PROTECTION`) to ease debugging by allowing the kernel to detect stack overflows.

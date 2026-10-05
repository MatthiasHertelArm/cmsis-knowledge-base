---
id: "alp-advanced-soc"
type: "concept"
domain: "project"
title: "Design an AXI-Lite peripheral to control GPIOs"
summary: "Learn how to design and integrate a custom AXI-Lite peripheral with a Cortex-A9 processor on the Zybo Z7-10 board using Vivado, configuring GPIOs to control LEDs based on switch inputs."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/advanced_soc/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/advanced_soc/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Learn how to design and integrate a custom AXI-Lite peripheral with a Cortex-A9 processor on the Zybo Z7-10 board using Vivado, configuring GPIOs to control LEDs based on switch inputs.

**Who is this for:** This is an introductory topic for software developers interested in System on Chip Design.

**Learning objectives:**

- Configure and integrate an AXI-Lite peripheral with a Cortex-A9 Processing System.
- Program the Cortex-A9 processor to read the state of switches and control the LEDs using a C program.
- Demonstrate a basic functional system that lights up the LEDs based on the status of the switches.

**Prerequisites:**

- Some familiarity with Verilog
- Basic understanding of System on Chip design
- A 'Zybo Z7-10' development board

**Steps:**

1. Setup a Workspace in Xilinx Vivado
2. Create a custom AXI4 Peripheral
3. Connect AXI4 Peripheral to ZYNQ Processing System
4. Generate the bitstream and write your application using Vitis IDE

Time: about 60 minutes.

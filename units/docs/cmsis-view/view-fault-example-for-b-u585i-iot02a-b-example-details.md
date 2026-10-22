---
id: "view-fault-example-for-b-u585i-iot02a-b-example-details"
type: "concept"
domain: "trace"
title: "Fault example for B-U585I-IOT02A board (Cortex-M33): Example details"
summary: "The example contains 2 applications: Secure and Non-Secure."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Examples/Fault/B-U585I-IOT02A/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Examples/Fault/B-U585I-IOT02A/README.md#example-details"
license: "Apache-2.0"
mode: "V"
---

Clock Settings:

- **System Core Clock**: **160 MHz**

The example contains 2 applications: **Secure** and **Non-Secure**.

**Secure application** (bare-metal, no RTOS):

- setups the system (clocks, power, security and privilege rights (GTZC), caching) according to the STM32CubeMX configuration
- provides a function for triggering a fault on the Secure side

**Non-Secure application** (uses RTX RTOS and Standard C Library):

- setups the peripherals used by the non-secure application (LED, USART1) according to the STM32CubeMX configuration
- it runs 2 threads:
  - `AppThread` thread: Blink Green LED with 1 second interval
  - `FaultTriggerThread` thread: Trigger a fault according to input from the STDIO

When a fault is triggered the fault handler saves the fault information with the `ARM_FaultSave` function.

When valid fault information exists it can be viewed with **Component Viewer** or with `ARM_FaultRecord` function the fault information
can be output to the **Event Recorder** or with the `ARM_FaultPrint` function it can be output to the STDIO.

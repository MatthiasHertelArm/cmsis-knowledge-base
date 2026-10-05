---
id: "intr-a-schematic-review-checklist-for-f-my-current-checklist"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers: My current checklist"
summary: "Given these experiences, I have compiled the following list:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist#my-current-checklist"
license: "CC-BY-SA-4.0"
mode: "V"
---

Given these experiences, I have compiled the following list:

### Power/Battery

- [x] How does the firmware shutdown the device? Especially for a battery
      powered device.[1](#story-1-brown-out-loop)
- [x] For a battery powered device, Can the firmware measure how much power is
      available? How much accuracy is needed in this measurement?
      [1](#story-1-brown-out-loop)
- [x] How does a user reset your device?[2](#story-2-reset)

### GPIOs

- [x] Provide a GPIO map in a spreadsheet, with main function after reset,
      intended function, and any additional notes.
      - [x] Include configuration of peripherals -> GPIOs to ensure any MCU-specific
              pin sharing constraints are met.
      - [x] Include other associated MCU resources, such as DMA or timers, to ensure
              that each of those resources are used only once.
- [x] Are all MCU peripherals used only once?
- [x] If the MCU is held in reset, are the peripheral devices held in their
      proper state? (Pull-up/pull-downs where needed)
- [x] Does the reset line have a proper pull-up or pull-down? (This is a common
      failure, so worth noting).

### Busses

- [x] Do you have a mechanism to reset all IC's attached to buses (when
      appropriate)?
- [x] Are all I2C devices on the same bus on different addresses?
- [x] If your MCU resets in the middle of an I2C read, how do you recover
      talking with the device you were reading from?[3](#story-3-i2c-resets)
- [x] If your MCU resets in the middle of a SPI transfer, how does the device
      the MCU was talking with handle that?
- [x] For all UART devices, are Rx/Tx lines setup properly (ensure Tx->Rx, and
      check the datasheets of the device to see if Rx means receiving on the
      peripheral side)?
- [x] For all UART devices, are RTS/CTS lines needed?
- [x] For all UART devices, are RTS/CTS lines setup properly (this is confusing,
      because RTS -> CTS, but some devices label them differently)?

### Memory/Flash Storage

- [x] Do you have a code size estimate? And RAM estimate? How much buffer do you
      have in case your estimate is low?
- [x] Do you have sufficient space for additional features over the lifetime of
      the product?
- [x] Where will crash logs be stored? (Typically need to survive a system
      reset). Think about this when thinking about RAM requirements.

### Debug/Test Infrastructure

- [x] How will you (a firmware engineer) attach a debugger to the board? (By
      soldering is not usually a good
      answer).[5](#story-5-too-much-or-to-little-debug)
- [x] Are non-essential, but helpful, GPIOs exposed for a debugger, such as SWO
      or ETM?
- [x] Do test points exist for power rails, analog signals, and buses?
- [x] If the target microcontroller constraints allow for it, are some GPIO pins
    assigned for arbitrary firmware development, measurements and debug
    purposes? [6](https://covemountainsoftware.com/2016/12/27/brother-can-you-spare-a-gpio/)
- [x] Subject to board layout constraints, are the debug GPIOs routed to
  test points that may be connected to an o-scope or other common
  tools with minimal risk to the PCB or personnel?
- [x] Are the debug GPIOs used _only_ for debug purposes?

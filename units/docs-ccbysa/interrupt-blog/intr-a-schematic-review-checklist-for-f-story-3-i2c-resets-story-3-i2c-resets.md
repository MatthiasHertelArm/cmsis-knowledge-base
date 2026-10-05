---
id: "intr-a-schematic-review-checklist-for-f-story-3-i2c-resets-story-3-i2c-resets"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers: Story 3 - I2C Resets {#story-3-i2c-resets}"
summary: "While developing a fitness tracker, I kept running into a bug where I occasionally needed to fully power cycle a device to get the temperature sensor to start working again."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist#story-3-i2c-resets-story-3-i2c-resets"
license: "CC-BY-SA-4.0"
mode: "V"
---

While developing a fitness tracker, I kept running into a bug where I
occasionally needed to fully power cycle a device to get the temperature sensor
to start working again. The temperature sensor was connected over I2C, and
digging into the issue, I found that, when this was happening, the I2C SDA line
was stuck low. We were able to reproduce that failure by having the MCU reset in
the middle of an I2C read. Because the I2C controller on the MCU was controlling
the clock and stopped clocking, the peripheral was still driving the SDA line,
waiting for the next clock signal.

We had no reset line headed to the I2C device, so we could not reset the I2C
device. However, we could manually clock out the remaining SCL cycles on the SCL
line, and so modified our boot sequence to manually toggle the SCL line to
"clock out" the remaining data, freeing up the I2C bus.

However, I'd still have preferred a true reset line.

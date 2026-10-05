---
id: "alp-arduino-pico-int-background-disadvantages-of-looping"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Learn about interrupts: Disadvantages of looping"
summary: "So far, you have used the Arduino loop() function to check the state of the PIR sensor multiple times per second. You have also had to store the state between checks so that the program knows when the state changes."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/int-background.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/int-background/#disadvantages-of-looping"
license: "CC-BY-SA-4.0"
mode: "V"
---

So far, you have used the Arduino `loop()` function to check the state of the PIR sensor multiple times per second. You have also had to store the state between checks so that the program knows when the state changes. While this approach is conceptually very simple and familiar to application developers, it does have some significant disadvantages in the resource constrained world of microcontrollers.

For starters, the program must keep running, constantly checking for a change in the PIR sensor. It never has the opportunity to enter a low-power state. In application development this isn't usually a concern, as a little excess CPU usage doesn't cost anything. But if your application is running on a device with a small battery, sometimes even a non-rechargeable one, excess CPU usage reduces the life expectancy of your device.

The other disadvantage is complexity. This example is simple from an application developer's perspective but from a microcontroller perspective, it could be even simpler. All the work the software does to maintain state information between checks of the PIR sensor can be handled by the hardware itself. Instead of checking the state on every iteration of the loop, you just need to know when the state has changed.

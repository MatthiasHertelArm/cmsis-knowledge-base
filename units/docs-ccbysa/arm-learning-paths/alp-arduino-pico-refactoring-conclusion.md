---
id: "alp-arduino-pico-refactoring-conclusion"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Refactor the application: Conclusion"
summary: "That's it! You have learned how to use interrupts. You can see how much smaller and simpler the use of interrupts makes things, even for an example that was small and simple to begin with."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/refactoring.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/refactoring/#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

That's it! You have learned how to use interrupts. You can see how much smaller and simpler the use of interrupts makes things, even for an example that was small and simple to begin with.

Not only that but using interrupts makes other improvements possible. For example, you could stop the `loop()` and put the device into a very low-power state while no motion is detected, and let the interrupt power it back up to respond.

You can download the complete [pir_sensor.ino](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/pir_sensor_2.ino) and try it out yourself.

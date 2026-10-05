---
id: "alp-arduino-pico-int-background-things-to-consider"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Learn about interrupts: Things to consider"
summary: "You do need to make sure that your interrupt code is small and fast because nothing else can run while your interrupt handler is running."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/int-background.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/int-background/#things-to-consider"
license: "CC-BY-SA-4.0"
mode: "V"
---

You do need to make sure that your interrupt code is small and fast because nothing else can run while your interrupt handler is running. Therefore, you want to make sure that it finishes quickly so your main application can resume. You should only use the interrupt handler to change the state of your application, not to respond to that changed state. Leave the response to your main code. In the example this would be the `loop()` function of the Arduino sketch.

Another thing to be aware of is what you can't do in your interrupt code. Since nothing else runs, not even in the background, you can't make calls to `delay()` because this relies on updates to the system clock but the system clock isn't being updated while your interrupt code is running. If you do call `delay(1000)` in your interrupt code, it will **never** return because it won't ever see that the system clock advanced by one second, and your interrupt code will freeze your whole device.

Likewise you can't read or write to your `Serial` console in interrupt code because those functions rely on background execution, and that background execution won't be running while your interrupt code is running. More complex interfaces, like I2C or SPI, are also unable to function from within your interrupt handler.

With this introduction to interrupts, you can revisit the example code for the motion detector and see how to get the same functionality with less code using interrupts.

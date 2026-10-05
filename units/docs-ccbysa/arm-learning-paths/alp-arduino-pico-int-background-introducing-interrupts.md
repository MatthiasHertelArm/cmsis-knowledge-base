---
id: "alp-arduino-pico-int-background-introducing-interrupts"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Learn about interrupts: Introducing interrupts"
summary: "As the name implies, an interrupt is something that can \"interrupt\" the running program."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/int-background.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/int-background/#introducing-interrupts"
license: "CC-BY-SA-4.0"
mode: "V"
---

As the name implies, an interrupt is something that can "interrupt" the running program. It's a way to make your CPU pause execution of one piece of code, begin executing another, and finally return to the original piece of code and continue executing where it left off. This can be done without threading, concurrency or adding mutexes to your code because the CPU makes sure that nothing else will change while the interrupt code is running. It may sound like advanced programming but in reality, it makes things much simpler.

To use an interrupt, you first have to define an interrupt handler. If you've used event handlers and callbacks in application development, you'll find these to be very familiar. An interrupt handler is just a function that contains the code you want to run when the interrupt condition happens. Again, nothing else will be running when your interrupt function is running, so you don't need to have event threads or concurrency checking.

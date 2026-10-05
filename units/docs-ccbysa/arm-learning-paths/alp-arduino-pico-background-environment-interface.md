---
id: "alp-arduino-pico-background-environment-interface"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: About Embedded Programming: Environment interface"
summary: "Another big difference is that your interactions will be with the physical environment more than with a user. Don't expect to have mouse or touch events to drive your interactions."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/background.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/background/#environment-interface"
license: "CC-BY-SA-4.0"
mode: "V"
---

Another big difference is that your interactions will be with the physical environment more than with a user. Don't expect to have mouse or touch events to drive your interactions. Most embedded programming won't even have a graphical interface to speak of. 

What you will have are sensors that will tell you about your physical environment: the temperature, pressure, level of noise or vibration, distance, speed, etc. You'll also have the ability to change things in your physical environment, with lights, motors, electrical relays, valves, etc. All of this your embedded program will do without any human interaction at all.

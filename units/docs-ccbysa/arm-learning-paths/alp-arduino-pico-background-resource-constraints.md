---
id: "alp-arduino-pico-background-resource-constraints"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: About Embedded Programming: Resource constraints"
summary: "Application developers have had the luxury of abundance and abstraction when it comes to resources. Today, even on mobile you'll have gigabytes of memory and CPUs running at several gigahertz at your disposal."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/background.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/background/#resource-constraints"
license: "CC-BY-SA-4.0"
mode: "V"
---

Application developers have had the luxury of abundance and abstraction when it comes to resources. Today, even on mobile you'll have gigabytes of memory and CPUs running at several gigahertz at your disposal. On a microcontroller, however, your code may need to fit in just a few hundred **kilobytes** of RAM and execute at a few hundred **megahertz** on the CPU.

It's not as dire is at sounds though. The tools, software, and libraries that have been built for embedded development will help you. Instead of a heavy operating system intended to support any hardware, you'll be using one that's been tailored for your specific device. The libraries you use, rather than trying to do as much as possible, have been designed to use the minimum amount of resources. You generally won't be sharing your resources with other applications as embedded systems tend to do one thing at a time (although this is changing with the advent of smart devices).

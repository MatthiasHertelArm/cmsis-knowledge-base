---
id: "alp-arduino-pico-background-in-real-time"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: About Embedded Programming: In real-time"
summary: "Lastly, the timing of your code's execution is going to be subtly different than it is for an application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/background.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/background/#in-real-time"
license: "CC-BY-SA-4.0"
mode: "V"
---

Lastly, the timing of your code's execution is going to be subtly different than it is for an application. You always want your code to be responsive and "fast" but that takes on a whole new meaning with embedded devices where milliseconds matter.

You know that when a user clicks on a button in your application, it will trigger some piece of your code to run. Eventually. But before that happens, the click "event" has to make it's way through the operating system's abstractions, wait for your application's process to be scheduled time on the CPU, and then eventually make it's way into the event thread of toolkit or webserver, before finally getting to your code.

This all takes too long when your embedded device is controlling a piece of heavy equipment or critical infrastructure. Instead, your embedded programming environment is going to make use of interrupts, ways of executing code immediately when something happens in the physical environment. Interrupts let your code preempt anything else running on the device and respond immediately to that change. The drawback of this is that, because nothing else can happen while your code is executing (not even the ticking of the system's clock) you have to make sure that it does whatever it needs to do as quickly as possible.

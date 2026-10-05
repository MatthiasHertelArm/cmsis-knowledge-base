---
id: "alp-arduino-pico-arm-embedded"
type: "concept"
domain: "project"
title: "Get started with Arm"
summary: "Now that you know the differences between application and embedded programming, as well as the differences in the hardware and software stack, it's time to take your first steps into embedded software development!"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/arm_embedded.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/arm_embedded/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that you know the differences between application and embedded programming, as well as the differences in the hardware and software stack, it's time to take your first steps into embedded software development!

(figure: Diagram showing the typical Arm embedded software stack with three layers: Cortex-M CPU at the bottom hardware layer, Mbed OS RTOS in the middle, and C application code with supporting libraries at the top. This illustrates the standard architecture for Arm microcontroller projects where the RTOS sits directly on hardware without a firmware abstraction layer.#center)

A typical embedded project for Arm devices looks like this. For microcontrollers, you'll have a CPU in the Cortex-M family and, as your RTOS, you'll use something like Mbed OS, which is provided by Arm and used by default in Arm Developer Studio and Keil MDK.

On top of that you will write your application in C, using any number of the available supporting libraries depending on your specific needs and use case.

If this is your first step into embedded programming, you can start with something easier, Arduino. 

# Arduino

As you know, these small, cheap, development prototyping boards have been around for years, and many people have made them blink some LEDs before shoving them into a drawer and going back to application development.

But they're so much more than just a toy for making lights flash. They're a really great way to get started with embedded programming!

(figure: Diagram showing Arduino's simplified embedded stack with Cortex-M0+ CPU at the hardware layer, Arduino core package in the middle providing hardware abstraction, and Arduino sketch written in C++ at the application layer. This shows how Arduino makes embedded development more accessible by hiding low-level hardware details behind the core package.#center)

The latest generations of Arduino use Arm Cortex-M microprocessors, such as the Cortex-M0+ in the Arduino Nano RP2040, making that more powerful and capable than before, while still providing a very simple and straightforward programming experience.

---
id: "alp-arduino-pico-arm-embedded-sketch"
type: "concept"
domain: "project"
title: "Get started with Arm: Sketch"
summary: "Finally, you have your sketch. Unlike a normal C application, your Arduino sketch doesn't start with a main() function."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/arm_embedded.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/arm_embedded/#sketch"
license: "CC-BY-SA-4.0"
mode: "V"
---

Finally, you have your sketch. Unlike a normal C application, your Arduino sketch doesn't start with a `main()` function. Instead the code you put inside `setup()` will be executed first and then the code you put inside `loop()` will be executed repeatedly after that. 

What's really happening when you click `Compile`, however, is that the Arduino IDE will generate C code with a `main()` function that calls `setup()` and `loop()` in your sketch. That C code is then combined with your sketch and the Arduino core RTOS into a single binary that gets flashed onto your board. So you still have everything that any other embedded program would have, it's just that Arduino has hidden most of it so that you can focus on your prototyping code.

---
id: "alp-arduino-pico-arduino-sketch-run-your-code"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Program your smart device prototype: Run your code"
summary: "Now that you have a good understanding of the code, you should run it on your device."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/arduino_sketch.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/arduino_sketch/#run-your-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that you have a good understanding of the code, you should run it on your device. With your Raspberry Pi Pico board plugged in to your computer, and the [correct board and port selected in the Arduino IDE](https://learn.arm.com/install-guides/arduino-pico/), click the `Upload` button on the IDE to build and install it on your device.

If successful, you should see the LED on your board light up. If you wave your hand in front of the sensor, you should also hear a double beep and see the LED turn off for a few seconds.

You can further check that your code is running properly by opening the `Serial Monitor` from the `Tools` menu of the Arduino IDE. There you should see all of the output messages, including count of detected motion events, coming from your sketch.

(figure: Screenshot of the Arduino IDE Serial Monitor window displaying debug messages from the motion detection sketch. The output shows repeated "Motion detected" messages followed by motion event counts, confirming that the PIR sensor is triggering correctly and the sketch is processing the interrupts.#center)

Congratulations! You have successfully programmed your microcontroller and built a working, if simple, smart device. 

Continue on to see how to improve the application by replacing the `loop()` and `delay()` calls with interrupts.

---
id: "alp-arduino-pico-int-setup-interrupt-handler"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Add the interrupt code: Interrupt handler"
summary: "The next thing to do is write the interrupt handling code."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/int-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/int-setup/#interrupt-handler"
license: "CC-BY-SA-4.0"
mode: "V"
---

The next thing to do is write the interrupt handling code. 

An interrupt handler is just a function in Arduino. Importantly, this function does not take any arguments and it doesn't return a value.

```arduino
void motion_detected() {
  motionDetected = true;
}
```

Remember that your interrupt handler should be small and fast. All you need to do is change the value of the `motionDetected` variable, it doesn't get much smaller or faster than that!

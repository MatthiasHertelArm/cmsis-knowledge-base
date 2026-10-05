---
id: "alp-arduino-pico-int-setup-remove-state"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Add the interrupt code: Remove state"
summary: "Previously, you used two variables to keep track of the current value and the previous value of the PIR sensor."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/int-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/int-setup/#remove-state"
license: "CC-BY-SA-4.0"
mode: "V"
---

Previously, you used two variables to keep track of the current value and the previous value of the PIR sensor. 

The variables were used to identify a change in state that needs a response: 

```arduino {linenos=table,linenostart=12}
// This variable will hold the current value of the motion detection pin's charge
// LOW means no motion is detected, HIGH means motion is detected
int motionState = LOW;

// This variable will hold the read value on each iteration of the loop
int val = 0;
```

The new code does not need to keep track of the state, only if the state changes.

You can replace the two variables with just one:

```arduino {linenos=table,linenostart=12}
// This variable tells us if motion triggered the interrupt
bool motionDetected = false;
```

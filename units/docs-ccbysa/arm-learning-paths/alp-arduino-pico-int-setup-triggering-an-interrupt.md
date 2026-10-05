---
id: "alp-arduino-pico-int-setup-triggering-an-interrupt"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Add the interrupt code: Triggering an interrupt"
summary: "Now that the handler function is in place, you need to tell the device when to call it. To do that, add the line below to the setup() function:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/int-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/int-setup/#triggering-an-interrupt"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that the handler function is in place, you need to tell the device when to call it. To do that, add the line below to the `setup()` function:

```arduino
attachInterrupt(digitalPinToInterrupt(motionPin), motion_detected, RISING);
```

The `attachInterrupt` function takes three arguments: 
- the interrupt number
- the interrupt handler function
- the interrupt condition

The arguments are described in the next three sections.

### Interrupt number

Depending on the CPU, there can be a number of things that can trigger an interrupt. The CPU gives each of these a number and you need to look at the documentation for your specific device to know which number corresponds to which trigger. In this Arduino sketch, you can use the `digitalPinToInterrupt()` function to look up the interrupt number for a given pin, such as the `motionPin` variable.

### Interrupt handler

This is a reference to your function. Be sure to use the function name and don't put parentheses after it or else it will execute the function and pass the return value to `attachInterrupt`, which isn't what you want.

### Interrupt condition

Depending on your hardware there may be different conditions that can be used to trigger an interrupt. Arduino typically supports `CHANGE`, `FALLING` and `RISING` to trigger interrupts based on changes to the pin's input voltage: 
- `FALLING` for a change from `HIGH` to `LOW`
- `RISING` for a change from `LOW` to `HIGH`
- `CHANGE` for a change in either direction

Use the `RISING` condition because you only want to do something when the PIR sensor changes from  `LOW` to `HIGH`. 

Continue to the next section to see the updated application code.

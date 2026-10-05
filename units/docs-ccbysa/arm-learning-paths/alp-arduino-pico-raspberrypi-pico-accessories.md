---
id: "alp-arduino-pico-raspberrypi-pico-accessories"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Build a smart device prototype: Accessories"
summary: "For interacting with the physical world you can use two cheap commodity components."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/raspberrypi_pico.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/raspberrypi_pico/#accessories"
license: "CC-BY-SA-4.0"
mode: "V"
---

For interacting with the physical world you can use two cheap commodity components. 

(figure: Diagram showing PIR motion sensor pinout with three pins labeled from left to right: VCC for power input, OUT for data signal output that goes high when motion is detected, and GND for ground. Understanding this pinout is essential for wiring the sensor correctly to the Pico's 3.3V power, ground, and GPIO pins.#center)

First a PIR motion sensor. This sensor reacts to infrared photons emitted by a warm moving object, like a person or animal. The interface is simple, it has one pin for input voltage, one pin for ground to complete the circuit, and a third pin that will have the same voltage as the input pin when motion is detected, and the same voltage as the ground pin when it isn't.


(figure: Diagram showing piezo-electric buzzer pinout with two terminals: a positive terminal marked with a plus sign that connects to a GPIO pin for signal input, and a negative terminal that connects to ground. When voltage is applied to the positive terminal, the buzzer emits a high-pitched beep to signal motion detection.#center)

Second, a very simple electric buzzer. You could get fancy with one of these and make it play different sounds with something called Pulse Width Modulation (PWM) but, for simplicity, you can give it a constant voltage which will result in a high-pitched beeping noise.

(figure: Diagram showing standard solderless breadboard layout with color-coded connection patterns. Holes in each column are connected vertically, while the center divider isolates left and right sides. Power rails along the edges run horizontally for distributing voltage and ground. This layout allows you to connect multiple components to the same Pico pins by plugging wires into holes on the same connected column.#center)

Finally, you can use a breadboard to connect the components together without having to do any soldering.

If you're not familiar with a breadboard, the image above shows you how all of the little holes are connected together. When you plug a wire into a hole, it connects it to every other hole on the same connected line. This configuration lets you connect multiple components to the same pin on your development board.

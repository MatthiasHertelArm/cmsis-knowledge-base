---
id: "alp-arduino-pico-raspberrypi-pico-assemble-your-system"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Build a smart device prototype: Assemble your system"
summary: "(figure: Photo showing Raspberry Pi Pico seated on a breadboard with its dual rows of GPIO pins straddling the center divider."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/raspberrypi_pico.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/raspberrypi_pico/#assemble-your-system"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Step 1: Seat your Raspberry Pi

(figure: Photo showing Raspberry Pi Pico seated on a breadboard with its dual rows of GPIO pins straddling the center divider. This placement ensures that each pin has its own column of connected holes on either side, allowing you to wire components to the Pico's GPIOs without creating short circuits across pins.#center)

Seat your Raspberry Pi Pico on the breadboard so that its rows of pins sit on either side of the center divider. Make sure that it's firmly pressed all the way down but be careful not to bend any of the pins.

### Step 2: PIR ground

(figure: Photo showing a black jumper wire connecting the PIR sensor's ground pin to physical pin 38 on the Raspberry Pi Pico. Pin 38 is one of the Pico's ground pins that completes the circuit for powering the PIR sensor. Using black wire for ground connections is a common convention that makes circuits easier to troubleshoot.#center)

Using a black jumper wire, connect the ground pin of your PIR sensor to pin #38 on your Pico. This pin is a ground voltage pin on the Pico.

### Step 3: PIR input voltage

(figure: Photo showing a red jumper wire connecting the PIR sensor's VCC power pin to physical pin 36 on the Raspberry Pi Pico. Pin 36 provides 3.3V output to power the PIR sensor. Using red wire for voltage connections follows standard wiring conventions and helps distinguish power connections from ground and signal lines.#center)

Using a red wire, connect the input voltage pin of your PIR sensor to pin #36 on your Pico. This pin is a 3.3 volt pin on the Pico and will supply power to your PIR sensor.

### Step 4: PIR data

(figure: Photo showing a jumper wire connecting the PIR sensor's data output pin to physical pin 34 on the Raspberry Pi Pico. This pin corresponds to GPIO 28, which your code will monitor to detect when the PIR sensor signals motion. Note the distinction between physical pin numbering and GPIO numbering, which is important when writing your Arduino sketch.#center)

The last step to connecting the PIR sensor is to connect the middle data pin to pin #34 on your Pico. This is a GPIO pin that you can use to either read or write data. 

Note that this is GPIO #28, even though it's physical pin #34. Physical pin number and GPIO numbers are not the same.

### Step 5: Buzzer ground

(figure: Photo showing a jumper wire connecting the piezo-electric buzzer's negative terminal to physical pin 23 on the Raspberry Pi Pico. Pin 23 is a ground pin that completes the buzzer circuit. With both ground and power connections in place, the buzzer will emit a tone when the GPIO pin provides voltage to signal detected motion.#center)

Next, it's time to connect the buzzer. Start by connecting the buzzer's ground pin to pin #23 on your Pico. This is another ground pin that is build into your board.

### Step 6: Buzzer input

(figure: Photo showing a jumper wire connecting the piezo-electric buzzer's positive terminal to physical pin 25 on the Raspberry Pi Pico. This pin corresponds to GPIO 19, which your Arduino code will control to trigger the buzzer when motion is detected. By setting this GPIO pin high, you provide voltage that causes the piezo element to vibrate and emit a beep.#center)

Then, connect the buzzer's input pin to pin #25 on your Pico. This is another GPIO pin, this time GPIO #19.

### Review

Your physical device is now assembled and ready. 

Here is a review:

The motion sensor is connected to power, ground, and GPIO #28, which is where you will read the motion state from.

The buzzer is connected to ground and GPIO #24, which is what you will use to turn it on and off.

Now it's time to start programming!

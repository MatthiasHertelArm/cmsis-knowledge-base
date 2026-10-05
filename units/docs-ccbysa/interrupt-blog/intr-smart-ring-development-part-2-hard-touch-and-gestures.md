---
id: "intr-smart-ring-development-part-2-hard-touch-and-gestures"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: Touch and gestures"
summary: "The main feature of Open Ring is the touch sensor, as it captures user input."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#touch-and-gestures"
license: "CC-BY-SA-4.0"
mode: "V"
---

The main feature of Open Ring is the touch sensor, as it captures user input.
The original idea was to use taps and swipes to control music (e.g., on a user's
smartphone), but these gestures can generally map to any allowed Bluetooth
action.

There are a few ways to detect gestures like this, with the most popular one
being capacitive sensing. Capacitive sensing detects changes in capacitance that
are caused by the human body. There are two main techniques to measure
capacitance for touch: self-capacitance and mutual capacitance. In very
simplified terms, a self-capacitance measurement circuit will measure the
capacitance of a touch pad (along with all the parasitic capacitance), while a
mutual capacitance circuit will measure the difference in capacitance between
two wires. A mutual capacitance circuit is more complicated, but yields better
results, lower noise, and better resistance to environmental factors.

It’s worth mentioning here an interesting find in Oura Gen 3 X-ray teardown
photos. The PCB hosts two large copper pads, which are most likely
self-capacitance wear detection circuitry, especially due to Oura using a
Cypress chip known for CapSense technology.

There are a few chip manufacturers that offer capacitive sense technology. This
capability will either be provided as one of the MCU peripherals or in a
standalone chip. With mutual capacitive sense, due to its more complex nature
(and therefore, setting up and tuning), the reasonable approach was to pick an
MCU.

It's worth noting that picking the chip is only the first step. The touch sensor
needs to be designed correctly using PCB copper layout. We've tried many
different mutual capacitance designs to pick the one that works best in a ring:
(figure: Open Ring touch sensor prototypes)

As for the MCU, we chose Atmel
[ATSAML10E16A ](https://github.com/stawiski/open-ring/blob/main/docs-ring/atmel/SAM-L10L11-Family-DataSheet-DS60001513F.pdf)
with QTouch in a tiny 2.8x2.8mm WLCSP package (remember: everything needs to be
absolutely tiny in a smart ring). This increases the complexity of the product a
fair bit due to dual MCU architecture, rather than having a single all-in-one
SoC. However, after a few prototypes with different chipsets at the time, we
concluded this was the best chip for this application. The architecture has a
Dialog BLE chip acting as the interface to the outside world, while Atmel
handles the real-time part: gesture sensing, haptics, wear detection, and
battery charging. The obvious challenge introduced by this architecture is
complexity of the firmware update process, where both MCUs must update
simultaneously, and they need to always be able to communicate with each other
if for any reason one of them fails to update.

With capacitive sense design in place, we arrived at the last feature of the
ring: haptics.

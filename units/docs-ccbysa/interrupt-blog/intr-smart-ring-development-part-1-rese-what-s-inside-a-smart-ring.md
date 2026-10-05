---
id: "intr-smart-ring-development-part-1-rese-what-s-inside-a-smart-ring"
type: "concept"
domain: "debug"
title: "Smart Ring Development  (Part 1) － Research and Prototype: What's inside a Smart Ring?"
summary: "So what would we find in a typical Smart Ring?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-06-13-smart-ring-development-part-1.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-1#what-s-inside-a-smart-ring"
license: "CC-BY-SA-4.0"
mode: "V"
---

So what would we find in a typical Smart Ring?

- There would be a small curved Li-Po battery
- Charging circuit for the battery
- Bluetooth SoC, usually acting as the main MCU
- Bluetooth antenna
- Power management circuit
- Some input/output circuitry (product dependent)

Additionally, there would be a charger for the Smart Ring. Usually, these
chargers come in the form of a wall charger or a USB charger. The charger could
make physical contact with the ring using charging pads or be wireless,
utilizing induction charging.

The input/output circuitry is the core functionality of the Smart Ring, as it
provides a means of interaction with the user. For a ring like the Oura (health
Smart Ring), we find circuitry that controls the LEDs and optical receivers to
monitor heart rate. In the now-discontinued Amazon Echo Loop ring, there was a
button, a microphone, and haptics, as this ring acted like a remote microphone
for Alexa.

For our music ring, the input was a touchpad for sensing user gestures such as
taps, tap-and-hold, and swipes. For output, we chose haptic feedback, a classic
UX feature when using capacitive touch sensing, since without a physical button
press, the user does not feel that an action has been registered.

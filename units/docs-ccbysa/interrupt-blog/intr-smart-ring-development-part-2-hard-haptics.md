---
id: "intr-smart-ring-development-part-2-hard-haptics"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: Haptics"
summary: "Haptics is often paired up with some form of user input, in our case a touch sensor, to give the user feedback about performed action (it’s often called “haptic feedback” for this reason)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#haptics"
license: "CC-BY-SA-4.0"
mode: "V"
---

Haptics is often paired up with some form of user input, in our case a touch
sensor, to give the user feedback about performed action (it’s often called
“haptic feedback” for this reason). If our sensor were replaced with physical
buttons that one can push and feel (good luck fitting that in!), there would be
no reason to put haptic feedback in the product.

However, with a touch sensor in a Bluetooth-connected device, things can go
wrong fast! The user can touch the sensor by mistake, there could be a Bluetooth
connection dropout, there could be water on the sensor, or mocking physical
touch, just to name a few. These problems stem from the nature of touch sensing,
as there is no immediate feedback for the user, hence why we introduced haptic
feedback to the product.

Haptic feedback is generally realised in the form of mass movement. This can be
simply realised by having an off-centre mass in a motor. When the motor is
actuated, the off-centre mass causes vibration. Another way can use
piezoelectric material which deforms when electric field is applied, effectively
causing a “click” feeling. This form of haptics has been used in Amazon’s
discontinued Echo Loop ring.

These two options come with significant challenges when you’re trying to fit
everything into a tiny smart ring. Piezoelectric actuators require a high
voltage (over 50V) and a circuit for waveform generation. This circuit will
usually consist of a boost converter (requires a coil) and an H-bridge.
Integrated circuits exist like
[Texas Instrument DRV2667](https://www.ti.com/product/DRV2667#product-details),
but even this comes in a 4x4x1mm package, not counting all other necessary
components, especially the piezo actuator.

On the other hand, vibration coin motors are extremely simple to drive. Like any
other DC motor, all they require is a switch. The significant disadvantage,
however, is the startup current, often in the 100mA+ range, which is needed to
get the mass into initial motion. A small curved Li-Ion battery of 17mAh
capacity cannot supply such a current. In the best case, we’re looking at a 3C
rate at 17mAh, which results in 51mA.

(figure: Open Ring tiny vibration motor)

Fortunately, we can solve this problem by adding lots of capacitors. This
solution balloons the BOM cost and takes up a lot of the PCB real estate, but
enables us to have haptics in the product. The advantage of capacitors is that
they can be added onto the flexible part of the rigid-flex PCB, while still
keeping the PCB bendable. This was simply not possible for BGA chips, and
especially anything as big as 4x4mm.

From our experiments, we’ve had good results with a capacitor bank of 940uF
total. This capacitance, combined with an engaged battery load switch, provided
a single vibration lasting about 300ms. There was not enough current for the
vibration to be continuous, but this was enough to have a working haptic
feedback in the solution. Just the capacitor bank added about $5 USD in total
BOM cost, so combined with a vibration motor, the haptic feedback sat at around
$10 USD total. This may sound ridiculously expensive, as it was; however, it
made having haptics with off-the-shelf components possible.

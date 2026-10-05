---
id: "intr-smart-ring-development-part-2-hard-wireless-charging"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: Wireless charging"
summary: "Basically, we can either charge the smart ring via physically exposed contacts or wirelessly. Physical contacts, while very simple on the electronics design level, come with their own mechanical challenge."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#wireless-charging"
license: "CC-BY-SA-4.0"
mode: "V"
---

Basically, we can either charge the smart ring via physically exposed contacts
or wirelessly. Physical contacts, while very simple on the electronics design
level, come with their own mechanical challenge. Pads need to be exposed, they
need to be invulnerable to a variety of environmental factors (sweat, water,
ESD, etc.), they need to align perfectly with charger contacts, and maintain
good pressure during charging.

All things considered, physical charging contacts are quite hard to get right
with product longevity and good user experience in mind. The other option is
wireless charging through induction. A wireless induction charger is a form of
an air-gapped transformer. Sounds pretty easy, right?

The induction charger consists of a primary and secondary coil, an air gap, and
housing material between them. The primary coil and secondary coils form simple
LC circuits, tuned in frequency to one another. The primary coil needs only a
simple square PWM drive to excite the LC circuit. It’s important to get the
frequency of the charger right, since the charger will also need to pass FCC
tests for emitted radiation. One of the most widely used frequencies for
wireless power systems is
[6.78 MHz](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-18)
(half of the popular 13.65 MHz for NFC/RFID). At 6.78 MHz, we can make a coil
simply out of the PCB tracks with an added ceramic capacitor to form our LC
circuit.

Our receiver coil on the smart ring side requires only a very simple half-bridge
rectifier made of two Schottky diodes. It’s important to pick fast Schottky
diodes with low parasitic capacitance, since we’re operating at 6.78 MHz here.
The rectifier gets us from induced AC into sweet DC, which we can work with. We
also add a few chunky capacitors to maintain a steady voltage, and a Zener diode
in case we’re inducing higher voltage than our
[BQ25125](https://github.com/stawiski/open-ring/blob/main/docs-ring/battery-charger/bq25125.pdf)
can take, and we’re done!

(figure: Open Ring charger receiver circuit)

To get the induction charging right, the most important bit is getting impedance
matched. The primary LC circuit in the ring charger needs to be tuned to the
secondary LC circuit in the ring. This also needs to account for all mechanical
offsets, like the tolerances of the coil placement in both the ring and the
charger, and the tolerance of the ring sitting in the charger during charging
(it will never sit perfectly).

(figure: Open Ring charger prototype)

With this in mind, we arrive at a big design decision. Do we make one charger to
rule them all (account for all ring sizes)? Or do we make multiple chargers (one
per ring sizing)?

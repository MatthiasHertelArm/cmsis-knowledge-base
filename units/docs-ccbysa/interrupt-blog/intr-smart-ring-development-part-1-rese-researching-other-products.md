---
id: "intr-smart-ring-development-part-1-rese-researching-other-products"
type: "concept"
domain: "debug"
title: "Smart Ring Development  (Part 1) － Research and Prototype: Researching other products"
summary: "As part of the market research, we've ordered all sorts of available Smart Rings: Oura Gen 2, Oura Gen 3, Amazon Echo Loop, ORII, and Motiv. This required some budget (around $1k USD) but provided invaluable insights."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-06-13-smart-ring-development-part-1.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-1#researching-other-products"
license: "CC-BY-SA-4.0"
mode: "V"
---

As part of the market research, we've ordered all sorts of available Smart
Rings: Oura Gen 2, Oura Gen 3, Amazon Echo Loop, ORII, and Motiv. This required
some budget (around $1k USD) but provided invaluable insights. After all, the
product experience starts with the purchase itself, through unboxing, setting
up, and pairing, to daily usage (often involves a mobile app). While in these
articles we will keep the focus only on the hardware and firmware aspects, it's
important to keep the whole solution in mind.

Getting the hardware and doing teardowns yourself is not the only option,
though. Some information can be obtained free of charge, for example, like
[this iFixit teardown for Oura Gen 2](https://www.ifixit.com/Teardown/Oura+Ring+2+Teardown/135207)
or FCC filings such as
[this one for Oura gen 2](https://fcc.report/FCC-ID/2AD7V-OURA2101#:~:text=FCC%20ID%202AD7V%2DOURA2101).
Reddit and dedicated electronics forums are also helpful here.

Now let's take a deeper look into the guts of the two most interesting of these
Smart Rings: Oura's and Amazon's.

### Oura Gen 2 & 3

Just from Oura's FCC filings, we inferred that their product used:

- Grepow batteries (from Shenzhen Grepow Battery)
- Different antenna matching circuits per ring size (means it's part of the
 trouble to support sizes from US6 to US13 ring size)
- Macronix or GD FLASH memory
- Rigid flex PCB as seen on photos from gen 2
- Open pads on the PCB (standard mass production technique for testing the
 hardware and flashing the firmware)

From iFixit teardown, we got more crucial information:

- There is a PCB pattern that looks like capacitive sense, so probably ring wear
 detection, which made sense for the Cypress chip they used (X-Ray photo)
- Antenna is a PCB antenna, very tightly routed through the ring and even
 through a microvia (X-Ray photo)
- Wireless charging coil design (X-Ray photo)
- BLE SoC was Cypress
- Texas Instruments BQ series battery charger

A big part of Oura's design is, of course, the whole LED and photodetector setup
for heart measurement, which included optical lenses made out of the ring's
housing.

(figure: Oura ring teardown)

From our own teardown, we additionally learned that:

- Induction charger used 6.8 MHz (half of 13.56 MHz, known for RFID)
- The charger base works by sensing the current in the coil. When the current
 gets low enough, the charger is going into "looking for a ring" state
- There is no communication between the charger and the ring; the only
 "information" is the load current of the ring, which affects the primary coil
 current

### Amazon Echo Loop

This ring from Amazon was discontinued shortly after launch. It was a really
cool piece of tech as it allowed the user to talk to Alexa with their finger, so
the hardware included a microphone, a speaker, and a Bluetooth audio chipset. It
also featured innovative haptic feedback design using piezo.

Here's an exploded photo of the ring from Amazon itself:

(figure: Exploded Amazon Echo Loop)

There were no known teardowns of this ring at the time, so we did our own:

(figure: Amazon Echo Loop Teardown - main board)
(figure: Amazon Echo Loop Teardown - battery)

Learnings:

- Realtek RTL8763B0A SoC
- Micro antenna connector left on the PCB (must have been for testing)
- Lishen curved Li-Ion battery
- 3 contacts left for charging
- Custom piezoelectric haptic feedback design

The charger's design for this ring was extremely simple, as Amazon decided to
use contact charging, which is a no-brainer. The only problems with such a
design are mechanical, wear and tear, and industrial design.

---
id: "intr-smart-ring-development-part-2-hard-ble-antenna"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: BLE antenna"
summary: "Closely tied to the BLE processor is the BLE antenna. The antenna design is generally independent of the chip itself, since the carrier frequency is the same 2.4GHz."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#ble-antenna"
license: "CC-BY-SA-4.0"
mode: "V"
---

Closely tied to the BLE processor is the BLE antenna. The antenna design is
generally independent of the chip itself, since the carrier frequency is the
same 2.4GHz. Often considered as “black magic”, the antenna design is indeed a
solid piece of engineering. Oura had a job position of “Senior RF Antenna Design
Engineer” just for this. After all, a product that emits radio waves falls under
the FCC category, so to be able to commercialize it, it requires a range of
certificates, including those for emitted radiation. A poor antenna design not
only comes with low effectiveness but can also cause interference to other radio
devices.

From the teardown of the Oura Ring Gen 3, we learned that their antenna was
designed as a microstrip antenna directly on the PCB. This is probably the best
way to go, and offers full flexibility, but is also the most expensive in terms
of development effort.

For these reasons, we opted for a simple integrated antenna component. It takes
up space on the PCB and is a bit tall, but it offers a packaged solution. Still,
a microstrip is required to route the 2.4GHz signal from the BLE chip to the
antenna, and this part of the PCB needs utmost care! It is a good practice to
share this information on a separate mechanical layer with the PCB manufacturer,
so they can adjust the microstrip accordingly to the stackup directly in the
gerber files.

(figure: W3008 chip antenna)

Below is the microstrip part as seen on the schematic:
(figure: Open Ring RF microstrip)

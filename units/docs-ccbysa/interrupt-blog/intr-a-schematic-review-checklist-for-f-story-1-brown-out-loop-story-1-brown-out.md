---
id: "intr-a-schematic-review-checklist-for-f-story-1-brown-out-loop-story-1-brown-out"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers: Story 1 - Brown-out Loop {#story-1-brown-out-loop}"
summary: "Years ago, I worked on an LTE enabled e-bike."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist#story-1-brown-out-loop-story-1-brown-out-loop"
license: "CC-BY-SA-4.0"
mode: "V"
---

Years ago, I worked on an LTE enabled e-bike. The LTE module was powered off the
battery that powered the electric assist for the bike, but had a single cell
backup battery that would be used if the main battery was removed from the
device.

Once these modules were in the field, we started getting reports of them being
bricked. Upon inspection, we found that many of these devices had external flash
corruption, which was creating a bricked device due to a corrupt data structure
in external flash which caused the filesystem to crash when booting.

Looking at some of the logs on these devices, we could see that before the flash
corruption occurred, the device was getting caught in a brown-out loop.
Reproducing this in the lab, we found that at low backup battery, during an LTE
transmission, the voltage of the battery would sag, the battery controller would
hit a low voltage cutoff, and the device would shut off. Once the device
shut-off, the LTE transmission would immediately stop, the voltage of the
battery would recover, and the battery controller would re-enable the battery.
Once the battery was re-enabled, the device would turn back on, where it would
attempt to write to flash on boot and simultaneously attempt an LTE
transmission, which would cause a brown-out, and we'd loop again. It would do
this thousands of times before the battery voltage was low enough that it would
stop recovering.

Because of this brown-out loop, we were stress testing our external flash power
cycle resilience, and needless to say, we found bugs. Unfortunately for us, our
hardware did not have a method of shutting itself off. This meant that, even if
we know the backup battery had insufficient power to power our device, we could
not shut-off the entire system.

As a workaround, we ended up putting a voltage detection circuit + loop at the
very start of our firmware. If the device was attempting to boot with a measured
voltage of < CUTOFF VOLTAGE and the device did not detect a second power source
(measured by a GPIO being pulled high), the device would sit in a
`while (!external_power_okay()) {pet_watchdog();}` style loop, keeping at least
external flash ok. We also upgraded our external flash filesystem to a version
that was much more resilient to boot loops.

After this story, I always look to see if a battery powered device can both: (1)
effectively monitor battery state of charge, and (2) shutdown in a low state of
charge condition to prevent these sort of brown-out loops.

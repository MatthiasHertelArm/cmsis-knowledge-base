---
id: "intr-a-schematic-review-checklist-for-f-story-2-reset-by-power-drain-story-2-res"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers: Story 2 - Reset By Power Drain {#story-2-reset}"
summary: "On that same project years back, we occasionally noticed the device would become unresponsive. While we had a watchdog, for some reason the watchdog was either not triggering, or not resetting enough state on the device."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist#story-2-reset-by-power-drain-story-2-reset"
license: "CC-BY-SA-4.0"
mode: "V"
---

On that same project years back, we occasionally noticed the device would become
unresponsive. While we had a watchdog, for some reason the watchdog was either
not triggering, or not resetting enough state on the device. Once we were able
to connect our debug tools (namely, a CAN dongle), we could send a reset command
the device, it would recover and work perfectly. However, we had missed
designing in from the beginning a mechanism to reset the device that was
accessible to our users.

Because we had a battery in the device, our instructions to our users were to
"set the device aside and wait for the battery to lose power." Unfortunately for
us, the bike stuck in this state was also in our lowest power mode and had no UX
difference between a bike with a dead battery. We instructed our users to let
bikes set for 4 days before they could recover. That's a pretty poor user
experience.

While we solved this in future releases by adding an NFC based reset, this is an
issue that can only be fixed going forward, and not in reverse. Adding a
physical way to reset the device for a human user from the beginning is a very
powerful solution. How many things are fixed by "turning it off and turning it
back on again"?

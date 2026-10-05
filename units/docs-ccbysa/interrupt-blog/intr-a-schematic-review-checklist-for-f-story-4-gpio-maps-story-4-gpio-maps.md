---
id: "intr-a-schematic-review-checklist-for-f-story-4-gpio-maps-story-4-gpio-maps"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers: Story 4: GPIO Maps {#story-4-gpio-maps}"
summary: "This is less of a war story and more of a shoutout to good electrical engineers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist#story-4-gpio-maps-story-4-gpio-maps"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is less of a war story and more of a shoutout to good electrical engineers.
Before walking into the schematic review for one project I was working on, the
EE on the project published a spreadsheet of all the GPIOs for the MCU. This
included their main function after reset, intended function, and any additional
notes. It made it very easy as a firmware engineer to scan the list of GPIOs and
ensure they were all configured properly. I'd recommend this is something that
all firmware engineers ask for when looking at a schematic.

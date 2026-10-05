---
id: "intr-smart-ring-development-part-2-hard-pcb-stackup"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: PCB stackup"
summary: "If we want to keep the smart ring as thin as possible (e.g., Oura Gen 4 is at 2.9mm), our PCB needs to be as thin as possible."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#pcb-stackup"
license: "CC-BY-SA-4.0"
mode: "V"
---

If we want to keep the smart ring as thin as possible (e.g., Oura Gen 4 is at
2.9mm), our PCB needs to be as thin as possible. The PCB will have to bend and
follow a ring shape, so we’re definitely looking at a flexible PCB. However, not
every component can be soldered onto a flexible PCB, and survive the stresses
caused by bending (think of all the BGAs), so it’s sensible to have a rigid
board as well.

That leaves us with a rigid-flex board, where parts of the PCB are flex and
others are rigid. The flex PCB stackup serves as the base, and the rigid part is
done by just sandwiching some more PCB layers on top of the flex. Flex PCBs can
be made very thin, which is a great advantage, and they generally support full
vias only. In the rigid part, these vias basically serve us as “free” buried
vias. After adding the rigid part, we can also have full thru vias, and we can
also get laser microvias (only from the outermost layer to the first next copper
layer).

The total stackup that would satisfy high-density component requirements is
shown below:
(figure: Open Ring PCB stackup)

The flex part has 0.22mm, and the flex-rigid part sits at 0.48mm. Thinking of
the component budget, if the aim is 2.9mm thickness, and assuming we need a
minimum of 0.2mm silicon outer layer, that leaves us at

of max component height on each side **if the components bent along the ring
curve**. Since they don't bend, we're working with some extremely tight spaces
here. Square chips in BGA and WLCP packages under 3mm width shouldn’t be a
problem, but some capacitors and inductors might get troublesome due to their
height, so we’ll be extra careful when selecting those. The general rule of
thumb is that we want to keep components as flat as possible, and put all tall
components in the middle of the rigid parts to **compensate for the ring
curvature.**

---
id: "intr-smart-ring-development-part-1-rese-prototype"
type: "concept"
domain: "debug"
title: "Smart Ring Development  (Part 1) － Research and Prototype: Prototype"
summary: "Having learned a ton from other products in the market, it was time to put together a plan for making our own Smart Ring. Our requirements were:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-06-13-smart-ring-development-part-1.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-1#prototype"
license: "CC-BY-SA-4.0"
mode: "V"
---

Having learned a ton from other products in the market, it was time to
put together a plan for making our own Smart Ring. Our requirements were:

- Normal-sized ring, similar to a typical wedding band (nothing bulky!)
- A touch pad for gestures
- Haptic feedback
- Induction charger
- Wear detection (for power saving)
- Lasting 2-3 days on a single charge with "normal" usage

The obvious problem was sizing. If space wasn't a concern, creating such a
product would be pretty easy, but fitting all of this inside a 2.6mm thick
curved band was the real challenge. Not to mention, fingers come in different
sizes, so we were looking at a product that comes in sizes from US 6 to US 13
(the standard for most population).

Without getting too deep (next article is about hardware design), we've built
some single board prototypes for each of the requirements. For the touch pad, we
settled on the Atmel SAM family as they came in WLCSP package and had mutual
capacitive sense technology, which was needed as the ring has no "real"
grounding (it's floating relative to the battery). The induction charging part
was quite easy as it was a simple flyback transformer with separated coils, with
each coil being on a PCB and an air gap between them rather than a ferrite core.

Haptic feedback turned out to be the trickiest of them all. We couldn't do a
piezoelectric haptic design like Amazon did, as we didn't have the funds to make
a fully custom solution, so we were looking for off the shelf components only.
Fortunately, we learned that coin vibration motors are made in very small sizes.
They require high startup current (>150mA), which can be solved by adding lots
of capacitance. Our final solution was a coin motor with enough capacitors to
make it vibrate for one single "buzz".

Fitting all these components in a Smart Ring factor seemed impossible until we
came up with a clever idea to 3D print all the PCB components from their STLs
and play with them like LEGO bricks to make it fit, which you can see in the
pictures below:

(figure: 3D printed components)

(figure: 3D printed ring housing)

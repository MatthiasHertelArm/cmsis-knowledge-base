---
id: "intr-smart-ring-development-part-2-hard-power-management"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: Power management"
summary: "A smart ring needs a battery, and a battery requires charging and battery management circuitry. Thankfully, integrated solutions exist that take care of both. One of them is Texas Instruments’ BQ2512x series (e.g."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#power-management"
license: "CC-BY-SA-4.0"
mode: "V"
---

A smart ring needs a battery, and a battery requires charging and battery
management circuitry. Thankfully, integrated solutions exist that take care of
both. One of them is Texas Instruments’ BQ2512x series (e.g.
[BQ25125](https://github.com/stawiski/open-ring/blob/main/docs-ring/battery-charger/bq25125.pdf)),
an intelligent battery charger with integrated DC/DC. This IC offers a couple of
really cool features:

- high efficiency (we do not want to waste power due to voltage conversion)
- safe battery charging with a temperature sensor
- shipping mode (equivalent to ultra-sleep mode to preserve the Li-Ion battery
  life during product shelf time)
- load switch controlled programmatically

The really cool feature that we want is the shipping mode, as we do not want the
Li-Ion battery to deplete and lose its full capacity, which is irreversible.
This battery depletion can happen not only during shipping or warehouse storage
when the ring is waiting for its new owner, but also if the customer stops
wearing the product for a while. If the battery depletes to very low levels
(close to 3V), we want to always enter the shipping mode for battery protection.
For this reason, our UX “0%” battery level needs to be mapped to a voltage
slightly higher than 3V, which is when irreversible battery damage starts
happening, to act as a safety margin.

The power management circuit can be paired up with a
[Grepow curved battery](https://www.grepow.com/shaped-battery/curved-battery.html),
perfect for electronics that wrap around the finger:
(figure: Open Ring Grepow curved battery)

[BQ25125](https://github.com/stawiski/open-ring/blob/main/docs-ring/battery-charger/bq25125.pdf)
will provide 1.8V for our system voltage, which will be used by all other ICs.
Dialog’s BLE chip will additionally make its own 1.1V rail.

With power circuitry resolved, we’re still left with charging the battery.

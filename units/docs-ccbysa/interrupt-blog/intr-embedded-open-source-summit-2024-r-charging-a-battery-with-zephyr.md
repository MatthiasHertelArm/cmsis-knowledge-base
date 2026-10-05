---
id: "intr-embedded-open-source-summit-2024-r-charging-a-battery-with-zephyr"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Charging a Battery with Zephyr"
summary: "The maintainer of the charger drivers API, Ricardo Rivera-Matos from Ciirus Logic, explains the role that a Zephyr host can play in controlling battery charging."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#charging-a-battery-with-zephyr"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=OAhP4c19FiQ&list=PLbzoR-pLrL6r63cNz4YY6OR7J-l7BShkY&index=3)
- Recommended by: Gilly

The maintainer of the charger drivers API, Ricardo Rivera-Matos from Ciirus
Logic, explains the role that a Zephyr host can play in controlling battery
charging. Notably, in enables setting the charge profile, setting protections
and limits for battery charging which could include limiting the maximum charge
percentage to improve battery life, and getting status info on charging. The
charger driver API was inspired by the Linux Power Supply Class, so for those
familiar with power management in Linux, the charger API should be familiar. We
also got a sneak peak at some of the improvements they want to make to the
charging API, including adding support for charger telemetry to observe a
charging session with ADCs, for example. This was a great talk that got me
wanting to try out this API!

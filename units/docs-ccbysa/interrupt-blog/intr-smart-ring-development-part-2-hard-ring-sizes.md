---
id: "intr-smart-ring-development-part-2-hard-ring-sizes"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: Ring sizes"
summary: "When it comes to user experience, it’s best to have a ring made per finger size. Most common ring sizes range from US6 to US13, which follows the general population’s ring finger distribution."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#ring-sizes"
license: "CC-BY-SA-4.0"
mode: "V"
---

When it comes to user experience, it’s best to have a ring made per finger size.
Most common ring sizes range from US6 to US13, which follows the general
population’s ring finger distribution. This means to accommodate the most
popular sizes, we need to make the product in 8 sizes (if that sounds like a
pain, then yes, it is)!

Another option that is significantly easier to manufacture and manage is to
group the sizes, often done in 3 discrete groups of S (small), M (medium), and L
(large).

It’s a common practice (same as you can see with smartphones) to put a bigger
battery in a larger ring, so with a greater ring size, the customer also gets
longer battery life.

The design around ring sizes needs to be based on the balance between
manufacturability and user experience. It will affect managing physical product
stock, the whole mechanical design, battery life, automated test equipment, and
other things.

(figure: Oura gen 3 sizing kit)

The way Open Ring was designed was to accommodate multiple ring sizes. The PCB
needs to be flat (component-free) at the part where the battery goes, so we
reuse that part for the touch sensor on the other side. This part can be cut to
different lengths as it exposes the copper pads to connect both the vibration
motor and the charging coil. This was a cheap way for us to support different
ring sizes; however, had the original product been a success, we would have made
a PCB for each ring size and embedded the charging coil directly into the main
ring PCB.

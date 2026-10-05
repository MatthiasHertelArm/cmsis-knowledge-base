---
id: "intr-smart-ring-development-part-1-rese-introduction"
type: "concept"
domain: "debug"
title: "Smart Ring Development  (Part 1) － Research and Prototype: Introduction"
summary: "In this first article, we'll look at the first typical stage of new product development for a hardware project － research and prototype. Let's first start with the idea, though."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-06-13-smart-ring-development-part-1.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-1#introduction"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this first article, we'll look at the first typical stage of new product
development for a hardware project － research and prototype. Let's first start
with the idea, though. In early 2020, my friend and I had an idea to build a
Smart Ring to control music. Back then, the only known Smart Ring was Oura, and
they were at their second generation, still off Kickstarter (after a very
successful first generation Kickstarter). It seemed the wearable market was
finally booming, and consumers were seeking new electronic gadgets. We thought
it would be really cool to build a Smart Ring that acts as a remote control for
music, offering typical functions like pause/play, volume up/down, and
next/previous track, all in a form that fits on the finger. The use case (not
particularly strong in hindsight, but more on that later) was to provide the
ability to control music at times when it's inconvenient to do so, such as when
cycling or at the gym (who wants to touch their phone with sweaty hands,
right?). Ultimately, the problem we were solving wasn't substantial enough from
a business standpoint, but we had a great deal of fun building this. Now this
work is released with open source hardware and firmware components as
[Open Ring on Github](https://github.com/stawiski/open-ring), and we hope it
will inspire others to build their own Smart Rings.

When starting a new project in a space that already has some products, it is a
natural course of action to thoroughly research existing products for
inspiration. In firmware and software development, this is even more pronounced;
we do not build anything from scratch but instead, try to use as many freely
available libraries as possible (provided the license allows). We don't want to
rewrite a JSON parsing library or a unit testing framework from the ground up:
who has time for that?

For hardware projects, things are not so straightforward. There are some
reusable components available (3D models, footprints, and schematic symbols),
but there are no fully functional modules to be found. Hardware is hard, after
all! It occupies physical space and has real-world constraints, and it is very
tightly coupled to the product.

Despite this, it is common in new product development (NPD) to tear down other
products to see how they work. While there were no "remote control" Smart Rings
on the market at that time, there were "other Smart Rings," and this family of
wearables had faced the same challenges we were about to encounter: how do you
fit all the necessary electronics in there?

(figure: A sneak peek of the Open Ring hardware!)

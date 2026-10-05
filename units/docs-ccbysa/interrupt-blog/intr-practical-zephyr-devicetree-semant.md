---
id: "intr-practical-zephyr-devicetree-semant"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4)"
summary: "Having covered the Devicetree basics in the previous article, we now add semantics to our Devicetree using so-called bindings: For each supported type, we'll create a corresponding binding and look at the generated output to understand how it …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics"
license: "CC-BY-SA-4.0"
mode: "V"
---

Having covered the *Devicetree basics* in the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_dt), we now add **semantics** to our *Devicetree* using so-called _bindings_: For each supported type, we'll create a corresponding _binding_ and look at the generated output to understand how it can be used with Zephyr's Devicetree API.



👉 Find the other parts of the *Practical Zephyr* series [here](https://interrupt.memfault.com/tags#practical-zephyr-series).

Notice that we'll only look at Zephyr's _basic_ Devicetree API and won't analyze specific subsystems such as `gpio` in detail. We're saving this for a practice round in the next article of this _Practical Zephyr_ series.

> 🎬
> [Listen to Martin on Interrupt Live](https://www.youtube.com/watch?v=ls_Y45WsTiA?feature=share)
> talk about the content and motivations behind writing this series.

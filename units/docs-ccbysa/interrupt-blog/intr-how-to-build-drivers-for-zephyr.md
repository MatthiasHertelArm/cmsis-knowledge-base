---
id: "intr-how-to-build-drivers-for-zephyr"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr"
summary: "If you've heard the news about the nRF9160 then you know it's a game-changer. ARM Cortex M33 + LTE Cat-M + NB-IoT and GPS all included under one System in Package. Drool-worthy, right?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you've heard the news about the nRF9160 then you know it's a game-changer. ARM Cortex M33 + LTE Cat-M + NB-IoT and GPS all included under one System in Package. Drool-worthy, right?

Well, if you've been using the nRF SDK to build nRF5x projects, you likely feel like you're hanging from your toes. That's because Nordic has chosen to adopt Zephyr as their RTOS of choice for the nRF9160.

Although there is [plenty of documentation about Zephyr](https://docs.zephyrproject.org/latest/), making the transition can still be tough. Many nRF SDK enthusiasts will find themselves lost in a sea of CMake files and Kconfigs. I'm here to help with that!

This is the guide I wish existed while I was developing some drivers for the [nRF9160 Feather][nrf9160-feather]. I spent weeks getting accustomed to how Zephyr worked, figuring out what files needed to be where, and how the heck to include a header file. (Fun times.)


In this post, I’ll go over some of the nuances related to creating drivers for your peripherals on Zephyr. We’ll talk about Device Tree organization, `Kconfig`, and `CMakeLists.txt` files. By the end, you should have an idea on how to tackle your own Zephyr driver aspirations!

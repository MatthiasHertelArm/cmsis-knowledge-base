---
id: "intr-zephyr-deep-dive-ring-buffers"
type: "concept"
domain: "debug"
title: "Zephyr Deep Dive: Ring Buffers"
summary: "Zephyr includes many built-in features like stacks for networking and BLE, Flash storage APIs, and many kernel services. These components allow you to quickly get up and running with a project and maintain less code!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-24-zephyr-ring-buffers.md"
doc_source: "https://interrupt.memfault.com/blog/zephyr-ring-buffers"
license: "CC-BY-SA-4.0"
mode: "V"
---

Zephyr includes many built-in features like stacks for networking and BLE, Flash
storage APIs, and many kernel services. These components allow you to quickly
get up and running with a project and maintain less code! Taking advantage of
these is a huge win for small firmware teams and was a huge motivation in
bringing Zephyr to my teams.



This post covers Zephyr's built-in ring buffer API, a component
commonly used in producer-consumer scenarios. We will cover how ring buffers
in Zephyr work, when to use them, and their strengths and weaknesses. This post
will close with an example of augmenting ring buffers with waiting capabilities.

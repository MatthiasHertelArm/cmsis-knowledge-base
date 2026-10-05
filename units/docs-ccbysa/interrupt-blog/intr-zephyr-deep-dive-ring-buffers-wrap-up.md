---
id: "intr-zephyr-deep-dive-ring-buffers-wrap-up"
type: "concept"
domain: "debug"
title: "Zephyr Deep Dive: Ring Buffers: Wrap-Up"
summary: "Zephyr has a variety of components that we can combine to suit practically anything your device requires. The hard part can be knowing where and what to start with."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-24-zephyr-ring-buffers.md"
doc_source: "https://interrupt.memfault.com/blog/zephyr-ring-buffers#wrap-up"
license: "CC-BY-SA-4.0"
mode: "V"
---

Zephyr has a variety of components that we can combine to suit practically
anything your device requires. The hard part can be knowing where and what to
start with. As we have covered in this post, ring buffers shine when used to
implement single producer single consumer designs. The ring buffer design
introduces little overhead and is efficient in reading and writing through the
use of its internal buffer and indices. The data structure is flexible in
multiple ways. It allows for a variable length of data operations. It offers
multiple data passing methods, whether through direct copy or referencing the
internal buffer. Finally, its API offers either an unstructured bytes-oriented
API or a more structured items API geared toward messages.

This post touches on just one of the many features provided out of the box by
Zephyr. Future posts in this series will examine its other offerings such as
data passing with FIFOs and mailboxes, memory management with slabs and pools,
and subsystems like RTIO and zbus. Please feel free to leave feedback, comments,
and Zephyr topic suggestions below!







{:.no_toc}

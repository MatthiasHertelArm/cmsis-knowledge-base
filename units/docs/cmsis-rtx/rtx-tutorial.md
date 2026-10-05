---
id: "rtx-tutorial"
type: "concept"
domain: "rtos"
title: "tutorial"
summary: "This tutorial is an introduction to using a small footprint real-time operating system on an Arm Cortex-M microcontroller."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md"
license: "Apache-2.0"
mode: "V"
---

﻿# Tutorial

This tutorial is an introduction to using a small footprint real-time operating system on an Arm Cortex-M microcontroller.

If you are used to writing procedural-based 'C' code on small 8-/16-bit microcontrollers, you may be doubtful about the need for such an operating system. If you are not familiar with using an RTOS in real-time embedded systems, you should read this chapter before dismissing the idea. The use of an RTOS represents a more sophisticated design approach, inherently fostering structured code development which is enforced by the RTOS application programming interface (API).

The RTOS structure allows you to take a more object-orientated design approach, while still programming in 'C'. The RTOS also provides you with multithreaded support on a small microcontroller. These two features actually create quite a shift in design philosophy, moving us away from thinking about procedural ‘C’ code and flow charts. Instead we consider the fundamental program threads and the flow of data between them. The use of an RTOS also has several additional benefits which may not be immediately obvious. Since an RTOS based project is composed of well-defined threads, it helps to improve project management, code reuse, and software testing.

The tradeoff for this is that an RTOS has additional memory requirements and increased interrupt latency. Typically, the Keil RTX5 RTOS will require 500 bytes of RAM and 5k bytes of code, but remember that some of the RTOS code would be replicated in your program anyway. We now have a generation of small low-cost microcontrollers that have enough on-chip memory and processing power to support the use of an RTOS. Developing using this approach is therefore much more accessible.

We will first look at setting up an introductory RTOS project for a Cortex-M based microcontroller. Next, we
will go through each of the RTOS primitives and how they influence the design of our application code. Finally, when we have a clear understanding of the RTOS features, we will take a closer look at the RTOS configuration options. If you are used to programming a microcontroller without using an RTOS i.e. bare metal, there are two key things to understand as you work through this tutorial. In the first section, we will focus on creating and managing Threads. The key concept here is to consider them running as parallel concurrent objects. In the second section, we will look at how to communicate between threads. In this section the key concept is synchronization of the concurrent threads.

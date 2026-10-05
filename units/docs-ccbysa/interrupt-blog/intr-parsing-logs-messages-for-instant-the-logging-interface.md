---
id: "intr-parsing-logs-messages-for-instant-the-logging-interface"
type: "concept"
domain: "debug"
title: "Parsing Logs Messages for Instant Crash Analysis: 📰 The Logging Interface"
summary: "Logging was historically done using the UART peripheral on the microcontroller."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-08-04-firmware-logs-stack-trace.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-logs-stack-trace#the-logging-interface"
license: "CC-BY-SA-4.0"
mode: "V"
---

Logging was historically done using the UART peripheral on the microcontroller. One could also use semihosting but it is more and more common to see Segger's RTT (Real-Time Transfer) being used as it is very efficient: it doesn't affect real-time behavior. I am still using the serial interface for some projects because using RTT requires to connect the debugger, which I don't do every time. Moreover, the RTT Client used to be a bit buggy. I hope that's not the case anymore and I should probably consider using RTT more than I do. In the last few years, I have been using RTT only to debug the bootloader on several targets. 🙄

In order to implement stack unbundling from the terminal client, we need to receive and parse the received characters. In the scope of this article, we are going to use the serial interface to make it easy to implement and focus on the important parts.

We could implement stack tracing from an RTT Client but it might be more interesting to have GDB connected if your debugger is attached anyway. For a good starting point, we have you covered[^debug_fault]

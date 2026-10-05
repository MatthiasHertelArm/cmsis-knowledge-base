---
id: "intr-lte-and-iot-how-we-got-here"
type: "concept"
domain: "debug"
title: "LTE and IoT - How We Got Here"
summary: "Cellular devices and networks have come a long way, from brick phones and Blackberrys to iPhones and Google Pixels."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-12-13-lte-and-iot.md"
doc_source: "https://interrupt.memfault.com/blog/lte-and-iot"
license: "CC-BY-SA-4.0"
mode: "V"
---

Cellular devices and networks have come a long way, from brick phones and Blackberrys to iPhones and Google Pixels. In addition to being the ubiquitous connectivity protocol that keeps the Internet at our fingertips at all times, LTE is appearing in IoT products across all industries. LTE modems now boast reduced power consumption and a more compact form factor than ever; coupled with the promises of 5G technology's support for millions more connected devices, there is no doubt that this is an exciting time to be working on an LTE-enabled device!

Lately, I have been learning everything I can about LTE as it pertains to IoT systems, starting from the ground up. I had to start from scratch because this recent dive was my first real foray into cellular technology. I began with dumping acronym definitions in a doc (UE, GSM, LPWAN, E-UTRAN, PTW, MNO — there are so many! 😱) until I realized that weaving these together into a cohesive story would help me and perhaps some readers too.



In this article, I describe some of my findings from a recent investigation of how LTE technology was built for IoT systems. Complete with some history
and a few diagrams to illustrate cellular network architecture and LTE power-saving features like eDRX and PSM, this read will give a nice introduction to LTE in embedded systems.







---

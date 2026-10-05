---
id: "intr-embedded-open-source-summit-2024-r-enabling-real-time-secure-connectivity-t"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Enabling Real-Time Secure Connectivity to the Industrial Edge with Single-Pair Ethernet and Zephyr"
summary: "Jason Murphy from Analog Devices discussed the usage of Zephyr on the industrial edge using support for 10BASE T1L Single-Pair Ethernet."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#enabling-real-time-secure-connectivity-to-the-industrial-edge-with-single-pair-e"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=krhiEAjwcvs&list=PLbzoR-pLrL6r63cNz4YY6OR7J-l7BShkY&index=21)
- Recommended by: Gilly

Jason Murphy from Analog Devices discussed the usage of Zephyr on the industrial
edge using support for 10BASE T1L Single-Pair Ethernet. He explained how Zephyr
is great for industrial edge applications because of its native TCP/IP
networking stack supporting Ethernet protocols and low-latency networking, among
the well-known benefits like portability and community support. He also walks
through the board configuration (devicetree and Kconfigs) to use the ethernet
drivers and board support for the ADI eval boards for 10BASE T1L. I liked
learning about this option for wired applications using Zephyr since most of the
conversation in IoT is around wireless protocols!

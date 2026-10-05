---
id: "txmw-chapter-1-introduction-to-netx-duo-ixanvl-test"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to NetX Duo: IxANVL Test"
summary: "NetX Duo is tested with IxANVL from IXIA. IxANVL is the industry standard for automated network and protocol validation. More information about IxANVL can be found at: https://www.ixiacom.com/products/ixanvl"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter1.md#ixanvl-test"
license: "MIT"
mode: "V"
---

NetX Duo is tested with IxANVL from IXIA. IxANVL is the industry standard for automated network and protocol validation. More information about IxANVL can be found at: [**https://www.ixiacom.com/products/ixanvl**](https://www.ipv6ready.org/)

In particular the following NetX Duo modules are tested with IxANVL:

| **Module**      | **Standard**                                                      |
| --------------- | ----------------------------------------------------------------- |
| IP              | RFC791 `</br>` RFC1122 `</br>` RFC894                                 |
| ICMP            | RFC792 `</br>` RFC1122 `</br>` RFC1812                                |
| UDP             | RFC768 `</br>` RFC1122                                              |
| TCP-Core        | RFC793 `</br>` RFC1122 `</br>` RFC2460                                |
| TCP-Advanced    | RFC1981</br>RFC2001</br>RFC2385</br>RFC2463</br>RFC813</br>RFC896 |
| TCP-Performance | RFC793</br>RFC1323</br>RFC2018                                    |

---
id: "mbedtls-mbed-tls-tutorial-the-stack"
type: "concept"
domain: "security"
title: "Mbed TLS tutorial: The stack"
summary: "The aim of this tutorial is to show you how to secure your client and server communication with Mbed TLS. The following major components are involved:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/mbedtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/mbedtls-tutorial.md#the-stack"
license: "Apache-2.0"
mode: "V"
---

The aim of this tutorial is to show you how to secure your client and server communication with Mbed TLS. The following major components  are involved:

(figure: Mbed TLS Stack.png)

From the bottom up:

**Hardware**

The hardware platform provides the physical processor, storage, memory and network interface.

**Operating system**

The operating system provides the Ethernet driver and standard services. Depending on the OS, this includes scheduling, thread-safety and a full network stack.

**Network stack**

Depending on the operating system, the network stack is either fully integrated or is a separate module that provides an abstraction layer from the network interface. The most commonly used are the [lwIP TCP/IP stack](http://savannah.nongnu.org/projects/lwip/) and the [uIP TCP/IP stack](https://en.wikipedia.org/wiki/UIP_(software)).

**Mbed TLS SSL/TLS library**

Building on top of the network interface, Mbed TLS provides an abstraction layer for secure communication.

**Client application**

The client application uses Mbed TLS to abstract the secure communication from itself.

The steps to integrate Mbed TLS in your application are very dependent on the specific components used above. In this basic tutorial, we assume an operating system with integrated BSD-like TCP/IP stack.

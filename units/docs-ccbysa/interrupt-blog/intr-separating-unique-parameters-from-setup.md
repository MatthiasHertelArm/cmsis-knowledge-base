---
id: "intr-separating-unique-parameters-from-setup"
type: "concept"
domain: "debug"
title: "Separating Unique Parameters from Firmware Binaries: Setup"
summary: "Before we get started let's write down our requirements and describe our setup."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-10-06-separating-unique-parameters.md"
doc_source: "https://interrupt.memfault.com/blog/separating-unique-parameters#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before we get started let's write down our requirements and describe our setup.

### Requirements

Our goal is simple:
1. We want a general method to separately load firmware and unique parameters.
   onto devices
2. We want to keep the number of programming steps to a minimum and rely on
   widely available tools.
3. We want to use off the shelf tools such as Make, Python, and shell scripts
   rather than build a custom solution.

### Hardware and Software

This blog post was written using a SAMR35-based LoRaWAN node.

LoRaWAN relies on a few device parameters that have to be unique:
1. the DevEUI (unique device ID)
2. the AppEUI (unique application ID)
3. the AppKey (encryption key used during activation)

 The LoRa nodes for this example are connected to [The Things
Network](https://www.thethingsnetwork.org/) (a.k.a. "TTN"), which has a CLI that we can
use to get the parameters and register new devices.

All of our firmware is written in C and compiled with GCC. We use J-Link
Commander for programming, and a `Makefile` with some bash scripts for
automation.

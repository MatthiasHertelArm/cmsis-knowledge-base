---
id: "view-fault-example-for-b-u585i-iot02a-b-user-interface"
type: "concept"
domain: "trace"
title: "Fault example for B-U585I-IOT02A board (Cortex-M33): User Interface"
summary: "This example uses Serial Terminal for User Interface."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Examples/Fault/B-U585I-IOT02A/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Examples/Fault/B-U585I-IOT02A/README.md#user-interface"
license: "Apache-2.0"
mode: "V"
---

This example uses **Serial Terminal** for User Interface.

The fault triggering is done by entering a number via **Serial Terminal** application, see possible values below:

- `1` : trigger the Non-Secure fault, Non-Secure data access Memory Management fault
- `2` : trigger the Non-Secure fault, Non-Secure data access Bus fault
- `3` : trigger the Non-Secure fault, Non-Secure undefined instruction Usage fault
- `4` : trigger the Non-Secure fault, Non-Secure divide by 0 Usage fault
- `5` : trigger the Secure fault, Non-Secure data access from Secure RAM memory
- `6` : trigger the Secure fault, Non-Secure instruction execution from Secure Flash memory
- `7` : trigger the Secure fault, Secure undefined instruction Usage fault

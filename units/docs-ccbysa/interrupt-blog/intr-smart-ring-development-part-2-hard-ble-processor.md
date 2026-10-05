---
id: "intr-smart-ring-development-part-2-hard-ble-processor"
type: "concept"
domain: "debug"
title: "Smart Ring Development (Part 2) － Hardware Design: BLE processor"
summary: "The heart of the smart ring, and the centre of communication with the outside world, will be the BLE MCU you choose."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-07-10-smart-ring-development-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-2#ble-processor"
license: "CC-BY-SA-4.0"
mode: "V"
---

The heart of the smart ring, and the centre of communication with the outside
world, will be the BLE MCU you choose. Even with Low Energy in the BLE acronym,
Bluetooth communication can still take up a significant part of your energy
budget, depending on the application. Health tracking smart rings, such as Oura,
can generally store measurements and sync them later, reducing this worry.
However, if the solution needs to perform an action in real time (such as
gestures on the ring controlling music on the phone), the BLE needs to be always
ready to send requests through. Fortunately, many of the BLE SoCs have advanced
sleep capabilities, allowing a solution to achieve this in a smart way with
minimal power usage.

We’ve settled on Dialog’s
[DA14531](https://www.renesas.com/en/products/wireless-connectivity/bluetooth-low-energy/da14531-smartbond-tiny-ultra-low-power-bluetooth-51-system-chip).
It was ahead of its time due to very low cost at high quantities, very clean
SDK, and very high efficiency of BLE transmission. It didn’t come with
all-advantages though. This chip has the old school one-time-programmable memory
for bootloader (you can’t go wrong programming that), external FLASH requiring a
separate chip on board, and it generally runs code from system RAM, which is
limiting. Another great option that was considered was Nordic MCUs such as
[nRF52805](https://www.nordicsemi.com/Products/nRF52805) in a 2.5x2.5mm WLCSP
package. Generally, it’s better to get more FLASH and RAM and not worry about
the firmware upgrades (as well as security updates, which in the BLE world are
common).

(figure: Dialog DA14531)

An important consideration around the BLE chip is the crystal. A typical BLE
crystal will be 32MHz, and it will provide the base for the high-frequency radio
signal. Care must be taken when selecting such a crystal, as due to aging, the
frequency of the crystal can shift and render the product useless. Dialog’s
recommendation around this is 10ppm base frequency tolerance and only 2ppm aging
per year. Such crystals will often be marked as “BLE application”. You can find
datasheets of crystals that adhere to this requirement
[here](https://github.com/stawiski/open-ring/tree/main/docs-ring/bluetooth-crystal).
Notably, the one we ultimately chose was Abracon's ABM12W (low height and
RoHS-compliant BLE crystal).

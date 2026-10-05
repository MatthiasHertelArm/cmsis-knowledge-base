---
id: "zepb-nrf52840dk-nrf52811-emulation-on-nrf52840-dk"
type: "concept"
domain: "bring-up"
title: "nrf52840dk: nRF52811 emulation on nRF52840 DK"
summary: "The nrf52840dk/nrf52811 board variant is a modified version of the nrf52840dk that enforces the limitations imposed by the nRF52811 IC, which is a variant of the original nRF52840."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nordic/nrf52840dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52811-emulation-on-nrf52840-dk"
license: "Apache-2.0"
mode: "V"
---

The `nrf52840dk/nrf52811` board variant is a modified version of the
nrf52840dk that enforces the limitations imposed by the nRF52811
IC, which is a variant of the original nRF52840. Since Nordic does not offer a
development kit for the nRF52811 you can use this board to develop for this IC
while using the nRF52840 Development Kit (PCA10056).

See nRF52811 website for the official reference on the IC itself.

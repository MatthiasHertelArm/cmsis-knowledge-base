---
id: "zep-babblesim-babblesim-and-zephyr"
type: "concept"
domain: "test"
title: "BabbleSim: BabbleSim and Zephyr"
summary: "In the Zephyr project we use the Babblesim simulator to test some of the Zephyr radio protocols, including the Bluetooth LE stack, 802.15.4, and some of the networking stack."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/bsim.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/bsim.rst"
license: "Apache-2.0"
mode: "V"
---

In the Zephyr project we use the Babblesim simulator to test some of the Zephyr radio protocols,
including the Bluetooth LE stack, 802.15.4, and some of the networking stack.

BabbleSim_ is a physical layer simulator, which in combination with the Zephyr
bsim boards
can be used to simulate a network of Bluetooth LE and 15.4 devices.
When we build Zephyr targeting a bsim board we produce a Linux
executable, which includes the application, Zephyr OS, and models of the HW.

When there is radio activity, this Linux executable will connect to the BabbleSim Phy simulation
to simulate the radio channel.

In the BabbleSim documentation you can find more information on how to
[get](https://babblesim.github.io/fetching.html) and
[build](https://babblesim.github.io/building.html) the simulator.
In the nrf52_bsim, nrf5340bsim,
and nrf54l15bsim boards documentation
you can find more information about how to build Zephyr targeting these particular boards,
and a few examples.

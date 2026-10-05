---
id: "intr-lte-and-iot-how-we-got-here-low-power-technologies"
type: "concept"
domain: "debug"
title: "LTE and IoT - How We Got Here: Low-power Technologies"
summary: "LTE-M and NB-IoT are the two primary cellular-based LPWAN standards. LTE-M, an abbreviation for LTE-MTC (Machine Type Communication), is more expensive but is better for devices requiring higher data rates."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-12-13-lte-and-iot.md"
doc_source: "https://interrupt.memfault.com/blog/lte-and-iot#low-power-technologies"
license: "CC-BY-SA-4.0"
mode: "V"
---

LTE-M and NB-IoT are the two primary cellular-based LPWAN standards. LTE-M, an abbreviation for LTE-MTC (Machine Type Communication), is more expensive but is better for devices requiring higher data rates. While differing in the environments and applications they are used in, they both support two modes that enable low-power behavior: eDRX (extended Discontinuous Reception) and PSM (Power Save Mode). They can be used together since they manage different parts of a cellular connection.

The power savings of these modes rely on two key factors:

- Being able to maintain "attached" to the network. Attaching is a very high-power procedure
- Being able to switch off the radio while in sleep or idle states. Turning on the radio is also high power

This first point about network attachment is key and explains why simply turning off the modem can hurt a device's power budget.

To stay attached to the network, a UE enters **RRC Idle** mode, during which the device listens for paging updates from the eNB (eDRX mode), and/or turns the radio completely off before waking up to give the eNB a tracking area update (PSM TAU value). After it wakes up, it enters **RRC Connected** mode, and UL and DL data are sent to/from the eNB. While learning about these power save modes, I put together a diagram to keep track of the relative power consumption of each, as well as the changes in the radio and RRC states (a lot is going on!).



  


### eDRX

DRX is a mode that allows more fine-tuning of the intervals at which a device switches from unreachable to reachable. eDRx enables longer **DRX cycle length** (sleep time), which is crucial for IoT systems that prioritize power savings over constant connectivity. In regular DRX, sleep time is only around 2.5 seconds whereas eDRX can be up to 43 minutes [^6]. During this interval, the UE is not reachable by the network. The **Paging Time Window** (PTW) is the period when the UE is reachable by the network and when it can communicate with the network.

Modems in eDRX tend to have a current draw in deep sleep on the order of 10-30 µA. I have recently been working with Nordic's nRF9160 modem, so I will use figures from that data sheet as an example for comparing current draw and wake-up times. The nRF91 modem's current draw during sleep with an eDRX interval at 82.91s at 3.7 V is 8 µA for LTE-M and 37 µA for NB-IoT [^7]. For both standards, the nRF91 takes about 1 ms to wake up and start receiving data [^8].

Some cellular modems allow you to set both the PTW and eDRX Cycle, but some modems only allow you to set the eDRX cycle. You will need to study the AT Commands manual from your cellular modem vendor to find out what applies to your modem.

### PSM

PSM requires very little power compared to eDRX. The device remains registered in the network, but the radio is off, therefore it does not transmit or receive data and cannot be reached from the outside. However, for a device to stay connected to the network, it must wake up periodically to update the network on its location. This interval is called the **Periodic TAU**, during which the UE will stay in power-saving mode before waking up to send a Tracking Area Update (TAU) to the network.

Modems in PSM have a current draw on the order of a few microamps. The nRF91 modem's current draw during sleep is about 2.7 µA at 3.7 V for both standards. The modem takes ~100-200 ms to wake up and receive data, a marked increase from waking up from eDRX.

PSM is a good option for systems that can tolerate higher latency and have stricter power requirements because it has a lower power draw in its deep sleep mode. However, it will not respond for the duration of its sleep, and it takes longer to get out of that sleep mode. For systems that need more frequent check-ins with the network but need more power savings than leaving the modem in the regular RRC Connected state, eDRX is the better option because it checks for data from the network more frequently and connects to the network faster coming out of sleep.

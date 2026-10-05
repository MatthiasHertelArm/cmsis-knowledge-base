---
id: "intr-lte-and-iot-how-we-got-here-cells-ues-and-enbs"
type: "concept"
domain: "debug"
title: "LTE and IoT - How We Got Here: Cells, UEs, and eNBs"
summary: "The word cell in cellular and cell phone comes from the network architecture -- a fact which I vaguely understood before but did not fully comprehend."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-12-13-lte-and-iot.md"
doc_source: "https://interrupt.memfault.com/blog/lte-and-iot#cells-ues-and-enbs"
license: "CC-BY-SA-4.0"
mode: "V"
---

The word cell in cellular and cell phone comes from the network architecture -- a fact which I vaguely understood before but did not fully comprehend. Cellular networks are composed of cells organized in a hexagonal pattern covering a geographic area. At the center of a cell is a base station with a transceiver, which provides network coverage to a cell. In other words, a cell is the coverage area of a base station.



  


In LTE networks, a cellular-enabled device called the **User Equipment (UE)** connects to a base station called the **evolved Node B (eNB)**. The signal traveling to the eNB is the **Uplink (UL)** signal, while the signal traveling to the UE is the **Downlink (DL)** signal. The UE, eNB, and E-UTRA (Evolved UMTS Terrestrial Radio Access), the wireless communication technology used in LTE networks, all make up what is called the E-UTRAN (Evolved UMTS Terrestrial Radio Access Network). This network is distinct from another entity, the Evolved Packet Core (EPC), which connects the radio access network to the Internet. Radio Resource Control (RRC) is the physical layer protocol of the E-UTRAN, and is used for communication between the UE and eNB. Two RRC states, idle and connected, will play a role in power save modes.



  


> Why hexagons? 🤔  While coverage from the transceiver's radio is circular, dividing up an area via circles would result in overlapping areas, so the abstraction of another shape is needed to represent coverage better and optimize for fewer base stations when laying out stations. To minimize the number of base stations, the shape chosen should maximize the area of the base station it is centered around. Of all the basic shapes, Hexagons take up the greatest percentage of a circle. Note there is still overlapping in regions where signals from two neighboring cells are available. Still, the area of these overlapping regions is smallest when using hexagons to organize stations.

---
id: "intr-lte-and-iot-how-we-got-here-a-brief-history"
type: "concept"
domain: "debug"
title: "LTE and IoT - How We Got Here: A Brief History"
summary: "To understand LTE, the standard backing 4G cellular networks, I wanted to understand some context around how the technology developed."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-12-13-lte-and-iot.md"
doc_source: "https://interrupt.memfault.com/blog/lte-and-iot#a-brief-history"
license: "CC-BY-SA-4.0"
mode: "V"
---

To understand LTE, the standard backing 4G cellular networks, I wanted to understand some context around how the technology developed. Before LTE, cellular networks went through several evolutions, and I have captured roughly where each evolution falls in terms of data rates in the image below.



  


>I had to bunch up the scale on the Y-axis to squeeze in 4G and 5G because the downlink speeds jumped so significantly! The standards relevant to today's technology map to 3GPP releases starting with release 8. Those release specifications are available on [3PGG's portal](https://portal.3gpp.org/#/55936-specifications) under the Specifications tab. A convenient link to all the 3GPP documents in the 36 series (the series on LTE) is available [here](https://www.3gpp.org/dynareport?code=36-series.htm), which is where I have been spending some quality time.

The first cellular network was launched in the 80s with just analog voice — no data. Then came the move to digital voice in the 90s, and a new network was created based on the GSM standard, which was labeled the 2G network, and its predecessor, the 1G. Data services also became available, enabling SMS text messaging and later, SMS's extension, MMS, which enabled sending pictures, video, and audio. The first "high speed" mobile network arrived with the 3G network in the early 2000s, which was based on the UMTS standard and had rates around 2 Mbps.

IoT products started leveraging cellular networks for connectivity with the introduction of 2G and 3G data services. 2G and 3G provided an opportunity for devices with low bandwidth requirements; with 3G technology, transmitting too much data incurred a power cost that did not support the widespread use of battery-powered IoT devices with higher data requirements, like the advanced asset tracking applications we see today.

A different technology was necessary to support demands for increased data consumption by low-power IoT devices. Furthermore, the nature of IoT communication was fundamentally different than human-generated traffic; data packets are shorter, delays are acceptable, most traffic is uplink, and a massive amount of devices connect to a single station [^1].

Enter LPWANs ([Low Power Wide Area Networks](https://www.testxchange.com/magazine/lpwa-low-power-wide-area/)), which use lower power communication protocols than traditional cellular connections. The major non-cellular-based technologies are Sigfox and LoRaWAN, which operate in unlicensed frequency bands [^2]. Sigfox started the development of LPWANs in 2010 [^3], two years after 3GPP (3rd Generation Partnership Project), an umbrella term for the organizations that develop mobile telecoms standards, launched the 4G network, which leverages the LTE (Long-Term Evolution) standard. 3GPP responded to the competing LPWANs and the market demand in 2013 with the development of LTE-based LPWAN technologies: LTE-M and NB-IoT.

An alternative standard that could work for some IoT applications, LTE Cat 1, is the first or lowest category of LTE with a throughput cap of 10 Mpbs for download and 5 Mpbs for upload and reasonably low power consumption [^4]. The advantage of LTE Cat 1 over LTE-M and NB-IoT is that it uses the same standard as LTE while LTE-M and NB-IoT are different standards. As a result, LTE-M and NB-IoT require new technology in networks that support them, and the rollout has been slower than expected. A regularly updated map is available [here](https://www.gsma.com/iot/deployment-map/) from GSMA depicting the coverage of LTE-M and NB-IoT worldwide; some countries only support one of the two. Finally, for some context on how LTE technologies like LTE-M and NB-IoT stack up in range, max data rate, and relative power consumption compared to other popular IoT connectivity protocols, below is a table from Saft Batteries [^5] that gives a nice summary.



  


Before zooming in on how LTE-M and NB-IoT work, let us first zoom out and take a look at how networks are structured.

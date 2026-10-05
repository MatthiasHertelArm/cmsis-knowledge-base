---
id: "ethu-general"
type: "concept"
domain: "edge-ai"
title: "General"
summary: "This documentation is organized as follows:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/general/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/general/src/main.md"
license: "Apache-2.0"
mode: "V"
---

This documentation is organized as follows:

- This chapter introduces the terminology, architecture, and deployment flow for
  ML models on an Edge AI MCU.
- Vela explains how to install and use the Vela compiler,
  obtain or create an Ethos-U configuration, create matching linker and driver
  configurations, and publish the configuration in a DFP.
- Driver describes the low-level Ethos-U driver API,
  execution contract, platform hooks, and bring-up checks.
- Integration explains how to keep the compiled ML
  model, memory placement, driver settings, and application consistent, and how
  to budget, validate, and tune the complete system.
- Zephyr explains how to configure, build, and run an
  Ethos-U-accelerated Zephyr application.

---
id: "zepb-ensemble-e8-ak-overview"
type: "concept"
domain: "bring-up"
title: "ensemble_e8_ak: Overview"
summary: "The Alif Ensemble E8 AI/ML AppKit is a development platform built around the CSP-packaged AE822FA0E5597BS0 device from the Alif Ensemble E8 series, targeted at artificial intelligence and machine learning applications."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/alif/ensemble_e8_ak/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/alif/ensemble_e8_ak/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The Alif Ensemble E8 AI/ML AppKit is a development platform built around the
CSP-packaged AE822FA0E5597BS0 device from the Alif Ensemble E8 series, targeted
at artificial intelligence and machine learning applications.

The Ensemble family of devices contain multiple CPU clusters: up to two
Cortex-M55 based Real Time SubSystems (RTSS), and a Cortex-A32 based
Application Processor SubSystem (APSS).

* **RTSS-HP** (High Performance): Cortex-M55 running at up to 400 MHz
* **RTSS-HE** (High Efficiency): Cortex-M55 running at up to 160 MHz
* **APSS** (Application Processor SubSystem): Cortex-A32 running at up to 800 MHz


### Board Identifiers


The following board identifiers are supported:

+----------------------------------------------+-------------+----------+
| Board Identifier                             | SoC Series  | Core     |
+==============================================+=============+==========+
| `ensemble_e8_ak/ae822fa0e5597bs0/rtss_he`  | E8          | RTSS-HE  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_ak/ae822fa0e5597bs0/rtss_hp`  | E8          | RTSS-HP  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_ak/ae822fa0e5597bs0/apss`     | E8          | APSS     |
+----------------------------------------------+-------------+----------+

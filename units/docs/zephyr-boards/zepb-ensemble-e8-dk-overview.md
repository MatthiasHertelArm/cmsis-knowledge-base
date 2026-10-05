---
id: "zepb-ensemble-e8-dk-overview"
type: "concept"
domain: "bring-up"
title: "ensemble_e8_dk: Overview"
summary: "The Alif Ensemble E8 Development Kit is a single-board development platform that can be configured to operate with the E4, E6, or E8 series devices in the Alif Ensemble family."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/alif/ensemble_e8_dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/alif/ensemble_e8_dk/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The Alif Ensemble E8 Development Kit is a single-board development
platform that can be configured to operate with the E4, E6, or E8 series devices
in the Alif Ensemble family.

The Ensemble family of devices can contain multiple CPU clusters: up to two
Cortex-M55 based Real Time SubSystems (RTSS), and on some devices a Cortex-A32
based Application Processor SubSystem (APSS).

* **RTSS-HP** (High Performance): Cortex-M55 running at up to 400 MHz
* **RTSS-HE** (High Efficiency): Cortex-M55 running at up to 160 MHz
* **APSS** (Application Processor SubSystem): Cortex-A32 running at up to 800 MHz


### Board Identifiers


The following board identifiers are supported:

+----------------------------------------------+-------------+----------+
| Board Identifier                             | SoC Series  | Core     |
+==============================================+=============+==========+
| `ensemble_e8_dk/ae402fa0e5597le0/rtss_he`  | E4          | RTSS-HE  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_dk/ae402fa0e5597le0/rtss_hp`  | E4          | RTSS-HP  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_dk/ae612fa0e5597ls0/rtss_he`  | E6          | RTSS-HE  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_dk/ae612fa0e5597ls0/rtss_hp`  | E6          | RTSS-HP  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_dk/ae822fa0e5597ls0/rtss_he`  | E8          | RTSS-HE  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_dk/ae822fa0e5597ls0/rtss_hp`  | E8          | RTSS-HP  |
+----------------------------------------------+-------------+----------+
| `ensemble_e8_dk/ae822fa0e5597ls0/apss`     | E8          | APSS     |
+----------------------------------------------+-------------+----------+

More information about the board can be found at the
Ensemble E8 DevKit Product Page.

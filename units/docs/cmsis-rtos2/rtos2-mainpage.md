---
id: "rtos2-mainpage"
type: "concept"
domain: "rtos"
title: "mainpage"
summary: "Modern embedded applications often need to concurrently execute multiple activities such as sensor readings, connectivity, machine-learning algorithms, graphics display and others."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/mainpage.md"
license: "Apache-2.0"
mode: "V"
---

﻿# Overview

Modern embedded applications often need to concurrently execute multiple activities such as sensor readings, connectivity, machine-learning algorithms, graphics display and others. A real-time operating system (RTOS) equips users with necessary mechanisms that simplify implementation of complex programs and ensure their reliable operation with deterministic timing.

**CMSIS-RTOS2** specifies a generic RTOS interface over real-time OS kernels running on Arm® Cortex® processor-based devices. Applications and middleware components can use CMSIS_RTOS2 API for better code reuse and simpler integration in various software ecosystems.

CMSIS-RTOS2 also specifies a standard OS Tick interface for use by RTOS kernels. It provides several OS tick implementations for simple kernel porting to different Cortex-M and Cortex-A processors.

(figure: CMSIS-RTOS2 interface)

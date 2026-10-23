---
id: "view-cmsis-view-readme"
type: "concept"
domain: "trace"
title: "cmsis-view README"
summary: "This project shows how to use start/stop events with the Event Recorder that allow to measure execution times with:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Examples/EventStatistic/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Examples/EventStatistic/README.md"
license: "Apache-2.0"
mode: "V"
---

﻿# Event Statistic Example

This project shows how to use start/stop events with the Event Recorder that allow to measure execution times with:

- different slots (0 - 15)
- different groups (A - D)

The following API calls control this time recording:

- `EventStart` starts a timer slot.
- `EventStop` stops the related timer.
- `EventStop` with slot 15 stops the timers of all slots for the specified group.

Refer to [Using Event Statistics](https://arm-software.github.io/CMSIS-View/main/ev_stat.html#es_use) for more information.

This demo application does some time consuming calculations that are recorded
and can be displayed in the Event Statistics window.

> **Note**  
> This example runs on the [**Arm Virtual Hardware**](https://www.arm.com/products/development-tools/simulation/virtual-hardware) simulator
> and does not require any hardware.

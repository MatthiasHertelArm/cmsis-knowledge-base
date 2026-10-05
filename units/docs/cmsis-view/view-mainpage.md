---
id: "view-mainpage"
type: "concept"
domain: "trace"
title: "mainpage"
summary: "With the software components of CMSIS-View, developers can collect time-accurate event-based information, display program execution status, and analyze fault exceptions. It allows to analyze execution flows, debug potential issues, and measure execution times."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/mainpage.md"
license: "Apache-2.0"
mode: "V"
---

﻿# Overview

**CMSIS-View** equips software developers with software components, utilities and methodologies that provide visibility into internal operation of embedded applications and software components.

With the software components of CMSIS-View, developers can collect time-accurate event-based information, display program execution status, and analyze fault exceptions. It allows to analyze execution flows, debug potential issues, and measure execution times. The data can be observed in real-time in an IDE or can be saved as a log file during program execution. 

A **Software Component Viewer Description** (*.SCVD) file in SCVD_Format (XML) defines the content that is displayed in the **Component Viewer** and **Event Recorder**.

In addition, using the Event Recorder API, you can annotate your code so that you can get statistical data on the time spent in a loop or on the energy consumption ([ULINKplus](https://developer.arm.com/Tools%20and%20Software/ULINKplus) required).

Key elements of CMSIS-View are:

 - Event Recorder - an embedded software component that provides Ref_EventRecorder for event annotations in the code.
 - eventlist utility - a command line tool for processing Event Recorder log files.
 - Fault - an embedded software component with infrastructure and Ref_Fault to store, record, and analyze exception fault information.

> **Note**
> - CMSIS-View replaces and extends functionality previously provided as part of *Keil::ARM_Compiler* pack.
> - See [Migrating projects from CMSIS v5 to CMSIS v6](https://learn.arm.com/learning-paths/microcontrollers/project-migration-cmsis-v6) for a guidance on updating existing projects to CMSIS-View.

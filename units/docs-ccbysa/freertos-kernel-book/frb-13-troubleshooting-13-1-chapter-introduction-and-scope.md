---
id: "frb-13-troubleshooting-13-1-chapter-introduction-and-scope"
type: "concept"
domain: "rtos"
title: "13 Troubleshooting: 13.1 Chapter Introduction and Scope"
summary: "This chapter highlights the most common issues encountered by users who are new to FreeRTOS."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch13.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch13.md#13-1-chapter-introduction-and-scope"
license: "CC-BY-SA-4.0"
mode: "V"
---

This chapter highlights the most common issues encountered by users who
are new to FreeRTOS. First, it focuses on three issues that have proven
to be the most frequent source of support requests over the years:
incorrect interrupt priority assignment, stack overflow, and
inappropriate use of printf(). It then briefly, and in an FAQ style,
touches on other common errors, their possible causes, and their
solutions.

> *Using `configASSERT()` improves productivity by immediately trapping and
> identifying many of the most common sources of error. It is strongly
> advised to have `configASSERT()` defined while developing or debugging a
> FreeRTOS application. `configASSERT()` is described in section 12.2.*

---
id: "view-event-statistics-overview"
type: "concept"
domain: "trace"
title: "Event Statistics: Overview"
summary: "The EventExecutionStatistic functions allow you to collect and statistical data about the code execution. Any debug adapter can be used to record execution timing and number of calls for annotated code sections:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ev_stat.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ev_stat.md#overview"
license: "Apache-2.0"
mode: "V"
---

The Event_Execution_Statistic functions allow you to collect and statistical data about the code execution. Any debug adapter can be used to record execution timing and number of calls for annotated code sections:

(figure: Event Statistics for user code)

Energy profiling is of annotated code sections is possible using [ULINKplus](https://developer.arm.com/Tools%20and%20Software/ULINKplus). When combined with power measurement, the Event Statistics window displays the energy consumption of the code section with min/man/average values:

(figure: User code energy profiling)

For more information, refer to the scvd_evt_stat example.

**Benefits of Event Statistics:**

 - Collect statistical data about the code execution (time and energy).
 - Log files enable comparisons between different build runs in continuous integration (CI) environments.
 - Improve overall code quality and energy profile (especially relevant for battery driven applications).

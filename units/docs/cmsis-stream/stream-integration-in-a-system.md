---
id: "stream-integration-in-a-system"
type: "concept"
domain: "cmsis-stream"
title: "Integration in a system"
summary: "CMSIS-Stream graph scheduling is a sequence of function calls organized thanks to the dataflow dependencies. There is no concept of time inside the graph."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Integration.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Integration.md"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Stream graph scheduling is a sequence of function calls organized thanks to the dataflow dependencies. There is no concept of time inside the graph.

But when the graph is integrated into a system, it must be synchronized with peripherals (sensors, audio ...)

There are two cases to consider.

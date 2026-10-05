---
id: "stream-sds-nodes-introduction-2"
type: "concept"
domain: "cmsis-stream"
title: "SDS Nodes: Introduction"
summary: "The SDS Framework is an Arm framework that allows to record streams of samples and replay them in Virtual Hardware."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/PythonSDS.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonSDS.md#introduction"
license: "Apache-2.0"
mode: "V"
---

The [SDS Framework](https://github.com/ARM-software/SDS-Framework/tree/main) is an Arm framework that allows to record streams of samples and replay them in Virtual Hardware.

The SDS nodes provides a way to use SDS from CMSIS-Stream.

Sensors are described with a `.yml` file containing the following information:
* Sampling rate
* Datatype of a sample

This `.yml` file is used in the Python API to create the sensor and recorder nodes.

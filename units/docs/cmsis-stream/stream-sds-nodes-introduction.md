---
id: "stream-sds-nodes-introduction"
type: "concept"
domain: "cmsis-stream"
title: "SDS Nodes: Introduction"
summary: "The SDS Framework is an Arm framework that allows to record streams of samples and replay them in Virtual Hardware."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/CPPSDS.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CPPSDS.md#introduction"
license: "Apache-2.0"
mode: "V"
---

The [SDS Framework](https://github.com/ARM-software/SDS-Framework/tree/main) is an Arm framework that allows to record streams of samples and replay them in Virtual Hardware.

The SDS nodes provides a way to use SDS from CMSIS-Stream.

SDS is made of several parts (refer to the project for more details):
* A .yml file describing the sensor (datatype and samplign frequency)
* Binary .sds files containing recorded samples
* Recorders to record samples through different physical interfaces (UART, USB, Wifi ...)
* Sensor API to access to the sensors
* SDS streams (FIFOs) used to read data from the sensors or send data to the recorder

The SDS nodes are providing:
* A SDS sensor class to interface with a sensor
* A SDS recorder class to record samples

There is also a [Python API](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonSDS.md) to use those nodes in the graph description.

The nodes are located in `Include/cg/nodes/cpp/sds`

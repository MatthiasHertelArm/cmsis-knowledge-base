---
id: "sds-overview"
type: "concept"
domain: "test"
title: "Overview"
summary: "The Synchronous Data Stream (SDS) Framework implements data stream management and provides methods and utilities for developing and optimizing embedded applications that use DSP, ML, or Edge AI algorithms."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/overview.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/overview.md"
license: "Apache-2.0"
mode: "V"
---

<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD036 -->

The Synchronous Data Stream (SDS) Framework implements data stream management and provides methods and utilities for developing and optimizing embedded
applications that use DSP, ML, or Edge AI algorithms. The SDS-Framework allows you to simultaneously capture multiple data streams from
different sources (sensors, audio, and video inputs) or the results of algorithms in real time directly on target hardware.
These data streams are stored in files.

(figure: SDS-Recorder connected to different sources)

The captured data streams are useful in various steps of the development cycle, for example to:

- Validate physical input signals from sensors or output of algorithms.
- Provide input data to Digital Signal Processing (DSP) development tools such as filter designers.
- Provide input data to ML/AI development systems for model classification, training, and performance optimization.
- Provide input data for simulation using Arm Virtual Hardware (AVH-FVP) models for testing and validation.

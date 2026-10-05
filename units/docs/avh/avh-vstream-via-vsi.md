---
id: "avh-vstream-via-vsi"
type: "concept"
domain: "test"
title: "vStream via VSI"
summary: "This directory contains the implementation of vStream interface for audio and video streaming using Virtual Streaming Interface (VSI)."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:interface/vstream/README.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/interface/vstream/README.md"
license: "Apache-2.0"
mode: "V"
---

This directory contains the implementation of vStream interface for audio and video streaming
using Virtual Streaming Interface (VSI). The vStream interface is defined by CMSIS-Driver and
offers standardized interface to interact with various streaming devices to allow seamless
development on one platform and deployment on another.

Implementation consists of two components

- vStream driver implementation in C (targeting embedded application)
- implementation of VSI Python interface in Python (targeting host PC)

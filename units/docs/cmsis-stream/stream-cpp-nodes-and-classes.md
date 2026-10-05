---
id: "stream-cpp-nodes-and-classes"
type: "concept"
domain: "cmsis-stream"
title: "CPP Nodes and classes"
summary: "CPP Nodes and classes"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/CPPNodes.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CPPNodes.md"
license: "Apache-2.0"
mode: "V"
---

- [CPP Nodes and classes](#cpp-nodes-and-classes)
  - [Mandatory classes](#mandatory-classes)
    - [FIFO](#fifo)
      - [FIFO for synchronous mode](#fifo-for-synchronous-mode)
      - [Buffer for synchronous mode](#buffer-for-synchronous-mode)
      - [FIFO for asynchronous mode](#fifo-for-asynchronous-mode)
    - [Nodes](#nodes)
      - [GenericNode](#genericnode)
      - [GenericNode12](#genericnode12)
      - [GenericNode13](#genericnode13)
      - [GenericNode21](#genericnode21)
      - [GenericSource](#genericsource)
      - [GenericSink](#genericsink)
      - [GenericToManyNode](#generictomanynode)
      - [GenericFromManyNode](#genericfrommanynode)
      - [GenericManyToManyNode](#genericmanytomanynode)
      - [Duplicate](#duplicate)
  - [Optional nodes](#optional-nodes)
    - [CFFT / CIFFT](#cfft--cifft)
    - [InterleavedStereoToMono](#interleavedstereotomono)
    - [MFCC](#mfcc)
    - [NullSink](#nullsink)
    - [OverlapAndAdd](#overlapandadd)
    - [SlidingBuffer](#slidingbuffer)
    - [ToComplex](#tocomplex)
    - [ToReal](#toreal)
    - [Unzip](#unzip)
    - [Zip](#zip)
    - [Host](#host)
      - [FileSink](#filesink)
      - [FileSource](#filesource)
  - [SDS Nodes](#sds-nodes)

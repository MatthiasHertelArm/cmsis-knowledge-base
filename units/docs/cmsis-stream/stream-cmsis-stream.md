---
id: "stream-cmsis-stream"
type: "concept"
domain: "cmsis-stream"
title: "CMSIS-Stream"
summary: "CMSIS-Stream is a low overhead framework that can be used to build AI + multi-media applications. It unifies the handling of video, audio, DSP and AI in the same framework."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/README.md"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Stream is a low overhead framework that can be used to build AI + multi-media applications.
It unifies the handling of video, audio, DSP and AI in the same framework.

Video, audio, AI, DSP components are all connected in a CMSIS Stream graph.

CMSIS Stream is low overhead : it can run on bare metal with no RTOS, on embedded systems with RTOS (Zephyr, RTX or any other RTOS) and it also works on Linux and Mac with optional interprocess communications.

CMSIS Stream is made of two parts : dataflow and events.

Processing elements in the graph can exchange data streams (dataflow) and send and receive events. An event is like a remote procedure call : it has a name and arguments.

CMSIS-Stream provides a Python package.

Python is used to:

* Describe the graph (streaming graph and event graph)
* Generate a **static scheduling** of the streaming graph that is computed **at build time** with several memory optimizations.
* Generate the code for this scheduler (state machine) as a simple C++ file (with a C API).
  * The scheduler can be run on bare metal devices. There is no dependencies to any RTOS. The scheduler is a sequence of function calls
* Connect all the nodes for events propagation in the graph of events

* Generate a graphical representation of the graph

The processing of the data streams in this graph has:

* low memory usage
* minimal overhead (build time computations)
* deterministic scheduling (state machine)
* modular design
* graphical representation

For the streaming part, C++ is only used for strong and static typing (template). The only part of the C++ library that is used is the memory allocator to create the objects before the graph is started. You control memory allocations during the execution of the graph.

For the event graph (which is optional) there is a dependency on the environment (RTOS, Rich OS or bare metal) and an implementation of the event runtime must be provided. See the section of the documentation about the event graph.

The current repository provides implementations of the runtime system for:
* Posix (but with no inter-process communication and memory sharing cross process in this version)
* Zephyr
* CMSIS RTOS API

A Linux version with inter process communication and buffer sharing cross process without copy is work in progress. This Linux version with IPC is not yet in the repository.

The provided implementations for posix, Zephyr and CMSIS-RTOS are simple : the event management uses only one thread but an implementation may decide to use a thread pool instead.

Here is an example of graph running on an embedded board and implementing a
keyword spotting demo for Cortex-M with DSP pre-processing (microphone + MFCC), TensorFlow Lite for Micro component and additional components for majority voting and display on LCD with animation:

(figure: KWS graph)

This demo uses Helium acceleration and the Ethos NPU and is multi-threaded with fading animations on the LCD when keywords are recognized.

---
id: "intr-building-an-on-device-embedded-tes-design"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Design"
summary: "The library itself is implemented as a two-part system:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#design"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Library Components

The library itself is implemented as a two-part system:

#### Reactor

The reactor is a module running on the embedded device and controls it to the necessary degree. It has a small footprint and limited functionality.

It can:
- register tests to itself
- store bare minimum information about firmware/tests
- execute the tests
- communicate information/exchange data between itself and the controller

#### Controller

The controller orchestrates the testing process and is run on the device that controls the tests, typically the host machine. It is still developed as microcontroller-compatible software (no dynamic memory, no exceptions), but there is a weak assumption that it will be mainly used on a system with GPOS (general-purpose operating system).

It can:
- communicate with and control the reactor
- load test information from the reactor
- orchestrate test execution
- provide input data for tests
- provide data collected from the tests

### Reactor and Controller Working Together

The separation of the design into two tools imposes restrictions: the tests on the embedded device can't be executed without the controller. 
But that allows a minimal memory footprint of the testing firmware on the firmware size, as I can move as much of the testing logic as reasonable to the controller side.
In particular, data collection can be done within the controller because it has ample storage.

The communication method between the two parts is not defined.
Both parts use messages for communication, but it is up to the user to implement how the messages are transferred.
Each expects to be provided with an interface that implements read/write methods, it's up to the user to design the implementation.
This makes it platform-independent and gives flexibility for various scenarios.
I do expect that a UART will be mostly used primarily to transfer data.

In the end, the perspective one can use for this is:
The testing library is just a fancy remote execution library - the controller executes functions registered to the reactor in the firmware and collects results.

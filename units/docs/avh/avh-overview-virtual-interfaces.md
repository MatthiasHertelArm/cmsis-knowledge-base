---
id: "avh-overview-virtual-interfaces"
type: "concept"
domain: "test"
title: "Overview: Virtual Interfaces"
summary: "The Arm Virtual Hardware FVPs implement various virtual interfaces that can be used to stimulate the application under test."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:DoxyGen/simulation/src/main.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/simulation/src/main.md#virtual-interfaces"
license: "Apache-2.0"
mode: "V"
---

The Arm Virtual Hardware FVPs implement various virtual interfaces that can be used to stimulate the application under
test.

(figure: AVH Virtual Interfaces)

- The arm_vio interface controls simple I/O such as LED and switches.
- The arm_vsi provides up to 8 channels for data streaming.
- The arm_vsocket connects the user application to [BSD sockets](https://en.wikipedia.org/wiki/Berkeley_sockets)
  on the host computer for IP network connectivity.

Both VIO and VSI connect to local python scripts and enable flexible scripting for test
automation. Eight VSI interfaces are available and may be used in parallel to stream simultaneous multi-channel inputs
and outputs. The interfaces are tailored for simulation, but can also map to physical target hardware, for example to a
video camera as a VSI input.

In addition the **Event Recorder Capturing** provides an interface for the
[Event Recorder](https://arm-software.github.io/CMSIS-View/latest/evr.html) API. This software component enables event
annotations in the application code or software component libraries. **Event Recorder** provides visibility to the
dynamic execution of an application, enables RTOS awareness, and
[Event Statistics](https://arm-software.github.io/CMSIS-View/latest/ev_stat.html) which helps to optimize the timing of
complex algorithms.

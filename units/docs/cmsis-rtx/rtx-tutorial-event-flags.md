---
id: "rtx-tutorial-event-flags"
type: "concept"
domain: "rtos"
title: "tutorial: Inter-thread Communication / Event Flags"
summary: "Event flags operate in a similar fashion to thread flags but must be created and then act as a global RTOS object that can be used by all the running threads."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#event-flags"
license: "Apache-2.0"
mode: "V"
---

_Part of: Inter-thread Communication_

Event flags operate in a similar fashion to thread flags but must be created and then act as a global RTOS object that can
be used by all the running threads.

First, we need to create a set of event flags, this is a similar process to creating a thread. We define an event flag
attribute structure. The attribute structure defines an ASCII name string, attribute bits, and memory detention. If we are
using the static memory model.

```c
osEventFlagsAttr_t {
  const char *name;   ///< name of the event flags
  uint32_t attr_bits; ///< attribute bits (none)
  void *cb_mem;       ///< memory for control block
  uint32_t cb_size;   ///< size of provided memory for control block
};
```

Next we need a handle to control access the event flags:

```c
osEventFlagsId_t EventFlag_LED;
```

Then we can create the event flag object:

```c
EventFlag_LED = osEventFlagsNew(&EventFlagAttr_LED);
```

Refer to CMSIS_RTOS_EventFlags for more information.

#### Exercise 10 - Event Flags

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 10 Event Flags** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

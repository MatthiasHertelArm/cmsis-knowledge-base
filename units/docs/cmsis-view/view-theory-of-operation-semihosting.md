---
id: "view-theory-of-operation-semihosting"
type: "concept"
domain: "trace"
title: "Theory of operation: Semihosting"
summary: "Semihosting is a mechanism that enables code running on an Arm target to communicate and use the input/output facilities on a host computer that is running a debugger."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/event_recorder.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/event_recorder.md#semihosting"
license: "Apache-2.0"
mode: "V"
---

Semihosting is a mechanism that enables code running on an Arm target to communicate and use the input/output facilities on a host computer that is running a debugger.

Examples of these facilities include keyboard input, screen output, and disk I/O. For example, you can use this mechanism to enable functions in the C library, such as `printf` and `scanf`, to use the screen and keyboard of the host instead of having a screen and keyboard on the target system.

In µVision, you can use semihosting to log data from Arm Virtual Hardware models, whereas in Keil Studio, you can also use semihosting to record data from real hardware targets.

### Semihosting in uVision

In µVision, you can use semihosting with models to write the events into a file on your PC. This works with [Arm
Fast Models](https://developer.arm.com/Tools%20and%20Software/Fast%20Models), [Arm Fixed Virtual Platforms](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms), and [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware) alike.

The file that is written is called `EventRecorder.log` and is a binary file that is available in the root directory of your project. Use evntlst to read and decode the binary data.

> **Note**
> - Your model needs to be configured for semihosting (refer to the documentation of your modeling technology on how to do that).
> - You can specify a different name for the log file by specifying a define called `EVENT_LOG_FILENAME`.
> - In µVision, once you start a new debug session, the log file will be overwritten. While in debug, new messages will be appended to the currently open log file.
> - In µVision, the semihosting variant will not work with real target hardware.
> - In µVision, you can still use the Event Recorder window in µVision to see the events coming in while the file is written to the hard drive of your PC.

### Semihosting in Keil Studio

In Keil Studio, you can use semihosting with any hardware to write the events into a file on your PC.

Follow these steps:

- Add the component `CMSIS-View:Event Recorder&Semihosting` to your project.
- [Optional] Remove any component that redirects `printf`, such as components from the `ARM:CMSIS-Compiler` pack.
- Initialize the Event Recorder and use Event Recorder functions to record data.
- Add the option `-S` to the `serverParameters` in the launch configuration of the `launch.json` script:
  ```json
              "target": {
                "server": "pyocd",
                "serverParameters": [
                    "gdbserver",
                    "--port",
                    "3333",
                    "--probe",
                    "cmsisdap:",
                    "--connect",
                    "attach",
                    "-S",
                    "--cbuild-run",
                    "${command:cmsis-csolution.getCbuildRunFile}"
                ],
                "port": "3333"
            },
```

The file that is written is called `EventRecorder.log` and is a binary file that is available in the root directory of your project. Use evntlst to read and decode the binary data.

> **Note**
> - You can specify a different name for the log file by specifying a define called `EVENT_LOG_FILENAME`.
> - Once you start a new debug session, the log file will be overwritten. While in debug, new messages will be appended to the currently open log file.

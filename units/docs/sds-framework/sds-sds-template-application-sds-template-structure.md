---
id: "sds-sds-template-application-sds-template-structure"
type: "concept"
domain: "test"
title: "SDS Template Application: SDS Template Structure"
summary: "The structure of the SDS template application is shown below. Two projects let you choose between a data communication test and a user algorithm test."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/template.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/template.md#sds-template-structure"
license: "Apache-2.0"
mode: "V"
---

The structure of the SDS template application is shown below. Two projects let you choose between a data communication test and a user algorithm test. Three target types are available, allowing the test application to be deployed either on hardware (an evaluation board) or on one of two AVH FVP simulation models.

A standard board layer, provided by several BSPs, implements the hardware interface. For communication, the SDSIO layer uses the MDK-Middleware or (for the AVH FVP target) a virtual simulation interface (VSI).

(figure: SDS Template Structure)

The `Debug` and `Release` build types differ only in the optimization level and the amount of debug information printed.
Both build types support recording and playback, controlled via `sdsFlags`. The `sdsFlags` value can be modified by the SDS application (using the function `sdsFlagsModify`) or by the SDSIO-Server, making it easy to switch between Record Mode and Playback Mode.

!!! Note
    The template-based file system implementation natively supports recording mode only.
    Playback mode can be enabled by adapting the provided template code.
    For example, an additional button on the board can be used to toggle between recording and playback modes.

### Record Mode

Record mode captures the input data stream and the algorithm output data stream simultaneously.

(figure: Record Mode)

### Playback Mode

Playback mode replays the input data stream while recording the algorithm output data stream at the same time.
The test application can run either on hardware (evaluation board) or on an AVH FVP (simulation model).
Because the input data stream can be repeated, it enables consistent verification and optimization of the algorithm while capturing the resulting output data stream.

(figure: Playback Mode)

### Thread Information

The application runs the thread `sdsControlThread`, which calls `sdsInit` to create `sdsThread` and then creates `AlgorithmThread`.

Thread             | Description                   | Stack size   | Priority
:------------------|:------------------------------|:-------------|:--------------------
`sdsControlThread` | Manages application control   | RTOS default | `osPriorityNormal1`
`sdsThread`        | Transfers SDS stream data     | 1024 bytes   | `osPriorityNormal1`
`AlgorithmThread`  | Processes user algorithm      | RTOS default | `osPriorityNormal`

The `sdsThread` values are the defaults defined by `SDS_THREAD_STACK_SIZE` and `SDS_THREAD_PRIORITY` and can be changed in `sds_config.h`.

!!! Note
    Keep SDSIO communication at a higher priority than the threads that produce or consume stream data.

**Details:**

- `sdsControlThread` initializes SDS, creates `AlgorithmThread`, exchanges server control information, handles the VIO button and LED, manages application state, and measures the idle rate.
- `sdsThread` transfers stream data through the selected SDSIO interface.
- `AlgorithmThread` initializes the input source and algorithm, acquires or plays back input data, runs the algorithm, and records input and output data.

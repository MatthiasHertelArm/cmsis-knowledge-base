---
id: "sds-theory-usage"
type: "concept"
domain: "test"
title: "theory: Usage"
summary: "The following diagram shows the usage of the SDS Stream Interface functions (executed in sdsThread). The sdsControlThread controls the overall execution. AlgorithmThread is the thread that executes Signal Conditioning (SC) and the ML Model."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/theory.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#usage"
license: "Apache-2.0"
mode: "V"
---

The following diagram shows the usage of the SDS Stream Interface functions (executed in `sdsThread`).  The `sdsControlThread` controls the overall execution. `AlgorithmThread` is the thread that executes Signal Conditioning (SC) and the ML Model.

When `AlgorithmThread` starts, it first calls the `InitInputData` function, which initializes the input interfaces
(camera, microphone or sensor interfaces). It then calls `InitAlgorithm`, which is responsible for initializing the ML algorithm.

After initialization, `AlgorithmThread` enters a loop in which it repeatedly calls `GetInputData`. This function provides a block of input data
used for a single inference. The inference itself is executed by the `ExecuteAlgorithm` function.

Two additional functions are also provided:

- `DiscardInputData`: used during playback to discard incoming live input data, since the actual input is read from the SDS file.
- `ResetAlgorithm`: called before each playback run to reset internal states, memory buffers, and results from previous inferences,
  ensuring a clean start for the new playback session.

```mermaid
sequenceDiagram
    participant sdsControlThread
    participant sdsThread
    participant AlgorithmThread
    Note over sdsControlThread: sdsInit
    activate sdsThread
    Note over sdsControlThread: Open data streams
    Note over sdsThread: Read content for<br/>'play' data streams
    activate AlgorithmThread
    loop periodic
        Note over AlgorithmThread: GetInputData<br/>(physical input or sdsRead)
        Note over AlgorithmThread: Execute algorithm
        Note over AlgorithmThread: sdsWrite data streams
        Note over sdsThread: Read/write data streams.
    end
    sdsControlThread-->>AlgorithmThread: Stop Algorithm
    AlgorithmThread-->>sdsControlThread: Stopped
    Note over sdsControlThread: Close data streams
    Note over sdsThread: Flush and close<br/> data streams
```

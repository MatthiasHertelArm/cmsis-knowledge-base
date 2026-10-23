---
id: "mlek-noise-reduction-code-sample-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Noise Reduction Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/noise_reduction.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/noise_reduction.md#setting-up-and-running-ethos-u-npu-code-sample"
license: "Apache-2.0"
mode: "V"
---

### Setting up the Ethos-U NPU Fast Model

The FVP is available publicly from [Arm Ecosystem FVP downloads](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps).

For the *Ethos-U* evaluation, please download the MPS3 based version of the Arm® *Corstone™-300* model that contains *Cortex-M55*
and offers a choice of the *Ethos-U55* and *Ethos-U65* processors.

To install the FVP:

- Unpack the archive,

- Run the install script in the extracted package:

```commandline
$./FVP_Corstone_SSE-300.sh
```

- Follow the instructions to install the FVP to your required location.

### Starting Fast Model simulation

Once the building step has completed, the application binary `mlek_noise_reduction.axf` can be
found in the `build/bin` folder. Assuming the install location of the FVP was set to
`~/FVP_install_location`, start the simulation with the following command:

```commandline
~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 ./bin/mps3-sse-300/mlek_noise_reduction.axf
```

A log output then appears on the terminal:

```log
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
```

This also launches a telnet window with the standard output of the sample application. It also
includes error log entries containing information about the pre-built application version,
TensorFlow Lite Micro library version used, and the data type. As well as the input and output
tensor sizes of the model that was compiled into the executable binary.

After the application has started inferences are executed on inputs from `noise_reduction_FILE_PATH`

### Running Noise Reduction

The following example illustrates an application output:

```log
INFO - Audio Clip dump header info (20 bytes) written to 0x80000000
INFO - Inference 1/136
INFO - Copied 960 bytes to 0x80000014
INFO - Inference 2/136
INFO - Copied 960 bytes to 0x800003d4
...
INFO - Inference 136/136
INFO - Copied 960 bytes to 0x8001fa54
INFO - Output memory dump of 130580 bytes written at address 0x80000000
INFO - Final results:
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 530
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 376
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 13911
INFO - NPU ACTIVE cycles: 103870
INFO - NPU IDLE cycles: 643
INFO - NPU TOTAL cycles: 104514
```

> **Note:** When running Fast Model, each inference can take several seconds on most systems.

Each inference dumps the post processed output to memory. For further information, please refer to:
[Dumping post processed results for all inferences](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#dumping-post_processed-results-for-all-inferences).

The profiling section of the log shows that for this inference:

- *Ethos-U* NPU PMU report for each inference:

  - 104514: The total number of NPU cycles.

  - 103870: How many NPU cycles were used for computation.

  - 643: How many cycles the NPU was idle for.

  - 530: The number of AXI beats with read transactions from AXI0 bus.
    > **Note:** The AXI0 is the bus where the *Ethos-U* NPU reads and writes to the computation
    > buffers, or the activation buf or tensor arenas.

  - 370: The number of AXI beats with write transactions to the AXI0 bus.

  - 13911: The number of AXI beats with read transactions from AXI1 bus.
    > **Note:** The AXI1 is the bus where *Ethos-U* NPU reads the model, which is read-only.

- For FPGA platforms, the CPU cycle count can also be enabled. However, for FVP, do not use the CPU
  cycle counters as the CPU model is not cycle-approximate or cycle-accurate.

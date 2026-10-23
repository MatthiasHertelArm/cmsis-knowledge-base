---
id: "mlek-automatic-speech-recognition-code-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Automatic Speech Recognition Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/asr.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/asr.md#setting-up-and-running-ethos-u-npu-code-sample"
license: "Apache-2.0"
mode: "V"
---

### Setting up the Ethos-U NPU Fast Model

The FVP is available publicly from
[Arm Ecosystem FVP downloads](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps).

For the *Ethos-U* evaluation, please download the MPS3 based version of the Arm® *Corstone™-300* model that contains *Cortex-M55*
and offers a choice of the *Ethos-U55* and *Ethos-U65* processors.

To install the FVP:

- Unpack the archive.

- Run the install script in the extracted package:

```commandline
./FVP_Corstone_SSE-300.sh
```

- Follow the instructions to install the FVP to the required location.

### Starting Fast Model simulation

Once the building has been completed, the application binary `mlek_asr.axf` can be found in the `build/bin` folder.

Assuming that the install location of the FVP was set to `~/FVP_install_location`, then the simulation can be started by
using:

```commandline
~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 ./bin/mps3-sse-300/mlek_asr.axf
```

A log output appears on the terminal:

```log
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
```

This also launches a telnet window with the standard output of the sample application. It also includes error log
entries containing information about the pre-built application version, TensorFlow Lite Micro library version used, and
data types. The log also includes the input and output tensor sizes of the model compiled into the executable binary.

After the application has started inferences are executed on inputs from `asr_FILE_PATH`.

### Running Automatic Speech Recognition

#### Running with *wav2letter*

The following example illustrates the output of the use case using *wav2letter* on *Corstone™-300*:

```log
INFO - Running inference on audio clip 0 => another_door.wav
INFO - Inference 1/2
INFO - Inference 2/2
INFO - Final results:
INFO - Total number of inferences: 2
INFO - For timestamp: 0.000000 (inference #: 0); label: and he walked immediately out of th
INFO - For timestamp: 0.000000 (inference #: 1); label: e apartment by another door
INFO - Complete recognition: and he walked immediately out of the apartment by another door
INFO - Profile for Inference :
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 6564262
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 928889
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 841712
INFO - NPU ACTIVE cycles: 28450696
INFO - NPU IDLE cycles: 476
INFO - NPU TOTAL cycles: 28451172
```

It can take several minutes to complete each inference. The average time is around 5-7 minutes,
and on this audio clip, multiple inferences were required to cover the whole clip.

The profiling section of the log shows that for the first inference:

- *Ethos-U* PMU report:

  - 28,451,172 total cycles: The number of NPU cycles.

  - 28,450,696 active cycles: The number of NPU cycles that were used for computation.

  - 476 idle cycles: The number of cycles for which the NPU was idle.

  - 6,564,262 AXI0 read beats: The number of AXI beats with read transactions from the AXI0 bus. AXI0 is the bus where
    the *Ethos-U* NPU reads and writes to the computation buffers, activation buf, or tensor arenas.

  - 928,889 AXI0 write beats: The number of AXI beats with write transactions to the AXI0 bus.

  - 841,712 AXI1 read beats: The number of AXI beats with read transactions from the AXI1 bus. AXI1 is the bus where the
    *Ethos-U55* NPU reads the model. So, read-only.

- For FPGA platforms, a CPU cycle count can also be enabled. However, do not use cycle counters for FVP, as the CPU
  model is not cycle-approximate or cycle-accurate.

The application prints the decoded output from each of the inference runs, and the final combined result.

#### Running with *Conformer*

The following example illustrates the output of the use case using *Conformer* on *Corstone™-320*:

```log
INFO - Using sample audio: another_door.wav
INFO - Profile for Inference:
INFO - NPU ACTIVE: 206205334 cycles
INFO - NPU ETHOSU_PMU_SRAM_RD_DATA_BEAT_RECEIVED: 13858306 beats
INFO - NPU ETHOSU_PMU_SRAM_WR_DATA_BEAT_WRITTEN: 7968438 beats
INFO - NPU ETHOSU_PMU_EXT_RD_DATA_BEAT_RECEIVED: 26978241 beats
INFO - NPU ETHOSU_PMU_EXT_WR_DATA_BEAT_WRITTEN: 18985466 beats
INFO - NPU IDLE: 722 cycles
INFO - NPU TOTAL: 206206056 cycles
INFO - Decoded output: and he walked immediately out of the apartment by another door
```

It can take several minutes to complete the inference.

The profiling section of the log shows that for the first inference:

- *Ethos-U* PMU report:

  - 206,206,056 total cycles: The number of NPU cycles.

  - 206,205,334 active cycles: The number of NPU cycles that were used for computation.

  - 722 idle cycles: The number of cycles for which the NPU was idle.

  - 13,858,306 SRAM read beats: The total number of AXI beats with
    read transactions from the AXI buses connected to SRAM.
    These are the buses through which the *Ethos-U* NPU reads and writes
    to the computation buffers, activation buf, or tensor arenas.

  - 7,968,438 EXT write beats: The total number of AXI beats with write transactions over the AXI buses connected to SRAM.

  - 26,978,241 EXT read beats: The total number of AXI beats with
    read transactions from the AXI buses connected to DRAM.
    These are the buses through the *Ethos-U* NPU reads the model. So, read-only.

- For FPGA platforms, a CPU cycle count can also be enabled. However, do not use cycle counters for FVP, as the CPU
  model is not cycle-approximate or cycle-accurate.

The application prints the decoded output from inference run.

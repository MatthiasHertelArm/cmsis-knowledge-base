---
id: "mlek-anomaly-detection-code-sample-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Anomaly Detection Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/ad.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/ad.md#setting-up-and-running-ethos-u-npu-code-sample"
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

> **Note:** The anomaly detection example does not come pre-built. Therefore, you must first follow the instructions in
> section three for building the application from source.

After building, and assuming the install location of the FVP was set to the `~/FVP_install_location`, the simulation can
be started by running:

```commandline
~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 ./bin/mlek_ad.axf
```

A log output now appears on the terminal:

```log
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
```

This also launches a telnet window with the standard output of the sample application. It also includes error log
entries containing information about the pre-built application version, TensorFlow Lite Micro library version used, and
data types. The log also includes the input and output tensor sizes of the model compiled into the executable binary.

After the application has started inferences are executed on inputs from `ad_FILE_PATH`.

### Running Anomaly Detection

The following example illustrates the output of an application:

```log
INFO - Running inference on audio clip 4 => random_id_00_000000.wav
INFO - Inference 1/1
INFO - Average anomaly score is: -0.883147
INFO - Anomaly threshold is: -0.800000
INFO - Everything fine, no anomaly detected!
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 485194
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 138111
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 56245
INFO - NPU ACTIVE cycles: 967731
INFO - NPU IDLE cycles: 441
INFO - NPU TOTAL cycles: 968172
```

As multiple inferences must be run for one clip, it takes around a minute for all inferences to complete.

For the `random_id_00_000000.wav` clip, after averaging results across all inferences needed, the score is less than the
chosen anomaly threshold. Therefore, an anomaly was not detected with the machine in this clip.

The profiling section of the log shows that for each inference. For the last inference, the profiling reports:

- *Ethos-U* PMU report:

  - 968,172 total cycle: The number of NPU cycles

  - 967,731 active cycles: number of NPU cycles that were used for computation

  - 441 idle cycles: number of cycles for which the NPU was idle

  - 48,5194 AXI0 read beats: The number of AXI beats with read transactions from AXI0 bus. AXI0 is the bus where
    *Ethos-U* NPU reads and writes to the computation buffers, activation buf, or tensor arenas.

  - 138,111 AXI0 write beats: The number of AXI beats with write transactions to AXI0 bus.

  - 56,245 AXI1 read beats: The number of AXI beats with read transactions from AXI1 bus. AXI1 is the bus where
   *Ethos-U* NPU reads the model. So, read-only.

- For FPGA platforms, a CPU cycle count can also be enabled. However, do not use cycle counters for FVP, as the CPU
  model is not cycle-approximate or cycle-accurate.

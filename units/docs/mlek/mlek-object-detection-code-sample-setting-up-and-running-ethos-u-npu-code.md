---
id: "mlek-object-detection-code-sample-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Object Detection Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/object_detection.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/object_detection.md#setting-up-and-running-ethos-u-npu-code-sample"
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

The pre-built application binary `mlek_object_detection.axf` can be
found in the `bin/mps3-sse-300` folder of the delivery package.

Assuming that the install location of the FVP was set to `~/FVP_install_location`, then the simulation can be started by
using:

```commandline
~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 ./bin/mps3-sse-300/mlek_object_detection.axf
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

After the application has started, inferences are executed on inputs from `object_detection_FILE_PATH`.

### Running Object Detection

The following example illustrates an application output for detection:

```log
INFO - Running inference on image 0 => couple.bmp
INFO - Final results:
INFO - Total number of inferences: 1
INFO - 0)  (0.999246) -> Detection box: {x=89,y=17,w=41,h=56}
INFO - 0)  (0.995367) -> Detection box: {x=27,y=81,w=48,h=53}
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 678955
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 467545
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 46895
INFO - NPU ACTIVE cycles: 2050339
INFO - NPU IDLE cycles: 855
INFO - NPU TOTAL cycles: 2051194
```

It can take several minutes to complete one inference run. The average time is around 10-20 seconds.

The log shows the inference results for `image 0`, so `0` - `index`, that corresponds to `couple.bmp` in the sample image
resource folder.

The profiling section of the log shows that for this inference:

- *Ethos-U* PMU report:

  - 2,051,194 total cycle: The number of NPU cycles.

  - 2,050,339 active cycles: The number of NPU cycles that were used for computation.

  - 855 idle cycles: The number of cycles for which the NPU was idle.

  - 678,955 AXI0 read beats: The number of AXI beats with read transactions from AXI0 bus. AXI0 is the bus where the
    *Ethos-U* NPU reads and writes to the computation buffers, activation buf, or tensor arenas.

  - 467,545 AXI0 write beats: The number of AXI beats with write transactions to AXI0 bus.

  - 46,895 AXI1 read beats: The number of AXI beats with read transactions from AXI1 bus. AXI1 is the bus where the
    *Ethos-U* NPU reads the model. So, read-only.

- For FPGA platforms, a CPU cycle count can also be enabled. However, do not use cycle counters for FVP, as the CPU
  model is not cycle-approximate or cycle-accurate

The application prints the detected bounding boxes for faces in image. The FVP window also shows the output on its LCD section.

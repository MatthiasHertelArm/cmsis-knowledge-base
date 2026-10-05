---
id: "mlek-image-classification-code-sample-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Image Classification Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/img_class.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/img_class.md#setting-up-and-running-ethos-u-npu-code-sample"
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

The pre-built application binary `mlek_img_class.axf` can be found in the `bin/mps3-sse-300` folder of the delivery
package.

Assuming that the install location of the FVP was set to `~/FVP_install_location`, then the simulation can be started by
using:

```commandline
~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 ./bin/mps3-sse-300/mlek_img_class.axf
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

### Running Image Classification

Please select the first menu option to execute Image Classification.

The following example illustrates an application output for classification:

```log
INFO - Running inference on image 0 => cat.bmp
INFO - Final results:
INFO - Total number of inferences: 1
INFO - 0) 282 (0.753906) -> tabby, tabby cat
INFO - 1) 286 (0.148438) -> Egyptian cat
INFO - 2) 283 (0.062500) -> tiger cat
INFO - 3) 458 (0.003906) -> bow tie, bow-tie, bowtie
INFO - 4) 288 (0.003906) -> lynx, catamount
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 2468259
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 1151319
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 432351
INFO - NPU ACTIVE cycles: 7345741
INFO - NPU IDLE cycles: 431
INFO - NPU TOTAL cycles: 7346172
```

It can take several minutes to complete one inference run. The average time is around 2-3 minutes.

The log shows the inference results for `image 0`, so `0` - `index`, that corresponds to `cat.bmp` in the sample image
resource folder.

The profiling section of the log shows that for this inference:

- *Ethos-U* PMU report:

  - 7,346,172 total cycle: The number of NPU cycles.

  - 7,345,741 active cycles: The number of NPU cycles that were used for computation.

  - 413 idle cycles: The number of cycles for which the NPU was idle.

  - 2,468,259 AXI0 read beats: The number of AXI beats with read transactions from AXI0 bus. AXI0 is the bus where the
    *Ethos-U* NPU reads and writes to the computation buffers, activation buf, or tensor arenas.

  - 1,151,319 AXI0 write beats: The number of AXI beats with write transactions to AXI0 bus.

  - 432,351 AXI1 read beats: The number of AXI beats with read transactions from AXI1 bus. AXI1 is the bus where the
    *Ethos-U* NPU reads the model. So, read-only.

- For FPGA platforms, a CPU cycle count can also be enabled. However, do not use cycle counters for FVP, as the CPU
  model is not cycle-approximate or cycle-accurate

The application prints the top five classes with indexes, a confidence score, and labels from the associated
labels file (e.g. `labels_mobilenet_v2_1.0_224.txt`). The FVP window also shows the output on its LCD section.

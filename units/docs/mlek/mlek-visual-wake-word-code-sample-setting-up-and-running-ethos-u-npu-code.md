---
id: "mlek-visual-wake-word-code-sample-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Visual Wake Word Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/visual_wake_word.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/visual_wake_word.md#setting-up-and-running-ethos-u-npu-code-sample"
license: "Apache-2.0"
mode: "V"
---

### Setting up the Ethos-U NPU Fast Model

The FVP is available publicly from
[Arm Ecosystem FVP downloads](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps).

For the *Ethos-U* evaluation, please download the MPS3 based version of the Arm® *Corstone™-300* model that contains *Cortex-M55*
and offers a choice of the *Ethos-U55* and *Ethos-U65* processors.

- Unpack the archive

- Run the install script in the extracted package

```commandline
$./FVP_Corstone_SSE-300.sh
```

- Follow the instructions to install the FVP to your desired location

### Starting Fast Model simulation

Pre-built application binary mlek_vww.axf can be found in the bin/mps3-sse-300 folder of the delivery
package. Assuming the install location of the FVP was set to ~/FVP_install_location, the simulation can be started by:

```commandline
$ ~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 ./bin/mps3-sse-300/mlek_vww.axf
```

A log output should appear on the terminal:

```log
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
```

This will also launch a telnet window with the sample application's standard output and error log entries containing
information about the pre-built application version, TensorFlow Lite Micro library version used, data type as well as
the input and output tensor sizes of the model compiled into the executable binary.

After the application has started, inferences are executed on inputs from `vww_FILE_PATH`.

### Running Visual Wake Word

The following example illustrates application output for classification:

```log
INFO - Running inference on image 0 => man_in_red_jacket.png
INFO - Final results:
INFO - Total number of inferences: 1
INFO - 0) 1 (3.211100) -> person
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 228679
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 153031
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 40625
INFO - NPU ACTIVE cycles: 706754
INFO - NPU IDLE cycles: 10954
INFO - NPU TOTAL cycles: 717708
```

It could take several minutes to complete one inference run (average time is 2-3 minutes).

The log shows the inference results for “image 1” (1 - index) that corresponds to man_in_red_jacket.png” in the sample
image resource folder.

The profiling section of the log shows that for this inference:

- Ethos-U's PMU report:

  - 717,708 total cycle: The number of NPU cycles

  - 706,754 active cycles: number of NPU cycles that were used for computation

  - 10,954 idle cycles: number of cycles for which the NPU was idle

  - 228,679 AXI0 read beats: The number of AXI beats with read transactions from AXI0 bus. AXI0 is the bus where
    Ethos-U NPU reads and writes to the computation buffers (activation buf/tensor arenas).

  - 153,031 AXI0 write beats: The number of AXI beats with write transactions to AXI0 bus.

  - 40,625 AXI1 read beats: The number of AXI beats with read transactions from AXI1 bus. AXI1 is the bus where
    Ethos-U NPU reads the model (read only)

- For FPGA platforms, CPU cycle count can also be enabled. For FVP, however, CPU cycle counters should not be used as
    the CPU model is not cycle-approximate or cycle-accurate.

The application prints the detection with label index, confidence score and labels from associated pd_labels.txt file.

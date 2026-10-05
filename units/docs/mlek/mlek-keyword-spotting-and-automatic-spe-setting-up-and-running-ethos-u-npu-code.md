---
id: "mlek-keyword-spotting-and-automatic-spe-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Keyword Spotting and Automatic Speech Recognition Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/kws_asr.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/kws_asr.md#setting-up-and-running-ethos-u-npu-code-sample"
license: "Apache-2.0"
mode: "V"
---

### Setting up the Ethos-U NPU Fast Model

The FVP is available publicly from
[Arm Ecosystem FVP downloads](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps).

For the *Ethos-U* evaluation, please download the MPS3 based version of the Arm® *Corstone™-300* model that contains *Cortex-M55*  and offers a choice of the *Ethos-U55* and *Ethos-U65* processors.

To install the FVP:

- Unpack the archive.

- Run the install script in the extracted package:

```commandline
./FVP_Corstone_SSE-300.sh
```

- Follow the instructions to install the FVP to the required location.

### Starting Fast Model simulation

Once the building has been completed, the application binary `mlek_kws_asr.axf` can be found in the `build/bin`
folder.

Assuming that the install location of the FVP was set to `~/FVP_install_location`, then the simulation can be started by
using:

```commandline
$ ~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 ./bin/mps3-sse-300/mlek_kws_asr.axf
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

After the application has started inferences are executed on inputs from `kws_asr_FILE_PATH` .

### Running Keyword Spotting and Automatic Speech Recognition

The following example illustrates the output of an application:

```log
INFO - KWS audio data window size 16000
INFO - Running KWS inference on audio clip 0 => yes_no_go_stop.wav
INFO - Inference 1/7
INFO - For timestamp: 0.000000 (inference #: 0); threshold: 0.900000
INFO -          label @ 0: yes, score: 0.997407
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 132130
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 48252
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 17544
INFO - NPU ACTIVE cycles: 413814
INFO - NPU IDLE cycles: 358
INFO - NPU TOTAL cycles: 414172
INFO - Keyword spotted
INFO - Inference 1/2
INFO - Inference 2/2
INFO - Result for inf 0: no go
INFO - Result for inf 1:  stop
INFO - Final result: no go stop
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 8895431
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 1890168
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 1740069
INFO - NPU ACTIVE cycles: 30164330
INFO - NPU IDLE cycles: 342
INFO - NPU TOTAL cycles: 30164672
INFO - Main loop terminated.
INFO - program terminating...
INFO - releasing platform Arm Corstone-300 (SSE-300)

```

It can take several minutes to complete one inference run. The average time is around 2-3 minutes.

Using the input `yes_no_go_stop.wav`, the log shows inference results for the KWS operation first. Detecting the trigger
word `yes` with the stated probability score. In this case, `0.99`. After this, the ASR inference is run, printing the
words recognized from the input sample.

The profiling section of the log shows that for the ASR inference:

- *Ethos-U* PMU report:

  - 30,164,672 total cycle: The number of NPU cycles.

  - 30,164,330 active cycles: The number of NPU cycles that were used for computation.

  - 342 idle cycles: The number of cycles for which the NPU was idle.

  - 8,895,431 AXI0 read beats: The number of AXI beats with read transactions from the AXI0 bus. AXI0 is the bus where
    the *Ethos-U* NPU reads and writes to the computation buffers, activation buf, or tensor arenas.

  - 1,890,168 AXI0 write beats: The number of AXI beats with write transactions to AXI0 bus.

  - 1,740,069 AXI1 read beats: The number of AXI beats with read transactions from the AXI1 bus. AXI1 is the bus where
    the *Ethos-U55* NPU reads the model. So, read-only.

- For FPGA platforms, a CPU cycle count can also be enabled. However, do not use cycle counters for FVP, as the CPU
  model is not cycle-approximate or cycle-accurate.

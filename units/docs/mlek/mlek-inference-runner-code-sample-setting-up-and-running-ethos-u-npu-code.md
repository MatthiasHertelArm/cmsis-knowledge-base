---
id: "mlek-inference-runner-code-sample-setting-up-and-running-ethos-u-npu-code"
type: "concept"
domain: "edge-ai"
title: "Inference Runner Code Sample: Setting up and running Ethos-U NPU code sample"
summary: "The FVP is available publicly from Arm Ecosystem FVP downloads."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/inference_runner.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/inference_runner.md#setting-up-and-running-ethos-u-npu-code-sample"
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

Once completed the building step, the application binary `mlek_inference_runner.axf` can be found in the `build/bin`
folder.

Assuming that the install location of the FVP was set to `~/FVP_install_location`, then the simulation can be started by
using:

```commandline
~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 -a ./bin/mps3-sse-300/mlek_inference_runner.axf
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

### Running Inference Runner

After the application has started the inference starts immediately and it outputs the results on the telnet terminal.

The following example illustrates application output:

```log
INFO - Final results:
INFO - Profile for Inference :
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 9332
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 3248
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 2219
INFO - NPU ACTIVE cycles: 33145
INFO - NPU IDLE cycles: 1033
INFO - NPU TOTAL cycles: 34178
```

After running an inference on randomly generated data, the output of the log shows the profiling results that for this
inference. For example:

- *Ethos-U* PMU report:

  - 34,178 total cycle: The number of NPU cycles.

  - 33,145 active cycles: The number of NPU cycles that were used for computation.

  - 1,033 idle cycles: The number of cycles for which the NPU was idle.

  - 9,332 AXI0 read beats: The number of AXI beats with read transactions from AXI0 bus. AXI0 is the bus where the
    *Ethos-U* NPU reads and writes to the computation buffers, activation buf, or tensor arenas.

  - 3,248 AXI0 write beats: The number of AXI beats with write transactions to AXI0 bus.

  - 2,219 AXI1 read beats: The number of AXI beats with read transactions from AXI1 bus. AXI1 is the bus where the
    *Ethos-U* NPU reads the model. So, read-only.

- For FPGA platforms, a CPU cycle count can also be enabled. However, do not use cycle counters for FVP, as the CPU
  model is not cycle-approximate or cycle-accurate.

### Building with dynamic model load capability

It is possible to build the inference runner application, targeting only the FVP environment, that allows
loading of the TFLite model file at runtime. In this build configuration, the model TFLite file is not
baked into the application but the application expects this model binary to be loaded at a specific address
by an external agent. This loading capability also extends to the input data for the model.

This feature depends on these addresses to be specified in target platform's CMake description and, by
default, is available for use on the MPS3 FVP platform.

> **Note:**: The application built with this support will not work on the FPGA. This capability is only
> provided for use with the FVP, to make it easier to try different ML workloads without having to build
> the applications with different TFLite files baked into the application statically.
> Also, this feature is not available for `native` target.

The parameter `inference_runner_DYNAMIC_MEM_LOAD_ENABLED` should be set to ON in the CMake configuration
command to enable this feature. For example, from a freshly created build directory, run:

```commandline
cmake .. \
  -Dinference_runner_DYNAMIC_MEM_LOAD_ENABLED=ON \
  -DUSE_CASE_BUILD=inference_runner
```

Once the configuration completes, running:

```commandline
make -j
```

will build the application that will expect the neural network model and the IFM to be loaded into
specific addresses. The default values for these addresses are defined in the use-case CMake file.

### Running the FVP with dynamic model loading

If the application has been built with dynamic loading capability, as described in the previous section,
the FVP can be invoked with command line parameters that will load specific data into memory. For example,
the command below loads a custom model at address `0x90000000`, a custom input from address `0x92000000`
and when the FVP exits, it dumps a file named `output.bin` with the output tensors consolidated into a
binary blob.

> **Note:** The CMake profile for the target should also give an indication of the maximum sizes for
> each of the regions. This is also mentioned in the linker scripts for the same target. For MPS3,
> the model size can be a maximum of 32MiB. The IFM and OFM spaces are both reserved as 16MiB sections.

```commandline
~/FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 \
  -a ./bin/mlek_inference_runner.axf \
  --data /path/to/custom-model.tflite@0x90000000 \
  --data /path/to/custom-ifm.bin@0x92000000 \
  --dump cpu0=/path/to/output.bin@Memory:0x93000000,1024
```

The above command will dump a 1KiB (1024 bytes) file with output tensors as a binary blob after it
has consumed the model and IFM data provided by the file paths specified and the inference is
executed successfully.
If the size of the output tensors is unknown before running the FVP, it can be run without the `--dump`
parameter to check the size of the output first by looking at the application log. Alternatively, a
size of 16MiB will dump the whole reserved section for the OFM to a file.

> **Note:**: When there are multiple input tensors, the application is set up to iterate over all of
> them and populate each of them, in sequence, with the required amount of data. The sequence in which
> these tensors are populated is governed by the index assigned to them within the TensorFlow Lite Micro
> framework. So, the input binary blob should be a consolidated file containing data for all the input
> tensors. The same packing is used for output binary dumps.

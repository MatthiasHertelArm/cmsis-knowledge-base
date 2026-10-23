---
id: "ethu-vela-examples"
type: "concept"
domain: "edge-ai"
title: "Vela: Examples"
summary: "The output directory contains the optimized ML model person_detect_vela.tflite and a report. The optimized model is for deployment to the Edge AI MCU."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#examples"
license: "Apache-2.0"
mode: "V"
---

### Compile for an Ethos-U reference system

```console
vela person_detect.tflite \
  --accelerator-config ethos-u55-128 \
  --config Arm/vela.ini \
  --system-config Ethos_U55_High_End_Embedded \
  --memory-mode Shared_Sram \
  --optimise Performance \
  --verbose-cycle-estimate
```

The `output` directory contains the optimized ML model `person_detect_vela.tflite` and a report.
The optimized model is for deployment to the Edge AI MCU.

The console output shows several details including configuration parameters, memory usage, and with `--verbose-cycle-estimate` a rough estimation of the inference time.

### Minimize peak SRAM

```console
vela keyword_spotting.tflite \
  --accelerator-config ethos-u55-64 \
  --optimise Size
```

`Size` scheduling favors tensor reuse and cascading. It can reread more weights
and reduce throughput, so measure both memory and performance.

### Set a performance-scheduler SRAM budget

```console
vela person_detect.tflite \
  --accelerator-config ethos-u55-128 \
  --optimise Performance \
  --arena-cache-size 61440
```

This supplies a 60 KiB cache budget. Reducing it may increase AXI1 traffic as
weights or feature-map data are reread. The reported `Total SRAM used` covers
the model's NPU-visible tensors and working buffers, not the RTOS, stacks,
application allocations, CPU kernels, or other firmware state.

### Compile TOSA for Ethos-U85 raw output

```console
vela my_network.tosa \
  --config Arm/vela.ini \
  --accelerator-config ethos-u85-256 \
  --system-config Ethos_U85_SYS_DRAM_High \
  --memory-mode Dedicated_Sram_384KB \
  --output-format raw
```

The resulting `.npz` contains the NPU command streams, constants, and
quantization metadata required by an integration that consumes raw compiler
output.

### Inspect placement and compiler decisions

```console
vela model.tflite \
  --accelerator-config ethos-u85-512 \
  --show-cpu-operations \
  --show-subgraph-io-summary \
  --verbose-config \
  --verbose-performance \
  --enable-debug-db
```

Start with focused reports. `--verbose-all` can produce impractically large
logs for representative ML models.

### Embed an optimized TFLite model in firmware

On hosts that provide `xxd`, convert the Vela compiler output to a C array:

```console
xxd -i output/my_network_vela.tflite my_network_model.h
```

Place the generated data in the linker region that matches the memory
configuration selected from `vela.ini`. Ensure that the ML inference runtime
registers the Ethos-U custom operator and uses an Ethos-U driver compatible with
the compiled command stream.

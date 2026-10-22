---
id: "ethu-integration-step-3-compile-and-inspect-the-ml-model"
type: "concept"
domain: "edge-ai"
title: "Integration: Tutorial: Create an Ethos-U application / Step 3: Compile and inspect the ML model"
summary: "Part of: Tutorial: Create an Ethos-U application"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/integration/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/integration/src/main.md#step-3-compile-and-inspect-the-ml-model"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tutorial: Create an Ethos-U application_

#### Update ML models of the example

The example contains the original quantized TensorFlow Lite models and Vela
output compiled for the original Ethos-U55-128 configuration. Recompile each
quantized model for the Ethos-U55-256 configuration and the device-specific
system and memory mode that is reported in the generated `Test-Ethos-U55.cbuild-mlops.yml` file.

The generated `*.cbuild-mlops.yml` file is the handoff point between
CMSIS-Toolbox and the ML model compilation step. It contains the device-specific
`vela.ini`, accelerator selection, system configuration, memory mode, optional
Vela arguments, and model selection.

#### Compile with an MLOps conversion script

The `Test-Ethos-U` example provides one conversion script that consumes the
generated MLOps file:

```console
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml
```

The script reads the generated MLOps file, runs Vela for each selected model,
emits the Vela-compiled `_vela.tflite` file, regenerates the C array
used by the application, and writes `VELA_SUMMARY.md`.

This script is example integration code, not the only supported MLOps flow.
Projects may replace it with their own training, quantization, validation,
artifact signing, packaging, or CI pipeline, provided that the pipeline consumes
the same generated Vela settings and produces the model artifacts expected by
the application.

#### Compile manually with Vela

For debugging, CI bring-up, or custom MLOps integrations, the same values can be
applied directly to Vela. Inspect `Test-Ethos-U55.cbuild-mlops.yml` and use its
`vela.ini`, `vela.options`, and model path when constructing the command. See
[MLOps Information](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information).

```console
vela Model/tiny_cnn/tiny_cnn_int8.tflite \
  --accelerator-config ethos-u55-256 \
  --config .cmsis/ensemble_vela.ini \
  --system-config RTSS_HP_SRAM_MRAM \
  --memory-mode Shared_Sram \
  --optimise Performance \
  --output-dir Model/tiny_cnn \
  --verbose-config
```

See Vela for details about command-line options.
Options such as `--optimise Size` can be added with the `mlops.vela.misc:`
control in the `*.csolution.yml` file.

Whether using the example script or a custom/manual flow, repeat compilation for
every quantized model in the model layer. Replace the previous Vela output used
by the application and regenerate its embedded C data if the project stores the
model as a C array. Keep the original quantized `.tflite` file as the portable
input; the `_vela.tflite` output is specific to the selected Ethos-U and memory
configuration. For more information about this handoff, see
[MLOps Information](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information).

#### Add application ML model

The supplied `ML-MyModels.clayer.yml` has the layer type `ML-Model`. It selects
the TensorFlow Lite Micro and Ethos-U kernel components and adds the model files
to the application. The layer contains:

- `model_data.h`, which declares the embedded models;
- `arena.c`, which reserves the shared tensor arena; and
- one directory per model with the original quantized `.tflite` file, the
  Vela-compiled `_vela.tflite` file, and the generated C array used by the
  application.

To use an application-specific model, copy or modify this layer, add the new
model files to its `groups:` node, and set `model.clayer` in the solution's
`mlops:` node to the resulting layer.

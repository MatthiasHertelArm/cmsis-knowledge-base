---
id: "ethint-cmsis-ethos-u-integration-example-integrate-a-new-model"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example: Integrate a new model"
summary: "2. Convert the model. Add <name>/<model>.tflite to the target solution's mlops.model.name list (relative to mlops.model.dir: ./ML). Open or build the solution to regenerate its MLOps file, then run, for example:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/README.md#integrate-a-new-model"
license: "Apache-2.0"
mode: "V"
---

Use an existing model as a template:

1. **Prepare the files.** Create `Model/<name>/` with the original quantized
   `.tflite`, reference input/output C arrays and header, and a brief README.

2. **Convert the model.** Add `<name>/<model>.tflite` to the target solution's
   `mlops.model.name` list (relative to `mlops.model.dir: ./ML`). Open or build
   the solution to regenerate its MLOps file, then run, for example:

   ```sh
   python script/model-converter.py Test-Ethos-U85.cbuild-mlops.yml
   ```

   The [converter](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/script/README.md) generates the compiled `.tflite`, model C
   array, and `VELA_SUMMARY.md`. Confirm zero CPU operators and review memory use.

3. **Register the files.** In `Model/ML-MyModels.clayer.yml`, add a model group
   listing those generated files, reference sources/header, original `.tflite`,
   and README. Add a unique define such as `MODEL_MY_MODEL`.

4. **Describe the test.** In `Source/app_main.cpp`, under that define, include
   the reference header, declare the generated model array, and initialize a
   `ModelData_Int8` with its name, model, input, expected output, buffer sizes,
   allowed error in quantized steps, and optional argmax check.

5. **Call the test.** Add `TestModel_Int8(Model_My_Model)` under the same
   `#if defined(MODEL_MY_MODEL)` guard, between the existing `TestInitialize()`
   and `TestSummary()` calls. Tests must run sequentially to share the arena.

6. **Build and validate.** Check that the model and arena fit NPU-accessible
   memory; increase `TENSOR_ARENA_SIZE` in `Source/model_test.cpp` if needed,
   allowing for TFLM metadata and scratch. Build for the matching AppKit-E8 NPU,
   load and run, and confirm the new model's `PASS` and final
   `TEST RESULT: PASS` on UART4.

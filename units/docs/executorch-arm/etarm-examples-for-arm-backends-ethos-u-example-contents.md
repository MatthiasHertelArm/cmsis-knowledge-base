---
id: "etarm-examples-for-arm-backends-ethos-u-example-contents"
type: "concept"
domain: "edge-ai"
title: "Examples for Arm backends Ethos-U, VGF and Cortex-M: Example Contents"
summary: "Examples for Arm backends Ethos-U, VGF and Cortex-M: Example Contents"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/README.md#example-contents"
license: "BSD-3-Clause"
mode: "V"
---

### Notebook examples

- [ethos_u_minimal_example.ipynb](https://github.com/pytorch/executorch/blob/658390c/examples/arm/ethos_u_minimal_example.ipynb) - Minimal
  Ethos-U AOT, runtime build, and FVP execution flow.
- [vgf_minimal_example.ipynb](https://github.com/pytorch/executorch/blob/658390c/examples/arm/vgf_minimal_example.ipynb) - Minimal VGF
  lowering and host execution flow.
- [cortex_m_mv2_example.ipynb](https://github.com/pytorch/executorch/blob/658390c/examples/arm/cortex_m_mv2_example.ipynb) - Cortex-M
  MobileNetV2 export, quantization, runtime build, and FVP execution flow.
- [pruning_minimal_example.ipynb](https://github.com/pytorch/executorch/blob/658390c/examples/arm/pruning_minimal_example.ipynb) - Model
  conditioning and pruning flow for Ethos-U85.
- [quantizer_tutorial.ipynb](https://github.com/pytorch/executorch/blob/658390c/examples/arm/quantizer_tutorial.ipynb) - Quantizer tutorial
  for TOSA, Ethos-U, and VGF quantizers.

### Application examples

- [minimal_classic_ml](https://github.com/pytorch/executorch/blob/658390c/examples/arm/minimal_classic_ml/) - Minimal single-shot runtime
  integration, intended for models such as MobileNetV2 and YOLO.
- [image_classification_example_ethos_u](https://github.com/pytorch/executorch/blob/658390c/examples/arm/image_classification_example_ethos_u/)
  - End-to-end DEiT-Tiny image classification flow for Ethos-U, including
  model fine-tuning, export, bare-metal runtime build, and Corstone-320 FVP
  execution.
 - [mobilesam_prompt_segmentation_example_ethos_u](https://github.com/pytorch/executorch/blob/658390c/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/)
   - End-to-end MobileSAM prompt segmentation flow for Ethos-U, including
   export, quantization, debug mask generation, bare-metal runtime build, and
   Corstone-320 FVP execution.
 - [image_classification_example_vgf](https://github.com/pytorch/executorch/blob/658390c/examples/arm/image_classification_example_vgf/) -
  DEiT-Tiny image classification flow for VGF host execution.
- [super_resolution_example_vgf](https://github.com/pytorch/executorch/blob/658390c/examples/arm/super_resolution_example_vgf) - Swin2SR image
  super-resolution.
- [example_modules/add.py](https://github.com/pytorch/executorch/blob/658390c/examples/arm/example_modules/add.py) - Small external model file
  usable with `run.sh --model_name=examples/arm/example_modules/add.py`.

### Utility examples and guides

- [executor_runner](https://github.com/pytorch/executorch/blob/658390c/examples/arm/executor_runner/) - Advanced test and diagnostic runner for
  BundleIO, ETDump, profiling, semihosted files, and backend regression tests.
- [ethos-u-porting-guide.md](https://github.com/pytorch/executorch/blob/658390c/examples/arm/ethos-u-porting-guide.md) - Notes for adapting
  the example Ethos-U runtime integration to another target.
- [model-explorer.md](https://github.com/pytorch/executorch/blob/658390c/examples/arm/model-explorer.md) - Visualize PTE and TOSA graphs and
  overlay per-operator Ethos-U cycle data collected from an FVP PMU trace.
- [export_standalone_tosa_graph.py](https://github.com/pytorch/executorch/blob/658390c/examples/arm/export_standalone_tosa_graph.py) -
  Example of exporting a standalone TOSA graph with multiple outputs.
- [visualize.py](https://github.com/pytorch/executorch/blob/658390c/examples/arm/visualize.py) - Helper used by `run.sh --model_explorer` to
  visualize TOSA or PTE graphs.

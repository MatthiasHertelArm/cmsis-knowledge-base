---
id: "alp-observing-ethos-u-on-alif-4-model-export-add-calibration-input"
type: "concept"
domain: "edge-ai"
title: "4 model export: Add calibration input"
summary: "The model is exported with int8 quantization, so the compiler needs a representative MNIST input during export."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export/#add-calibration-input"
license: "CC-BY-SA-4.0"
mode: "V"
---

The model is exported with int8 quantization, so the compiler needs a representative MNIST input during export. 

This input is not the image that runs on the board. It's used only to set quantization ranges when generating the `.pte` file.

Download the calibration sample:
```bash
curl -L -o /home/developer/output/sample_one.pt https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/sample_one.pt
```

The downloaded sample contains one normalized MNIST-style grayscale image, saved as a PyTorch tensor (`.pt`) with shape `[1, 1, 28, 28]` and type `float32`. 
This allows `mnist_model.py` to load the exact format it needs without any image preprocessing step.

For production-quality quantization, you'd normally calibrate with a larger and more diverse set of representative inputs. To keep the export flow small and reproducible, you'll use one sample.

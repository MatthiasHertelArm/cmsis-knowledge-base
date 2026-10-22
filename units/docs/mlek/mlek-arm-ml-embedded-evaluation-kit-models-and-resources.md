---
id: "mlek-arm-ml-embedded-evaluation-kit-models-and-resources"
type: "concept"
domain: "edge-ai"
title: "Arm® ML embedded evaluation kit: Models and resources"
summary: "The TensorFlow Lite models used in the use-cases implemented in this project can be downloaded from:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/documentation.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/documentation.md#models-and-resources"
license: "Apache-2.0"
mode: "V"
---

### TensorFlow Lite models

The TensorFlow Lite models used in the use-cases implemented in this project can be downloaded from:

- [Arm ML-Zoo](https://github.com/ARM-software/ML-zoo) ( [Apache 2.0 License](https://github.com/ARM-software/ML-zoo/blob/master/LICENSE) )
  - [Mobilenet V2](https://github.com/ARM-software/ML-zoo/tree/e0aa361b03c738047b9147d1a50e3f2dcb13dbcb/models/image_classification/mobilenet_v2_1.0_224/tflite_int8)
  - [MicroNet for Keyword Spotting](https://github.com/ARM-software/ML-zoo/tree/9f506fe52b39df545f0e6c5ff9223f671bc5ae00/models/keyword_spotting/micronet_medium/tflite_int8)
  - [Wav2Letter](https://github.com/ARM-software/ML-zoo/tree/1a92aa08c0de49a7304e0a7f3f59df6f4fd33ac8/models/speech_recognition/wav2letter/tflite_pruned_int8)
  - [MicroNet for Anomaly Detection](https://github.com/ARM-software/ML-zoo/tree/7c32b097f7d94aae2cd0b98a8ed5a3ba81e66b18/models/anomaly_detection/micronet_medium/tflite_int8)
  - [MicroNet for Visual Wake Word](https://github.com/ARM-software/ML-zoo/raw/7dd3b16bb84007daf88be8648983c07f3eb21140/models/visual_wake_words/micronet_vww4/tflite_int8/vww4_128_128_INT8.tflite)
  - [RNNoise](https://github.com/ARM-software/ML-zoo/raw/a061600058097a2785d6f1f7785e5a2d2a142955/models/noise_suppression/RNNoise/tflite_int8/rnnoise_INT8.tflite)

- [Emza Visual Sense ModelZoo](https://github.com/emza-vs/ModelZoo) ( [Apache 2.0 License](https://github.com/emza-vs/ModelZoo/blob/v1.0/LICENSE) )
  - [YOLO Fastest](https://github.com/emza-vs/ModelZoo/blob/v1.0/object_detection/yolo-fastest_192_face_v4.tflite)

### ExecuTorch models

- [torchvision](https://docs.pytorch.org/vision/0.28/)
  - [MobileNet V2](https://docs.pytorch.org/vision/main/models/generated/torchvision.models.mobilenet_v2.html)

- [Hugging Face - PyTorch Image Models (timm)](https://huggingface.co/timm) ( [Apache 2.0 License](https://github.com/huggingface/pytorch-image-models/blob/main/LICENSE) )
  - [DeiT tiny](https://huggingface.co/timm/deit_tiny_patch16_224.fb_in1k)

- [Hugging Face - Arm](https://huggingface.co/Arm/)
  - [Conformer](https://huggingface.co/Arm/stt_en_conformer_executorch_small) ( [BigScience OpenRAIL-M v1.1](https://huggingface.co/Arm/stt_en_conformer_executorch_small/blob/main/LICENSE) )

### Vela compiler

When using *Ethos-U* NPU backend, Vela compiler optimizes the NN model. However, if not and it is supported by
TensorFlow Lite Micro, then it falls back on the CPU and executed.

(figure: Vela compiler)

The Vela compiler is a tool that can optimize a neural network model into a version that run on an embedded system
containing the *Ethos-U* NPU.

The optimized model contains custom operators for sub-graphs of the model that the *Ethos-U* NPU can accelerate. The
remaining layers that cannot be accelerated, are left unchanged, and are run on the CPU using optimized, `CMSIS-NN`, or
reference kernels provided by the inference engine.

For detailed information, see: [Optimize model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/./sections/building.md#Optimize-custom-model-with-Vela-compiler).

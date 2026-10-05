---
id: "alp-nav-mlek-sw-machine-learning-frameworks"
type: "concept"
domain: "edge-ai"
title: "Navigate Machine Learning development with Ethos-U processors: Software development considerations: Machine learning Frameworks"
summary: "LiteRT for Microcontrollers, formerly known as TensorFlow Lite for Microcontrollers is one of the more common framework for microcontroller ML applications."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/nav-mlek/sw.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/nav-mlek/sw/#machine-learning-frameworks"
license: "CC-BY-SA-4.0"
mode: "V"
---

[LiteRT for Microcontrollers](https://ai.google.dev/edge/litert/microcontrollers/overview), formerly known as TensorFlow Lite for Microcontrollers is one of the more common framework for microcontroller ML applications.

TensorFlow uses [`xxd`](https://linux.die.net/man/1/xxd/) to convert TensorFlow Lite models into C data structures. 

[PyTorch](https://pytorch.org/) is also commonly used on microcontrollers. 

[Apache TVM](https://tvm.apache.org/) is an open-source compiler framework for ML and can be used on microcontrollers.

The ML ecosystem is changing rapidly with many new companies and software. You can refer to the [AI Ecosystem Catalog](https://www.arm.com/partners/ai-ecosystem-catalog/) to find ML solutions for Cortex-M microcontrollers.

### Ethos optimized model

[Vela](https://pypi.org/project/ethos-u-vela/) is used to compile a TFLM neural network model into an optimized version that can run on hardware containing an Arm Ethos-U NPU.

Install it using `pip3`:

```console
pip install ethos-u-vela
```

### CMSIS-NN

The [CMSIS-NN](https://www.keil.com/pack/doc/CMSIS/NN/html/index.html) software library is a collection of efficient neural network kernels developed to maximize the performance and minimize the memory footprint of neural networks on Arm Cortex-M processors.

The library is used by frameworks for operations that cannot be executed on the Ethos processor.

[Accelerated inference on Arm microcontrollers with TensorFlow Lite for Microcontrollers and CMSIS-NN](https://blog.tensorflow.org/2021/02/accelerated-inference-on-arm-microcontrollers-with-tensorflow-lite.html) provides an excellent overview.

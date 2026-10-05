---
id: "cmlek-target-configuration-reference-app-reference-applications"
type: "concept"
domain: "edge-ai"
title: "Target Configuration Reference Application Hardware: Reference Applications"
summary: "The KWS template demonstrates real-time wake word detection:"
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:docs/target_configuration_refapp.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/docs/target_configuration_refapp.md#reference-applications"
license: "Apache-2.0"
mode: "V"
---

### Audio Template: Keyword Spotting

The KWS template demonstrates real-time wake word detection:

**Key Features:**

- Real-time audio preprocessing (MFCC feature extraction)
- Optimized neural network inference using CMSIS-NN
- Configurable wake word models
- Performance profiling and benchmarking

**Getting Started:**

1. Build and run the template on your target platform
2. Speak the wake word (e.g. "Yes" or "Up")
3. Observe detection results via UART output or LEDs
4. Replace the model with your custom wake word model

**Customization Points:**

- `kws/src/kws_model.cpp`: Replace with your TensorFlow Lite model
- `kws/src/audio_preprocessing.cpp`: Modify audio preprocessing pipeline  
- `kws/config/kws_config.h`: Adjust detection thresholds and parameters

### Video Template: Object Detection

The object detection template provides real-time computer vision:

**Key Features:**

- Camera input processing and frame buffering
- Object detection using MobileNet-based models
- Bounding box visualization
- Multi-object detection and classification

**Getting Started:**

1. Build and run the template with camera input
2. Point camera at objects for detection
3. View detection results on display or via debug output
4. Integrate your custom object detection model

**Customization Points:**

- `object-detection/src/detection_model.cpp`: Replace with your model
- `object-detection/src/image_preprocessing.cpp`: Modify image preprocessing
- `object-detection/config/detection_config.h`: Adjust detection parameters

### Generic Template: Inference Runner 
(available in pack version 1.0+)

The generic inference template provides maximum flexibility:

**Key Features:**

- Framework for any TensorFlow Lite model
- Configurable input/output tensors
- Performance benchmarking utilities
- Extensible architecture for custom applications

**Getting Started:**

1. Replace the example model with your TensorFlow Lite model
2. Configure input/output tensor specifications
3. Implement custom preprocessing/postprocessing
4. Build and test your custom ML application

**Customization Points:**

- `inference_runner/Model/`: Replace with your TensorFlow Lite model files
- `inference_runner/src/inference_runner.cpp`: Modify inference pipeline
- `inference_runner/config/`: Adjust model and application configuration

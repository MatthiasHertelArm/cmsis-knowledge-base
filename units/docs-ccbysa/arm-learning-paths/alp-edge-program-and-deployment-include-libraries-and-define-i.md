---
id: "alp-edge-program-and-deployment-include-libraries-and-define-i"
type: "concept"
domain: "edge-ai"
title: "define LED_PIN 2                            // Update the pin number to match the digital pin you intend to use for the LED: Include libraries and define infere"
summary: "This block sets up the core dependencies for running Edge Impulse inference on audio input. It includes the necessary libraries and defines a structure inference_t that holds the audio buffer and relevant state needed to manage sampling and inferencing."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/edge/program-and-deployment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/edge/program-and-deployment/#include-libraries-and-define-inference-data-structure"
license: "CC-BY-SA-4.0"
mode: "V"
---

This block sets up the core dependencies for running Edge Impulse inference on audio input. It includes the necessary libraries and defines a structure `inference_t` that holds the audio buffer and relevant state needed to manage sampling and inferencing.

```c
#include <Name_of_your_library_inferencing.h>  // Include the Edge Impulse inference SDK for running the model
#include <PDM.h>  // Include the Pulse Density Modulation (PDM) library for audio input

// Define a structure to store inference-related audio data
typedef struct {
    int16_t *buffer;       // Pointer to the audio sample buffer (16-bit signed integers)
    uint8_t buf_ready;     // Flag to indicate if the buffer is ready for inference (1 = ready)
    uint32_t buf_count;    // Number of audio samples currently in the buffer
    uint32_t n_samples;    // Total number of samples required for a complete inference
} inference_t;
```

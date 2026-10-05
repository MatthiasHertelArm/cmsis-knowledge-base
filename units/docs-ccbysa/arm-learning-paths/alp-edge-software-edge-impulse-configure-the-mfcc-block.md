---
id: "alp-edge-software-edge-impulse-configure-the-mfcc-block"
type: "concept"
domain: "edge-ai"
title: "Learn how to run AI on Edge devices using Arduino Nano RP2040: Train and deploy a TinyML audio classifier with Edge Impulse: Configure the MFCC block"
summary: "Next, you'll configure the MFCC (Mel Frequency Cepstral Coefficients) processing block. This block transforms raw audio into features suitable for training your model."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse/#configure-the-mfcc-block"
license: "CC-BY-SA-4.0"
mode: "V"
---

Next, you'll configure the **MFCC (Mel Frequency Cepstral Coefficients)** processing block. This block transforms raw audio into features suitable for training your model.

Click **MFCC** in the left-hand menu under the **Impulse design** section.

Set the parameters exactly as shown in the screenshot. These settings determine how the audio input is segmented and analyzed. Once complete, make sure to **save the parameters**.

These defaults are chosen for this Learning Path, but you can experiment with different values once you're more familiar with Edge Impulse.

(figure: Screenshot showing the MFCC configuration page in Edge Impulse with time and frequency parameters set for feature extraction alt-text#center)

**Note:**
The green-highlighted section on the MFCC configuration page provides an estimate of how the model will perform on the target device. This includes memory usage (RAM and flash) and latency, helping ensure the model fits within hardware constraints.

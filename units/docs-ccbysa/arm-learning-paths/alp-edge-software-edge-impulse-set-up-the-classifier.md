---
id: "alp-edge-software-edge-impulse-set-up-the-classifier"
type: "concept"
domain: "edge-ai"
title: "Learn how to run AI on Edge devices using Arduino Nano RP2040: Train and deploy a TinyML audio classifier with Edge Impulse: Set up the classifier"
summary: "Now it's time to configure the neural network classifier, which learns to recognize different audio commands. Click Classifier under Impulse design and set the parameters as shown in the screenshot."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse/#set-up-the-classifier"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now it's time to configure the **neural network classifier**, which learns to recognize different audio commands. Click **Classifier** under **Impulse design** and set the parameters as shown in the screenshot.

**Note:**
For this Learning Path, use a learning rate of `0.002` even though the screenshot shows `0.005`. You can experiment later, but `0.002` is a good starting point.


Once all parameters are set, click **Save and train** to begin training your model.

(figure: Screenshot showing the classifier configuration screen in Edge Impulse with neural network settings for audio classification alt-text#center)

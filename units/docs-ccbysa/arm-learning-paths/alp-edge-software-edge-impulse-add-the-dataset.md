---
id: "alp-edge-software-edge-impulse-add-the-dataset"
type: "concept"
domain: "edge-ai"
title: "Learn how to run AI on Edge devices using Arduino Nano RP2040: Train and deploy a TinyML audio classifier with Edge Impulse: Add the dataset"
summary: "With your device configured, the next step is to add your dataset to the project. Click Add existing data and follow the configuration settings shown in the screenshot."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse/#add-the-dataset"
license: "CC-BY-SA-4.0"
mode: "V"
---

With your device configured, the next step is to add your dataset to the project. Click **Add existing data** and follow the configuration settings shown in the screenshot. This lets you upload pre-recorded data instead of collecting it live, which can save time during development.

An example repository has been prepared with assets used throughout this Learning Path. You can clone it with the following command:

```bash
git clone https://github.com/e-dudzi/Learning-Path.git
```

The repository contains a `Dataset.zip` file with the dataset used in this project. Extract the contents to your local machine. For convenience, the dataset is already split into **training** and **testing** sets.

(figure: Screenshot showing the Edge Impulse interface with the Add existing data panel open, used to upload pre-recorded datasets alt-text#center)


**Note:**
Do not check the green highlighted area during upload. The dataset already includes metadata. Enabling that option may result in much slower upload times and is unnecessary for this project.


(figure: Screenshot showing the Data acquisition tab in Edge Impulse with uploaded samples organized by label alt-text#center)

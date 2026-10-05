---
id: "alp-avh-ppocr-overview-overview-of-optical-character"
type: "concept"
domain: "edge-ai"
title: "Deploy PaddlePaddle on Arm Cortex-M with Arm Virtual Hardware: Overview of OCR: Overview of optical character recognition (OCR)"
summary: "Optical character recognition (OCR) aims at recognizing the text content in a fixed image area. It is one of the key applications in the field of computer vision (CV)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_ppocr/overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_ppocr/overview/#overview-of-optical-character-recognition-ocr"
license: "CC-BY-SA-4.0"
mode: "V"
---

Optical character recognition (OCR) aims at recognizing the text content in a fixed image area. It is one of the key applications in the field of computer vision (CV).

OCR has been widely used in many industry scenarios such as ticket information extraction, manufacturing product traceability, and government medical document processing. 

Text recognition is a sub-task of OCR. It's the step after text detection in OCR's two-stage algorithm which converts image information into text information.

(figure: Sample image showing the word GREENGUARD in uppercase letters on a textured background, demonstrating a typical OCR text recognition input used for testing English character recognition models#center)


In this Learning Path, you'll learn how to apply deep learning (DL) to the OCR text recognition task and set up a development flow from model training to application deployment. 

You'll learn how to:
- Use [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) to obtain a trained English text recognition model
- Export the Paddle inference model 
- Compile the Paddle inference model with [TVMC](https://tvm.apache.org/docs/tutorial/tvmc_command_line_driver.html#sphx-glr-tutorial-tvmc-command-line-driver-py) for the target device
- Build a text recognition application and deploy it on the [Corstone-300 FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) with [Arm Cortex-M55](https://www.arm.com/products/silicon-ip-cpu/cortex-m/cortex-m55).

This project is a collaboration between Arm and Baidu to improve PaddlePaddle model deployment to Arm Cortex-M devices. This gives developers more choices by increasing the number of deep learning models supported on Cortex-M.

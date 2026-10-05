---
id: "alp-avh-ppocr-overview-pp-ocrv3"
type: "concept"
domain: "edge-ai"
title: "Deploy PaddlePaddle on Arm Cortex-M with Arm Virtual Hardware: Overview of OCR: PP-OCRv3"
summary: "PaddleOCR provides an OCR system named PP-OCR. This is a practical, ultra-lightweight OCR system created by the Baidu Paddle Team."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_ppocr/overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_ppocr/overview/#pp-ocrv3"
license: "CC-BY-SA-4.0"
mode: "V"
---

PaddleOCR provides an OCR system named PP-OCR. This is a practical, ultra-lightweight OCR system created by the Baidu Paddle Team. 

It is a two-stage OCR system, in which the text detection algorithm is called [DB](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/algorithm_det_db_en.md), and the text recognition algorithm is called [CRNN](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/algorithm_rec_crnn_en.md). 

As seen in Figure 2, the overall pipeline of PP-OCRv3 is similar to PP-OCRv2 with some further optimizations to the detection model and recognition model.

For example, the text recognition model introduces [SVTR](https://arxiv.org/abs/2205.00159) (Scene Text Recognition with a Single Visual Model) based on PP-OCRv2. The model also uses [GTC](https://arxiv.org/pdf/2002.01276.pdf) (Guided Training of CTC) to guide training and model distillation. For more details, refer to the PP-OCRv3 [technical report](https://arxiv.org/abs/2206.03001v2).

(figure: Architecture diagram showing the PP-OCRv3 pipeline with text detection and recognition stages, including SVTR-based recognition model improvements over PP-OCRv2#center)

In the next section, you'll deploy a trained PP-OCR text recognition model on the Arm Corstone-300 FVP.

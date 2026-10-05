---
id: "alp-training-inference-pytorch-fine-tune-2-about-the-script"
type: "concept"
domain: "edge-ai"
title: "Edge AI on Arm: PyTorch and ExecuTorch rock-paper-scissors: Train and Test the rock-paper-scissors Model: Build the model / About the script"
summary: "The script handles the entire workflow: data generation, model training, and a simple command-line game."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fine-tune-2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fine-tune-2/#about-the-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Build the model_

The script handles the entire workflow: data generation, model training, and a simple command-line game.

- Synthetic Data Generation: the script includes a function `render_rps()` that generates 28x28 grayscale images of the letters 'R', 'P', and 'S' with random rotations, blurs, and noise. This creates a diverse dataset that's used to train the model.
- Model Architecture: the model, a TinyRPS class, is a simple Convolutional Neural Network (CNN). It uses a series of 2D convolutional layers, followed by pooling layers to reduce spatial dimensions, and finally, fully connected linear layers to produce a final prediction. This architecture is efficient and well-suited for edge devices.
- Training: the script generates synthetic training and validation datasets. It then trains the CNN model using the **Adam optimizer** and **Cross-Entropy Loss**. It tracks validation accuracy and saves the best-performing model to `rps_best.pt`.
- ExecuTorch Export: a key part of the script is the `export_to_pte()` function. This function uses the `torch.export module` (or a fallback) to trace the trained PyTorch model and convert it into an ExecuTorch program (`.pte`). This compiled program is highly optimized for deployment on any target hardware, for example Cortex-M or Cortex-A CPUs for embedded devices.
- CLI Mini-Game: after training, you can play an interactive game. The script generates an image of your move and a random opponent's move. It then uses the trained model to classify both images and determines the winner based on the model's predictions.

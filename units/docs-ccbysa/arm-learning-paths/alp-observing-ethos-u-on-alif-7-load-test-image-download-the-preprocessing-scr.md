---
id: "alp-observing-ethos-u-on-alif-7-load-test-image-download-the-preprocessing-scr"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Process and copy a sample image into the Alif E8 CMSIS project: Download the preprocessi"
summary: "The MNIST model expects one grayscale 28 × 28 image. You'll use a preprocessing script to resize the image, convert it to grayscale, scale pixel values to the range 0 to 127, and write the result to input_mnist.h."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image/#download-the-preprocessing-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

The MNIST model expects one grayscale 28 × 28 image. You'll use a preprocessing script to resize the image, convert it to grayscale, scale pixel values to the range 0 to 127, and write the result to `input_mnist.h`.

Download `prepare_mnist_image.py` into the image directory:

```bash
cd ~/mnist_alif/image
curl -o prepare_mnist_image.py https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/prepare_mnist_image.py
```
Open `prepare_mnist_image.py` and inspect.

The script defines command-line arguments, checks that the input image exists, then converts the image to 28 × 28 grayscale pixels. It also handles image inversion so black-on-white images can be converted to the white-on-black style used by MNIST.

The key conversion step scales each pixel into a value within the non-negative int8 range (0 to 127) and flattens the output into a one-dimensional array:
```python
pixels = np.clip(np.rint(pixels * 127.0 / 255.0), 0, 127).astype(np.int8)
flat = pixels.reshape(-1)
```
The generated header will contain a total of 784 values, one for each pixel in the 28 × 28 input image.

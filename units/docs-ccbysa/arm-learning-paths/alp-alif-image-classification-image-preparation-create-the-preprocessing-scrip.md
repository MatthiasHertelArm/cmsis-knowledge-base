---
id: "alp-alif-image-classification-image-preparation-create-the-preprocessing-scrip"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Prepare a test image: Create the preprocessing script"
summary: "Create a directory for the image and script:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation/#create-the-preprocessing-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create a directory for the image and script:

```bash
mkdir -p ~/alif/image
```

Place a test image in this directory. You can use any JPEG or PNG image. This Learning Path uses the provided `cat.jpg` image as the example:

(figure: Test image of a cat used for classification#center)

Create a file called `image/prepare_image.py` with the following content:

```python
from PIL import Image
import numpy as np

IMG_SIZE = 224

img = Image.open("cat.jpg").convert("RGB")
img = img.resize((IMG_SIZE, IMG_SIZE))

x = np.asarray(img).astype(np.float32)

# ImageNet normalization
mean = np.array([0.485, 0.456, 0.406]) * 255
std  = np.array([0.229, 0.224, 0.225]) * 255
x = (x - mean) / std

# HWC -> CHW
x = np.transpose(x, (2, 0, 1))

# Quantize to int8
x = np.clip(x, -128, 127).astype(np.int8)

# Emit C array
with open("input_image.h", "w") as f:
    f.write("#include <stdint.h>\n\n")
    f.write("const int8_t input_image[3][224][224] = {\n")
    for c in range(3):
        f.write("{\n")
        for row in x[c]:
            f.write("{" + ",".join(map(str, row)) + "},\n")
        f.write("},\n")
    f.write("};\n\n")
    f.write("const unsigned int input_image_len = 3 * 224 * 224;\n")
```

The script resizes the image to 224 x 224 pixels and applies ImageNet normalization by subtracting the dataset mean and dividing by the standard deviation. It then transposes the layout from HWC (height, width, channels) to CHW (channels, height, width) format. The batch dimension is added later in the application. Finally, it quantizes the values to int8 range (-128 to 127) and writes the pixel data to a C header as a constant array.

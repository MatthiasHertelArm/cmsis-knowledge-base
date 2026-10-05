---
id: "alp-observing-ethos-u-on-alif-4-model-export-download-the-model-files"
type: "concept"
domain: "edge-ai"
title: "4 model export: Download the model files"
summary: "To export an MNIST PyTorch model to ExecuTorch .pte format, start by downloading the model files."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export/#download-the-model-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

To export an MNIST PyTorch model to ExecuTorch `.pte` format, start by downloading the model files. 

**Note:**
If you're using the provided `.pte` file instead, skip the entire model export section and proceed with [Prepare firmware artifacts](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/).


From inside your container, create the model and output directories:

```bash
# Create directories (use full paths, not ~)
mkdir -p /home/developer/models
mkdir -p /home/developer/output
```

Download the model script and the training script:

```bash
curl -L -o /home/developer/models/mnist_model.py https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/mnist_model.py
curl -L -o /home/developer/models/train_mnist.py https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/train_mnist.py
```

The model script (`mnist_model.py`) defines a small convolutional network for 28 × 28 grayscale MNIST images. It has two convolution blocks followed by two fully connected layers:
```python
def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        # Fully Connected Layers
        self.fc1 = nn.Linear(32 * 7 * 7, 64)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(64, 10)
```
The convolution layers extract image features such as strokes, edges, and digit shapes. Each output channel from a convolution is called a feature map.

Layer 1 (`fc1`) takes in 32 feature maps of size 7 x 7 each, and reduces those values to 64 features. The final layer (`fc2`) then maps those 64 features to 10 digit scores (0 to 9).

The same file also exposes the objects expected by the ExecuTorch ahead-of-time compiler:
```python
ModelUnderTest = MNISTModel() # PyTorch model to export
ModelInputs = (load_calibration_input(),) 
```

The training script, however, downloads the [MNIST dataset](https://datasetsearch.research.google.com/search?query=mnist&docid=L2cvMTF0ZGh0cHRmMA%3D%3D), normalizes the images, trains the model, and saves the trained weights to `/home/developer/models/mnist_model.pth`.
<!-- **Note:**
The model input is a normalized float32 tensor with shape [1, 1, 28, 28]. The output is 10 logits, one for each digit from 0 to 9.
 -->

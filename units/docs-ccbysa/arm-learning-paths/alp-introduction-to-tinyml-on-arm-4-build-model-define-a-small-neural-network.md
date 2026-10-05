---
id: "alp-introduction-to-tinyml-on-arm-4-build-model-define-a-small-neural-network"
type: "concept"
domain: "edge-ai"
title: "4 build model: Define a small neural network using Python"
summary: "With your development environment set up, you can create a simple PyTorch model to test the setup."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model/#define-a-small-neural-network-using-python"
license: "CC-BY-SA-4.0"
mode: "V"
---

With your development environment set up, you can create a simple PyTorch model to test the setup.

This example defines a small feedforward neural network for a classification task. The model consists of two linear layers with ReLU activation in between.

Use a text editor to create a file named `simple_nn.py` with the following code:

```python
import torch
from torch.export import export
from executorch.exir import to_edge

# Define a simple Feedforward Neural Network
class SimpleNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Create the model instance
input_size = 10   # example input feature size
hidden_size = 5   # hidden layer size
output_size = 2   # number of output classes

model = SimpleNN(input_size, hidden_size, output_size)

# Example input tensor (batch size 1, input size 10)
x = (torch.randn(1, input_size),)

# Add arguments to be parsed by the Ahead-of-Time (AoT) Arm compiler
ModelUnderTest = model
ModelInputs = x

print("Model successfully exported to simple_nn.pte")
```

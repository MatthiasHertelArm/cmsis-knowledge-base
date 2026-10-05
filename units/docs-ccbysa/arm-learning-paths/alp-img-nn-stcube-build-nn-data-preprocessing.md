---
id: "alp-img-nn-stcube-build-nn-data-preprocessing"
type: "concept"
domain: "edge-ai"
title: "build nn: Data preprocessing"
summary: "To create the NN model, there are certain data pre-processing steps that need to be performed."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/img_nn_stcube/build_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/img_nn_stcube/build_nn/#data-preprocessing"
license: "CC-BY-SA-4.0"
mode: "V"
---

To create the NN model, there are certain data pre-processing steps that need to be performed.

First, open the Jupyter Notebook through an Anaconda Prompt.

```console
jupyter notebook
```
Open `lab.ipynb` from the extracted project files folder on the notebook.

Execute (click `Run`) the first code block to import the required packages:
```python
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D, 
BatchNormalization, Activation

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import random

from PIL import Image

import os
```

Next, load the `CIFAR-10` dataset. TensorFlow provides an API for downloading well-known datasets, such as CIFAR-10 and MNIST. Execute the next code block to get the dataset.

```python
# Load data from TF Keras
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# CIFAR10 class names
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 
'Horse', 'Ship', 'Truck']
num_classes = len(class_names)
```

Then, you will save one image per class from the test set for testing with the board later. Execute the following code block to save the images.

```python
path_images = "./Data/images/"

# Create directory
if not os.path.exists(path_images):
 os.mkdir(path_images)

# Save one image per class 
ext=".jpg"
for image_index in range(0,100):
 im = Image.fromarray(x_test[image_index])
 im.save("./images/"+str(class_names[int(y_test[image_index])])+ext)
```

This code block below will visualize the saved images.

```python
# Show saved images
files = os.listdir(path_images) 
for img in files:
 if os.path.splitext(img)[1] == ext and os.path.splitext(img)[0] in class_names:
 #print(os.path.splitext(img)[0])
 plt.subplot(2,5,class_names.index(os.path.splitext(img)[0])+1)
 plt.xticks([])
 plt.yticks([])
 plt.grid(False)
 plt.imshow(mpimg.imread(path_images+img),)
 plt.xlabel(os.path.splitext(img)[0])
plt.show()
```

The expected output is shown below

(figure: output1)

Next, normalize all the training and testing data to have values between 0 and 1. This normalization facilitates machine learning. Each RGB value ranges from 0 to 255, so divide the training and testing data by 255.

```python
# Normalize pixel values to be between 0 and 1
x_train = x_train.astype(np.float32)/255
x_test = x_test.astype(np.float32)/255
# Convert class vectors to binary class matrices.
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)
# Print arrays shape
print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print('x_test shape:', x_test.shape)
print('y_test shape:', y_test.shape)
```

The expected output is shown below:

```output
x_train shape: (50000, 32, 32, 3)
y_train shape: (50000, 10)
x_test shape: (10000, 32, 32, 3)
y_test shape: (10000, 10)
```

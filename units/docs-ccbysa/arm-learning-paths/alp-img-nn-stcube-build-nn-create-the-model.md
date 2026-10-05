---
id: "alp-img-nn-stcube-build-nn-create-the-model"
type: "concept"
domain: "edge-ai"
title: "Build and run an image classification NN model on an STM32L4 Discovery board: Build an image classification NN model trained with the CIFAR-10 dataset: Create t"
summary: "You are going to create a small convolutional neural network for image classification. The image size of CIFAR10 is 32 by 32, and the number of color channels is 3."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/img_nn_stcube/build_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/img_nn_stcube/build_nn/#create-the-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

You are going to create a small convolutional neural network for image classification. The image size of CIFAR10 is 32 by 32, and the number of color channels is 3. So, the input shape of the first convolution layer is (32, 32, 3). Since the number of classes is 10, so the last dense layer should have 10 units.

Here is an image illustrating the network architecture. Note that only convolution and dense layers are illustrated in this image.

(figure: output2)

Execute the code blocks below to create a sequential model and add the layers

```python
# Hyperparameters
batch_size = 32
num_classes = len(class_names)
epochs = 1
img_rows, img_cols = x_train.shape[1], x_train.shape[2]
input_shape = (x_train.shape[1], x_train.shape[2], 1)
```

```python
# Creating a Sequential Model and adding the layers
model = Sequential()
model.add(Conv2D(16, (3, 3), padding='same', input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(16, (3, 3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=(2, 2)))
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=(2, 2)))
model.add(Dropout(0.3))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=(2, 2)))
model.add(Dropout(0.4))
model.add(Flatten())
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10)) #The number of classes
model.add(Activation('softmax'))
```

Execute the code blocks below to compile and train the model. If tens of epochs are used, the training might take more than 10 hours because the dataset has 50,000 training images. Therefore, the model trained for 50 epochs is provided for testing (File: ‘Data/models/cifar10_model.h5’). You can use the model if you don't have enough time to train your own model. 

```python
# Check model structure and the number of parameters
model.summary()
# Let's train the model using Adam optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam', 
metrics=['accuracy'])
# Train model
history = model.fit(x=x_train,
 y=y_train,
 batch_size=batch_size,
 epochs=epochs, 
 validation_data=(x_test, y_test))
```

Save the model and evaluate the model. Note that since the model was trained for 1 epoch only, the accuracy would not be that good. Please try a larger number of epochs later to obtain better performance.

```python
# Save keras model
path_models = "./Data/models/"
path_keras_model = path_models + "own_cifar10_model.h5"
# Create directory
if not os.path.exists(path_models):
 os.mkdir(path_models)
model.save(path_keras_model)
# Score trained model.
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
```

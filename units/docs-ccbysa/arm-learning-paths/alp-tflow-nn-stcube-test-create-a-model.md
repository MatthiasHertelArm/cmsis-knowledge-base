---
id: "alp-tflow-nn-stcube-test-create-a-model"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Train the model: Create a model"
summary: "Now you will train a multi-layer perceptron model with the dataset. Define a multi-layer perceptron model with 3 dense layers."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test/#create-a-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now you will train a multi-layer perceptron model with the dataset. Define a multi-layer perceptron model with 3 dense layers.

```python
x_train, y_train = sklearn.utils.shuffle(np.array(data), np.array(labels))
y_train = tf.keras.utils.to_categorical(y_train, len(np.unique(y_train)))

model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=(3, stride)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(30, activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(len(np.unique(y_train)), activation="softmax")
        ]
    )

model.summary()
```
This step will output a report showing there are `3392` parameters in total.
```output
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 flatten (Flatten)           (None, 90)                0         
 dense (Dense)               (None, 30)                2730      
 dropout (Dropout)           (None, 30)                0         
 dense_1 (Dense)             (None, 20)                620       
 dropout_1 (Dropout)         (None, 20)                0         
 dense_2 (Dense)             (None, 2)                 42        
=================================================================
Total params: 3,392
Trainable params: 3,392
Non-trainable params: 0
```

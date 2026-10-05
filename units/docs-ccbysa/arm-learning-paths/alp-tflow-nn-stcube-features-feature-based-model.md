---
id: "alp-tflow-nn-stcube-features-feature-based-model"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Feature extraction: Feature based model"
summary: "Create a new multi-layer perceptron model for the features. The new model has 1592 parameters because it uses a smaller input than the previous model. Train the model and check the accuracy."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/features.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/features/#feature-based-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create a new multi-layer perceptron model for the features. The new model has `1592` parameters because it uses a smaller input than the previous model. Train the model and check the accuracy. 

```python
x_train, y_train = sklearn.utils.shuffle(np.array(feature_data), np.array(feature_labels))
y_train = tf.keras.utils.to_categorical(y_train, len(np.unique(y_train)))

data_shape = x_train[0].shape
model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=data_shape),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(data_shape[0] * data_shape[1], activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation="relu"),
            tf.keras.layers.Dense(len(np.unique(y_train)), activation="softmax")
        ]
    )

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
```
```python
model.fit(x_train, y_train, batch_size=32, epochs=500, validation_split=0.4)
```

You see the accuracy improved with the feature extraction. Test the new model with this code block to check if the model generates better results. 

```python
input('Press Enter once MCU is ready')
line = ser.readline()
lineList = convert_to_list(str(line))
new_df = convert_list_to_df(lineList)
print('New data acquired:\n', new_df.describe())

x = new_df['X'].to_numpy()
y = new_df['Y'].to_numpy()
z = new_df['Z'].to_numpy()

# Mean feature
x_mean_ext = np.array([np.mean(x[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
y_mean_ext = np.array([np.mean(y[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
z_mean_ext = np.array([np.mean(z[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
# STD feature
x_std_ext = np.array([np.std(x[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
y_std_ext = np.array([np.std(y[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])
z_std_ext = np.array([np.std(z[i:i + slidingWindowExt]) for i in range(0, stride, slidingWindowExt)])

inf_data = np.array([x_mean_ext, y_mean_ext, z_mean_ext, x_std_ext, y_std_ext, z_std_ext])
# For inference, explicitly tell that the data has a batch size of 1
plot_single_feature_sample(data_sample=inf_data)
inf_data = inf_data.reshape((1, data_shape[0], data_shape[1]))

pred = model.predict(inf_data)
print('Model Prediction: ', np.argmax(pred))
```

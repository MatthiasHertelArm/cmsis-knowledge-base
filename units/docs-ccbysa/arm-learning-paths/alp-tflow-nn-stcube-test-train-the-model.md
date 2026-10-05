---
id: "alp-tflow-nn-stcube-test-train-the-model"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Train the model: Train the model"
summary: "Plot the training and validation accuracy over epoch."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test/#train-the-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

Train the model for 200 epochs.
```python
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, y_train, batch_size=1, epochs=200, validation_split=0.4)

model.save('raw_model.h5')
```
### Plot the training accuracy

Plot the training and validation accuracy over epoch.
```python
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')

plt.figure()
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1000])
plt.legend(loc='lower right')
```
In this example, see that the training and validation accuracy start to converge after around 150 epochs. This means that the 200 epochs are enough to train the model. If you train the model for too many epochs, then the validation accuracy may drop due to overfitting. If you experience this, re-run [training](#train) with an appropriate epoch value.

(figure: output2)

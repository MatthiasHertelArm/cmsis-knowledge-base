---
id: "alp-tflow-nn-stcube-test-investigate-learning-rate-opti"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Train the model: Investigate learning rate (optional)"
summary: "For training the model, you used the default learning rate. But how will the model change with different learning rates?"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test/#investigate-learning-rate-optional"
license: "CC-BY-SA-4.0"
mode: "V"
---

For training the model, you used the default learning rate. But how will the model change with different learning rates? If the learning rate is too high, the model is more likely to overshoot the minima, meaning that the model cannot converge to the minima. On the other hand, if the learning rate is too low, the model reaches the minima too slowly, requiring more training time.

First try a high learning rate. Here, you set the learning rate of the optimizer as 1000. Execute the code block. This graph shows the training and validation loss values over epoch. You can see that the loss values fluctuate a lot so the model has difficulty in reaching the minima.

```python
# High learning rate (lr = 1000)
model_hlr = tf.keras.models.clone_model(model)

optimizer = tf.optimizers.Adam(learning_rate = 1000)
model_hlr.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history = model_hlr.fit(x_train, y_train, batch_size=32, epochs=100, validation_split=0.4)

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1000])
plt.legend(loc='lower right')
```
Expected output shown below:

(figure: output3)

Now try a lower learning rate, which is 0.0001. Execute the code block. The graph shows the training and validation loss values decrease much more slowly. So, it is important to use a proper learning rate in training.

```python
# Low learning rate (lr = 0.0001)
model_llr = tf.keras.models.clone_model(model)

optimizer = tf.optimizers.Adam(learning_rate = 0.0001)
model_llr.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history = model_llr.fit(x_train, y_train, batch_size=32, epochs=100, validation_split=0.4)

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1000])
plt.legend(loc='lower right')
```

Expected output shown below:

(figure: output4)

With the model trained, you are now ready to test it.

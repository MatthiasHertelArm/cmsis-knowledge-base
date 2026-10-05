---
id: "alp-tflow-nn-stcube-test-test-the-model"
type: "concept"
domain: "edge-ai"
title: "test: Test the model"
summary: "To test the model you trained, run the code block shown below."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/test/#test-the-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

To test the model you trained, run the code block shown below. 

```python
input('Press Enter once MCU is ready')
line = ser.readline()
lineList = convert_to_list(str(line))
new_df = convert_list_to_df(lineList)
print('New data acquired:\n', new_df.describe())

x = new_df['X'].to_numpy()
y = new_df['Y'].to_numpy()
z = new_df['Z'].to_numpy()

inf_data = np.array([x, y, z])
plot_single_sample(data_sample=inf_data.reshape((3, stride)))

# For inference you have to explicitly tell that the data has a batch size of 1
inf_data = inf_data.reshape((1, 3, stride))

pred = model.predict(inf_data)
print('Model Prediction: ', np.argmax(pred))
```

1. Press the blue button on the board, and "write" your letter, as before.
2. Press `Enter` in the notebook to sample data.
3. Check whether the prediction is correct or not.

Replay the step as often as you wish to test.

---
id: "alp-tflow-nn-stcube-train-nn-load-the-dataset"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Collect training data: Load the dataset"
summary: "Check the dataset you collected. Execute this code block to load the dataset."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/train_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/train_nn/#load-the-dataset"
license: "CC-BY-SA-4.0"
mode: "V"
---

Check the dataset you collected. Execute this code block to load the dataset.

```python
data_files = [file for file in os.listdir(samples_dir) if '.csv' in file]

stride = 30
data = []
labels = []
for idx, file in enumerate(data_files):
    df = pd.read_csv(os.path.join(samples_dir, file))
    x = df['X'].to_numpy()
    y = df['Y'].to_numpy()
    z = df['Z'].to_numpy()
    
    for i in range(int(df.shape[0]/stride)):
        base_idx = i * stride
        batch = np.array([x[base_idx:base_idx+stride], y[base_idx:base_idx+stride], z[base_idx:base_idx+stride]])
        batch = batch.reshape((3, stride))
        data.append(batch)
        labels.append(idx)
        
    print('Added {} data to the data list with label: {}'.format(file, idx))
```
If in your dataset you used the letters `a` and `z`, where the label for `a` is `0` and the label for `z` is `1`, this step should output:
```output
Added letter_a_stride_30.csv data to the data list with label: 0
Added letter_z_stride_30.csv data to the data list with label: 1
```

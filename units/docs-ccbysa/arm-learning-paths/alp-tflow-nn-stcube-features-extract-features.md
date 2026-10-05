---
id: "alp-tflow-nn-stcube-features-extract-features"
type: "concept"
domain: "edge-ai"
title: "features: Extract features"
summary: "First, extract the features from the collected dataset and save the features for training."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/features.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/features/#extract-features"
license: "CC-BY-SA-4.0"
mode: "V"
---

First, extract the features from the collected dataset and save the features for training.

```python
data_files = [file for file in os.listdir(samples_dir) if '.csv' in file]

stride = 30
slidingWindowExt = 6
feature_data = []
feature_labels = []
for idx, file in enumerate(data_files):
    df = pd.read_csv(os.path.join(samples_dir, file))
    x = df['X'].to_numpy()
    y = df['Y'].to_numpy()
    z = df['Z'].to_numpy()
    
    for i in range(int(df.shape[0]/stride)):
	base_idx = i * stride

        # Mean feature
        x_mean_ext = np.array([np.mean(x[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        y_mean_ext = np.array([np.mean(y[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        z_mean_ext = np.array([np.mean(z[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        # STD feature
        x_std_ext = np.array([np.std(x[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        y_std_ext = np.array([np.std(y[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        z_std_ext = np.array([np.std(z[i:i + slidingWindowExt]) for i in range(base_idx, base_idx + stride, slidingWindowExt)])
        
        batch = np.array([x_mean_ext, y_mean_ext, z_mean_ext, x_std_ext, y_std_ext, z_std_ext])
        feature_data.append(batch)
        feature_labels.append(idx)
        
    print('Added {} data to the feature data list with label: {}'.format(file, idx))
```
### Plot features

You can check the extracted features with this code block. These are the extracted features from one data sample.
Expected output shown below:

(figure: output5)

---
id: "alp-tflow-nn-stcube-train-nn-acquire-the-dataset"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Collect training data: Acquire the dataset"
summary: "Execute the code block shown below. This code block will acquire accelerometer data from the board, and save training samples for machine learning."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/train_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/train_nn/#acquire-the-dataset"
license: "CC-BY-SA-4.0"
mode: "V"
---

Execute the code block shown below. This code block will acquire accelerometer data from the board, and save training samples for machine learning. 

```python
letter = input('Please insert letter to collect data: ')
stride = 30
f = os.path.join(samples_dir, 'letter_{}_stride_{}.csv'.format(letter, stride))
if os.path.exists(f):
    print('File exists and data will be appended...')
    xyz_df = pd.read_csv(f)
else:
    print('New sample, starting blank...')
    xyz_df = pd.DataFrame(columns=['X', 'Y', 'Z'])

while input('1 - acquire sample, 2 - exit: ') == '1':
    line = ser.readline()
    lineList = convert_to_list(str(line))
    new_df = convert_list_to_df(lineList)
    print('New data acquired:\n', new_df.describe())
    xyz_df = pd.concat([xyz_df, new_df], ignore_index=True)
    print('Total Data count:', int(xyz_df.shape[0]/stride))

print('Saving data to:', f)
print('Total data of sample {}:\n'.format(letter), xyz_df.describe())
xyz_df.to_csv(f, index=False)
```

1. When prompted, enter a lower case letter (`a`) which you want to collect samples for.
2. Pick up the board, press the blue button (Green LED turns on), and "write" the letter in the air with the board. The green LED turns off when sampling ends.
3. In the notebook, enter `1` to save the accelerometer data.
4. Repeat this process until you get enough samples. The more data samples you collect, the better model you will probably get. Suggest 30+ samples.
5. Enter `2` when you want to finish the acquisition.

6. Re-execute this step in the notebook with a different letter (`z`).

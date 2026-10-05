---
id: "alp-img-nn-stcube-build-nn-save-data-for-testing"
type: "concept"
domain: "edge-ai"
title: "build nn: Save Data for Testing"
summary: "Finally, save the validation data and the labels for testing. This code block will sample 50 images from the dataset and save them in CSV format. Execute the code block to save the test data."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/img_nn_stcube/build_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/img_nn_stcube/build_nn/#save-data-for-testing"
license: "CC-BY-SA-4.0"
mode: "V"
---

Finally, save the validation data and the labels for testing. This code block will sample 50 images from the dataset and save them in CSV format. Execute the code block to save the test data.

```python
path_csv = "./Data/"
path_csv_file = path_csv+"own_cifar10_validation_20image.csv"
# Create directory
if not os.path.exists(path_csv):
 os.mkdir(path_csv)
# Remove old csv file
if os.path.exists(path_csv_file):
 os.remove(path_csv_file)
# Load data from TF Keras
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
# CIFAR10 class names
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 
'Horse', 'Ship', 'Truck']
# Normalize pixel values to be between 0 and 1
x_train = x_train.astype(np.float32)/255
x_test = x_test.astype(np.float32)/255
# Print arrays shape
print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print('x_test shape:', x_test.shape)
print('y_test shape:', y_test.shape)
 
# Save csv file that contain pixel's value
num_sample = 50
rx = random.sample(range(0,len(x_test)),num_sample)
for i in range(0,num_sample):
 data = x_test[rx[i]]
 #print(data.shape)
data = data.flatten()
 output = y_test[rx[i]]
 data=np.append(data,output)
 data = np.reshape(data, (1,data.shape[0]))
 #print(data.shape)
 with open(path_csv_file, 'ab') as f:
 np.savetxt(f, data, delimiter=",")
```

This code block will save the list of image classes. Execute the code block to save the label file.

```python
path_labels = "./Data/labels/”
path_labels_file = path_labels+"own_cifar10_labels.txt"
# Create directory
if not os.path.exists(path_labels):
 os.mkdir(path_labels)
 
# Remove old label file
if os.path.exists(path_labels_file):
 os.remove(path_labels_file)
# Create label file
for i in range(0,len(class_names)):
 with open(path_labels_file, 'a') as f:
 f.write(str(i)+","+class_names[i]+"\n")
```
You have now completed the steps to create the model and are ready to deploy it on the ST board.

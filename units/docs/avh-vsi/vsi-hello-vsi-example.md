---
id: "vsi-hello-vsi-example"
type: "concept"
domain: "debug"
title: "Hello VSI example"
summary: "This example uses the Virtual Streaming Interface (VSI)) to simulate a peripheral sensor. The example sensor will send data in form of bytes to the application running on an AVH FVP Model."
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:hello_vsi/README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_vsi/README.md"
license: "Apache-2.0"
mode: "V"
---

This example uses the [Virtual Streaming Interface (VSI)](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi.html)) to simulate a peripheral sensor. The example sensor will send data in form of bytes to the application running on an [AVH FVP Model](https://arm-software.github.io/AVH/main/overview/html/index.html). The virtual peripheral is controlled by a python script `arm_vsi0.py` that reads the data from a text file called `intdata.txt`. This is a minimal example of how to use Arm VSI, and you can modify the python script and the sensor driver in order to match your use case.

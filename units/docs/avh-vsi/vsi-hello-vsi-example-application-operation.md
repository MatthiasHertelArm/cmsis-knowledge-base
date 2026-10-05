---
id: "vsi-hello-vsi-example-application-operation"
type: "concept"
domain: "debug"
title: "Hello VSI example: Application operation"
summary: "The application receives sensor data from the intdata.txt file and prints the values to the console."
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:hello_vsi/README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_vsi/README.md#application-operation"
license: "Apache-2.0"
mode: "V"
---

The application receives sensor data from the `intdata.txt` file and prints the values to the console. For each loop, the application will wait until DMA block is filled, at that point the application will proceed to copy the data from a data buffer and print out to the console. When end of `intdata.txt` file is reached, the operation loop is stopped.

You can modify the streaming and driver operation using data and DMA parameters in `app.c` file.

The application supports **Corstone-320**, **Corstone-315**, **Corstone-310** and **Corstone-300** targets, and can be compiled with **Arm Compiler 6** or **GCC**.

See **Application flows** below for additional details.

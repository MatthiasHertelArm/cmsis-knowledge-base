---
id: "dv-examples"
type: "concept"
domain: "drivers"
title: "Examples"
summary: "The CMSIS-Driver Validation Software Pack includes example projects that demonstrate how to use the CMSIS-Driver Validation on real hardware, providing a reference and comparison point for user validation projects."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DriverValidation.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/examples.html"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Driver Validation Software Pack includes example projects that demonstrate how to use the CMSIS-Driver Validation on real hardware,
providing a reference and comparison point for user validation projects.

Follow these steps to use the validation examples:

1. In the **CMSIS** extension, click **Create a New Solution**.
2. Select the **Target Board** (**NUCLEO-H563ZI** for **Ethernet** example, **B-U585I-IOT02A** for **all other examples**).
3. Under **Templates, Reference Applications, and Examples**, select desired **Driver Validation Example**.
4. Choose **Solution Base Folder**, click **Create**.
5. Setup the required hardware as described in the example's **README.md** file
6. Build and Run the application

For details about specific examples check **README.md** of desired example in the example's root folder.

Available examples:

| Validation for Driver  | Board             | Additional required hardware                      |
|------------------------|-------------------|---------------------------------------------------|
| Ethernet               | ST NUCLEO-H563ZI  | Ethernet loopback plug                            |
| GPIO                   | ST B-U585I-IOT02A | ST STM32F429I-DISC1, 1kOhm resistor               |
| SPI                    | ST B-U585I-IOT02A | ST STM32F429I-DISC1, 10kOhm resistor, some wires  |
| USART                  | ST B-U585I-IOT02A | ST STM32F429I-DISC1, some wires                   |
| WiFi on-board EMW3080  | ST B-U585I-IOT02A | ST B-U585I-IOT02A, PC with MS Windows             |
| WiFi ESP8266           | ST B-U585I-IOT02A | SparkFun ESP8266 Shield, PC with MS Windows       |
| WiFi ISM43662          | ST B-U585I-IOT02A | Inventek ISMART43362-E Shield, PC with MS Windows |
| WiFi WizFi360          | ST B-U585I-IOT02A | WIZnet WizFi360-EVB Shield, PC with MS Windows    |

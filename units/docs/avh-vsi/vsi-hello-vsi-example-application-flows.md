---
id: "vsi-hello-vsi-example-application-flows"
type: "concept"
domain: "debug"
title: "Hello VSI example: Application flows"
summary: "The sections below explain the application flows for the supported build types."
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:hello_vsi/README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/hello_vsi/README.md#application-flows"
license: "Apache-2.0"
mode: "V"
---

The sections below explain the application flows for the supported build types.

### Event Driven Flow

Sensor data is continuously streamed from the sensor. When DMA block is filled with data a sensor event is triggered, the block is copied and application prints obtained values into the console.

Use `.event` as the build type, followed by the target platform.

```mermaid
sequenceDiagram
    participant Main
    participant Driver
    participant Peripheral
        Main->>+Driver: Init Driver 
        Driver->>+Peripheral: Init Peripheral
    loop Every sample
        Main->>+Main: Wait for Data Event
        Peripheral->>+Driver: Stream Data
        Driver->>+Main: Data Event Interrupt
        Main->>+Driver: Call Get_Data
        Driver->>+Main: Copy Data
        Main->>+Main: Print Data
    end
```

### Gated fetch Flow

Sensor data is fetched only when requested so by the application. The peripheral will be paused between each data fetch.

Use `.gated` as the build type, followed by the target platform.

```mermaid
sequenceDiagram
    participant Main
    participant Driver
    participant Peripheral
        Main->>+Driver: Init Driver 
        Driver->>+Peripheral: Init Peripheral
    loop Every sample 
        Main->>+Driver: Call Get_Data
        Driver->>+Driver: Wait for new data
        Peripheral->>+Driver: Stream Data Interupt
        Driver->>+Main: Copy Data
        Main->>+Main: Print Data
    end
```

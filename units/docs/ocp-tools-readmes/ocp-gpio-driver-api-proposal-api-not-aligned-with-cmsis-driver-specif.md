---
id: "ocp-gpio-driver-api-proposal-api-not-aligned-with-cmsis-driver-specif"
type: "concept"
domain: "project"
title: "GPIO Driver API Proposal: API not aligned with CMSIS-Driver specification"
summary: "Proposed API for GPIO Driver is fairly simple. Using CMSIS-Driver Common Functions might introduce unnecessary overhead and complexity. Alternative is a simpler API which is however not aligned with CMSIS-Driver specification."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:interface/gpio/include/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/interface/gpio/include/README.md#api-not-aligned-with-cmsis-driver-specification"
license: "Apache-2.0"
mode: "V"
---

Proposed API for GPIO Driver is fairly simple. Using CMSIS-Driver Common Functions might introduce unnecessary overhead and complexity. 
Alternative is a simpler API which is however not aligned with CMSIS-Driver specification.

CMSIS-Driver Common Functions (**Initialize**, **Uninitialize**, **PowerControl**) are replaced by a single function **Setup** 
which behaves as combined **Initialize** and **PowerControl**(ARM_POWER_FULL).

Other Common Functions (**GetVersion**, **GetCapabilities**) are dropped for further simplification.

The API consists of the following functions:
```
int32_t  (*Setup)           (ARM_GPIO_Pin_t pin, ARM_GPIO_SignalEvent_t cb_event)
int32_t  (*SetDirection)    (ARM_GPIO_Pin_t pin, ARM_GPIO_DIRECTION direction)
int32_t  (*SetOutputMode)   (ARM_GPIO_Pin_t pin, ARM_GPIO_OUTPUT_MODE mode)
int32_t  (*SetPullResistor) (ARM_GPIO_Pin_t pin, ARM_GPIO_PULL_RESISTOR resistor)
int32_t  (*SetEventTrigger) (ARM_GPIO_Pin_t pin, ARM_GPIO_EVENT_TRIGGER trigger) 
void     (*SetOutput)       (ARM_GPIO_Pin_t pin, uint32_t level)
uint32_t (*GetInput)        (ARM_GPIO_Pin_t pin)
void     (*SignalEvent)     (ARM_GPIO_Pin_t pin, uint32_t event);  // Callback
```

>Note: Functions are still exposed in an access structure as in CMSIS-Driver (could be changed).

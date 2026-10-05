---
id: "cfrt-cmsis-freertos-examples-run-example-project-on-virtual-hardware"
type: "concept"
domain: "rtos"
title: "CMSIS-FreeRTOS Examples: Run Example Project on Virtual Hardware Target model"
summary: "<model-executable> -f ./Target/<target_type>/fvp_config.txt ./out/<project>/<project>.axf"
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:CMSIS/RTOS2/FreeRTOS/Examples/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/CMSIS/RTOS2/FreeRTOS/Examples/README.md#run-example-project-on-virtual-hardware-target-model"
license: "Apache-2.0"
mode: "V"
---

Run command syntax:

`<model-executable> -f ./Target/<target_type>/fvp_config.txt ./out/<project>/<project>.axf`

Examples:

- Run Hello World project executable on Cortex-M3 model

```sh
FVP_MPS2_Cortex-M3 -f ./Board/CM3/fvp_config.txt ./out/Hello/CM3/Debug/Hello.axf --simlimit 25
```

- Run Hello World project executable on Cortex-M55 model

```sh
FVP_Corstone_SSE-300 -f ./Board/CM55_noTZ/fvp_config.txt ./out/Hello/CM55_noTZ/Debug/Hello.axf --simlimit 25
```

- Run TrustZone executable on model for Cortex-M55

```sh
FVP_Corstone_SSE-300 -f ./Board/CM55/fvp_config.txt -a ./out/TZ_NonSecure/CM55/Debug/TZ_NonSecure.axf -a ./out/TZ_Secure/CM55/Debug/TZ_Secure.axf --simlimit 25
```

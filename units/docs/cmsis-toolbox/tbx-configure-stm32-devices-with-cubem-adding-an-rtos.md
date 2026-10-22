---
id: "tbx-configure-stm32-devices-with-cubem-adding-an-rtos"
type: "concept"
domain: "project"
title: "Configure STM32 Devices with CubeMX: Adding an RTOS"
summary: "Many applications require an RTOS kernel. By default, CubeMX implements interrupt functions for all Cortex-M exception handlers. However, some exception handlers are typically required for the RTOS kernel execution."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/CubeMX.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/#adding-an-rtos"
license: "Apache-2.0"
mode: "V"
---

Many applications require an RTOS kernel. By default, CubeMX implements interrupt functions for all Cortex-M exception handlers. However, some exception handlers are typically required for the RTOS kernel execution.

Adding an RTOS kernel requires these steps:

### Step 1: Add RTOS

The example below adds the [CMSIS-RTX](https://github.com/ARM-software/CMSIS-RTX) RTOS kernel to a project.
Other kernels require different components and packs, but the concept is similar.

   **File: `CubeMX.cproject.yml`**

```yml
project:
  packs:
    - pack: ARM::CMSIS-RTX                    # RTOS Software Pack
  groups:
    - group: MyApp
      files:
        - file: MyMain.c
  components:
    - component: CMSIS:CORE                   # CMSIS-Core component is required
    - component: Device:CubeMX                # Component that connects to CubeMX
    - component: CMSIS:RTOS2:Keil RTX5&Source # RTOS component
    - component: CMSIS:OS Tick:SysTick        # OS Tick implementation for RTOS
```

### Step 2: Configure interrupt handlers

Configure the interrupt handlers by running CubeMX with:

```bash
csolution CubeMX.csolution.yml run --generator CubeMX --active MyBoard@Debug
```

Open the dialog *Pinout & Configuration - System Core NVIC - Code generation* and disable *Generate IRQ handler* for:

- System service call via SWI instruction
- Pendable request for system service
- System tick timer

(figure: STM32CubeMX - configure interrupt handlers)

Then click the button `GENERATE CODE` to update the generated files in the directory `STM32CubeMX/MyBoard`.

---
id: "armsw-readme-mainpage-omit-from-toc-3-examples-benchmark-and-templates"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: 3 Examples, Benchmark and Templates"
summary: "There is no public 2D image processing benchmark available for microcontrollers. To facilitate the library development and optimization, we overcome this problem with the following methods:"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#3-examples-benchmark-and-templates"
license: "Apache-2.0"
mode: "V"
---

### 3.1 Summary

| Projects                                          | Description                                                  | Folder                                                      | Note                                   |
| :------------------------------------------------ | :----------------------------------------------------------- | :---------------------------------------------------------- | :------------------------------------- |
| \[template\]\[bare-metal\]\[mps2\]                | It is a bare-metal project for processors running on the [MPS2 platforms](https://developer.arm.com/Tools%20and%20Software/MPS2%20Plus%20FPGA%20Prototyping%20Board). | examples/\[template\]\[bare-metal\]\[mps2\]                 |                                        |
| \[template\]\[bare-metal\]\[an552\]               | It is a bare-metal project for the Cortex-M55 processor([AN552](https://developer.arm.com/downloads/view/AN552)) running on the [MPS3 platforms](https://developer.arm.com/Tools%20and%20Software/MPS3%20FPGA%20Prototyping%20Board). | examples/\[template\]\[bare-metal\]\[an552\]                |                                        |
| \[template\]\[bare-metal\]\[cortex-m85\]          | It is a bare-metal project for the Cortex-M85 processor.     | examples/\[template\]\[bare-metal\]\[cortex-m85\]           |                                        |
| \[template\]\[bare-metal\]\[helium-aci\]          | It is a bare-metal project to demonstrate the Cortex-M55 ([AN552](https://developer.arm.com/downloads/view/AN552))  Helium ACI running on [MPS3 platforms](https://developer.arm.com/Tools%20and%20Software/MPS3%20FPGA%20Prototyping%20Board). | examples/\[template\]\[bare-metal\]\[helium-aci\]           |                                        |
| \[template\]\[bare-metal\]\[STM32F746G-Discovery] | It is a bare-metal project for the [STM32F746G-Discovery](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html) board. | examples/\[template\]\[bare-metal\]\[STM32F746G-Discovery\] | Arm Compiler 5, Arm Compiler 6 and GCC |
| \[template\]\[cmsis-rtos2\]                       | It is a project template for the RTOS environment, which uses CMSIS-RTOS2 as an example to show how Arm-2D can work with an RTOS. | examples/\[template\]\[cmsis-rtos2\]                        |                                        |
| \[template\]\[pc\]\[vscode\]                      | It is a project template for PC (i.e. **MacOS**, **Windows** and **Linux**) using **VS Code + SDL2** | examples/\[template\]\[pc\]\[vscode\]                       |                                        |
| \[template\]\[csolution\]                         | It is a csolution project template.                          | examples/\[template\]\[csolution\]                          |                                        |
| \[template\]\[pico\]\[oled]                       | An MDK project template for Raspberry Pi Pico to demonstrate OLED (monochrome) display. | examples/\[template\]\[pico\]\[oled]                        |                                        |

### 3.2 Benchmark

There is no public 2D image processing benchmark available for microcontrollers. To facilitate the library development and optimization,  we overcome this problem with the following methods:

- **Choose the widely used algorithms in embedded GUI as the body of the benchmark**
  - Alpha-blending
  - Colour-Keying
  - Blit
  - Tiling
  - Transform
  - Mirroring
  - Masking
  - Colour-Filling (with alpha gradient)
- **Simulate a typical application scenario with sufficient complexity**
  - Background with Texture Tiling (switching mirroring modes every 4 seconds)
  - Foreground picture
  - Two layers for alpha-blending and tiling with colour keying
  - Moving icons
  - Spinning wheels
- **Choose a typical low-cost LCD resolution 320*240 in RGB565**
- **Let those layers float with different speeds and directions to cover corner cases.**
- **Accumulate the cycle count used for 1000 frames (iterations)**

**Figure 1-4 A snapshot of the generic benchmark running in Simulation**

 

- **Calculate the average cycle count of 1000 frames, and use as the benchmark score (FPS30Freq)**
- For typical embedded applications, we derive a more meaningful metric called the **Minimal Frequency Required for 30 FPS (MHz), a.k.a FPS30Freq** as shown in **Figure 1-5**.

**Figure 1-5 Performance Comparison among some Cortex-M processors**

(figure: Performance Comparison among some Cortex-M processors)

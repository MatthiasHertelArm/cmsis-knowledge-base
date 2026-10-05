---
id: "intr-mcu-peripheral-forwarding-option-2-compile-time-instrumentation"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding: Option 2: Compile-Time Instrumentation"
summary: "To address the issue of excessive checks during runtime, an alternative approach involves selectively transforming the code that interacts with the peripherals at compile time."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding#option-2-compile-time-instrumentation"
license: "CC-BY-SA-4.0"
mode: "V"
---

To address the issue of excessive checks during runtime, an alternative approach involves selectively transforming the code that interacts with the peripherals at compile time. By focusing on the specific sections of code that handle peripheral operations, unnecessary checks and interruptions can be avoided, leading to improved performance and efficiency.

```cpp
#define GPIOC ((GPIO_TypeDef*)0x08000000)
...
int a = 0;                 // no need instrumentation, local variable
int b = a + 1;             // no need instrumentation, local variable
GPIOC->PIN1 = 0x1 << 4;    // need instrumentation, GPIOC is address of GPIOC peripheral, setup PIN1
b = GPIOC->PIN2 | 1 << 2;  // need instrumentation, GPIOC is address of GPIOC peripheral, read state of PIN2
```

This technique, known as [Compile-Time Instrumentation](https://developers.redhat.com/blog/2021/05/05/memory-error-checking-in-c-and-c-comparing-sanitizers-and-valgrind#performance), entails modifying the source code or utilizing specialized tools during the compilation process to introduce additional instructions or perform static analysis. The goal is to validate and optimize the code responsible for accessing peripheral registers, ultimately eliminating the need for excessive checks during runtime.

When working with microcontroller peripherals, developers typically rely on specialized software development kits (SDKs) provided by chip vendors or third-party providers. In the context of optimizing code for peripheral operations, it becomes advantageous to selectively instrument the code within the MCU's SDK.

For instance, among the Open Source SDKs I've instrumented, we have notable examples like:
 * [STM32 Standard Peripheral Libraries](https://www.st.com/en/embedded-software/stm32-standard-peripheral-libraries.html)
 * [Nordicsemi nRF5 SDK](https://www.nordicsemi.com/Products/Development-software/nrf5-sdk)
 * [Infineon XMC Peripheral Library](https://documentation.help/XMC/)
 * [Silabs Gecko SDK](https://www.silabs.com/developers/gecko-software-development-kit)
 * [Atmel ASF3 SDK](https://www.microchip.com/en-us/tools-resources/develop/libraries/advanced-software-framework)

By focusing on the code segments responsible for interacting with peripherals, we can introduce optimizations and eliminate unnecessary checks to enhance performance and efficiency.

---
id: "intr-mcu-peripheral-forwarding-option-1-dynamic-binary-instrumentation"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding: Option 1: Dynamic Binary Instrumentation"
summary: "Consider a scenario where we attempt to execute firmware code designed for the STM32F103 microcontroller directly on a PC. Take, for instance, the following simple program snippet:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding#option-1-dynamic-binary-instrumentation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Consider a scenario where we attempt to execute firmware code designed for the STM32F103 microcontroller directly on a PC. Take, for instance, the following simple program snippet:

```c
#include <stdio.h>

// ==========================================
// from stm32f10x.h header file
typedef struct
{
  int CRL;
  int CRH;
  int IDR;
  int ODR;
  int BSRR;
  int BRR;
  int LCKR;
} GPIO_TypeDef;

//peripheral GPIO address
#define GPIOC ((GPIO_TypeDef*)0x40011000)
// ==========================================


int main() {
  // read the state of PC0 pin
  int pin_PC0_value = GPIOC->IDR & 0x1;
  // write the value to console
  printf("PC0 value: %d\n", pin_PC0_value);

  return 0;
}
```

While this code might build successfully on our PC, directly executing it fails. The PC application can't directly access the memory address 0x40011000, as it's specific to the STM32F103 microcontroller's GPIOC peripheral.

The challenge is to enable the program to remain valid and successfully retrieve the state from a real STM32F103 chip without altering the existing codebase.
Fortunately, the PC platform offers powerful Dynamic Binary Instrumentation (DBI) tools, empowering developers to dynamically intercept and modify memory operations during runtime.
In the context of peripheral operations, these DBI tools become instrumental. When a memory operation targeting the peripheral address occurs, these tools can intercept the operation.

```c
int pin_PC0_value = GPIOC->IDR & 0x1;
```

During this interception, a DBI tool can load a value directly from the GPIOC peripheral register of the STM32F103 chip. With the aid of a debugger, for example, we can acquire the valid value from the physical hardware and seamlessly return it to the executing operation.


(figure: Intercept operation)


### Pintool

It is important to note that not all DBI toolkits can interrupt memory operations. While there are various DBI toolkits available, only one option stands out for this particular task: Intel's [PinTool](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html). Unlike other DBI tools, PinTool offers the capability to interrupt memory operations, making it a suitable choice for this approach.

In the pursuit of this approach, I have developed a [proof of concept](https://github.com/ser-mk/AddressIntercept-example-UART-DMA) using PinTool. This example uses a [custom plugin](https://github.com/ser-mk/AddressIntercept), designed for Intel PinTool.
[The plugin](https://github.com/ser-mk/AddressIntercept) is engineered to dynamically intercept all memory operations executed by the instrumented PC program. Given that the X86 processor predominantly utilizes the `mov` instruction for memory-related tasks, the plugin intercepts every `mov` instruction during runtime.

(figure: C Asm intercepted code)

It then examines the runtime arguments of these instructions, specifically focusing on address arguments, and comparing them against the addresses of the microcontroller's peripheral registers. Once identified, the plugin takes the necessary steps to initiate the execution of the peripheral operation on the MCU.

(figure: Loading by address)

To achieve this seamless execution, the PinTool plugin establishes communication with the debugger using either the [OpenOCD server](https://openocd.org/) or the [GDB server](https://en.wikipedia.org/wiki/Gdbserver). Both servers offer robust APIs that enable developers to execute memory operations on the target device.

*[15.4 Memory access commands](http://openocd.org/doc/html/General-Commands.html) of OpenOCD server*

> *mdw, mdh, mdb — Display contents of address addr, as 32-bit words (mdw), 16-bit halfwords (mdh), or 8-bit bytes (mdb).*
> 
> *mww, mwh, mwb — Writes the specified word (32 bits), halfword (16 bits), or byte (8-bit) value, at the specified address addr.*
> 

### Cons

While the PinTool plugin offers a viable solution for mapping peripheral registers to PC address space, excessive checks and overhead can impact performance, especially as the program complexity increases. Additionally, it's worth noting that PinTool, although proprietary, is freely accessible to users. Furthermore, its compatibility is limited to Intel processors. When it comes to debugging programs that utilize dynamic binary instrumentation (DBI) tools like PinTool, additional complexities are involved. DBI-based debugging requires a thorough understanding of the underlying architecture, as well as the intricacies of the tool itself. Considering the limitations and factors mentioned, it becomes crucial to explore alternative approach that can address performance concerns, provide cross-platform compatibility, and offer greater flexibility.

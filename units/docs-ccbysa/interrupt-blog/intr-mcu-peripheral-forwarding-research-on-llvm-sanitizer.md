---
id: "intr-mcu-peripheral-forwarding-research-on-llvm-sanitizer"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding: Option 2: Compile-Time Instrumentation / Research on LLVM Sanitizer"
summary: "Part of: Option 2: Compile-Time Instrumentation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding#research-on-llvm-sanitizer"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Option 2: Compile-Time Instrumentation_

Compile-time instrumentation is commonly used in debugging and optimization, and tools like LLVM sanitizers provide powerful mechanisms to detect and address issues in code, including memory access errors, data races, and undefined behavior. The [AddressSanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer) (ASan) is one such sanitizer that can be particularly useful in our context.

(figure: Asan insert function)

[AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html) (ASan) instruments the code by adding checks before each memory access instruction. ASan accomplishes this by inserting calls to an ASan library routine, which performs the necessary checks at runtime.

With some modifications to AddressSanitizer (ASan), we can adapt it to serve as an interceptor for peripheral operations. We would need to modify the ASan code to:

1. Instead of inserting the calls before each memory operation, we would need to modify the ASan code to include calls to our custom library routine in place of memory operations. This routine will handle the interception and validation of peripheral accesses. For example:

    ```cpp
    *p = 0xb00;
    int var = *p;
    ```
    
    Modify to
    
    ```cpp
    our_store_function(p, 0xb00);
    int var = our_load_function(p);
    ```

2. Identify specific memory addresses corresponding to peripheral registers: We will need to identify the specific memory addresses that correspond to the peripheral registers we want to intercept. It is a challenging task, especially when the information about which operations correspond to peripherals or local memory is not readily available. This is particularly true in cases where functions receive pointers as arguments, as it becomes more difficult to precisely identify operations related to peripheral accesses. For example:

    ```c
    void foo(void *p){
      *(int*)p = 0;
    }
    ```

To address the challenge of distinguishing between local memory operations and peripheral operations, a possible solution is to perform runtime checks for all instrumentation operations, except in cases where we can definitively determine whether it is a local memory operation or a peripheral operation.

The LLVM framework provides [APIs](https://github.com/remotemcu/adin-llvm-pass/blob/master/src/AddressIntercept.cpp#L141) that allow us to check whether an operation involves local variables or global variables. By leveraging these APIs, we can determine whether an operation is likely a local memory operation.

```cpp
int g = 0;

void foo(){
  int v;
  g = 0;
  v = 1;
} 
```

Using the LLVM API, we can determine the code above does not require instrumentation. By analyzing the code, LLVM can identify memory operations corresponding to local PC pointers and exclude them from the instrumentation process.

However, for cases where the distinction is unclear, you must check every memory address against a set of peripheral address intervals. For example, in the case of the STM32L0 chip, the peripheral registers are located within specific address intervals, such as 0x40000000 - 0x40008000, 0x40010000 - 0x40018000, 0x4002 0000 - 0x4002 63FF and 0x5000 0000 - 0x5000 1FFF. By comparing the accessed address with these intervals, you can determine if it corresponds to a peripheral address. 

(figure: STM32L0 memory map)

If the checking address falls within one of the defined peripheral address intervals, it can be considered a peripheral address. Conversely, if the checking address falls outside these intervals, it is likely a local host address.

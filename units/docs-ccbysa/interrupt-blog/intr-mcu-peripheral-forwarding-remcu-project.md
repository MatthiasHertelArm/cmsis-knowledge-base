---
id: "intr-mcu-peripheral-forwarding-remcu-project"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding: Option 2: Compile-Time Instrumentation / REMCU Project"
summary: "Part of: Option 2: Compile-Time Instrumentation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding#remcu-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Option 2: Compile-Time Instrumentation_

I have implemented the necessary functions for address [checking](https://github.com/remotemcu/remcu/blob/master/src/addressintercept.cpp#L176) and [executing operations](https://github.com/remotemcu/remcu/blob/master/src/addressintercept.cpp#L185) on the MCU within a separate repository called [REMCU](https://github.com/remotemcu/remcu). REMCU provides the functionality to handle peripheral register operations using an OpenOCD and GDB client. This client enables communication with the debugger to execute peripheral register operations on the MCU chip. The OpenOCD and GDB client implementation allows you to interact with the MCU using the debugger, providing a convenient way to send commands and data to the peripheral registers.

Furthermore, REMCU is extensible and adaptable to 
different communication protocols. You can implement your own client 
using protocols such as UART, CAN bus, or any other suitable 
communication method. Simply create a new class that derives from the `ClientBase` [class](https://github.com/remotemcu/remcu/blob/master/include/BaseClient.h#L15) in REMCU and implement the necessary communication functionality specific to your chosen protocol.

```cpp
struct ClientBase {
    bool connect(const std::string, const uint16_t port, int timeout_sec) const ;
    virtual bool store2RemoteAddr(const llvm_ocd_addr addr, const llvm_value_type value, const llvm_pass_arg sizeVal) const ;
    virtual bool loadFromRemoteAddr(const llvm_ocd_addr addr, llvm_value_type & value, const llvm_pass_arg sizeVal) const ;
    virtual bool arrayWrite2RemoteMem(const uintptr_t addr, const uint8_t*  sink, const size_t size) const ;
    virtual bool arrayLoadFromRemoteMem(const uintptr_t addr, const size_t size, uint8_t*  dist) const ;
    virtual bool resetRemoteUnit(const ResetType) const ;
    virtual bool ping() const ;
    bool close() const ;
};
```

Establishing a connection with the MCU through the debugger protocol provides a robust and dependable solution. This connection is unaffected by issues such as the chip clock signal or chip reset, ensuring consistent communication between the PC and the MCU.

The REMCU also offers helpful [build scripts](https://github.com/remotemcu/remcu/tree/master/cmake) that automate the process of building the MCU's SDK into a separate shared library(*.so, *.dll, *.dylib) for various platforms, including embedded Linux (such as Raspberry Pi).

These build scripts simplify the setup and configuration process and streamline the integration of the MCU's SDK with the necessary instrumentation, making it easier to incorporate the modified SDK into your project. By running these build scripts, you can automatically generate a shared library that contains the instrumented code and the implementation of the handler functions using an NRF SDK example as a reference.

Preparing the SDK for your specific MCU and the corresponding build process will be covered in detail in [the article](https://ser-mk.github.io/remcu/tutorial-preparing-nrf51-sdk/). The article will provide step-by-step instructions and guidelines on preparing the SDK and building the necessary shared library with the instrumentation and REMCU handler functions.

---
id: "intr-mcu-peripheral-forwarding-how-to-use"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding: Option 2: Compile-Time Instrumentation / How to use"
summary: "Part of: Option 2: Compile-Time Instrumentation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding#how-to-use"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Option 2: Compile-Time Instrumentation_

Getting started with REMCU is relatively straightforward and involves a few simple steps to set up the necessary components. The key steps to prepare for working with REMCU are as follows:

1. Connect a target MCU to your PC host:
(figure: connect MCU to debugger)

2. Run OpenOCD or GDB server:
(figure: GDB Jlink server)

3. Set up OpenOCD or a GDB client: Depending on your preference and specific requirements, you can choose either OpenOCD or a GDB client. By running the corresponding functions below, you can establish the connection between the PC and the MCU.
    
    
    ```cpp
    /**
     * @brief remcu_connect2OpenOCD
     * The function is used to create a connection to the OpenOCD server destination
     * @param host - ip address of OpenOCD server "XXX.XXX.XXX.XXX". If the server runs on the host machine, the argument should be "localhost" or "127.0.0.1" value.
     * @param port - port of OpenOCD server. Default is 6666
     * @param timeout_sec - This parameter specifies the length of time, in seconds, to wait for a response when establishing communications. It can not be negative!
     * @return If no error occurs, function returns true
     */
    REMCULIB_DLL_API bool remcu_connect2OpenOCD(const char* host, const uint16_t port,
                          const int timeout_sec);
    
    /**
     * @brief remcu_connect2GDB
     * The function is used to create a connection to the GDB server destination
     * @param host - ip address of GDB server "XXX.XXX.XXX.XXX". If the server runs on the host machine, the argument should be "localhost" or "127.0.0.1" value.
     * @param port - port of GDB server. Default of OpenOCD is 3333
     * @param timeout_sec - This parameter specifies the length of time, in seconds, to wait for a response when establishing communications. It can not be negative!
     * @return If no error occurs, function returns true
     */
    REMCULIB_DLL_API bool remcu_connect2GDB(const char* host, const uint16_t port,
                           const int timeout_sec);
    ```

4. Reset the chip: Once the connection is established, you can utilize the [remcu_resetRemoteUnit](https://github.com/remotemcu/remcu/blob/master/export/remcu.h#L107) function to reset the MCU. This step ensures a clean starting point and prepares the chip for further operations.

    ```cpp
    remcu_resetRemoteUnit(__HALT);
    ```

Now, You can execute any SDK peripheral driver functions!

---
id: "core-using-trustzone-for-armv8-m-simplified-use-case-with-trustzone"
type: "concept"
domain: "core"
title: "Using TrustZone for Armv8-M: Simplified Use Case with TrustZone"
summary: "An Armv8-M TrustZone enabled device has restricted access for data, code, and I/O access to trusted software that runs in the Secure state. Typical applications are secure IoT nodes, firmware IP protection, or multi-party embedded software deployments."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/using_tz.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/using_tz.md#simplified-use-case-with-trustzone"
license: "Apache-2.0"
mode: "V"
---

An Armv8-M TrustZone enabled device has restricted access for data, code, and I/O access to trusted software that runs in the Secure state. Typical applications are secure IoT nodes, firmware IP protection, or multi-party embedded software deployments.

The figure **Simplified Use Case** shows and embedded application that is split into a **User Project** (executed in Non-secure state) and a **Firmware Project** (executed in Secure state).

 - **System Start:** after power on or reset, an Armv8-M system starts code execution in the **Secure state**. The access rights for the **Non-secure state** is configured.

 - **User Application:** control can be transferred to **Non-secure state** to execute user code. This code can only call functions in the **secure state** that are marked for execution with the **SG** (secure gate) instruction and memory attributes. Any attempt to access memory or peripherals that are assigned to the **Secure state** triggers a security exception.

 - **Firmware callbacks:** code running in the **Secure state** can execute code in the **Non-secure state** using call-back function pointers. For example, a communication stack (protected firmware) could use an I/O driver that is configured in user space.



(figure: Simplified Use Case)

Program execution in the **Secure state** is further protected by TrustZone hardware from software failures.

For example, an Armv8-M system may implement two independent SYSTICK timers which allows to stop code execution in **Non-secure state** in case of timing violations. Also function pointer callbacks from **Secure state** to **Non-secure state** protected by a special CPU instruction and the address bit 0 which prevents anciently executing code in **Non-secure state**.

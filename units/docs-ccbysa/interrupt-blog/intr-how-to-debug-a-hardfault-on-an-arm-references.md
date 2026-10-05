---
id: "intr-how-to-debug-a-hardfault-on-an-arm-references"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: References"
summary: "[^1]: See \"A4.1.1 ARMv7-M and interworking support\" [^2]: MBed OS fault handler [^3]: Zephyr ARM fault handler [^4]: CMSIS-SVD [^5]: CMSIS Software Packs [^6]: PyCortexMDebug [^7]: See \"3.3.9 Auxiliary Bus Fault Status Register\" [^8]: Segger JTrace & Lauterbach …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#references"
license: "CC-BY-SA-4.0"
mode: "V"
---

[^1]: [See "A4.1.1 ARMv7-M and interworking support"](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf)
[^2]: [MBed OS fault handler](https://github.com/ARMmbed/mbed-os/blob/2e96145b7607de430235dd795ab5350c1d4d64d7/platform/source/TARGET_CORTEX_M/mbed_fault_handler.c#L44-L81)
[^3]: [Zephyr ARM fault handler](https://github.com/intel/zephyr/blob/e09a04f0689fd29aa909cc49ee94fd129798f986/arch/arm/core/fault.c#L55-L275)
[^4]: [CMSIS-SVD](https://arm-software.github.io/CMSIS_5/SVD/html/index.html)
[^5]: [CMSIS Software Packs](https://developer.arm.com/tools-and-software/embedded/cmsis)
[^6]: [PyCortexMDebug](https://github.com/bnahill/PyCortexMDebug)
[^7]: [See "3.3.9 Auxiliary Bus Fault Status Register"](http://infocenter.arm.com/help/topic/com.arm.doc.ddi0489b/DDI0489B_cortex_m7_trm.pdf)
[^8]: [Segger JTrace](https://www.segger.com/products/debug-probes/j-trace/) & [Lauterbach Trace32](https://www.lauterbach.com/frames.html?home.htmlLink lauterbach) are both capable of analyzing the ETM
[^9]: [See B3.5.1 "Relation of the MPU to the system memory map"](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf)
[^10]: [See "4.2.3 Memory map"](https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.0.pdf)
[^11]: [See "5.3.6.8 Reset behavior"](https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.0.pdf)
[^12]: [JLinkGDBServer](https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/)
[^13]: [nRF52840 Development Kit](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-DK)
[^14]: [The Tower of Terror: A Bug Mystery](https://medium.com/fitbit-tech-blog/the-tower-of-terror-a-bug-mystery-c57f51981eff)
[^15]: [See "B1.5.5 Reset behavior" & "B1.4.2 The special-purpose program status registers, xPSR"](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf)
[^16]: [GNU ARM Embedded toolchain for download](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)

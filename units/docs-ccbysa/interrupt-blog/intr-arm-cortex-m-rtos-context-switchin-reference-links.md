---
id: "intr-arm-cortex-m-rtos-context-switchin-reference-links"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Reference Links"
summary: "[^1]: ARM Architecture Procedure Calling Standard(AAPCS) [^2]: ARMv7-M Architecture Reference Manual [^3]: FreeRTOS [^4]: ARMv8-M link [^5]: Cortex-M4F Lazy Stacking and Context Switch App note [^6]: See B1.5.6 Exception entry behavior [^7]: nRF52840 Development Kit [^8]: JLinkGDBServer [^9]: …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#reference-links"
license: "CC-BY-SA-4.0"
mode: "V"
---

[^1]: [ARM Architecture Procedure Calling Standard(AAPCS)](http://infocenter.arm.com/help/topic/com.arm.doc.ihi0042f/IHI0042F_aapcs.pdf)
[^2]: [ARMv7-M Architecture Reference Manual](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf)
[^3]: [FreeRTOS](https://www.freertos.org/)
[^4]: [ARMv8-M link](https://static.docs.arm.com/ddi0553/a/DDI0553A_e_armv8m_arm.pdf)
[^5]: [Cortex-M4F Lazy Stacking and Context Switch App note](https://static.docs.arm.com/dai0298/a/DAI0298A_cortex_m4f_lazy_stacking_and_context_switching.pdf)
[^6]: [See B1.5.6 Exception entry behavior](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf)
[^7]: [nRF52840 Development Kit](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-DK)
[^8]: [JLinkGDBServer](https://www.segger.com/products/debug-probes/j-link/tools/j-link-gdb-server/about-j-link-gdb-server/)
[^9]: [GNU ARM Embedded toolchain for download](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
[^10]: [Creating a FreeRTOS Project](https://www.freertos.org/Creating-a-new-FreeRTOS-project.html)
[^11]: [Github FreeRTOS Kernel](https://github.com/FreeRTOS/FreeRTOS-Kernel/tree/master/portable)
[^12]: [FreeRTOS Heap documentation](https://www.freertos.org/a00111.html)
[^13]: [FreeRTOSConfig.h documentation](https://www.freertos.org/a00110.html)
[^14]: [ISB after mrs](https://www.freertos.org/FreeRTOS_Support_Forum_Archive/March_2017/freertos_ISB_isntructions_on_Cortex-M4_port_6fc12825j.html)
[^15]: [Extended Asm](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Extended-Asm.html)
[^16]: [Discussion about DSB in FreeRTOS port](https://www.freertos.org/FreeRTOS_Support_Forum_Archive/May_2017/freertos_Use_of_barriers_when_setting_BASEPRI_on_Cortex_M7_8a85181fj.html)
[^17]: [See "Visibility of changes in execution priority resulting from executing an MSR instruction"](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf)

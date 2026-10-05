---
id: "intr-a-guide-to-watchdog-timers-for-emb-configuring-a-hardware-watchdog"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: Configuring a Hardware Watchdog"
summary: "When first configuring a hardware watchdog, it's important to read the fine print in the datasheet about how the peripheral works. The peripheral is vendor specific so even if you are using the same chip family (e.g."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#configuring-a-hardware-watchdog"
license: "CC-BY-SA-4.0"
mode: "V"
---

When first configuring a hardware watchdog, it's important to read the fine print in the datasheet about how the peripheral works. The peripheral is vendor specific so even if you are using the same chip family (e.g. an ARM Cortex-M MCU) the behavior of the watchdog peripheral will be different. Nuances in implementations can lead to unexpected issues later on. Let's walk through a quick list of things to check.

{: #watchdog-configuration-questions}

### When does the watchdog configuration get reset?

Typically, you'll see one of:

- The watchdog can be enabled and disabled multiple times and **must** be configured on each boot.
- The watchdog can only be configured and enabled once. Once enabled, only certain types of resets (e.g. a "Power on Reset" (POR)) will disable the watchdog).

### How does the watchdog behave with a debugger?

The watchdog is often disabled by developers for debug builds in an effort to prevent resets on boards actively being developed. However, I would argue this is a **big** mistake. This almost always leads to issues going unnoticed until a release build is cut that could have been identified and fixed in the development phase instead.

A less known fact is that most MCU vendors have special configurations that can be used while the system is halted to pause the watchdog timer. That way, if you add a breakpoint and are inspecting code, you don't have to worry about a watchdog firing. Not all hardware supports this feature however. In these scenarios, the debugger can be configured to issue register writes that pause or feed the peripheral. We will explore an example of how to do this with GDB later in the article.

> Fun Fact: For Cortex-M's, I've always been very impressed with the configuration options that STMicroelectronics exposes for STM32s via the DBGMCU component. From there one can chose to "freeze" any peripheral clock while the system is halted.

### What happens when the watchdog expires?

Some of the typical options you will see are:

- When the watchdog expires, the hardware will immediately reset the system.
- An interrupt can be enabled which will fire when the watchdog timer is getting close to expiration. In the interrupt handler, the software can decide to "feed" the watchdog to prevent the system from resetting.
- An interrupt can be enabled which will fire when the watchdog expires. The MCU will give you a few extra clock cycles to do cleanup and then _reset_ the MCU. I find this variant to be one of the more frustrating ones because, unless you are very careful about how many cycles your cleanup code takes to execute, the hardware may reset the system in the middle of cleanup!

### How do I find out if a watchdog reset took place?

Almost every silicon vendor exposes information about the type of hardware reset which took place via a register. If the MCU implements a watchdog peripheral, one of the bits within the register will indicate if a watchdog reset took place.

> Implementation Note: Typically, the settings in these registers are "sticky". That is, after you read them on boot, you will need to clear them. Otherwise, you will keep seeing the same value every time the system boots until a full Power-On-Reset occurs.

#### Examples of Reset Reason Register Name By Vendor

Here are some of the names used for the reset reason register based on chip family:

| Silicon Vendor       | Chip Family | Register Name                        |
| -------------------- | ----------- | ------------------------------------ |
| Espressif Systems    | ESP32       | RTC_CNTL_RESET_CAUSE\[PROCPU/APPCPU] |
| Maxim Integrated     | MAX32       | PWRSEQ_FLAGS                         |
| NXP                  | LPC         | AOREG1                               |
| Nordic Semiconductor | NRF52       | RESETREAS                            |
| STMicroelectronics   | STM32F      | RCC_CSR                              |
| STMicroelectronics   | STM32H      | RCC_RSR                              |

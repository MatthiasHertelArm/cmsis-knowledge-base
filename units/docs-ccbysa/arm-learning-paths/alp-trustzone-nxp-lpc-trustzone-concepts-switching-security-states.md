---
id: "alp-trustzone-nxp-lpc-trustzone-concepts-switching-security-states"
type: "concept"
domain: "core"
title: "Get started with TrustZone on NXP LPCXpresso55S69: Breaking down the application: Switching security states"
summary: "Start another debug session with the application. This time, instead of hitting \"Run\" and viewing the complete output you will walk through some key TrustZone concepts used in this application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/trustzone_nxp_lpc/trustzone_concepts.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/trustzone_nxp_lpc/trustzone_concepts/#switching-security-states"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start another debug session with the application. This time, instead of hitting "Run" and viewing the complete output you will walk through some key TrustZone concepts used in this application.
At the start of execution, the program counter is at the start of `main()` in `hello_world_s.c`. The secure mode copy of the startup code has already been executed right at reset time. 

In the `main()` function, board hardware initialization is performed followed by the first 2 `printf` statements you saw in the console output:

```output
PRINTF("Hello from secure world!\r\n");
PRINTF("Entering normal world.\r\n");
```
The Cortex-M33 processor on the NXP board is running in secure mode up to this point. After these prints, the `TZM_JumpToNormalWorld(NON_SECURE_START)` function is called which initiates the switch to the non-secure world. This function is defined in the `tzm_api.c` source file. This function sets up the non-secure main stack and vector table and gets a pointer to the non-secure reset handler with `__attribute__((cmse_nonsecure_call))`. This key attribute directs the compiler (Arm compiler for embedded in this example) to generate a `BLXNS` instruction. This instruction causes the processor to switch from secure to non-secure world.

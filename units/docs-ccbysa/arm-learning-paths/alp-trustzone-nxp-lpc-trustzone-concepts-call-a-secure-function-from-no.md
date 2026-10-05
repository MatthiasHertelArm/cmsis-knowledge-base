---
id: "alp-trustzone-nxp-lpc-trustzone-concepts-call-a-secure-function-from-no"
type: "concept"
domain: "core"
title: "Get started with TrustZone on NXP LPCXpresso55S69: Breaking down the application: Call a secure function from non-secure world"
summary: "Now that the processor has switched to non-secure mode it will not be able to access memory and peripherals of the secure world."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/trustzone_nxp_lpc/trustzone_concepts.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/trustzone_nxp_lpc/trustzone_concepts/#call-a-secure-function-from-non-secure-world"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that the processor has switched to non-secure mode it will not be able to access memory and peripherals of the secure world. The processor now executes the non-secure copy of the startup code and reaches the `main()` function of the `hello_world_ns.c` source file. 

Here again there are two key print statements which you previously saw in the output:

```output
PRINTF_NSE("Welcome in normal world!\r\n");
PRINTF_NSE("This is a test printed from the normal world!\r\n");
```
`PRINTF_NSE()` function is defined with `__attribute__((cmse_nonsecure_entry))`. This attribute is used to call the `PRINTF()` function. which is defined in secure mode. 
Using this attribute, a secure function can be called from the non-secure world. The functions executes an `SG` instruction which is a Secure Gateway instruction. Non-secure code can only call a secure function if the first instruction is a Secure Gateway instruction and it is in a non-secure callable memory region. If these rules are not followed during execution then it results in a security violation. 

You have now summarized some important attributes and instructions used while building TrustZone applications all using the simple hello world example on the NXP LPCXpresso55S69 board.

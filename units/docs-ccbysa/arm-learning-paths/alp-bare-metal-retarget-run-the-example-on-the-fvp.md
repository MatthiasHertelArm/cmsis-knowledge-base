---
id: "alp-bare-metal-retarget-run-the-example-on-the-fvp"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Modify the example to use the UART for printf output: Run the example on the FVP"
summary: "Launch the simulation model with the newly built image."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/retarget.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/retarget/#run-the-example-on-the-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

Launch the simulation model with the newly built image. 
```console
FVP_Base_AEMvA -a hello.axf
```
All `printf()` output is now directed to `UART0` of the FVP.

You'll see a terminal pop-up with the output:
```output
Hello World!
In _sys_exit. Use Ctrl+C to quit.
```

**Telnet Client:**
Windows users may need to first [enable Telnet Client](https://social.technet.microsoft.com/wiki/contents/articles/38433.windows-10-enabling-telnet-client.aspx) to see the output message.



The code ends in an infinite loop (in the retargeted `__sys_exit()`), and so you must manually terminate (for example with `Ctrl+C`) the FVP.

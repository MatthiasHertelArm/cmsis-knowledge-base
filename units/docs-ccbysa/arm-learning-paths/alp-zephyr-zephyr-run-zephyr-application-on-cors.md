---
id: "alp-zephyr-zephyr-run-zephyr-application-on-cors"
type: "concept"
domain: "rtos"
title: "Run the Zephyr RTOS on Arm Corstone-300: Build and run Zephyr applications: Run Zephyr application on Corstone-300 FVP"
summary: "Execute on the machine with the installed Corstone-300 FVP:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr/zephyr.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr/zephyr/#run-zephyr-application-on-corstone-300-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

Execute on the machine with the installed Corstone-300 FVP: 

```fvp { fvp_name="FVP_Corstone_SSE-300_Ethos-U55",cwd="/shared/zephyrproject/zephyr" }
FVP_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf -C mps3_board.visualisation.disable-visualisation=1 --simlimit 30
```

**Optional switches:**
`-C mps3_board.visualisation.disable-visualisation=1` disables the FVP visualization. This can speed up launch time for the FVP.

`--simlimit 30` terminates the FVP after 30 seconds. Remove or extend if necessary. The FVP can also be manually terminated with `Ctrl+C`.


You will see telnet terminal windows pop up from the running simulation on the FVP with the output similar to:

```output
*** Booting Zephyr OS build zephyr-v3.4.0-3573-g79158a777b37  ***
Hello World! mps3_an547
```

You have successfully built a Zephyr application and run it on the Corstone-300.

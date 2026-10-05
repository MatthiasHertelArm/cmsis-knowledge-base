---
id: "vgs-get-started-with-visual-studio-cod-build-the-solution"
type: "concept"
domain: "project"
title: "Get started with Visual Studio Code: Build the solution"
summary: "In the CMSIS view, use the build button (hammer icon) to build the solution. In the background, cbuild will be run:"
status: "draft"
collection: "vscode-get-started"
source: "Open-CMSIS-Pack/vscode-get-started@675c86f:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-get-started/blob/675c86f/README.md#build-the-solution"
license: "Apache-2.0"
mode: "V"
---

In the **CMSIS** view, use the build button (hammer icon) to build the solution. In the background,
[`cbuild`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#cbuild-invocation) will be run:

```txt
Execute: cbuild /Users/user/vscode-get-started/get_started.csolution.yml --rebuild --active Corstone-300-FVP --packs
+-----------------------------------------------------
(1/1) Cleaning context: "hello.debug+Corstone-300-FVP"
+-----------------------------------------------------
(1/1) Building context: "hello.debug+Corstone-300-FVP"
Using AC6 V6.24.0 compiler, from: '/Users/user/.vcpkg/artifacts/2139c4c6/compilers.arm.armclang/6.24.0/bin/'
Building CMake target 'hello.debug+Corstone-300-FVP'
[1/20] Building C object CMakeFiles/Group_Source.dir/Users/user/vscode-get-started/hello/main.o
[2/20] Building C object CMakeFiles/ARM_CMSIS_OS_Tick_SysTick_1_0_5.dir/Users/user/.cache/arm/packs/ARM/CMSIS/6.1.0/CMSIS/RTOS2/Source/os_systick.o
[3/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_memory.o
[4/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_delay.o
[5/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_lib.o
[6/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_evr.o
[7/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_kernel.o
[8/20] Building ASM object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/GCC/irq_armv8mml.o
[9/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_evflags.o
[10/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_mempool.o
[11/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_mutex.o
[12/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_msgqueue.o
[13/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/vscode-get-started/hello/RTE/CMSIS/RTX_Config.o
[14/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_semaphore.o
[15/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_system.o
[16/20] Building C object CMakeFiles/ARM_Device_Startup_C_Startup_2_0_0.dir/Users/user/vscode-get-started/hello/RTE/Device/SSE-300-MPS3/system_SSE300MPS3.o
[17/20] Building C object CMakeFiles/ARM_Device_Startup_C_Startup_2_0_0.dir/Users/user/vscode-get-started/hello/RTE/Device/SSE-300-MPS3/startup_SSE300MPS3.o
[18/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_timer.o
[19/20] Building C object CMakeFiles/ARM_CMSIS_RTOS2_Keil_RTX5_Source_5_9_0.dir/Users/user/.cache/arm/packs/ARM/CMSIS-RTX/5.9.0/Source/rtx_thread.o
[20/20] Linking C executable /Users/user/vscode-get-started/out/hello/Corstone-300-FVP/debug/hello.axf
Program Size: Code=14030 RO-data=974 RW-data=188 ZI-data=29312  
+------------------------------------------------------------
Build summary: 1 succeeded, 0 failed - Time Elapsed: 00:00:02
+============================================================
Completed: cbuild succeed with exit code 0
Build complete
```

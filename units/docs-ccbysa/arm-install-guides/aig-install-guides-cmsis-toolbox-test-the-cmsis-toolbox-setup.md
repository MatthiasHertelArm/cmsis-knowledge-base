---
id: "aig-install-guides-cmsis-toolbox-test-the-cmsis-toolbox-setup"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox: Test the CMSIS-Toolbox setup"
summary: "You can find example projects on GitHub."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/cmsis-toolbox.md"
doc_source: "https://learn.arm.com/install-guides/cmsis-toolbox/#test-the-cmsis-toolbox-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can find example projects on [GitHub](https://github.com/Open-CMSIS-Pack/csolution-examples).

Clone the repository to your build machine:

```command
git clone https://github.com/Open-CMSIS-Pack/csolution-examples
```

Navigate to the `Hello` example:

```command
cd csolution-examples/Hello
```

### Build the solution

Use the [cbuild](https://github.com/Open-CMSIS-Pack/cbuild) utility (a component of `CMSIS-Toolbox`) to build.

Add `--packs` to the command line to download and install any necessary software packs not currently installed.

```command
cbuild Hello.csolution.yml --packs
```

The build will proceed and generate an executable image(s). The output is similar to:

```output
ARM::CMSIS@6.0.0
ARM::CMSIS-Compiler@2.0.0
ARM::CMSIS-RTX@5.8.0
ARM::V2M_MPS3_SSE_300_BSP@1.5.0
I: Downloading ARM.CMSIS.pdsc...
I: Adding pack "ARM::CMSIS@6.0.0"
I: Downloading ARM.CMSIS.6.0.0.pack...
...
...
(1/2) Building context: "Hello.Debug+AVH"
Building CMake target 'Hello.Debug+AVH'
[1/31] Building C object CMakeFiles/Group_Main.dir/home/ubuntu/csolution-examples/Hello/main.o
...
[31/31] Linking C executable /home/ubuntu/csolution-examples/Hello/out/Hello/AVH/Debug/Hello.axf
Program Size: Code=29968 RO-data=1584 RW-data=244 ZI-data=37072
+------------------------------------------
(2/2) Building context: "Hello.Release+AVH"
Building CMake target 'Hello.Release+AVH'
[1/31] Building C object CMakeFiles/Group_App.dir/home/ubuntu/csolution-examples/Hello/hello.o
...
[31/31] Linking C executable /home/ubuntu/csolution-examples/Hello/out/Hello/AVH/Release/Hello.axf
Program Size: Code=17664 RO-data=988 RW-data=196 ZI-data=37112
+------------------------------------------------------------
Build summary: 2 succeeded, 0 failed - Time Elapsed: 00:00:03
+============================================================
```

You are now ready to use CMSIS-Toolbox.

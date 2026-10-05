---
id: "alp-zephyr-zephyr-build-the-hello-world-sample-a"
type: "concept"
domain: "rtos"
title: "Run the Zephyr RTOS on Arm Corstone-300: Build and run Zephyr applications: Build the hello world sample application"
summary: "There are sample applications included in the Zephyr source code repository."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr/zephyr.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr/zephyr/#build-the-hello-world-sample-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are sample applications included in the Zephyr source code repository. 

You can build the [hello world](https://docs.zephyrproject.org/latest/samples/hello_world/README.html) application for the Corstone-300 using `west`: 

```bash { env_source="/shared/zephyrproject/.venv/bin/activate",cwd="/shared" }
cd zephyrproject/zephyr
west build -p auto -b mps3/corstone300/fvp samples/hello_world samples/hello_world
```

**Note:**
[MPS3](https://developer.arm.com/Tools%20and%20Software/MPS3%20FPGA%20Prototyping%20Board) [AN547](https://developer.arm.com/downloads/-/download-fpga-images) is the hardware twin of the Corstone-300 FVP.



The application binaries are placed in the `~/zephyrproject/zephyr/build/zephyr/` directory.

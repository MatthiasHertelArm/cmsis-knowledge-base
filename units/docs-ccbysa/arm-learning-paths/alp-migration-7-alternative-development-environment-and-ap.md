---
id: "alp-migration-7-alternative-development-environment-and-ap"
type: "concept"
domain: "project"
title: "Migrating x86_64 workloads to aarch64: Evaluating performance on Arm hardware (Optional): Development environment and application porting"
summary: "Use the same Dockerfile as before, see Development environment."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/7_alternative.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/7_alternative/#development-environment-and-application-porting"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use the same Dockerfile as before, see [Development environment](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/4_development_environment/#gcc-container).

You can build the development environment natively on Arm using `docker build` instead of `docker buildx`. 

To build the GCC development environment, run the following command:

```bash
docker build -t sobel_gcc_example .
```

Run the container:

```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_gcc_example
```

Follow the same steps to port the application as described in [Application porting](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/5_application_porting/) to build and run the application.

### ACfL

In addition to the GCC development environment, you can also use Arm Compiler for Linux ([ACfL](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux)). 

Pull the development container from the `armswdev` repository and rename it `sobel_acfl_example`:

```bash
docker pull armswdev/arm-compiler-for-linux
docker tag armswdev/arm-compiler-for-linux sobel_acfl_example
```

Run the container:

```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_acfl_example
```

The container doesn't have OpenCV.

Install OpenCV by running the command:

```bash
sudo apt-get update && sudo apt-get install -y libopencv-dev
```

Follow the same steps to port the application as described in [Application porting](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/5_application_porting/). 

To use Arm Compiler for Linux you need to change the compiler in `CMakeLists.txt` as shown below:

```output
set(CMAKE_C_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang")
set(CMAKE_CXX_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang++")
```

Make the changes by running the following command:

```bash
sed -i "6i set(CMAKE_C_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang\")" src/CMakeLists.txt
sed -i "7i set(CMAKE_CXX_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang++\")\n" src/CMakeLists.txt
```

---
id: "alp-migration-5-application-porting-compiler-options-porting"
type: "concept"
domain: "project"
title: "Application porting: Compiler options porting"
summary: "The -mavx compiler option needs to be removed. You can add the optimization flag -O2 as it's recommended when transitioning to Arm."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/5_application_porting.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/5_application_porting/#compiler-options-porting"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `-mavx` compiler option needs to be removed. You can add the optimization flag `-O2` as it's recommended [when transitioning to Arm](https://simd-everywhere.github.io/blog/2020/06/22/transitioning-to-arm-with-simde.html). 

Below you can see the changes to make in `CMakeLists.txt`:

```output
# Enable SIMD instructions for Intel Intrinsics
# https://software.intel.com/sites/landingpage/IntrinsicsGuide/
if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2")
endif()
```

Make the changes by running the following command:

```bash
sed -i "s/-mavx/-O2/g" src/CMakeLists.txt
```

**Note:**
Compiler options should be tuned and optimized to achieve higher performance, but you can keep it simple for now as performance optimization comes at a later phase of the project.


Application porting is now complete. Go to the next section to compile and run the ported application.

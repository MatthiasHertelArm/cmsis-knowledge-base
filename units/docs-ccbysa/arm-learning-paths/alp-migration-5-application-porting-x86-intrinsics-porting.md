---
id: "alp-migration-5-application-porting-x86-intrinsics-porting"
type: "concept"
domain: "project"
title: "Application porting: x86 intrinsics porting"
summary: "To port the AVX intrinsics, you can use SIMD Everywhere (SIMDe). By using SIMDe you can keep the AVX intrinsics in the source code and the intrinsics will be replaced by Neon instructions."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/5_application_porting.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/5_application_porting/#x86-intrinsics-porting"
license: "CC-BY-SA-4.0"
mode: "V"
---

To port the AVX intrinsics, you can use SIMD Everywhere ([SIMDe](https://github.com/simd-everywhere/simde)). By using SIMDe you can keep the AVX intrinsics in the source code and the intrinsics will be replaced by Neon instructions. 

Start by cloning the SIMDe repository:

```bash
git clone https://github.com/simd-everywhere/simde.git
```

Here are the changes required in `CMakeLists.txt`:

```output
# Add SIMDe options
include_directories(../simde)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
```

Run the command below to make the changes: 

```bash
sed -i "28i # Add SIMDe options\ninclude_directories(../simde)\nset(CMAKE_CXX_STANDARD 14)\nset(CMAKE_CXX_STANDARD_REQUIRED ON)\nset(CMAKE_CXX_EXTENSIONS OFF)\n" src/CMakeLists.txt
```

Finally, you need to include SIMDe AVX headers in `main.cpp` like this:

```output
#define SIMDE_ENABLE_NATIVE_ALIASES
#ifdef __aarch64__
#include "simde/x86/avx.h"
#else
#warning AVX support is not available. Code will not compile
#endif
```

The changes can be made by running: 

```bash
sed -i "40i #define SIMDE_ENABLE_NATIVE_ALIASES\n#ifdef __aarch64__\n#include \"simde/x86/avx.h\"\n#else\n#warning AVX support is not available. Code will not compile\n#endif" src/main.cpp
```

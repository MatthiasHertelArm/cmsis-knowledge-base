---
id: "ethu-driver-ethos-u-driver-source-code"
type: "concept"
domain: "edge-ai"
title: "Driver: Ethos-U driver source code"
summary: "The driver source is maintained in the Ethos-U core-driver repository. The software pack ARM::CMSIS-Ethos-U includes this source code unchanged and makes it available to CMSIS-based applications as a software component."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/driver/src/main.md#ethos-u-driver-source-code"
license: "Apache-2.0"
mode: "V"
---

The driver source is maintained in the
[Ethos-U core-driver repository](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver).
The software pack `ARM::CMSIS-Ethos-U` includes this source code unchanged and
makes it available to CMSIS-based applications as a software component. The
same source can therefore be obtained directly from the repository for use with
other build environments. The pack also includes CMSIS-RTOS2, FreeRTOS and
cache-management interfaces as optional source code templates.

| File or directory | Content |
| --- | --- |
| `include/` | Public driver, device, data-type, and PMU header files. |
| `src/` | Common driver code, variant-specific backend and PMU implementations, default configuration headers, register interfaces, and private headers. |
| `zephyr/` | Metadata for using the driver as a Zephyr module. |
| `CMakeLists.txt` | Build description for integrating or building the driver with CMake. |
| `README.md` | Standalone build instructions and driver API examples. |
| `LICENSE.txt`, `SECURITY.md` | License and security information for the driver source. |

### CMSIS Software component

The pack `ARM::CMSIS-Ethos-U` provides the software component `ARM::Machine Learning:NPU Support:Ethos-U Driver` in multiple variants. For using the driver add one variant of the component as shown below:

```yaml
components:
  - component: "ARM::Machine Learning:NPU Support:Ethos-U Driver&Generic U55" # For Ethos-U55 single-variant
```

```yaml
components:
  - component: "ARM::Machine Learning:NPU Support:Ethos-U Driver&Generic U65" # For Ethos-U65 single-variant
```

```yaml
components:
  - component: "ARM::Machine Learning:NPU Support:Ethos-U Driver&Generic U85" # For Ethos-U85 single-variant
```

```yaml
components:
  - component: "ARM::Machine Learning:NPU Support:Ethos-U Driver&Multi-Variant" # For runtime Ethos-U selection
```

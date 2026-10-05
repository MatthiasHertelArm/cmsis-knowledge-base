---
id: "rtx-trustzone-nortos-project-project-structure"
type: "concept"
domain: "rtos"
title: "TrustZone NoRTOS Project: Project Structure"
summary: "The project is generated using the CMSIS-Toolbox and is defined in csolution format:"
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/TrustZoneV8M/NoRTOS/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/TrustZoneV8M/NoRTOS/README.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

The project is generated using the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/) and
is defined in [`csolution`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/) format:

- `NoRTOS.csolution.yml` defines the hardware target and build-types (along with the compiler).
- `CM33_ns.cproject.yml` lists the required packs and defines the source files and software components for the non-secure application.
- `CM33_s.cproject.yml` lists the required packs and defines the source files and software components for the secure application.

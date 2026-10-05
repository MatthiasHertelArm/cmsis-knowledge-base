---
id: "sds-sds-with-sdsio-via-vsi-simulator-project-configuration"
type: "concept"
domain: "test"
title: "SDS with SDSIO via VSI (Simulator): Project Configuration"
summary: "During the simulation, the SDS files are saved on or read from the host computer. The following steps are required to configure the project for execution on the AVH-FVP simulator:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:template/sdsio/fvp/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/template/sdsio/fvp/README.md#project-configuration"
license: "Apache-2.0"
mode: "V"
---

During the simulation, the SDS files are saved on or read from the host computer. The following steps are required to configure the project for execution on the AVH-FVP simulator:

- create a [New Solution](https://arm-software.github.io/SDS-Framework/main/template.html#create-new-solution) named `SDS` in an empty folder with VS Code IDE.
- select the active target `SSE-300-U55` or `SSE-320-U85`, build and run the application.

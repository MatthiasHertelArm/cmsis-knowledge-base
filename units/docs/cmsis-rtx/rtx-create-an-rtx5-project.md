---
id: "rtx-create-an-rtx5-project"
type: "concept"
domain: "rtos"
title: "Create an RTX5 Project"
summary: "\\if FuSaRTS FuSa RTX5 installation and project setup are explained in fusartxinstallation. \\endif"
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/project.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/project.md"
license: "Apache-2.0"
mode: "V"
---

\if FuSaRTS
FuSa RTX5 installation and project setup are explained in fusa_rtx_installation.
\endif

\ifnot FuSaRTS
The steps to create a microcontroller application using RTX5 are:

- Install the pack.
- In your IDE, create a new project and select a microcontroller device.
- comp-sel "Add the Keil RTX5 software components" to your project.

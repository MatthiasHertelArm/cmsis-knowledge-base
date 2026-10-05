---
id: "tfm-details-for-the-platform-folder-system-startup"
type: "concept"
domain: "security"
title: "Details for the platform folder: System Startup"
summary: "Before calling main(), platform startup code should initialise all system clocks, perform runtime initialisation and other steps such as setting the vector table. Configuration of the following features is optional as TF-M architecture code will check and initialise them:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/source_structure/platform_folder.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/platform_folder.html#system-startup"
license: "BSD-3-Clause"
mode: "V"
---

Before calling `main()`, platform startup code should initialise all system
clocks, perform runtime initialisation and other steps such as setting the
vector table. Configuration of the following features is optional as TF-M
architecture code will check and initialise them:

  - The Security Extension.
  - The Floating-point Extension.

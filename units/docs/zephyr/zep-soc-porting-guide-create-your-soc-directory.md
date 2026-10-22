---
id: "zep-soc-porting-guide-create-your-soc-directory"
type: "concept"
domain: "bring-up"
title: "SoC Porting Guide: Create your SoC directory"
summary: "Each SoC must have a unique name. Use the official name given by the SoC vendor and check that it's not already in use. In some cases someone else may have contributed a SoC with identical name."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/soc_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/soc_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Each SoC must have a unique name. Use the official name given by the SoC vendor
and check that it's not already in use. In some cases someone else may have
contributed a SoC with identical name. If the SoC name is already in use, then
you should probably improve the existing SoC instead of creating a new one.
The script `list_hardware` can be used to retrieve a list of all SoCs known
in Zephyr, for example `./scripts/list_hardware.py --soc-root=. --socs` from
the Zephyr base directory for a list of names that are already in use.

Start by creating the directory `zephyr/soc/<VENDOR>/soc1`, where
`<VENDOR>` is your vendor subdirectory.


**Note:** A `<VENDOR>` subdirectory is mandatory if contributing your SoC to Zephyr, but if your SoC is placed in a local repo, then any folder structure under `<your-repo>/soc` is permitted. The `<VENDOR>` subdirectory must match a vendor defined in the list in have a prefix in that list, then one must be created.


**Note:** The SoC directory name does not need to match the name of the SoC. Multiple SoCs can even be defined in one directory. In Zephyr, SoCs are often organized in sub-folders in a common SoC Family or SoC Series tree.

Your SoC directory should look like this:

```none

soc/<VENDOR>/<soc-name>
├── soc.yml
├── soc.h
├── CMakeLists.txt
├── Kconfig
├── Kconfig.soc
└── Kconfig.defconfig
```
Replace `<soc-name>` with your SoC's name.


The mandatory files are:

#. `soc.yml`: a YAML file describing the high-level meta data of the
   SoC such as:

   - SoC name: the name of the SoC
   - CPU clusters: CPU clusters if the SoC contains one or more clusters
   - SoC series: the SoC series to which the SoC belong
   - SoC family: the SoC family to which the series belong

#. `soc.h`: a header file which can be used to describe or provide
   configuration macros for the SoC. The `soc.h` will often be included in
   drivers, sub-systems, boards, and other source code found in Zephyr.

#. `Kconfig.soc`: the base SoC configuration which defines a Kconfig SoC
   symbol in the form of `config SOC_<soc-name>` and provides the SoC name to
   the Kconfig `SOC` setting.
   If the `soc.yml` describes a SoC family and series, then those must also
   be defined in this file. Kconfig settings outside of the SoC tree must not be
   selected. To select general Zephyr Kconfig settings the `Kconfig` file
   must be used.

#. `CMakeLists.txt`: CMake file loaded by the Zephyr build system. This
   CMake file can define additional include paths and/or source files to be used
   when a build targets the SoC. Also the base line linker script to use must be
   defined.

The optional files are:

- `Kconfig`, `Kconfig.defconfig` software configuration in
  kconfig format. These select the architecture and peripherals
  available.

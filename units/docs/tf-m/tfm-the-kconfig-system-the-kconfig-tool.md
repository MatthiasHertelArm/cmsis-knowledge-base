---
id: "tfm-the-kconfig-system-the-kconfig-tool"
type: "concept"
domain: "security"
title: "The Kconfig System: The Kconfig tool"
summary: "The Kconfig tool is a python script based on Kconfiglib to generate the following config files:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/configuration/kconfig_system.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/kconfig_system.html#the-kconfig-tool"
license: "BSD-3-Clause"
mode: "V"
---

The Kconfig tool is a python script based on [Kconfiglib](https://github.com/ulfalizer/Kconfiglib)
to generate the following config files:

- CMake config file

  Contains CMake cache variables of building options.

- Header file

  Contains component options in the header file system.
  Component options are gathered together in a separate menu `TF-M component configs` in
  The Kconfig files.

- The .config and .config.old files

  The `.config` file which contains all the above configurations in the Kconfig format.
  It will be created after the first execution of the script. It is only used to allow
  users to make adjustments basing on the previous settings.
  The Kconfig tool will load it if it exists and `.config.old` will be created to
  save the previous configurations.

The tool supports loading multiple pre-set configuration files merging into a single one.
The first loaded options are overridden by later ones if the config files contain duplicated
options.
And dependencies between config options are taken care of.
It then launches a configuration GUI for users to change any config options if the `MENUCONFIG` is
enabled in build command line.


### Integration with TF-M build system

TF-M build system includes `kconfig.cmake` to integrate this tool.
It prepares the parameters for the script and invokes it to load multiple configuration files basing
on your build setup, including but not limited to

  - Build type bound configurations, decided by `CMAKE_BUILD_TYPE`
  - Profile configurations, decided by `TFM_PROFILE`

---
id: "tfm-the-kconfig-system-customizing-config-options"
type: "concept"
domain: "security"
title: "The Kconfig System: Customizing config options"
summary: "By default, the Kconfig system only merges configuration files and generated the final config files. To customize the config options, there are several approaches."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/configuration/kconfig_system.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/kconfig_system.html#customizing-config-options"
license: "BSD-3-Clause"
mode: "V"
---

By default, the Kconfig system only merges configuration files and generated the final config files.
To customize the config options, there are several approaches.


### Menuconfig

Menuconfig is the recommended approach to adjust the values of the config options because it has
a graphic interface for you to easily change the options without worrying about dependencies.

To launch the menuconfig, you need to enable `MENUCONFIG` in addition to enabling
`USE_KCONFIG_TOOL`.

```bash

cmake -S . -B cmake_build -DTFM_PLATFORM=arm/mps2/an521 \
                          -DUSE_KCONFIG_TOOL=ON \
                          -DMENUCONFIG=ON
```

**Note:** Although the Kconfiglib provides three [menuconfig interfaces](https://github.com/ulfalizer/Kconfiglib#menuconfig-interfaces), only GUI menuconfig can be launched by CMake for the time being.


### Command line options

The support of passing configurations via command line is kept for the Kconfig system.

```bash

cmake -S . -B cmake_build -DTFM_PLATFORM=arm/mps2/an521 \
                          -DUSE_KCONFIG_TOOL=ON \
                          -DTFM_ISOLATION_LEVEL=2
```

### Kconfig file

You can also put the frequently used config options into a Kconfig file. When you need to apply the
config options in that file, pass it via command line option `-DKCONFIG_CONFIG_FILE`

```bash

cmake -S . -B cmake_build -DTFM_PLATFORM=arm/mps2/an521 \
                          -DTFM_ISOLATION_LEVEL=2 \
                          -DUSE_KCONFIG_TOOL=ON \
                          -DKCONFIG_CONFIG_FILE=my_config.conf
```

**Note:** The command line set options override the ones in the config file. And you can always launch menuconfig to do the final adjustments.

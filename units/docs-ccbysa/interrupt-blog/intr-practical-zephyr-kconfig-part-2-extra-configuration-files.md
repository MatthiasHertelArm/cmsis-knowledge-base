---
id: "intr-practical-zephyr-kconfig-part-2-extra-configuration-files"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Using different configuration files / Extra configuration files"
summary: "Part of: Using different configuration files"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#extra-configuration-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Using different configuration files_

There is one more option to modify the _Kconfig_, listed among the [important build system variables in Zephyr's official documentation](https://docs.zephyrproject.org/latest/develop/application/index.html#important-build-system-variables): `EXTRA_CONF_FILE`. This build system variable accepts one or more additional _Kconfig_ fragments. This option can be useful, e.g., to specify additional configuration options used by multiple build types (normal builds, "release" builds, "debug" builds) in a separate fragment. An example could be adding TLS configs with a `tls.conf` or adding external NOR configs with `qspi_nor.conf`

> **Note:** Since [Zephyr 3.4.0](https://docs.zephyrproject.org/latest/releases/release-notes-3.4.html) the `EXTRA_CONF_FILE` build system variable replaces the deprecated variable `OVERLAY_CONFIG`.

Let's add two _Kconfig_ fragments `extra0.conf` and `extra1.conf`:

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── boards
│   ├── nrf52840dk_nrf52840.conf
│   └── nrf52840dk_nrf52840_release.conf
├── src
│   └── main.c
├── CMakeLists.txt
├── extra0.conf
├── extra1.conf
├── prj.conf
└── prj_release.conf

$ cat extra0.conf
CONFIG_DEBUG=n

$ cat extra1.conf
CONFIG_GPIO=n
```

> **Notice:** In an actual project, you'll need to pick better names for the extra configuration files, e.g., `no-debug.conf` and `no-gpio.conf`. I'm using `extra0.conf` and `extra1.conf` to explicitly show their use and to make the order in which the files are applied visible, as you'll see just now.

We can now pass the two extra configuration fragments to the build system using the `EXTRA_CONF_FILE` variable. The paths are relative to the project root and can either be separated using semicolons or spaces:

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build -- \
  -DEXTRA_CONF_FILE="extra0.conf;extra1.conf"
```

```
Parsing /opt/nordic/ncs/v3.2.1/zephyr/Kconfig
Loaded configuration '/opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig'
Merged configuration '/path/to/01_kconfig/prj.conf'
Merged configuration '/path/to/01_kconfig/boards/nrf52840dk_nrf52840.conf'
Merged configuration '/path/to/01_kconfig/extra0.conf'
Merged configuration '/path/to/01_kconfig/extra1.conf'
Configuration saved to '/path/to/build/zephyr/.config'
```

The fragments specified using the `EXTRA_CONF_FILE` variable are merged into the final configuration in the given order. E.g., we can create a `release` build and reverse the order of the fragments:

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build -- \
  -DCONF_FILE="prj_release.conf" \
  -DEXTRA_CONF_FILE="extra1.conf;extra0.conf"
```

```
Parsing /opt/nordic/ncs/v3.2.1/zephyr/Kconfig
Loaded configuration '/opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig'
Merged configuration '/path/to/01_kconfig/prj_release.conf'
Merged configuration '/path/to/01_kconfig/boards/nrf52840dk_nrf52840_release.conf'
Merged configuration '/path/to/01_kconfig/extra1.conf'
Merged configuration '/path/to/01_kconfig/extra0.conf'
Configuration saved to '/path/to/build/zephyr/.config'
```

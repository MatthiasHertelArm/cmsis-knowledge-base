---
id: "zep-setting-kconfig-configuration-valu-the-initial-configuration"
type: "concept"
domain: "project"
title: "Setting Kconfig configuration values: The Initial Configuration"
summary: "The initial configuration for an application comes from merging configuration settings from three sources:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/setting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/setting.rst"
license: "Apache-2.0"
mode: "V"
---

The initial configuration for an application comes from merging configuration
settings from three sources:

1. A `BOARD`-specific configuration file stored in
   `boards/<VENDOR>/<BOARD>/<BOARD>_defconfig`

2. Any CMake cache entries prefix with `CONFIG_`

3. The application configuration

The application configuration can come from the sources below (each file is
known as a Kconfig fragment, which are then merged to get the final
configuration used for a particular build). By default, `prj.conf` is
used.

#. If `CONF_FILE` is set, the configuration file(s) specified in it are
   merged and used as the application configuration. `CONF_FILE` can be set
   in various ways:

   1. In `CMakeLists.txt`, before calling `find_package(Zephyr)`

   2. By passing `-DCONF_FILE=<conf file(s)>`, either directly or via `west`

   3. From the CMake variable cache

#. Otherwise, if `boards/<BOARD>.conf` exists in the application
   configuration directory, the result of merging it with `prj.conf` is
   used.

#. Otherwise, if board revisions are used and
   `boards/<BOARD>_<revision>.conf` exists in the application
   configuration directory, the result of merging it with `prj.conf` and
   `boards/<BOARD>.conf` is used.

#. Otherwise, `prj.conf` is used from the application configuration
   directory. If it does not exist then a fatal error will be emitted.

Furthermore, applications can have SoC Kconfig fragments added to the configuration,
the file `socs/<SOC>_<BOARD_QUALIFIERS>.conf` will be applied if it exists,
after the main project configuration has been applied and before any board Kconfig
fragments files have been applied.

All configuration files will be taken from the application's configuration
directory except for files with an absolute path that are given with the
`CONF_FILE`, `EXTRA_CONF_FILE`, `DTC_OVERLAY_FILE`, and
`EXTRA_DTC_OVERLAY_FILE` arguments.  For these,
a file in a Zephyr module can be referred by escaping the Zephyr module dir
variable like this `\${ZEPHYR_<module>_MODULE_DIR}/<path-to>/<file>`
when setting any of said variables in the application's `CMakeLists.txt`.

See Application Configuration Directory
on how the application configuration directory is defined.

If a symbol is assigned both in `<BOARD>_defconfig` and in the
application configuration, the value set in the application configuration takes
precedence.

The merged configuration is saved to `zephyr/.config` in the build
directory.

As long as `zephyr/.config` exists and is up-to-date (is newer than any
`BOARD` and application configuration files), it will be used in preference
to producing a new merged configuration. `zephyr/.config` is also the
configuration that gets modified when making changes in the :ref:`interactive
configuration interfaces <menuconfig>`.

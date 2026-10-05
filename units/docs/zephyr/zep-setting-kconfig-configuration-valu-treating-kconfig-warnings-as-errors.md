---
id: "zep-setting-kconfig-configuration-valu-treating-kconfig-warnings-as-errors"
type: "concept"
domain: "project"
title: "Setting Kconfig configuration values: Treating Kconfig warnings as errors"
summary: "Some Kconfig warnings abort the build by default, for example assignments to undefined symbols."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/setting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/setting.rst"
license: "Apache-2.0"
mode: "V"
---

Some Kconfig warnings abort the build by default, for example assignments to
undefined symbols. Others are only printed, for example when a symbol is set
more than once, or when an assignment is ignored because the dependencies of
the symbol are not satisfied.

Set the `KCONFIG_WARNING_AS_ERROR` CMake variable to treat *every*
Kconfig warning as an error:

```console

west build -b <board> <app> -- -DKCONFIG_WARNING_AS_ERROR=y
```
This is useful in CI, where a silently ignored configuration setting is likely
to be a mistake. It is read with `zephyr_get()`, so it can also be given as
an environment variable or through a
cmake_build_config_package.

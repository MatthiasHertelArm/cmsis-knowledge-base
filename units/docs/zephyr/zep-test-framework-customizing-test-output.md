---
id: "zep-test-framework-customizing-test-output"
type: "concept"
domain: "test"
title: "Test Framework: Customizing Test Output"
summary: "Customization is enabled by setting CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE to \"y\" and adding a file tc_util_user_override.h with your overrides."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

Customization is enabled by setting `CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE` to "y"
and adding a file `tc_util_user_override.h` with your overrides.

Add the line `zephyr_include_directories(my_folder)` to
your project's `CMakeLists.txt` to let Zephyr find your header file during builds.

See the file `subsys/testsuite/include/zephyr/tc_util.h` to see
which macros and/or defines can be overridden.
These will be surrounded by blocks such as:

```C

#ifndef SOMETHING
#define SOMETHING <default implementation>
#endif /* SOMETHING */
```

---
id: "zep-logging-usage"
type: "concept"
domain: "debug"
title: "Logging: Usage"
summary: "In order to use logging in the module, a unique name for the module must be specified and the module must be registered using LOG_MODULE_REGISTER."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Logging in a module


In order to use logging in the module, a unique name for the module must be
specified and the module must be registered using `LOG_MODULE_REGISTER`.
Optionally, a compile time log level for the module can be specified as the
second parameter. The default log level (`CONFIG_LOG_DEFAULT_LEVEL`) is used
if a custom log level is not provided.

```c

#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(foo, CONFIG_FOO_LOG_LEVEL);
```
If the module consists of multiple files, then `LOG_MODULE_REGISTER()` should
appear in exactly one of them. Each other file should use
`LOG_MODULE_DECLARE` to declare its membership in the module.
Optionally, a compile time log level for the module can be specified as
the second parameter. The default log level (`CONFIG_LOG_DEFAULT_LEVEL`)
is used if a custom log level is not provided.

```c

#include <zephyr/logging/log.h>
/* In all files comprising the module but one */
LOG_MODULE_DECLARE(foo, CONFIG_FOO_LOG_LEVEL);
```
In order to use the logging API in a function implemented in a header file,
`LOG_MODULE_DECLARE` macro must be used in the function body
before the logging API is called. Optionally, a compile time log level for the module
can be specified as the second parameter. The default log level
(`CONFIG_LOG_DEFAULT_LEVEL`) is used if a custom log level is not
provided.

```c

#include <zephyr/logging/log.h>

static inline void foo(void)
{
    LOG_MODULE_DECLARE(foo, CONFIG_FOO_LOG_LEVEL);

    LOG_INF("foo");
}
```
The dedicated Kconfig template (`subsys/logging/Kconfig.template.log_config`)
can be used to create a local log level configuration.

The example below shows the template being used. As a result, `CONFIG_FOO_LOG_LEVEL`
will be generated:

```none

module = FOO
module-str = foo
source "subsys/logging/Kconfig.template.log_config"
```

### Logging in a module instance


In case there are modules which are multi-instance and instances are widely used
across the system, enabling logs will lead to flooding. The logging API provides tools
which can be used to filter logs on the instance level rather than the module
level. For example, logging can be enabled for a particular instance only.

In order to use instance level filtering, the following steps must be performed:

- A pointer to a specific logging structure is declared in the instance structure.
  `LOG_INSTANCE_PTR_DECLARE` is used for that.

```c

#include <zephyr/logging/log_instance.h>

struct foo_object {
    LOG_INSTANCE_PTR_DECLARE(log);
    uint32_t id;
}
```
- The module must provide a macro for its instantiation. In that macro, the logging instance
  is registered and the log instance pointer is initialized in the object structure.

```c

#define FOO_OBJECT_DEFINE(_name)                             \
    LOG_INSTANCE_REGISTER(foo, _name, CONFIG_FOO_LOG_LEVEL) \
    struct foo_object _name = {                             \
        LOG_INSTANCE_PTR_INIT(log, foo, _name)          \
    }
```
Note that when logging is disabled, the logging instance and pointer to that instance
are not created.

In order to use the instance logging API in a source file, a compile-time log
level must be set using `LOG_LEVEL_SET`.

```c

LOG_LEVEL_SET(CONFIG_FOO_LOG_LEVEL);

void foo_init(foo_object *f)
{
    LOG_INST_INF(f->log, "Initialized.");
}
```
In order to use the instance logging API in a header file, a compile-time log
level must be set using `LOG_LEVEL_SET`.

```c

static inline void foo_init(foo_object *f)
{
    LOG_LEVEL_SET(CONFIG_FOO_LOG_LEVEL);

    LOG_INST_INF(f->log, "Initialized.");
}
```

### Controlling the logging


By default, log processing in deferred mode is handled internally by a
dedicated task which starts automatically. However, it might not be available
if multithreading is disabled. It can also be disabled by unsetting
`CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD`. In that case, logging can
be controlled using the API defined in `include/zephyr/logging/log_ctrl.h`.
Logging must be initialized before it can be used. Optionally, the user can provide
a function which returns a timestamp value. If not provided, `k_cycle_get`
or `k_cycle_get_32` is used for timestamping.
The `log_process` function is used to process one log
message (if pending), and returns true if there are more messages pending.
However, it is recommended to use macro wrappers (`LOG_INIT` and
`LOG_PROCESS`), which handle the case where logging is disabled.

The following snippet shows how logs can be processed in a simple infinite loop.

```c

#include <zephyr/logging/log_ctrl.h>

int main(void)
{
    LOG_INIT();
    /* If multithreading is enabled provide thread id to the logging. */
    log_thread_set(k_current_get());

    while (1) {
        if (LOG_PROCESS() == false) {
            /* sleep */
        }
    }
}
```
If logs are processed from a thread (user or internal), then it is possible to enable
a feature which will wake up the processing thread when a certain number of log messages is
buffered (see `CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD`).

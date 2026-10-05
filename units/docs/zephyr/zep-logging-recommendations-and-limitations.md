---
id: "zep-logging-recommendations-and-limitations"
type: "concept"
domain: "debug"
title: "Logging: Recommendations and limitations"
summary: "Logging: Recommendations and limitations"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

Consider the following recommendations:

* Enable `CONFIG_LOG_SPEED` to slightly speed up deferred logging at the
  cost of a slight increase in memory footprint.
* It is recommended to cast a pointer to `const char *` when it is used with a `%s`
  format specifier and it points to a constant string.
* It is recommended to cast a pointer to `char *` when it is used with a `%s`
  format specifier and it points to a transient string.
* It is required to cast a character pointer to non character pointer
  (e.g., `void *`) when it is used with a `%p` format specifier.

```c

LOG_WRN("%s", str);
LOG_WRN("%p", (void *)str);
```
Consider the following limitations:

* Logging does not support string format specifiers with width (e.g., `%.*s` or `%8s`). That
  is because format string content is not used to build a log message, only argument types.
* If deferred logging is used and log messages are prefixed with the thread name
  (Kconfig option `CONFIG_LOG_THREAD_ID_PREFIX=y` and `CONFIG_THREAD_NAME=y`), it is assumed that
  the corresponding `k_thread` structure is still valid when the log message is
  formatted. This can be an issue when that structure is allocated dynamically, using `k_malloc` or
  `malloc` for instance. In this case, if the thread logs some messages and then gets
  stopped and its `struct k_thread` is freed, the log system will still try to access that
  structure when handling the message later. This creates a use-after-free scenario.
  To avoid this, a solution consists in calling `log_flush` before freeing the structure.

```c

struct k_thread *thread = k_malloc(sizeof(*thread)); /* struct allocated dynamically */
k_thread_create(thread, ...);
k_thread_name_set(thread, "foobar");

/* Thread calls LOG_*(...) */

k_thread_join(thread, K_FOREVER);
log_flush();  /* flush log buffer before freeing the struct k_thread */
k_free(thread); /* avoid a potential use-after-free scenario if deferred logging is used */
```

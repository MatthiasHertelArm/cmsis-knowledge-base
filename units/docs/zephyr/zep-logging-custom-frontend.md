---
id: "zep-logging-custom-frontend"
type: "concept"
domain: "debug"
title: "Logging: Architecture / Custom Frontend"
summary: "Custom frontend is enabled using CONFIG_LOG_FRONTEND. Logs are directed to functions declared in include/zephyr/logging/log_frontend.h. If option CONFIG_LOG_FRONTEND_ONLY is enabled then log message is not created and no backend is handled. Otherwise, custom frontend can coexist with backends."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Architecture_

Custom frontend is enabled using `CONFIG_LOG_FRONTEND`. Logs are directed
to functions declared in `include/zephyr/logging/log_frontend.h`.
If option `CONFIG_LOG_FRONTEND_ONLY` is enabled then log message is not
created and no backend is handled. Otherwise, custom frontend can coexist with
backends.

In some cases, logs need to be redirected at the macro level. For these cases,
`CONFIG_LOG_CUSTOM_HEADER` can be used to inject an application provided
header named `zephyr_custom_log.h` at the end of `include/zephyr/logging/log.h`.


#### Frontend using ARM Coresight STM (System Trace Macrocell)


For more details about logging using ARM Coresight STM see logging_cs_stm.

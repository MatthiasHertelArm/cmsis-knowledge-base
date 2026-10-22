---
id: "zep-logging-rate-limited-logging"
type: "concept"
domain: "debug"
title: "Logging: Rate-limited logging"
summary: "Rate-limited logging macros provide a way to prevent log flooding when messages are generated frequently. These macros ensure that log messages are not output more frequently than a specified interval, similar to Linux's printk_ratelimited functionality."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

Rate-limited logging macros provide a way to prevent log flooding when messages are
generated frequently. These macros ensure that log messages are not output more
frequently than a specified interval, similar to Linux's `printk_ratelimited`
functionality.

The rate-limited logging system provides two types of macros:

**Convenience macros (using default rate):**
- `LOG_ERR_RATELIMIT` - Rate-limited error messages
- `LOG_WRN_RATELIMIT` - Rate-limited warning messages
- `LOG_INF_RATELIMIT` - Rate-limited info messages
- `LOG_DBG_RATELIMIT` - Rate-limited debug messages
- `LOG_HEXDUMP_ERR_RATELIMIT` - Rate-limited error hexdump
- `LOG_HEXDUMP_WRN_RATELIMIT` - Rate-limited warning hexdump
- `LOG_HEXDUMP_INF_RATELIMIT` - Rate-limited info hexdump
- `LOG_HEXDUMP_DBG_RATELIMIT` - Rate-limited debug hexdump

**Explicit rate macros (with custom rate):**
- `LOG_ERR_RATELIMIT_RATE` - Rate-limited error messages with custom rate
- `LOG_WRN_RATELIMIT_RATE` - Rate-limited warning messages with custom rate
- `LOG_INF_RATELIMIT_RATE` - Rate-limited info messages with custom rate
- `LOG_DBG_RATELIMIT_RATE` - Rate-limited debug messages with custom rate
- `LOG_HEXDUMP_ERR_RATELIMIT_RATE` - Rate-limited error hexdump with custom rate
- `LOG_HEXDUMP_WRN_RATELIMIT_RATE` - Rate-limited warning hexdump with custom rate
- `LOG_HEXDUMP_INF_RATELIMIT_RATE` - Rate-limited info hexdump with custom rate
- `LOG_HEXDUMP_DBG_RATELIMIT_RATE` - Rate-limited debug hexdump with custom rate

The convenience macros use the default rate specified by `CONFIG_LOG_RATELIMIT_INTERVAL_MS`
(5000ms by default). The explicit rate macros take a rate parameter (in milliseconds) that specifies
the minimum interval between log messages. The rate limiting is per-macro-call-site, meaning
that each unique call to a rate-limited macro has its own independent rate limit.

Example usage:

```c

#include <zephyr/logging/log.h>
#include <zephyr/kernel.h>

LOG_MODULE_REGISTER(my_module, CONFIG_LOG_DEFAULT_LEVEL);

void process_data(void)
{
    /* Convenience macros using default rate (CONFIG_LOG_RATELIMIT_INTERVAL_MS) */
    LOG_WRN_RATELIMIT("Data processing warning: %d", error_code);
    LOG_ERR_RATELIMIT("Critical error occurred: %s", error_msg);
    LOG_INF_RATELIMIT("Processing status: %d items", item_count);
    LOG_HEXDUMP_WRN_RATELIMIT(data_buffer, data_len, "Data buffer:");

    /* Explicit rate macros with custom intervals */
    LOG_WRN_RATELIMIT_RATE(1000, "Fast rate warning: %d", error_code);
    LOG_ERR_RATELIMIT_RATE(30000, "Slow rate error: %s", error_msg);
    LOG_INF_RATELIMIT_RATE(2000, "Custom rate status: %d items", item_count);
    LOG_HEXDUMP_ERR_RATELIMIT_RATE(5000, data_buffer, data_len, "Error data:");
}
```
Rate-limited logging is particularly useful for:

- Error conditions that might occur frequently but don't need to flood the logs
- Status updates in tight loops or high-frequency callbacks
- Debug information that could overwhelm the logging system
- Network or I/O operations that might fail repeatedly


### Configuration


Rate-limited logging can be configured using the following Kconfig options:

- `CONFIG_LOG_RATELIMIT` - Master switch to enable/disable rate-limited logging
- `CONFIG_LOG_RATELIMIT_INTERVAL_MS` - Default interval for convenience macros (5000ms)

When `CONFIG_LOG_RATELIMIT` is disabled, the behavior of rate-limited macros is controlled
by the `CONFIG_LOG_RATELIMIT_FALLBACK` choice:

- `CONFIG_LOG_RATELIMIT_FALLBACK_LOG` - All rate-limited macros behave as regular logging macros
- `CONFIG_LOG_RATELIMIT_FALLBACK_DROP` - All rate-limited macros expand to no-ops (default)

This allows you to control whether rate-limited log macros should always print or be completely
suppressed when rate limiting is not available.

The rate limiting is implemented using static variables and `k_uptime_get_32`
to track the last log time for each call site.

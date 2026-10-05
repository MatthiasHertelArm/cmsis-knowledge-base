---
id: "intr-a-guide-to-watchdog-timers-for-emb-a-basic-implementation"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: A Basic Implementation"
summary: "Let's start with a very naive implementation and build up from there. We'll create a low priority thread. If it's able to run, we'll feed the watchdog."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#a-basic-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's start with a _very_ naive implementation and build up from there. We'll create a low priority thread. If it's able to run, we'll feed the watchdog. If a task gets starved or something higher priority is stuck in a loop, the system should reboot.

```c
static void prvWatchdogTask(void *pvParameters) {
  while (1) {
    vTaskDelay(1000);
    hardware_watchdog_feed();
  }
}
```

### Hang while polling a Sensor

One common class of hangs results from polling a sensor while you wait for a transaction to complete. Here's such an example:

```c
// main.c
void erase_external_flash(void) {
  // some logic to start a flash erase
  // poll for completion
  while (!spi_flash_erase_complete()) { };
  // we never get here!
}
```

> Implementation Note: Instead of polling in a loop indefinitely, we could have also added a timeout. However, for most simple devices a response _is_ expected. Failure to see a response is often a software issue such as an interrupt or peripheral misconfiguration. Adding timeout logic and attempting to gracefully recover is something that should be done sparingly. When this is done, you open yourself to more complex recovery paths that may have problems of their own. Additionally, important state about the underlying issue is lost making root cause analysis even harder. Failing out exactly where the hang is taking place makes it easier to root cause and fix the actual problem.

Let's see if our watchdog implementation can catch this type of hang!

```
(gdb) mon reset
Resetting target
(gdb) break main
Breakpoint 1 at 0x174: file interrupt/example/watchdog-example/main.c, line 151.
(gdb) continue
Continuing.

Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:151
151   prv_check_and_reset_reboot_reason();

// Select the polling hang configuration
(gdb) set g_watchdog_hang_config=2
(gdb) continue
Continuing.

Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:151
151   prv_check_and_reset_reboot_reason();
(gdb) c
Continuing.

[ ... wait about 10 seconds ... ]
Program received signal SIGTRAP, Trace/breakpoint trap.
prv_check_and_reset_reboot_reason () at interrupt/example/watchdog-example/main.c:146
146     __asm("bkpt 10");
```

Sweet, it did! We see we fell into the catch for watchdog resets upon reboot.

### Hang waiting for a mutex

Let's explore another class of hang due to a missing release of a mutex.

```c
int read_temp_sensor(uint32_t *temp) {
  xSemaphoreTake(s_temp_i2c_mutex, portMAX_DELAY);
  int rv = i2c_read_temp(temp);
  if (rv == -1) {
    // BUG: Semaphore should have been released here!
    return rv;
  }
  xSemaphoreGive(s_temp_i2c_mutex);
  return 0;
}
```

```
(gdb) mon reset
Resetting target
(gdb) break main
Breakpoint 1 at 0x174: file interrupt/example/watchdog-example/main.c, line 151.
(gdb) continue
Continuing.

Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:151
151   prv_check_and_reset_reboot_reason();

// Select the mutex hang configuration
(gdb) set g_watchdog_hang_config=3
(gdb) continue
Continuing.
// observe no reboot
```

Wait, what .. No reboot?!

This hang is a bit more _subtle_. The high priority thread is not
executing any code because it is suspended waiting for a mutex. This means our low priority thread
will be scheduled to run by the RTOS and can keep feeding the watchdog.

---
id: "intr-a-guide-to-watchdog-timers-for-emb-adding-a-task-watchdog"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: Adding a \"Task\" Watchdog"
summary: "So we've just discovered our simple watchdog scheme has some shortcomings ... it is not able to catch deadlocks between tasks."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#adding-a-task-watchdog"
license: "CC-BY-SA-4.0"
mode: "V"
---

So we've just discovered our simple watchdog scheme has some shortcomings ... it is not able to catch deadlocks between tasks. It seems like what we really want is a way to monitor that our event loops are making forward progress.

This can be achieved by wrapping our hardware watchdog implementation. Instead of unconditionally
calling `hardware_watchdog_feed()`, we will add an API tasks can register with and _only_ feed the
hardware watchdog if all tasks have recently checked in.

### C Code Example

```c
static uint32_t s_registered_tasks = 0;
static uint32_t s_fed_tasks = 0;

static void prv_task_watchdog_check(void) {
  if ((s_fed_tasks & s_registered_tasks) == s_registered_tasks) {
    // all the tasks have been fed or are idle!
    hardware_watchdog_feed();
    s_fed_tasks = 0;
  }
}

void task_watchdog_register_task(uint32_t task_id) {
  __disable_irq();

  s_registered_tasks |= (1 << task_id);

  __enable_irq();
}

void task_watchdog_unregister_task(uint32_t task_id) {
  __disable_irq();

  s_registered_tasks &= ~(1 << task_id);
  s_fed_tasks &= ~(1 << task_id);
  prv_task_watchdog_check();

  __enable_irq();
}

void task_watchdog_feed_task(uint32_t task_id) {
  __disable_irq();

  s_fed_tasks |= (1 << task_id);
  prv_task_watchdog_check();

  __enable_irq();
}
```

> NOTE: Since `s_fed_tasks` and `s_registered_tasks` are accessed by multiple tasks, I added
> "locking" around the updates to prevent corruption by disabling interrupts. Since the number of
> cycles for the update is really short, this should not be a problem. However, with GCC, one could
> have also made use of the builtin atomic APIs[^8].

#### Pseudocode for Usage of Task Watchdog

All embedded systems operate on an event loop of some sort. Here's an example of how we could use the above API in a loop to get a better sense of how it works.

```c
static void background_service_event_loop(void) {
  while (1) {
    const int task_id = kTaskId_BackGroundWorkLoop;
    // Since it could be a long time between events
    // unregister the task watchdog
    task_watchdog_unregister_task(task_id);
    wait_for_work();

    // we have work to do, so register a watchdog to catch
    // situations where the work takes an unreasonable amount of
    // time to complete
    task_watchdog_register_task(task_id);

    // OPTIONAL: If the task to perform takes a very long
    // time (i.e a flash chip erase), feed the task watchdog
    // to give us a little extra time.
    //
    // NOTE: The watchdog timeout you chose should
    // be sufficient for nearly every system event
    // so this pattern should be used _very_ sparingly
    task_watchdog_feed_task(task_id);

    [... perform work ...]
  }
}
```

##### Task Watchdog in Hardware

> NOTE: The astute reader might note that this sounds like a use case for the multiple reload request registers on the NRF52 that we mentioned [above](#reload-request-registers). You aren't wrong! It's a pretty nifty hardware feature. However, not all watchdog peripherals have this feature and the cost of implementing it in code is very small (< 100 bytes). In this situation, I'd typically favor a software implementation that can be shared across a range of MCUs and easily unit tested.

#### Adding Task Watchdog To Example App

If you are following along with the code example, at this point you can pick up the task watchdog changes by doing the following:

```
$ cd $INTERRUPT_REPO/example/watchdog-example/
$ git apply 01-patch-task-watchdog.patch
$ make
```

### Retry "Hang waiting for a mutex"

Let's apply a patch that leverages the new task watchdog for the tasks in the example app and retry

```
(gdb) mon reset
(gdb) continue
Continuing.

Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:162
162   prv_check_and_reset_reboot_reason();
(gdb)  set g_watchdog_hang_config=3
(gdb) continue
Continuing.

Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:160
160   prv_check_and_reset_reboot_reason();
(gdb) continue

Program received signal SIGTRAP, Trace/breakpoint trap.
prv_check_and_reset_reboot_reason () at interrupt/example/watchdog-example/main.c:157
157     __asm("bkpt 10");
```

Awesome, it worked!

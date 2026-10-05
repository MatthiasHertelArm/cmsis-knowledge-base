---
id: "intr-a-guide-to-watchdog-timers-for-emb-root-causing-watchdogs"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: Root Causing Watchdogs"
summary: "It's great that we can now catch system hangs but how do we debug them?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#root-causing-watchdogs"
license: "CC-BY-SA-4.0"
mode: "V"
---

It's great that we can now catch system hangs but how do we debug them? At the moment all we see is
one bit on reset _after_ the watchdog has taken place which is not particularly helpful for root
causing the original issue.

What we really want is to be able to do is execute code prior to a watchdog reset occurring. As we
explored [above](#nrf52-watchdog-interrupt), the NRF52 does have an interrupt we can enable but it
gives us no control over deferring the reboot to do any cleanup. In this situation it's usually pretty easy to re-purpose a built-in peripheral timer to accomplish this.

### Adding a "Software" Watchdog

For the purposes of this example we will use the NRF52 Timer0 Peripheral to implement our software
watchdog. We'll want the timeout to be a little less than the hardware watchdog timeout so for this
example lets use a timeout of 7 seconds. To "feed" this watchdog, we will just restart the timer. If 7 seconds elapses without a feed, the ISR will fire and we know the system is about to watchdog.

We can then treat this interrupt as another "fault handler" and apply the [lessons learned from our post](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug) about debugging Cortex-M faults to this situation as well!

#### Software Watchdog Example C Code

```c
void TimerTask0_Handler(void) {
  __asm volatile(
      "tst lr, #4 \n"
      "ite eq \n"
      "mrseq r0, msp \n"
      "mrsne r0, psp \n"
      "b watchdog_fault_handler_c \n");
}

// Disable optimizations for this function so "frame" argument
// does not get optimized away
__attribute__((optimize("O0")))
void watchdog_fault_handler_c(sContextStateFrame *frame) {
  // If and only if a debugger is attached, execute a breakpoint
  // instruction so we can take a look at what triggered the fault
  HALT_IF_DEBUGGING();

  // We are about to watchdog so do one last feed
  // to give us time to cleanup & then explicitly reboot
  hardware_watchdog_feed();

  // Logic for dealing with the exception. Typically:
  //  - Save a coredump for postmortem analysis so you
  //    can root cause deadlocks or hangs
  //  - perform any shutdown/cleanup needed before reboot
  //  - reboot the system
}
```

#### Adding Software Watchdog To Example App

If you are following along with the code example, at this point you can pick up the task watchdog changes by doing the following:

```
$ cd $INTERRUPT_REPO/example/watchdog-example/
$ git apply 02-patch-software-watchdog.patch
$ make
```

### Debugging our example hangs

Let's walk back through some of the examples we explored early in the article and see if we can root cause what led to the hang!

#### Hang while polling a Sensor

```
(gdb) mon reset
Resetting target

(gdb) break main
Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:162
162   prv_check_and_reset_reboot_reason();

(gdb) set g_watchdog_hang_config=2
(gdb) continue
Continuing.

[... wait about seven seconds ...]

Program received signal SIGTRAP, Trace/breakpoint trap.
0x00002bbc in watchdog_fault_handler_c (frame=0x200003b8 <ucHeap+592>) at interrupt/example/watchdog-example/software_watchdog.c:81
81    HALT_IF_DEBUGGING();

(gdb) p/a *frame
$3 = {
  r0 = 0x0 <g_pfnVectors>,
  r1 = 0x200001bc <ucHeap+84>,
  r2 = 0x20000164 <s_registered_tasks>,
  r3 = 0x2 <g_pfnVectors+2>,
  r12 = 0x200003e0 <ucHeap+632>,
  lr = 0x10b <erase_external_flash+6>,
  return_address = 0x2b8 <spi_flash_erase_complete>,
  xpsr = 0x61000000
}
```

Great we see the `pc` & `lr` point exactly to the loop we were spinning on:

```c
void erase_external_flash(void) {
  // some logic to start a flash erase
  // poll for completion
  while (!spi_flash_erase_complete()) { };
}
```

#### Hang while waiting for a Mutex

Now let's try debugging the hang that resulted from a deadlock.

```
(gdb) mon reset
Resetting target
(gdb) break main
Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:162
162   prv_check_and_reset_reboot_reason();
(gdb) set g_watchdog_hang_config=3
(gdb) continue
Continuing.
[... wait about seven seconds ...]
Program received signal SIGTRAP, Trace/breakpoint trap.
0x00002bbc in watchdog_fault_handler_c (frame=0x20000b10 <ucHeap+2472>) at interrupt/example/watchdog-example/software_watchdog.c:81
81    HALT_IF_DEBUGGING();
(gdb) p/a *frame
$4 = {
  r0 = 0x0 <g_pfnVectors>,
  r1 = 0x0 <g_pfnVectors>,
  r2 = 0x0 <g_pfnVectors>,
  r3 = 0x0 <g_pfnVectors>,
  r12 = 0x0 <g_pfnVectors>,
  lr = 0x2741 <prvTaskExitError>,
  return_address = 0x39a <prvIdleTask+14>,
  xpsr = 0x61000000
}
```

This one is a bit more involved. The `$pc` and `$lr` are in the FreeRTOS Idle task. Recall the thread which is wedged is blocked so other code _is_ able to execute. We can compare `s_registered_tasks` & `s_fed_tasks` to find out what task id is stuck:

```
(gdb) p/x s_registered_tasks&~s_fed_tasks
$8 = 0x2
```

So it's task id 1 that is stuck. From our Task Id list we know this is the Pong task:

```c
typedef enum {
  kWatchdogExampleTaskId_Ping = 0,
  kWatchdogExampleTaskId_Pong,
  kWatchdogExampleTaskId_Watchdog,
} eWatchdogExampleTaskId;
```

If your debugger is FreeRTOS thread aware, you can switch to this thread to view the
backtrace. Alternatively you can use a tool like [Memfault](https://try.memfault.com/register)
(Disclosure: the author is founder & CTO at Memfault) to extract the data and run the analysis in the cloud. Let's try that out.

```
(gdb) memfault coredump -r 0x20000000 262144
One moment please, capturing memory...

[...]
Are you currently at the start of an exception handler [y/n]?n
[...]
Cortex-M4 detected
Collected MPU config
Capturing RAM @ 0x20000000 (1048576 bytes)...
Captured RAM @ 0x20000000 (1048576 bytes)
Symbols have already been uploaded, skipping!
Coredump uploaded successfully!
```

Then from the Memfault Issue Detail UI we can easily view the Pong task and see it's blocked waiting on a call to `xQueueSemaphoreTake`.



### Using GDB Python to prevent Software Watchdog Misfires

Unfortunately, unlike the watchdog timer, there does not appear to be a way to halt the clock driving the timer peripheral while a debugger is attached on the NRF52. This means that if we halt using a debugger for more than 7 seconds, we will hit the software watchdog ISR immediately upon resumption. Let's confirm that's the case:

```
(gdb) CTRL-C
[... wait 7 seconds ...]
(gdb) continue
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x00002bbc in watchdog_fault_handler_c (frame=0x20002a78) at interrupt/example/watchdog-example/software_watchdog.c:81
81    HALT_IF_DEBUGGING();
```

This is a situation where we can leverage GDB's Python API! (For a deeper dive into the GDB Python API check out [this post](https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api)).

Specifically, we can make use of the Events API[^9], to pause
the peripheral timer when the system halts and resume it when the system continues.

#### Example Code to Pause Software Watchdog While Debugging

```python
# gdb_resume_handlers.py
try:
    import gdb
except ImportError:
    raise Exception("This script can only be run within gdb!")

import struct


class Nrf52Timer0:
    TIMER0_TASKS_START_ADDR = 0x40008000
    TIMER0_TASKS_STOP_ADDR = 0x40008004

    @staticmethod
    def _trigger_task(addr):
        gdb.selected_inferior().write_memory(addr, struct.pack("<I", 1))

    @classmethod
    def start(cls):
        print("Resuming Software Watchdog")
        cls._trigger_task(cls.TIMER0_TASKS_START_ADDR)

    @classmethod
    def stop(cls):
        print("Pausing Software Watchdog")
        cls._trigger_task(cls.TIMER0_TASKS_STOP_ADDR)


def nrf52_debug_stop_handler(event):
    Nrf52Timer0.stop()


def nrf52_debug_start_handler(event):
    Nrf52Timer0.start()


gdb.events.stop.connect(nrf52_debug_stop_handler)
gdb.events.cont.connect(nrf52_debug_start_handler)
```

Now when we invoke GDB we can add the argument `--ex="source gdb_resume_handlers.py"` and the timer will be automatically paused by GDB for us while the debugger is halted.

```
$ arm-none-eabi-gdb-py --eval-command="target remote localhost:2331"  \
    --ex="mon reset" --ex="load" --ex="mon reset"                     \
    --ex="source gdb_resume_handlers.py" --se=build/nrf52.elf
Program received signal SIGTRAP, Trace/breakpoint trap.
main () at interrupt/example/watchdog-example/main.c:134
134   }
Pausing Software Watchdog
(gdb) c
Continuing.
Resuming Software Watchdog
```

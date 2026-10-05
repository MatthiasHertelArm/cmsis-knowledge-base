---
id: "intr-a-guide-to-watchdog-timers-for-emb-enabling-a-hardware-watchdog-in-a-system"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: Enabling a Hardware Watchdog in a System"
summary: "Now that we have a basic foundation of what a watchdog is and how it works, let's apply what we have learned, configure a watchdog, and use it to track down hangs in a real system."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#enabling-a-hardware-watchdog-in-a-system"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have a basic foundation of what a watchdog is and how it works, let's apply what we have learned, configure a watchdog, and use it to track down hangs in a real system.

We will walk through a provided example app running FreeRTOS which passes a message between two tasks. I've instrumented the code such that there are a variety of different ways the software can hang.

{:.no_toc}

### Example Project Setup

The example app can be downloaded from [Interrupt's Github page](https://github.com/memfault/interrupt/tree/master/example/watchdog-example)

```
$ git clone git@github.com:memfault/interrupt.git
$ cd interrupt/example/watchdog-example/
```

For testing the example code, we will be using:

- the GNU Arm Embedded Toolchain 9-2019-q4-update[^4] for our compiler
- the nRF52840-DK[^5] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^6] as our GDB Server.

### Examining the NRF52840 Hardware Watchdog Behavior

Let's take a look at the NRF52840 datasheet[^2] and see if we can answer [the questions from above](#watchdog-configuration-questions). The "6.36 WDT — Watchdog timer" section of the datasheet is a good place to start.

#### 1. Configuration Reset Behavior

From "6.36.3 Watchdog reset":

> The watchdog must be configured before it is started. After it is started, the watchdog’s configuration
> registers, which comprise registers CRV, RREN, and CONFIG, will be blocked for further configuration.
> The watchdog can be reset from several reset sources, see Reset behavior on page 70
> [...] 

The important takeaway here is that a normal reset ("Soft reset") does _not_ reset the watchdog
timer. This could cause issues, for example, if the main application enabled the watchdog but the
bootloader wasn't aware. If the bootloader performed a long running operation such as a firmware
update, the watchdog would still be running and might reset the system in the middle of the process!

> NOTE: In the case of the NRF52, the bootloader provided with the SDK does feed the watchdog if it was enabled by the main application.

#### 2. Behavior with a debugger

From "6.36.2 Temporarily pausing the watchdog" we have:

> By default, the watchdog will be active counting down the down-counter while the CPU is sleeping and
> when it is halted by the debugger. It is however possible to configure the watchdog to automatically pause
> while the CPU is sleeping as well as when it is halted by the debugger.

Great! So when a debugger is attached we can configure the peripheral to pause the counter. This will allow us to debug issues without worrying about a system reset as soon as we `continue`.

{: #wdt-debug-behavior}
Reading further into the datasheet, it actually looks like the documentation is **not** entirely correct. By _default_, the watchdog _is_ disabled for us when the debugger is halted (bit 3 defaults to 0) so we can just leverage the chip default configuration!



#### 3. Watchdog Expiration Behavior

From "6.36.3 Watchdog reset" we have:

> If the watchdog is configured to generate
> an interrupt on the TIMEOUT event, the watchdog reset will be postponed with two 32.768 kHz clock
> cycles after the TIMEOUT event has been generated. Once the TIMEOUT event has been generated, the
> impending watchdog reset will always be effectuated.

{: #nrf52-watchdog-interrupt}
So an interrupt can be enabled to fire upon a watchdog timeout. However, once the interrupt fires there will only be two 32kHz clock cycles before the system reboots anyway. The CPU core of the NRF52840 runs at 64 MHz so in practice this means we would only have about `(64MHz * 2) / 32768 = 3900 core clock cycles` to do any cleanup.

> NOTE: To avoid running the risk of a reset during cleanup we will avoid using this feature and explore alternatives later in the article.

#### 4. RESETREAS

Section "5.3.7.11 RESETREAS" of the data sheet contains a summary of the reset reasons.



The important things to note here are that reading bit 1 will tell us whether or not a watchdog reset took place and that we will have to write 1 to the bits we want to clear so they don't stick across reboots.

### Choosing a timeout value

Since the watchdog is really a last line of defense, I like to choose a timeout that is much larger
than the time it should take to handle a majority of the events being serviced by the RTOS task or
baremetal `while()` loop. A good rule of thumb is to use a timeout somewhere in the 5-30 second range. For the purposes of this demo, we will use a timeout of 10 seconds.

### Configuring the NRF52 Hardware Watchdog

Okay, now that we understand how the NRF52840 hardware watchdog peripheral works, let's enable it!

We know the NRF52840 watchdog is comprised of three configuration registers that can only be set _once_: `CRV`, `RREN`, and `CONFIG`.

From the discussion [above](#wdt-debug-behavior), we also know that the default `CONFIG` register
value matches what we want (pause the watchdog while the system is halted at a breakpoint).

{: #reload-request-registers}
The `RREN`register allows us to configure the number of "reload request registers" that can be used to
request that the watchdog counter gets reloaded. There are eight "reload request registers" and by
default only one is enabled. For the hardware watchdog to get its counter reset _all_ the enabled
"reload request registers" must be written to. One use case for enabling multiple reload request registers would be to
independently monitor different tasks or state machines in the system. For the purposes of this example, we'll use the
default configuration here with only the first "reload request register" enabled.

#### Code to Enable the NRF52840 Watchdog

So our configuration code reduces to:

```c
// hardware_watchdog.c
// ...
#define HARDWARE_WATCHDOG_TIMEOUT_SECS 10
// ...
void hardware_watchdog_enable(void) {
  if ((WDT->RUNSTATUS & 0x1) != 0) {
    // the watchdog is already running and cannot be configured
    return;
  }

  // "Counter reload value" - The number of 32.768kHz
  // clock cycles to elapse before a watchdog timeout
  WDT->CRV = 32768 * HARDWARE_WATCHDOG_TIMEOUT_SECS;

  // Enables the watchdog peripheral
  WDT->TASKS_START = 0x1;
}
```

#### Code to Feed the NRF52840 Watchdog

We'll also need a routine we can call to feed the watchdog. Recall we have enabled the first "reload request register" so we will have to write to that register to cause the watchdog count down to be restarted.

```c
// hardware_watchdog.c
void hardware_watchdog_feed(void) {
  // Per "6.36.4.10" if this value is written to a reload
  // register that is enabled, the watchdog counter will be reset
  //
  // NOTE: It's common to see "magic" numbers as reload values
  // in an effort to prevent a bad memory access from
  // inadvertently resetting the watchdog
  const uint32_t reload_magic_value = 0x6E524635;
  WDT->RR[0] = reload_magic_value;
}
```

### Checking the Hardware Reboot Reason

I've also instrumented the example app to check and reset the `RESETREAS`. If a watchdog took place, a breakpoint instruction will automatically be executed:

```c
// main.c
static void prv_check_and_reset_reboot_reason(void) {
  const uint32_t last_reboot_reason = *RESETREAS;
  // clear any enabled reset reasons
  *RESETREAS |= *RESETREAS;
  // Halt the system on boot-up if a
  // Watchdog Reset took place
  const uint32_t watchdog_reset_mask = 0x2;
  if ((last_reboot_reason & watchdog_reset_mask) == watchdog_reset_mask) {
    __asm("bkpt 10");
  }
}
```

### Sanity Checking the Configuration

The example app has a global variable defined in `main.c`, `g_watchdog_hang_config`, which we will be setting in gdb to control the type of hang which takes place. The startup code basically reduces to:

```c
//main.c
int main(void) {
  prv_check_and_reset_reboot_reason();

  hardware_watchdog_enable();
  //...
  // enter different hang based on g_watchdog_hang_config
```

By default, the code will just enter `while (1) {}` loop on boot-up. So if everything is configured correctly after we flash we should see the debugger halt inside `prv_check_and_reset_reboot_reason()` after 10 seconds. Let's try it out.

```
$ cd example/watchdog-example/
$ make
$ arm-none-eabi-gdb --eval-command="target remote localhost:2331"  --ex="mon reset" --ex="load" --ex="mon reset" --se=build/nrf52.elf
(gdb) continue
[ ... wait about 10 seconds ...]
Program received signal SIGTRAP, Trace/breakpoint trap.
prv_check_and_reset_reboot_reason () at interrupt/example/watchdog-example/main.c:157
157     __asm("bkpt 10");
(gdb)
```

Great, the watchdog works!

Now let's try a `while(1) {}` loop that repeatedly calls `hardware_watchdog_feed()`. If the feed routine we wrote above works, the program should run indefinitely.

```
(gdb) mon reset
(gdb) break main
(gdb) continue
Continuing.

Breakpoint 1, main () at interrupt/example/watchdog-example/main.c:162
162   prv_check_and_reset_reboot_reason();
(gdb) set g_watchdog_hang_config=1
(gdb) continue
[... should observe no reboot ...]
```

We can also halt and check the run status just to make sure the watchdog is running and the peripheral is configured as expected:

```
(gdb) p/x *WDT
$3 = {
  TASKS_START = 0x0,
  RSVD = {0x0 <repeats 63 times>},
  EVENTS_TIMEOUT = 0x0,
  RSVD1 = {0x0 <repeats 128 times>},
  INTENSET = 0x0,
  INTENCLR = 0x0,
  RSVD2 = {0x0 <repeats 61 times>},
  RUNSTATUS = 0x1,
  REQSTATUS = 0x1,
  RSVD3 = {0x0 <repeats 63 times>},
  CRV = 0x50000,
  RREN = 0x1,
  CONFIG = 0x1,
  RSVD4 = {0x0 <repeats 60 times>},
  RR = {0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0}
}
```

> NOTE: Since the counter is paused while the system is halted resuming will not trigger a reset either.

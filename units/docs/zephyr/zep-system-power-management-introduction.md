---
id: "zep-system-power-management-introduction"
type: "concept"
domain: "optimization"
title: "System Power Management: Introduction"
summary: "The kernel enters the idle state when it has nothing to schedule. Enabling CONFIG_PM allows the kernel to call upon the power management subsystem to put an idle system into one of the supported power states."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/system.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/system.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel enters the idle state when it has nothing to schedule.
Enabling `CONFIG_PM` allows the kernel to call upon the
power management subsystem to put an idle system into one of the supported power states.
The kernel requests an amount of time it would like to suspend, then the PM subsystem decides
the appropriate power state to transition to based on the configured power management policy.

It is the application's responsibility to set up a wake-up event.
A wake-up event will typically be an interrupt triggered by an SoC peripheral module.
Examples include a SysTick, RTC, counter, or GPIO.
Keep in mind that depending on the SoC and the power mode in question,
not all peripherals may be active, and therefore
some wake-up sources may not be usable in all power modes.

The following diagram describes system power management:

The idle thread locks interrupts before calling `pm_system_suspend`
and keeps ownership of the original architecture interrupt key. If the PM
subsystem enters a low-power state, PM resume bookkeeping runs with interrupts
still locked after any system-managed devices have been resumed, including
`pm_state_exit_post_ops`, PM exit notifications, and system clock
idle-exit accounting. After that bookkeeping is complete and
`pm_system_suspend` returns, the idle thread restores the original
interrupt key.

Architectures and SoCs that do not select `CONFIG_PM_STATE_SET_IRQ_UNLOCKED`
use the architecture hooks immediately around the low-power instruction so that
it can still observe a wake event without dispatching the wake-source ISR first.
In that mode, `pm_state_set` and
`pm_state_exit_post_ops` must be used for SoC-specific hardware work
only, not as final interrupt unmask points.

When this default contract is used, the interrupt ownership sequence is:

    power state, architecture PM state hooks allowing wake without ISR
    dispatch, PM resume bookkeeping, and idle unlocking interrupts.

sequenceDiagram
     participant Workers as Other threads
     participant Idle as idle()<br/>(idle thread context)
     participant PM as pm_system_suspend()
     participant SoC as pm_state_set()<br/>(SoC hook)
     participant HW as Hardware

     loop Idle cycle
         Note over Workers: Thread enters SLEEP/PENDING state<br/>e.g. k_sleep() / k_sem_take()
         alt Runnable thread(s) remaining
             Workers-->>Workers: Schedule another thread
         else No runnable thread remaining
             Workers-->>Idle: Switch to idle thread
         end
         Idle->>Idle: Lock interrupts
         Note left of Idle: Interrupts are locked<br/>during PM sequence
         Idle->>PM: Suspend idle CPU
         PM->>PM: Suspend devices<br/>(if applicable)
         PM->>PM: Set idle timeout
         PM->>PM: Notify PM state entry
         PM->>SoC: Enter power state
         SoC->>SoC: SoC-specific pre-entry operations
         SoC->>SoC: Run arch PM prepare hook
         SoC->>HW: Trigger low-power state entry
         HW-->>SoC: Wake-up event occurs
         SoC->>SoC: Run arch PM finish hook
         SoC->>SoC: SoC-specific post-wakeup operations
         SoC-->>PM: Power state exit complete
         PM->>PM: Resume devices<br/>(if applicable)
         PM->>PM: Run post ops, notify exit, clock idle exit
         PM-->>Idle: Resume complete
         Idle->>Idle: Unlock interrupts
         HW-->>Idle: Pending interrupts are handled
         Idle-->>Workers: Idle thread yields<br/>or is preempted
         Note over Workers: Non-idle thread starts executing
     end
SoC implementations that use this default contract must not unmask interrupts
from `pm_state_set` or `pm_state_exit_post_ops`. Legacy
implementations that still call `irq_unlock(0)`, `arch_irq_unlock(0)`,
`__enable_irq()`, or equivalent operations from those hooks must select
`CONFIG_PM_STATE_SET_IRQ_UNLOCKED` until they are migrated.


**Note:** The ordering guarantee above applies only to interrupts that ordering. See zlis.


### Power States


The power management subsystem defines a set of states described by the
power consumption and context retention associated with each of them.

The set of power states is defined by `pm_state`. In general, lower power states
(higher index in the enum) will offer greater power savings and have higher wake latencies.


### Power Management Policies


The power management subsystem supports the following power management policies:

* Residency based
* Application defined

The policy manager is the component of the power management subsystem responsible
for deciding which power state the system should transition to.
The policy manager can only choose between states that have been defined for the platform.
Other constraints placed upon the decision may include locks disallowing certain power states,
or various kinds of minimum and maximum latency values, depending on the policy.

More details on the states definition can be found in the
`zephyr,power-state` binding documentation.


#### Residency


Under the residency policy, the system will enter the power state which offers the highest
power savings, with the constraint that the sum of the minimum residency value (see
`zephyr,power-state`) and the latency to exit the mode must be
less than or equal to the system idle time duration scheduled by the kernel.

Thus the core logic can be summarized with the following expression:

```c

if (time_to_next_scheduled_event >= (state.min_residency_us + state.exit_latency)) {
   return state
}
```

#### Application


The application defines the power management policy by implementing the
`pm_policy_next_state` function. In this policy, the application is free
to decide which power state the system should transition to based on the
remaining time until the next scheduled timeout.

An example of an application that defines its own policy can be found in
`tests/subsys/pm/power_mgmt/`.


#### Custom ticks hook


In addition to the kernel tick expiration and the PM policy event list,
applications and SoC-specific code may need to derive the next wake-up time
from proprietary or hardware-specific data sources. Examples include hardware
registers, binary-only third-party modules, or complex/legacy data structures
that are not practical to model as standard PM policy events.

When `CONFIG_PM_CUSTOM_TICKS_HOOK` is enabled, the PM core calls the
optional function `pm_policy_next_custom_ticks()` during
`pm_system_suspend()`. The hook returns the ticks to the next custom
event, or `K_TICKS_FOREVER` if no custom event needs to be considered.

The PM core then selects the earliest expiration among:

* kernel tick expiration,
* PM policy event list ticks (from `pm_policy_next_event_ticks()`),
* the custom ticks value (from `pm_policy_next_custom_ticks()`).

This mechanism allows boards and applications to integrate additional timing
sources into the system power management decisions without modifying the PM
event list infrastructure.


#### Policy and Power States


The power management subsystem allows different Zephyr components and
applications to configure the policy manager to block the system from transitioning
into certain power states. This can be used by devices when executing tasks in
background to prevent the system from going to a specific state where it would
lose context. See `pm_policy_state_lock_get`.


### Examples


Some helpful examples showing different power management features:

* `samples/boards/st/power_mgmt/blinky/`
* `samples/boards/espressif/deep_sleep/`
* `samples/subsys/pm/device_pm/`
* `tests/subsys/pm/power_mgmt/`
* `tests/subsys/pm/power_mgmt_soc/`
* `tests/subsys/pm/power_states_api/`

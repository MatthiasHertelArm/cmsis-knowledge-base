---
id: "tfm-tf-m-power-management-service-desi-service-description"
type: "concept"
domain: "security"
title: "TF-M Power Management Service design (RFC): Service description"
summary: "The service provides a generic implementation for some of the CPU power and operating modes as described by the Cortex-M55 TRM [1], Power mgmt section (the same applies to Cortex-M85)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_power_mgmt.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_power_mgmt.html#service-description"
license: "BSD-3-Clause"
mode: "V"
---

The service provides a generic implementation for some of the CPU power and
operating modes as described by the Cortex-M55 TRM [1]_, Power mgmt section
(the same applies to Cortex-M85).

Note that each individual platform has the flexibility to implement power states
and domains arbitrarily so the generic implementation, albeit functional, may
need to be extended by custom platform code. This can be done via the provided
callback hooks.

The service is implemented as stateless and allows mm-iovec mapping.
Note that for cpu power states the call is blocking as it affects its own
processing, while for custom states, that depends on the hooks' implementation.



### Power states groups


There are two classes of power states exposed by the service:
  - PWR_STATE_<OFF, SLEEP, DEEPSLEEP, SUSPEND, HIBERNATE>
  - PWR_STATE_CUSTOM_<any>

+---------------------+--------------------------------------------------------+
| Power state group   |                                                        |
| TFM_POWER_MGMT_PWR\_| CPU power state applied                                |
+=====================+========================================================+
| STATE_OFF           | OFF                                                    |
+---------------------+--------------------------------------------------------+
| STATE_SLEEP         | ON (unchanged)                                         |
+---------------------+--------------------------------------------------------+
| STATE_DEEPSLEEP     | ON (unchanged)                                         |
+---------------------+--------------------------------------------------------+
| STATE_SUSPEND       | MEM_RET (Cache)                                        |
+---------------------+--------------------------------------------------------+
| STATE_HIBERNATE     | OFF                                                    |
+---------------------+--------------------------------------------------------+
| STATE_CUSTOM        | CPU power state is unchanged                           |
|                     | This groups is to support custom states i.e. to control|
|                     | power or clocks of peripherals or similar              |
+---------------------+--------------------------------------------------------+



### CPU STATES


For general cpu power state transitions, the flow is usually as below. The
platform code can be plumbed in to support extra features before and after the
state transition.
This is because the cpu power state transitions are forced through the WFI/WFE
instructions.

Simple flow::
```
┌────────┐      ┌───────────┐      ┌──────────┐      ┌──────────┐
│ caller │ ---> │ pwr-mgmt  │ ---> │ pwr-mgmt │ ---> │ platform │
│        │ <--- │ interface │ <--- │ service  │ <--- │ code     │
└────────┘      └───────────┘      └──────────┘      └──────────┘
                                        ^
                                        |
                                        v
                                    ┌────────┐
                                    │ POWER  │
                                    │ STATE  |
                                    | CHANGE │
                                    └────────┘
```
+---------------------+--------------------------------------------------------+
| TFM_POWER_MGMT_PWR\_| Description                                            |
| Power state         |                                                        |
+=====================+========================================================+
| STATE_SLEEP         | Simply performs WFx                                    |
| (shallowest)        | For shallow modes with callbacks                       |
+---------------------+--------------------------------------------------------+
| STATE_DEEPSLEEP     | Performs WFx with SCR.SLEEPDEEP set                    |
|                     | For shallow modes with callbacks & platform-hw         |
|                     | additional intervention                                |
+---------------------+--------------------------------------------------------+
| STATE_SUSPEND       | Performs CPU power-off with memory retention           |
|                     | The service save and restore the context of the CPU.   |
|                     |                                                        |
|                     | This state is described as MEM_RET in the Cortex-M TRM |
|                     | Requires a platform-capable PDRAMS power domain        |
+---------------------+--------------------------------------------------------+
| STATE_HIBERNATE     | Turns OFF the cpu domains. Callbacks are expected to   |
| (deepest)           | enable and re-route the WIC to allow power-up          |
|                     |                                                        |
|                     | Does not return, the CPU starts from reset.            |
+---------------------+--------------------------------------------------------+

Each power state transition can be selected with the choice of either wait for
interrupt or wait for event, via a call parameter.

+----------------------+-------------------------------------------------------+
| TFM_POWER_MGMT_WAIT\_| Description                                           |
|                      |                                                       |
+======================+=======================================================+
| FOR_EVENT            | Performs WFE, then wait for:                          |
|                      | interrupts transitioning from the inactive to the     |
|                      | pending state that target that security state are     |
|                      | wakeup events                                         |
|                      | SEV instruction by any other PE in the same           |
|                      | multiprocessor system                                 |
|                      | Any exception at a priority that would preempt the    |
|                      | current execution priority                            |
|                      | A debug event, any IMP_DEF event, a Warm reset        |
+----------------------+-------------------------------------------------------+
| FOR_INTERRUPT        | Performs WFI, then wait for:                          |
|                      | Any asynchronous exception at a priority that would   |
|                      | preempt any currently active exceptions (see PRIMASK) |
|                      | A debug event, any IMP_DEF event, a Warm reset        |
+----------------------+-------------------------------------------------------+
| FOR_NONE             | Performs neither. Only valid for custom states        |
+----------------------+-------------------------------------------------------+



### NON-CPU STATES


These states do not involve any changes in the CPU, they are intended to be
exclusively callback-controlled.

Examples: Crypto HW engine, LCD display, etc.

For non-cpu power state transitions, the platform code will ultimately drive the
power state change, for example via setting registers, PPUs or scaling voltage.

The service will not alter the CPU power states::
```
┌────────┐      ┌───────────┐      ┌──────────┐      ┌──────────┐      ┌────────┐
│ caller │ ---> │ pwr-mgmt  │ ---> │ pwr-mgmt │ ---> │ platform │ <--> │ POWER  │
│        │ <--- │ interface │ <--- │ service  │ <--- │ code     │      │ STATE  |
└────────┘      └───────────┘      └──────────┘      └──────────┘      | CHANGE │
                                                                       └────────┘
```

### CALLBACKS


For each power state transitions, platform code can be hooked in via the callbacks,
in both pre and post state transitions.

Platform code can provide a table of calbacks on a per-state basis.

Callbacks are *optional*.

Callbacks define a policy that applies to each: graceful or forceful.
When the callback is performed but does not complete successfully, the service
needs to know if abort the entire sequence or carry on.
If the policy is `POLICY_GRACEFUL`, then the sequence carries on.
If the policy is `POLICY_FORCEFUL``, then the sequence is interrupted and the
power transition does not take place.

This policy is configurable for each callback.

The order of callback is important.

To keep the implementation simple the integrators should ensure that the table
of callbacks is set up correctly and ordered.
The expectation from the service is that the order by which the callbacks are
presented matters.
Assume that for a state change operation A needs to take place before
operation B. When the state change is to be reversed, operation B must take
place before operation A.

Simply::
```
custom_power_state_request
    -> ops_A -> ops_B
     -> state_change -> event
         -> ops_B -> ops_A -> call_complete
```
To achieve the above there is no explicit configuration for the different ops
but rather the order of callbacks inside the table determines it.
Alternatively, the order can be achieved within the same callback(s).

See examples below.

---
id: "tfm-scheduling-for-a-hybrid-platform-s-integration-examples"
type: "concept"
domain: "security"
title: "Scheduling for a Hybrid Platform Solution: Integration examples"
summary: "In the platform configuration settings file config_tfm_target.h choose"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/hybrid_platform_solution.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/hybrid_platform_solution.html#integration-examples"
license: "BSD-3-Clause"
mode: "V"
---

### Hybrid Platform with SPE scheduling


In the platform configuration settings file  `config_tfm_target.h` choose

```c

#define CONFIG_TFM_HYBRID_PLAT_SCHED_TYPE   TFM_HYBRID_PLAT_SCHED_SPE
```

### Hybrid Platform with NSPE scheduling


If your platform implements a custom set of RPC operations, then add the
`process_new_msg` handler:

```c

static int32_t platform_process_new_msg(uint32_t *nr_msg)
{
    /* some optional platform tasks */

    /*
     * Note that it's the platform's choice on whether or not to return the
     * number of mailbox messages processed.
     */
    return platform_handle_req();
}

static struct tfm_rpc_ops_t rpc_ops = {
    .handle_req = platform_handle_req,
    .reply = platform_mailbox_reply,
    .handle_req_irq_src = platform_handle_req_irq_src,
    .process_new_msg = platform_process_new_msg,
};
```
The platform interrupt handler is already expected to call
`spm_handle_interrupt()`, so to correctly handle the set/clear of IRQs, the
platform shall also call `tfm_multi_core_set_mbox_irq()` right after it as
shown below.

```c

void mailbox_IRQHandler(void)
{
    /* some optional platform tasks */

    spm_handle_interrupt(p_pt, p_ildi);

#if (CONFIG_TFM_HYBRID_PLAT_SCHED_TYPE == TFM_HYBRID_PLAT_SCHED_NSPE)
    tfm_multi_core_set_mbox_irq(p_ildi);
#endif
}
```
The counterpart `tfm_multi_core_clear_mbox_irq()` is called instead by the
mailbox partition.

In the platform configuration settings file  `config_tfm_target.h` choose

```c

#define CONFIG_TFM_HYBRID_PLAT_SCHED_TYPE   TFM_HYBRID_PLAT_SCHED_NSPE
```
Then, in the `local client` NSPE, where the scheduling decisions are made,
simply call the auxiliary mailbox service to process any pending mailbox
messages:

```c

psa_status_t status;
uint32_t num_msg;

psa_outvec out_vec[] = {
    {
        .base = &num_msg,
        .len = sizeof(num_msg),
    },
};

status = psa_call(
    NS_AGENT_MBOX_PROCESS_NEW_MSG_HANDLE,
    PSA_IPC_CALL,
    NULL, 0,
    out_vec, IOVEC_LEN(out_vec));
if (status < 0) {
  /* process the error */
} else {
  /* num_msg contains the number of mailbox slots/messages processed */
}
```

### Hybrid Platform with BALANCED scheduling


All the above for `TFM_HYBRID_PLAT_SCHED_NSPE` plus the following changes,
where required, for the mailbox manifest.

```c

"services": [
  {
    "<attribute>" : "<value>"
    ...
  },
],
"irqs": [
  {
    "<attribute>" : "<value>"
    ...
    "mbox_flags": MBOX_IRQ_FLAGS_<DEFAULT|DEFER>_SCHEDULE,
  },
  ...
],
```
Currently, the mailbox flags `mbox_flags` supported are:

- MBOX_IRQ_FLAGS_DEFAULT_SCHEDULE: the requests via mailbox transport are managed
  accordingly to the default hybrid platform scheduling options (this is always
  the default option)

- MBOX_IRQ_FLAGS_DEFER_SCHEDULE: the requests via mailbox transport are deferred
  until the local NSPE calls the mailbox partition auxiliary service
  `NS_AGENT_MBOX_PROCESS_NEW_MSG`

The `mbox_flags` is optional, it can be omitted when this feature is not
required.

In the platform configuration settings file  `config_tfm_target.h` choose

```c

#define CONFIG_TFM_HYBRID_PLAT_SCHED_TYPE   TFM_HYBRID_PLAT_SCHED_BALANCED
```

### Hybrid Platform and common binary image


For homogeneous hybrid platform topology, the same binary image is likely to be
deployed across cores. In that case, both mailbox and TrustZone agents will be
in use. Therefore, the API for PSA calls would be, from each client's
perspective, virtually the same.
In that event, the APIs provided by both agents need to be available
simultaneously, and thus, a component that coordinates the redirection is
required.

To achieve this, a `TFM_HYBRID_PLATFORM_API_BROKER` is supplied. This
component simply redirects the standard PSA calls from the client to the correct
interface.
The redirection choice is made at initialization time, where the local or remote
NSPE sets the respective interface API.

For such hybrid platforms, the common build flags configuration would be
as follows:


+---------------------------------------+---------------------+
| Config Option                         | Set to              |
+=======================================+=====================+
| CONFIG_TFM_USE_TRUSTZONE              | ON                  |
+---------------------------------------+---------------------+
| TFM_HYBRID_PLATFORM_API_BROKER        | ON                  |
+---------------------------------------+---------------------+
| TFM_MULTI_CORE_TOPOLOGY               | ON                  |
+---------------------------------------+---------------------+
| TFM_MULTI_CORE_NS_OS                  | user's requirements |
+---------------------------------------+---------------------+
| TFM_MULTI_CORE_NS_OS_MAILBOX_THREAD   | user's requirements |
+---------------------------------------+---------------------+
| TFM_MULTI_CORE_TEST                   | user's requirements |
+---------------------------------------+---------------------+


The NSPE is expected to have a mechanism to detect its execution target, that is
being remote or local. This is *IMPLEMENTATION DEFINED*.

This mechanism should drive the main application to initialize the appropriate
interface, where the API broker is configured for the correct execution
environment.

See an example below.


```c

#define EXEC_TARGET_LOCAL  true
#define EXEC_TARGET_REMOTE false
bool plat_is_this_client_local(void)
{
    /*
     * An implementation-defined mechanism to detect the execution target.
     * For example, a RO memory location could hold such information.
     */

    return <EXEC_TARGET_LOCAL | EXEC_TARGET_REMOTE>;
}
```
Then, the main implementation simply calls the mechanism logic function and
calls either the interface for TrustZone or Mailbox.
Subsequently, the interface sets the execution environment within the API
broker.

```c

/*
 * The corresponding init function sets the execution environment via the API
 * broker.
 */
if (plat_is_this_client_remote()) {
    tfm_ns_multi_core_boot();
} else {
    tfm_ns_interface_init();
}
```

### Hybrid Platform and NSPE reentrancy


With scheduling set to `TFM_HYBRID_PLAT_SCHED_SPE`, the non-secure state can
be interrupted, allowing execution to switch to the secure side until it
completes.
In systems where NSPE has no knowledge on when - or even if - there is a secure
service in action, a non-secure application can interrupt and take over
execution.
This is the case, for example, when a standard RTOS runs its scheduler (by
pre-empting the secure side) and later a new task runs.
That task can attempt to request services from the secure state, which could
lead to an intentional system panic.
To safely deal with such scenario, NSPE has a way to detect if reentrancy is
allowed. To do so, enable `TFM_TZ_REENTRANCY_CHECK` in the build and
include a validation check at run-time.
The following diagram illustrates an example for a NSPE with an RTOS and a
possible scenario of a secure service pre-empted by a new task.



**Note:** The sequence diagram above demonstrates the denial of re-entry until the secure service completes; non-secure applications must check tfm_ns_check_safe_entry() and yield otherwise.

For the task in the non-secure side that makes a request to a secure service
(attempting to reenter), below is a possible use case of the reentrancy check:


```c

psa_status_t ns_status = PSA_ERROR_CONNECTION_REFUSED;
enum tfm_reenter_check_err_t reenter_status;
os_status_t os_status;

reenter_status = tfm_ns_check_safe_entry();
if (reenter_status == TFM_REENTRANCY_CHECK_SUCCESS) {
    ns_status = psa_call(
        SERVICE_HANDLE,
        SERVICE_ID,
        in_vec, IOVEC_LEN(in_vec),
        out_vec, IOVEC_LEN(in_vec));
    if (ns_status != PSA_SUCCESS) {
        /* handle error */
    }

    /*
     * Release re-entry guard.
     * Must be called on the same call path after a successful secure entry.
     */
    tfm_ns_check_exit();
} else {
    os_status = osThreadYield(); /* also possible osDelay(delayTime); */
    if (os_status != osOK) {
        /* handle error */
    }
}
```
The RTOS yielding mechanism directly influences task scheduling and the
continuation of preempted secure services.
There may be better functions than the one shown above that allow to achieve the
sought scheduling sequence.



### Limitations


Currently Hybrid Platform is supported only for the IPC model.
Testing is limited.


--------------

*SPDX-License-Identifier: BSD-3-Clause*

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*

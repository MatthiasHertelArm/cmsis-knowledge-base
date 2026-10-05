---
id: "tfm-secure-partition-manager-serving"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Runtime management / Serving"
summary: "Two execution categories work under this state:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#serving"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Runtime management_

Two execution categories work under this state:

- Partition initialization routine execution.
- Secure service access.

This state indicates the serving is ongoing. It is mainly the service routine
execution, plus a few SPM executions when SPM API gets called.


**Important:** The service access process introduced in this chapter (Such as Secure service access) is abstracted from the FF-M specification. Reference the FF-M specification for the details of each step.


#### Partition initialization routine execution

The partition initialization routines get called. One partition may access its
depending services during initializing, then this procedure is a
Secure service access.

The initialization routine gets called initially by
`Partition initialization client`, also can be called by Client API before
service access, if the target partition is not initialized but a service
access request is raised by one client.


#### Secure service access

The process of service access:

#. A `client` calls an FF-M Client API.
#. `SPM` validates inputs and looks up for the targeted service.
#. `SPM` constructs the request to be delivered under a proper runtime
   mechanism.
#. The target service gets executed. It can perform internal executions or
   access depending services to prepare the response. It also can wait for
   specific signals.
#. The target service calls FF-M Secure Partition API to request a reply to
   the client.
#. SPM delivers the response to the client, and the API called by the client
   returns.

The mechanism of how SPM interact with the target partition depends on the
partition runtime model.

- Access to a service in an SFN partition is a function call, which does not
  switch the current process indicator.
- Access to a service in an IPC partition leads to scheduling, which switches
  the current process indicator.
- When the execution roams between components because of a function call or
  scheduling, the isolation boundaries NEED to be switched if there are
  boundaries between components.

No matter what kind of partition a client is trying to access, the SPM API is
called firstly as it is the interface for service access. There are two ABI
types when calling SPM API: Cross-boundary or No-cross-boundary.


#### Calling SPM API

SPM is placed in the PRoT domain. It MAY have isolation boundaries under
particular isolation levels. For example:

- There are boundaries between ARoT components and SPM under isolation level 2
  and 3.

The API SPM provided needs to support the function call (no boundary
switching) and cross-boundary call. A direct call reaches the API entrance
directly, while a cross-boundary call needs a mechanism (Supervisor call e.g.)
to cross the boundary first before reaching the API entrance.


#### SPM internal execution flow

SPM internal execution flow as shown in diagram:

The process:

- PSA API gets called by one of the ABI mentioned in the last chapter as
  `ABI 1` in the diagram.
- The unified API Handler calls FF-M and backend subroutines in sequence.
- The `FF-M` subroutine performs `FF-M` defined operations.
- The backend operations perform target partition runtime model decided
  operations. For example, enqueue message into the target partition under
  the IPC runtime model, or prepare to call context with the message as the
  parameters under the SFN runtime model.
- API Handler triggers different ABI based on the result of the backends.

The API handler:

- Can process the `PROGRAMMER_ERROR` in a unified place.
- Can see the prepared caller and callee context, with exited SPM context. It
  is an ideal place for subsequent operations such as context switching.

An example code:

```c

void abi(void *p)
{
    status = spm_api(p);
    /*
     * Now both the caller and callee contexts are
     * managed by spm_api.
     */
    if (status == ACTION1) {
        /*
         * Check if extra operations are required
         * instead of a direct return.
         */
        exit_action1();
    }
}
```
The explanation about `Scheduler Lock`:

Some FF-M API runs as a generic thread to prevent long time exclusive
execution. When a preemption happens, a new partition thread can call SPM API
again, makes SPM API nested. It needs extra memory in SPM to be allocated to
store the preempted context. Lock the scheduler while SPM API is executing can
ensure SPM API complete execution after preemption is handled. There can be
multiple ways to lock the scheduler:

- Set a scheduler lock.
- Set SPM API thread priority as the highest.


#### Backend service messaging

A message to service is created after the target service is found and the
target partition runtime model is known. The preparation before ABI triggers
the final accessing:

- The message is pushed into partition memory under a specific ABI mechanism
  if the target partition model is `SFN` and there are boundaries between SPM
  and the target partition. After this, requests a specific call type to the
  SPM ABI module.
- The target service routine is called with the message parameter if
  there are no boundaries between SPM and the target partition and the
  partition runtime is `SFN`.
- The message is queued into the partition message list if the target
  partition runtime model is `IPC`.
- IPC partition replies to the client by `psa_reply`, which is another SPM API
  call procedure.
- SFN partition return triggers an implied `psa_reply`, which is also another
  SPM API call procedure.


**Note:** The backends also handle the isolation boundary switching.


#### Sessions and contexts

FF-M API allows multiple sessions for a service if the service is classic
connection-based. The service can maintain multiple local session data and use
`rhandle` in the message body to identify which client this session is bound
with.

But this does not mean when an ongoing service accessing is preempted,
another service access request can get a chance for new access. This is
because of the limited context storage - supporting multiple contexts in a
common service costs much memory, and runtime operations (allocation and
re-location). Limited the context content in the stack only can mitigate the
effort, but this requirement requires too much for the service development.

The implementation-decisions are:

- IPC partitions handles messages one by one, the client gets blocked before
  the service replying to the client.
- The client is blocked when accessing services are handling a service
  request in an SFN partition.


#### ABI type summary

The interface type is decided by the runtime model of the target component.
Hence PSA API has two types of ABI: `Cross-boundary ABI` and
`Function call ABI`. After SPM operations, one more component runtime type
shows up: The IPC partition, hence `schedule` is the mechanism when accessing
services inside an IPC partition.


**Note:** The API that does not switch context returns directly, which is not covered in the above diagram.

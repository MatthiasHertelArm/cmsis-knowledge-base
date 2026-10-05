---
id: "tfm-secure-partition-manager-practical-implementation-items"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Practical implementation items"
summary: "This chapter describes the practical implementation contents."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#practical-implementation-items"
license: "BSD-3-Clause"
mode: "V"
---

This chapter describes the practical implementation contents.


**Important:** Arm M-profile architecture is the default hardware architecture when describing architecture-specific items.

The general M-profile programming is not involved in this document. The
following chapters introduce the mandatory settings for security
requirements.


### Architecture security settings

When an `Armv8m Security Extension` (Aka `Trustzone-M`) is available in the
system, these settings are required to be set:

- The MSPLIM needs to be set correctly to prevent stack overflow.
- The exception handler priority needs to be decided.
- Boost the secure handler mode priority to prevent NSPE from preempting SPE
  handler mode execution(`AIRCR.PRIS`).
- Disable NSPE hardware faults when a secure fault is happening. Trap in the
  secure fault with the highest priority can be a valid option.
- Push seals on the stack top when a stack is allocated (`TFMV-1`). Also
  check Stack seal chapter for details.

Besides `Armv8m Security Extension`, these settings need to care when
`Floatpoint Extension` is enabled for partition usage:

- `FPCCR.TS`, `FPCCR.CLRONRET` and `FPCCR.CLRONRETS` need to be set when
  booting.
- `CPACR.CP10` and `CPACR.CP11` need to be set when booting.


**Important:** Floatpoint usage is prohibited in SPM and background execution.


#### Stack seal

When Trustzone-M is applied, the architecture specification recommends sealing
the secure stack by:

- Push two `SEAL` values (`0xFEF5EDA5`) at the stack bottom, when a stack is
  allocated.
- Push two `SEAL` values on the stack pointer which is going to be switched
  out.

Check architecture specification and vulnerability `TFMV-1` for details.


#### Trustzone-M reentrant

The Trustzone-M has characteristics that:

- SPE keeps the last assigned stack pointer value when execution leaves SPE.
- SPE execution can be preempted by NSPE which causes an execution left.

It is possible that NSPE preemption caused a second thread calls into SPE and
re-uses the secure stack contains the first thread's context, which obviously
causes information leakage and runtime state inconsistent.

Armv8.1-M provides the hardware setting `CCR_S.TRD` to prevent the reentrant.
On an Armv8.0-M architecture, extra software logic needs to be added at the
veneer entry:

- Check if the local stack points to a `SEAL` when veneer code get executed.

```c

/* This is a theoretical code that is not in a real project. */
veneer() {
    content = get_sp_value();
    if (context != SEAL) /* Error if reentrant detected */
        error();
}
```

### SPM Runtime ABI

This chapter describes the runtime implementation of SPM.


#### Scheduling

The scheduling logic is put inside the PendSV mode. PendSV mode's priority
is set as one level higher than the default thread mode priority. If
`Trustzone-M` is present, the priority is set as the lowest just above NS
exception priority to prevent a preemption in secure exceptions.

PendSV is an ideal place for scheduling logic, because:

- An interrupt triggered scheduling during PendSV execution lead to another
  PendSV execution before exception return to the thread mode, which can find
  the latest run-able thread.


#### Function call ABI

In the diagram fig-abi_scheduler, the ABI can have two basic
types: cross-boundary and direct call (No-cross-boundary).

When applying `SVCall` (`SVC`) as the cross-boundary mechanism, the
implementation can be straight like:

- The SVC handler calls SPM internal routines, and eventually back to the
  handler before an exit.

Under the IPC model implementation, to reuse `ABI 2` in `No-cross-boundary`,
a software ABI needs to be provided.

While under the SFN model plus isolation level 1, both `ABI 1` and `ABI 2` can
be a direct function call.


### NS Agent

The `NS Agent` (`NSA`) forwards NSPE service access request to SPM. It is a
special `partition` that:

- It does not provide FF-M aligned secure services.
- It runs with the second-lowest priority under `IPC model implementation`
  (The IDLE thread has the lowest priority).
- It has isolation boundaries and an individual stack.
- It requires specific services and mechanisms compared to common partitions.

There are two known types for NS Agent:

- Trustzone-M based.
- Remote Procedure Call (RPC) based.

This process is put inside the ARoT domain, to prevent assign unnecessary
PRoT permissions to the NSPE request parsing logic.


#### Trustzone-M specific

The functionalities of a Trustzone-M specific NSA is:

- Launch NSPE when booting.
- Wait in the veneer code, and get executed when NSPE accesses services.

As there may be multiple NSPE threads calling into SPE, and SPM wants to
identify them, special mechanisms can be proposed to provide the identification.
Check specific NS ID client ID or context related documents for details.


#### RPC specific

Compared to Trustzone-M NSA, RPC NSA looks closer to a generic partition:

- It has a message loop, keep waiting for RPC events.
- It converts received RPC events into FF-M API call to target services.

And compared to generic partitions, the differences are:

- It parses RPC messages to know which NSPE thread is accessing services.
  Hence it needs special interfaces to help SPM to identify the NSPE clients.
- It needs to check NSPE client memory and map to local before calling SPM API.
- It cannot be blocked during API calls, which affects handling the RPC
  requests.


### Partition

A partition is a set of services in the same scope. Services are generally
implemented as functions, and the partition exposes the services in different
ways based on the partition model: `IPC` or `SFN`.

A partition build generates these outputs:

- A partition load information, used by SPM.
- A partition program containing service interface and logic, typically a
  library.
- An optional service API set for easier client usage, by encapsulating
  the low-level `FF-M` Client API. These API needs to be integrated
  into client space.


#### Partition loading

SPM needs to set up runtime objects to manage partitions by parsing the load
information of partitions. In general, the partition load information is
stored in a const memory area can be random read directly, hence SPM can direct
link runtime objects to the load information without a copy operation. This
is called a `Static Load` mechanism.

Each partition has different numbers of dependencies and services, this makes
the load information size of each partition different, it would be hard to put
such variable size elements in an array. The solution here is putting these
elements in a dedicated section, for SPM enumerating while loading.
Each partition can define variable size load information type based on the
common load info type.

The common load information:

```c

struct partition_load_info_t {
    uint32_t        psa_ff_ver;     /* Encode the version with magic    */
    int32_t         pid;            /* Partition ID                     */
    uint32_t        flags;          /* ARoT/PRoT, SFN/IPC, priority     */
    uintptr_t       entry;          /* Entry point                      */
    size_t          stack_size;     /* Stack size                       */
    size_t          heap_size;      /* Heap size                        */
    uint32_t        ndeps;          /* Dependency number                */
    uint32_t        nservices;      /* Service number                   */
    uint32_t        nassets;        /* Asset numbers                    */
    uint32_t        nirqs;          /* Number of IRQ owned by Partition */
    int32_t         client_id_base; /* The min translated client ID     */
    int32_t         client_id_limit;/* The max translated client ID     */
    uint16_t        load_order;     /* loading order of this partition  */
};

And the example for a specific partition load info:
struct partition_example_load_info_t {
    struct partition_load_info_t ldi;      /* Common info info          */
    uint32_t                     deps[10]; /* Dependencies              */
    /*                    ... other infos ...                           */
};
```

#### Peripheral binding

A partition can declare multiple peripherals (Interrupts are part of
peripherals). The peripherals binding process:

- The tooling references symbols in a fixed pattern in the partition load
  information.
- The HAL implementation needs to provide the symbols being referenced.
- SPM calls HAL API to bind the partition info with devices when the partition
  gets loaded.
- The platform HAL acknowledges the binding if validation pass on SPM given
  load information.

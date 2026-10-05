---
id: "tfm-secure-partition-manager-initializing"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Runtime management / Initializing"
summary: "The goal of TF-M initializing is to perform necessary initialization and move to the Serving state. This state starts with platform-specific power on sequence, then SPM takes over the execution to perform these operations:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#initializing"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Runtime management_

The goal of TF-M initializing is to perform necessary initialization and
move to the Serving state. This state starts with platform-specific power
on sequence, then `SPM` takes over the execution to perform these operations:

#. A preparation initialization process before SPM runtime initialization.
#. SPM runtime initialization.
#. A post initialization happens after the SPM runtime initialization and
   before the first partition gets launched.


**Note:** These procedures and their sub-routines are recommended to be applied with execution measurement mechanism to mitigate the `Hardware Fault Injection` attack.


#### Preparation initialization

The purpose of this preparation initialization is to provide a chance for
performing those security required but generic platform power-on skipped
operations, such as:

- Restrict `SPM` execution, for example, set up memory overflow settings for
  SPM runtime memory, or set code out of SPM as un-executable, even though
  SPM is a privileged component in general.


**Note:** The `logging`-related peripheral can be set up **AT THIS STEP**, if logging is enabled and it needs peripheral support. There is no standalone initializing HAL API proposed for logging, so here is an ideal place for initializing them.

This procedure is abstracted into one `HAL`, and a few example procedures
are implemented as its sub-routines for reference:

- Architecture extensions initialization, Check chapter
  Architecture security settings for detailed information.
- Isolation and lifecycle initialization.

The load isolation boundaries need to be set up here, such as SPE/NSPE
boundary, and ARoT/PRoT boundary if isolation level 2 is applied.

The lifecycle is initiated by a secure bootloader usually. And in this stage
of SPM initializing, SPM double-checks the lifecycle set up status (following
a specific lifecycle management guidelines). Note that the hardware debugger
settings can be part of lifecycle settings.


**Important:** Double-check debugger settings when performing a product release.


#### SPM runtime initialization

This procedure initializes necessary runtime operations such as memory
allocator, loading partitions and partition-specific initialization
(binding partitions with platform resources).

The general processes:

#. Initialize runtime functionalities, such as memory allocator.
#. Load partitions by repeating below steps:

    * Find a partition load information.
    * Allocate runtime objects for this partition.
    * Link the runtime objects with load information.
    * Init partition contexts (Thread and call context).
    * Init partition isolation boundaries (MMIO e.g.).
    * Init partition interrupts.

After no more partitions need to be loaded, the SPM runtime is set up but
partitions' initialization routines have not run yet - the partition runtime
context is initialized for the routine call.

The partition initialization routine is a special service that serves SPM
only, because:

- SPM needs to call the initialization routine, just like it calls into
  the service routine.
- The partition initialization routine can access its depending services.
  Putting initialization routine in the same runtime environment as common
  service routines can avoid special operations.

Hence a `Partition initialization client` needs to be created to initialize
the SFN partitions, because:

- `SPM runtime initialization` happen inside a special runtime environment
  compare to the partition runtime execution, then an environment switching
  is needed.
- IPC partitions are initialized by the scheduler and dependencies are
  handled by signals and messages asynchronously, hence IPC partitions can
  process the dependencies by their own.

The `Partition initialization client` is created differently based on the
implementation runtime model:

- A SFN client is created under the SFN model implementation.
- A IPC client is created under the IPC model implementation. This client
  thread has the highest priority.

As the other partitions, the client is created with context standby, and it
is executed after the Post initialization stage.


#### Post initialization

Platform code can change specific partition settings in this procedure before
partitions start. A few SPM API is callable at this stage, such as set a
signal into a specific partition, or customized peripheral settings.

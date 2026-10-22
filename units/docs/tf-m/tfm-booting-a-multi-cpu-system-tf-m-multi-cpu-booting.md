---
id: "tfm-booting-a-multi-cpu-system-tf-m-multi-cpu-booting"
type: "concept"
domain: "security"
title: "Booting a Multi CPU System: TF-M Multi CPU Booting"
summary: "In an effort to make the problem manageable, as well as to provide a system with good performance, that is flexible enough to work for a variety of multi cpu systems, the following design decisions have been made:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/booting_a_multi_cpu_system.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/booting_a_multi_cpu_system.html#tf-m-multi-cpu-booting"
license: "BSD-3-Clause"
mode: "V"
---

In an effort to make the problem manageable, as well as to provide a system
with good performance, that is flexible enough to work for a variety of multi
cpu systems, the following design decisions have been made:

- TF-M will (for now) only support systems where the secure core has full
  access to the Flash that the non-secure core will boot from

    - This keeps the boot flow as close as possible to the single core design,
      with the secure core responsible for maintaining the chain of trust for
      the entire system, and for upgrade of the entire system

- The secure code will make a platform-specific call immediately after setting
  up hardware protection to (potentially) start the non-secure core running

    - This is the earliest point at which it is safe to allow the non-secure
      code to start running, so starting it here ensures system integrity while
      also giving the non-secure code the maximum amount of time to perform its
      initialization

    - Note that this is after the bootloader has validated the non-secure image,
      which is the other key part to maintain security

    - This also means that only tfm_s and tfm_ns have to change, and not mcuboot

- Both the secure and non-secure code will make platform-specific calls to
  establish a synchronization point. This will be after both sides have done
  any initialization that is required, including setting up inter-core
  communications. On a single core system, this would be the point at which the
  secure code jumps to the non-secure code, and at the very start of the
  non-secure code.

- After completing initialization on the secure core (at the point where on a
  single core system, it would jump to the non-secure code), the main thread on
  the secure core will be allowed to die

    - The scheduler has been started at this point, and an idle thread exists.
      Any additional work that is only required in the multi cpu case will be
      interrupt-driven.

    - All work related to the non-secure core will take place from a
      `ns_agent_mailbox` partition, which will establish communication with
      the non-secure core and then act on its behalf

- Because both cores may be booting in parallel, executing different
  initialization code, at different speeds, the design must be resilient if
  either core attempts to communicate with the other before the latter is ready.
  For example, the client (non-secure) side of the IPC mechanism must be able
  to handle the situation where it has to wait for the server (secure) side to
  finish setting up the IPC mechanism.

    - This relates to the synchronization calls mentioned above. It means that
      those calls cannot utilise the IPC mechanism, but must instead use some
      platform-specific mechanism to establish this synchronization. This could
      be as simple as setting aside a small area of shared memory and having
      both sides set a “ready” flag, but may well also involve the use of
      interrupts.

    - This also means that the synchronization call must take place after the
      IPC mechanism has been set up but before any attempt (by either side) to
      use it.

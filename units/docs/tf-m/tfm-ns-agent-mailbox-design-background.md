---
id: "tfm-ns-agent-mailbox-design-background"
type: "concept"
domain: "security"
title: "NS Agent Mailbox Design: Background"
summary: "The SPE communicates with a remote NSPE through the 'NS Agent Mailbox'. A physical mailbox mechanism is required for this partition to work."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/mailbox_design.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/mailbox_design.html#background"
license: "BSD-3-Clause"
mode: "V"
---

The SPE communicates with a remote NSPE through the 'NS Agent Mailbox'.
A physical mailbox mechanism is required for this partition to work.

The `NS Agent Mailbox` operates like a `partition`.
The agent has an endless loop and waits for signals, calls the FF-M API based on
the parsed communication messages.

Because it acts as an agent, you must consider several key design details:

- The SPM treats the FF-M Client API caller’s ID as the client ID. However,
  because the NS Agent Mailbox may represent multiple non-secure clients, it
  must inform SPM which client it represents.
  The standard FF-M Client API lacks support for this requirement.
- The FF-M Client API blocks the caller until a reply is received. However,
  the NS Agent Mailbox must respond to non-secure interrupts promptly. Blocking
  can delay the handling of non-secure communication messages.


**Note:** All the concepts for dual-cpu can be extended to multi-cpu without loss of generality. Also see the Hybrid Platform section for further details.

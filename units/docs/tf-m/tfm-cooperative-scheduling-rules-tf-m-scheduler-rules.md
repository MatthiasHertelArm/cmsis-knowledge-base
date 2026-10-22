---
id: "tfm-cooperative-scheduling-rules-tf-m-scheduler-rules"
type: "concept"
domain: "security"
title: "Cooperative Scheduling Rules: TF-M Scheduler - Rules"
summary: "On ArmV8-M CPUs, NSPE and SPE share the same physical processing element(PE). A TF-M enabled systems need to be able to handle asynchronous events (interrupts) regardless of current security state of the PE, and that may lead to scheduling decisions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/tfm_cooperative_scheduling_rules.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/tfm_cooperative_scheduling_rules.html#tf-m-scheduler-rules"
license: "BSD-3-Clause"
mode: "V"
---

On ArmV8-M CPUs, NSPE and SPE share the same physical processing element(PE). A
TF-M enabled systems need to be able to handle asynchronous events (interrupts)
regardless of current security state of the PE, and that may lead to scheduling
decisions. This introduces significant complexity into TF-M. To keep the
integrity of (NSPE and SPE) schedulers and call paths between NSPE and SPE,
following set of rules are imposed on the TF-M scheduler design.

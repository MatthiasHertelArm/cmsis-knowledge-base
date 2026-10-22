---
id: "tfm-ns-agent-mailbox-design-design"
type: "concept"
domain: "security"
title: "NS Agent Mailbox Design: Design"
summary: "The following figure shows the overall design of the relevant components. NS Agents are implementation-defined components that provide FF-M-compliant Client APIs to non-secure clients. From the client’s perspective, these APIs behave according to the FF-M specification."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/mailbox_design.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/mailbox_design.html#design"
license: "BSD-3-Clause"
mode: "V"
---

The following figure shows the overall design of the relevant components.
NS Agents are implementation-defined components that provide FF-M-compliant
Client APIs to non-secure clients.
From the client’s perspective, these APIs behave according to the FF-M
specification.
However, NS Agents require customization and additional handling in the SPM
because they carry extra requirements compared to standard secure partitions.


**Note:** `NS Agent TrustZone` is mentioned for the comparison purpose. The implementation details are out of scope for this document.

To align with FF-M compliance, the NS Agent Mailbox is designed to:

- operate like a standard Secure Partition under the IPC model, with one single
  thread and the ability to call standard FF-M APIs
- include a manifest file that describes its attributes and resources
- be assigned a positive partition ID

Services rely on the `client_id` for policy enforcement. When the NS Agent
Mailbox calls a Client API, the SPM must know which `client_id` the agent is
representing. Since standard APIs treat the caller as the service client, a
specific API is needed to support identifying the represented non-secure client.

The SPM sets the non-secure `client_id` into the message just before it sends
the message. Until then, it uses the agent’s ID.

This specific `Agent API` is non-blocking, unlike the standard FF-M Client APIs.
It improves communication efficiency between NS clients and NS Agent Mailbox.
This mechanism also requires additional signals and APIs for message
acknowledgments.


**Note:** A standard Secure Partition cannot use the `Agent API`. If attempted, an error is returned.

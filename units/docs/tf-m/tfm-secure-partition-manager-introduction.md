---
id: "tfm-secure-partition-manager-introduction"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Introduction"
summary: "Secure services (aka Service) is the component providing secure functionalities in SPE, and Client is the user of the Service. A service acts as a client when it is accessing its depending services."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The service access process of FF-M:

Secure services (aka `Service`) is the component providing secure
functionalities in `SPE`, and `Client` is the user of the `Service`. A service
acts as a client when it is accessing its depending services.

Services are grouped into `Secure Partition` (aka `partition`). A partition:

- Contains services with the same purpose.
- Provides implementation required isolation boundaries.
- Is a software development unit.

Each service exposes its `Service ID` (`SID`) and `Handle` for client access
usage. Clients access services by `SID` or `Handle` through FF-M `Client API`.
Partitions use FF-M `Secure Partition API` when it needs to operate on client
data or reply to a client.

`SPM` is the centre of an FF-M compliant implementation, which sets up and
maintains a firmware framework that:

- Implements `Client API` and `Secure Partition API`.
- Manages partition runtime to follow FF-M.
- Involves necessary implementation-defined items to support the
  implementation.

SPM interfaces consist of these two categories:

- FF-M defined API.
- Extended API to support the implementation.

Both API categories are compliant with FF-M concepts and guidelines. The core
concept of TF-M SPM surrounds the FF-M defined service management and access
process. Besides this, another important implementation part is partition
runtime management.


### Partition runtime model

One partition must work under as `ONE` of the runtime models:
`Inter-process communication` (`IPC`) model or `Secure Function` (`SFN`)
model.

A partition that runs under the `IPC` model looks like a classic `process`.
There is `ONE` thread inside the partition keeps waiting for signals. SPM
converts the service accessing info from the `Client API` call into messages
and assert a signal to the partition. The partition calls corresponded service
function indicated by the signal and its bound message, and reply service
returned result to the client. The advantages of this model:

- It provides better isolation by limiting the interfaces on data interactive.
  Data are preferred to be processed in a local buffer.
- It provides a mechanism for handling multiple service access. There is no
  memory mapping mechanism in the MCU system, hence it is hard to provide
  multiple function call contexts when serving multiple-threaded clients if
  the service access is implemented in a function-call based mechanism. This
  model converts multiple service accesses into messages, let the partition
  handles the service access in messages one by one.

The `Secure Function` (`SFN`) model partition is close to a `library`. Each
service is provided as a function entry inside the partition. SPM launches
the target service function after the service is found. The whole procedure
(from client to service function) is a function call. This model:

- Saves the workloads spent on `IPC` scheduling.

Meanwhile, it relaxes the data interactive mechanism, for example, allow
direct memory access (MMIOVEC). And it is hard to enable multiple-threaded
clients service access because of multiple call context-maintenance
difficulties.

An implementation contains only `SFN` partitions fits better in the
resource-constrained devices, it is called an `SFN model implementation`. And
it is an `IPC model implementation` when `IPC` partitions exist in the system.


**Note:** `IPC model implementation` can handle access to the services in the `SFN` partition.


### Components and isolation levels

There are `THREE` isolation levels defined in `FF-M`. These levels can
fulfil different security requirements by defining different isolation
boundaries.


**Note:** Concept `ARoT`, `PRoT`, `domain`, and boundaries are in the `FF-M` specification.

Not like an `SPE` client that can call `Client API` to access the secure
services in one step, an `NSPE` client needs to cross the secure boundaries
first before calling `Client API`. The component `NS Agent` in
fig-modelisolation represents `NSPE` clients after they crossed
the secure boundaries. This could help `SPM` handles the request in a
unified way instead of care about the special boundaries.


**Note:** `NS Agent` is a necessary implementation-defined component out of FF-M specification. `NS Agent` has a dedicated stack because secure and non-secure can not share the stack. It also has dedicated execution bodies. For example, RPC-based `NS Agent` has a while loop that keeps waiting for messages; and Trustzone-based `NS Agent` has veneer code to take over `NSPE` secure call. This makes `NS Agent` to be a component more like a `process`. Hence in the simplest implementation (`SFN model implementation` mentioned above), `NS Agent` is the only process in the system, the scheduling logic can be extremely simplified since no other process execution needs to be scheduled. But the scheduling interface is still necessary to SPM, this could help SPM treat both `SFN` and `IPC` model implementation in a unified way. Check NS Agent for details.


### Implementation principle

The principles for TF-M SPM implementation:


**Important:** - SPM can treat these components as the client: NS Agent, SFN Partition, and IPC partition. - These components can provide services: SFN Partition, IPC partition, and built-in services. A built-in service is built up with SPM together. - All partition services must be accessed by `Client API`. - Partitions interact with client data by `Secure Partition API`. - Built-in services are strongly recommended to be accessed by `Client API`. Customized interfaces are restricted. - Built-in services can call SPM internal interfaces directly.

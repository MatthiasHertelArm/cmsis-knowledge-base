---
id: "ocp-open-cmsis-pack-taxonomy"
type: "concept"
domain: "pack"
title: "Open-CMSIS-Pack-Taxonomy"
summary: "Open-CMSIS-Pack enables software re-use across software vendors and companies. This repository organizes the usage of Cclass and Cgroup definitions that provide access to:"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Taxonomy@5173cb1:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/Open-CMSIS-Pack-Taxonomy/blob/5173cb1/README.md"
license: "Apache-2.0"
mode: "V"
---

Open-CMSIS-Pack enables software re-use across software vendors and companies. This repository organizes the usage of `Cclass` and `Cgroup` definitions that provide access to:

- Software components that are defined with the element [`<components>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html).
- Application Programming Interfaces (API) are defined with the element [`<apis>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html).

The `Cclass` and `Cgroup` names are used to select software components. The file [`Open-CMSIS-Pack-Taxonomy.yaml`](https://github.com/Open-CMSIS-Pack/Open-CMSIS-Pack-Taxonomy/blob/main/Open-CMSIS-Pack-Taxonomy.yaml) contains the registered `Cclass` names and describes their usage.

Each new `Cclass` name should be registered with an **Mode** (explained below) to avoid conflicts with other software packs.  A `CGroup` name needs to be registered only when there is strict control about the usage.

[**Request a new Cclass name >**](https://github.com/Open-CMSIS-Pack/Open-CMSIS-Pack-Taxonomy/issues/new?assignees=&labels=new+Cclass&projects=&template=cclass_request.yml&title=%5BCclass+Request%3A%5D+Cclass+%3D+)

The following **Mode** types allows validation tools to perform checks:

- **Mode: Open** allows components from multiple vendors. Every vendor can add additional Cgroup names. As a component has also a Cvendor, an name clash between different vendors can be resolved. Still it is recommended to avoid name clashes at the Cgroup level.
- **Mode: Device** are device specific software components. New Cgroup names are allowed, but each component must have a dependency to a device (otherwise similar to Mode: Open).
- **Mode: Board** are board specific software components. New Cgroup names are allowed, but each component must have a dependency to a board (otherwise similar to Mode: Open).
- **Mode: Controlled** are controlled by the Owner (=vendor). CMSIS, LVGL, or Memfault could be examples for such a Cclass.
- **Mode: Bundle** publish a complete software stack with fixed functionality (i.e. File System, TCP/IP stack, etc.). Additional Cgroup names can only be added using the same Cvendor name. It is possible to have multiple bundles that use the same Cclass name.
- **Mode: API** are Cclass names defined with [`<apis>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html) and controlled by the Owner (=vendor). Driver implementations can be provided by various vendors using a Csub name. Depending on the attribute exclusive one or more implementations may be provided.

The long-term implications of the different modes are:
- **Mode: Open** new Cgroup names are accepted. There might be a check for duplicates in other packs.
- **Mode: Device** new Cgroup names are accepted. There is a check for a device condition as the components are device specific.
- **Mode: Board** new Cgroup names are accepted. There is a check for a board condition as the components are boards specific.
- **Mode: Controlled** components that are not provided by the owner are flagged.
- **Mode: Bundle** check that a bundle name is unique, otherwise flagged.
- **Mode: API** same as Mode:Controlled as new APIs can only be added by the Owner (=vendor).

> **Note:**
>
> A `Cclass` name that is incorrectly applied may result to unexpected behaviour of the Open-CMSIS-Pack system. Sometimes even established software packs become unusable or users get confused by way components are represented. It is therefore mandantory to register the `Cclass` taxonomy using this repository.

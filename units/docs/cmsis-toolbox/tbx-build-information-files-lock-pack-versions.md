---
id: "tbx-build-information-files-lock-pack-versions"
type: "concept"
domain: "project"
title: "Build Information Files: Lock Pack Versions"
summary: "A csolution project refers to packs in different files (.csolution.yml, .cproject.yml or .clayer.yml). To ensure consistent pack usage during application development (for example when new target-types or build-types are introduced), the .cbuild-pack.yml file records the exact pack versions."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#lock-pack-versions"
license: "Apache-2.0"
mode: "V"
---

A *csolution project* refers to packs in different files (`*.csolution.yml`, `*.cproject.yml` or `*.clayer.yml`). To ensure consistent pack usage during application development (for example when new `target-types` or `build-types` are introduced), the `*.cbuild-pack.yml` file records the exact pack versions.

The required packs can be specified in *csolution project files* in the following ways:

- exactly, e.g. `ARM::CMSIS@5.9.0`
- with range, e.g. `ARM::CMSIS@>=5.8.0`
- without version, e.g. `ARM::CMSIS`
- with wildcards on the pack name, e.g. `ARM::CMSI*`
- without pack name, e.g. `ARM`

The required packs are resolved to an exact pack version that is recorded in the `*.cbuild-pack.yml` file as shown below:

```yml
cbuild-pack:
  resolved-packs:
    - resolved-pack: ARM::CMSIS@5.9.0
      selected-by-pack:
        - ARM
        - ARM::CMSI*
        - arm::cmsis
        - ARM::CMSIS@>=5.8.0
        - ARM::CMSIS@5.9.0
```

The `resolved-pack:` node uses the canonical vendor and pack-name spelling from the PDSC file, while `selected-by-pack:` preserves the spelling used in the project input. If *csolution project files* are modified, the `selected-by-pack` information ensures that consistent pack versions are used. If a required pack is no longer used or present in the *csolution project*, the relevant entry `resolved-pack:` in  the `*.cbuild-pack.yml` file is removed.

The `*.cbuild-pack.yml` file is located in the same directory as the `*.csolution.yml` file and is used by the `csolution` for every command that uses a `*.csolution.yml` file. Examples are:

- `csolution convert` - uses **and updates** the `*.cbuild-pack.yml` file.
- `csolution list ...` - uses the `*.cbuild-pack.yml` file
- `csolution run` - uses the `*.cbuild-pack.yml` file.
- `csolution update-rte` - uses **and updates** the `*.cbuild-pack.yml` file.

The operation of the `csolution` command is as follows:

- Load the *csolution project files* (`*.csolution.yml`, `*.cproject.yml` or `*.clayer.yml`).
- Initially there is no `*.cbuild-pack.yml` file. If it exists, the `*.cbuild-pack.yml` file is loaded. The packs are aligned with the `resolved-pack:` information of the `*.cbuild-pack.yml` file in these steps:
    - *PopulateContexts*: Add `resolved-pack:` information to the *solution data model*.
    - *AddPackRequirements*: Pack version ranges and pack wildcards are matched to fully qualified versions of the *solution data model*. Pack wildcards are expanded to fully qualified packs using cbuild-pack.yml. Pack wildcards are kept for further expansion in the *solution data model*.
- Execute the `csolution` command, for example `convert`, `list`, `run`, or `update-rte`.
- Update the `*.cbuild-pack.yml` file (only if the content changes):
    - *GenerateCbuildPack*: Generate the `resolved-pack:` list of packs required by all *contexts*. The original `pack:` specification is stored under `selected-by-pack:`.

With the subsequent `csolution` command, the information of the `*.cbuild-pack.yml` file is used to load the appropriate fully qualified pack versions, matching previously used packs.

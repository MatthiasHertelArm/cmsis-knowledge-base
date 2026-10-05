---
id: "tbx-csolution-project-structure-reproducible-builds"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Reproducible builds"
summary: "Reproducible builds are supported by the .cbuild-pack.yml file that is created and read by the csolution project manager. This file:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#reproducible-builds"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

Reproducible builds are supported by the [*.cbuild-pack.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-packyml) file that is created and read by the **csolution** project manager. This file:

- Records the exact list of the pack versions used during the creation of an application.
- Ensures that pack versions do not change during development, even when new packs are installed on the host computer, for example, to develop other applications.

!!! Note
    - The [*.cbuild-pack.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-packyml) file should be committed to a repository to ensure reproducible builds.
    - The `cbuild` option `--frozen-packs` checks that the [*.cbuild-pack.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-packyml) file exists and reports an error if any pack is changed or not available.
    - Before updating, use `csolution check pack-updates` to review available versions and release notes. Then change the applicable `pack:` requirement or remove only that pack's `resolved-pack:` entry from `*.cbuild-pack.yml` and run `cbuild setup <solution>.csolution.yml --update-rte` or `csolution update-rte`. Review the resulting configuration-file changes before committing the updated `*.cbuild-pack.yml` and RTE files. Deleting the entire file resolves every pack again and should be reserved for an intentional full refresh.

#### Repository Contents

To support reproducible builds, the following files should be committed to a repository of a version control system.

- All user source code files.
- All *csolution project files* (`cdefault.yml`, `*.csolution.yml`, `*.cproject.yml`, etc.).
- All files in the RTE directory
    - Ensure that there are no files with the extension *.update@* as this indicates that configuration files are not up-to-date due to updated software packs.
- The file `*.cbuild-pack.yml` to allow [reproducible builds](#reproducible-builds).

---
id: "armsw-cortex-dfp-generating-software-pack"
type: "concept"
domain: "core"
title: "Cortex_DFP: Generating Software Pack"
summary: "Some helper scripts are provided to generate the release artifacts from this repository."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Cortex_DFP@cd38dbb:README.md"
doc_source: "https://github.com/ARM-software/Cortex_DFP/blob/cd38dbb/README.md#generating-software-pack"
license: "Apache-2.0"
mode: "V"
---

Some helper scripts are provided to generate the release artifacts from this repository.

### CMSIS-Pack Bundle

The CMSIS-Pack bundle can be generated with

```sh
Cortex_DFP $ ./gen_pack.sh
```

Prerequisites for this script to succeed are:

- 7z/GNU Zip
- packchk (e.g., via CMSIS-Toolbox)
- xmllint (optional)

### Version and Changelog Inference

The version and changelog embedded into the documentation and pack are inferred from the
local Git history. In order to get the full changelog one needs to have a full clone (not
a shallow one) including all release tags.

The version numbers and change logs are taken from the available annotated tags.

### Release Pack

A release is simply done via the GitHub Web UI. The newly created tag needs to have
the pattern `v<version>` where `<version>` shall be the SemVer `<major>.<minor>.<patch>`
version string for the release. The release description is used as the change log
message for the release.

When using an auto-generated tag (via Web UI) the release description is used as the
annotation message for the generated tag. Alternatively, one can prepare the release
tag in the local clone and add the annotation message independently from creating the
release.

Once the release is published via the GitHub Web UI the release workflow generates the
documentation and the pack (see above) and attaches the resulting pack archive as an
additional asset to the release.

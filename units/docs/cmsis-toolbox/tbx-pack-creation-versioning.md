---
id: "tbx-pack-creation-versioning"
type: "concept"
domain: "pack"
title: "Pack Creation: Versioning"
summary: "The CMSIS-Pack system uses version numbers to track and differentiate various releases of packs, components, and configuration files. It supports these versioning schemas:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#versioning"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Pack system uses version numbers to track and differentiate various releases of packs, components, and configuration files. It supports these versioning schemas:

1. **Semantic Versioning** ([SemVer](https://semver.org/)) is the recommended format with  `MAJOR.MINOR.PATCH`. for example: `1.4.2`. [SemVer](https://semver.org/)

    - `MAJOR` indicates big updates that break backward compatibility.
    - `MINOR` indicates new features, but still backward-compatible.
    - `PATCH` indicates bug fixes or minor tweaks.

2. **Calendar Versioning** ([CalVer](https://calver.org/)) is accepted when higher values indicated newer releases. The format should be therefore `YY.MM.DD`, or `YY.MM.PATCH`. For example:

    - `22.04.1` indicates April 2022 release, patch version 1.
    - `25.02.07` indicates release date 7. Feb. 2025.

Both versioning schemas support `-pre-release` labels that may be used during development and testing. For example:

- `1.0.0-alpha` for early testing.
- `22.04.0-rc.1` for a release candidate that is close to final.

Product Lifecycle Management (PLM) and versioning are closely connected. Versioning ensures that each stage of PLM is properly controlled and documented. The CMSIS-Toolbox accepts therefore version numbers and ranges for `packs` and `components` and outputs version details in [build information files](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-CBuild-Format.md).

**Semantic Versioning** ([SemVer](https://semver.org/)) is recommended as it supports the PLM features of the CMSIS-Toolbox. It enables [PLM of configuration files](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#plm-of-configuration-files) and simplifies the software pack updates. For example: `- pack: ARM::CMSIS@^6.1.0` accepts any release version equal or higher but with the same `MAJOR` version. To accept also pre-release versions, use `- pack: ARM::CMSIS@^6.1.0-0`.

!!! Note
    - During the development of a pack `+build` information may be used. This `+build` information is ignored by the CMSIS-Toolbox and should be not part of a public released pack.

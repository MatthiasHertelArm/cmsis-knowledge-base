---
id: "tbx-csolution-project-format-pack-name-conventions"
type: "concept"
domain: "project"
title: "CSolution Project Format: Name Conventions / `pack:` Name Conventions"
summary: "The csolution Project Manager uses the following syntax to specify the pack: names in the .yml files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#pack-name-conventions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Name Conventions_

The **`csolution` Project Manager** uses the following syntax to specify the `pack:` names in the `*.yml` files.

```yml
vendor::pack-name                # Use the latest version of the pack
vendor::pack-name@version        # With exact version
vendor::pack-name@>=version      # With version equal or higher
vendor::pack-name@^version       # With version equal or higher but the same major version
vendor::pack-name@~version       # With version equal or higher but the same major and minor version
```

Element      |              | Description
:------------|:-------------|:---------------------
`vendor`     | **Required** | Vendor name of the software pack.
`pack-name`  | **Required** | Name of the software pack; wildcards (\*, ?) can be used.
`@version`   |   Optional   | Software pack version number must exactly match, i.e. `@1.2.3`
`@>=version` |   Optional   | Automatically update to any version higher or equal.
`@^version`  |   Optional   | Automatically update minor/patch version, i.e. `@^1.2.3` uses releases from `1.2.3` to `< 2.0.0`.
`@~version`  |   Optional   | Automatically update patch version, i.e. `@~1.2.3` uses releases from `1.2.3` to `< 1.3.0`.

!!! Note
    - Pack vendor and pack names are matched case-insensitively. Their spelling does not need to match the `<vendor>` and `<name>` values in the PDSC file. Generated build information uses the canonical spelling from the PDSC file.
    - When no version is specified, the **`csolution` Project Manager** only loads the latest installed version of a software pack. This also applies when wildcards are used in the `pack-name`.
    - When the same pack is specified both without a version and with an exact version, the exact version is used for both requirements, even if a newer version is installed. This rule applies across all input files of the solution.
    - Use [**`cpackget`**](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-tools.md#cpackget-invocation) to download and install new pack versions.
    - To accept a [pre-release version of a pack](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/pack-tools.md#versioning) specify the `-pre-release` label. Use for example `- pack: Keil::MDK-Middleware@^8.0.0-0` to accept any pre-release version that is higher or equal.

**Examples:**

```yml
- pack:   ARM::CMSIS@5.9.0                 # 'CMSIS' Pack with version 5.9.0
- pack:   arm::cmsis@^6.0.0                # Pack vendor and name matching is case-insensitive
- pack:   Keil::MDK-Middleware@>=7.13.0    # latest version 7.13.0 or higher
- pack:   Keil::MDK-Middleware@^7.13.0     # latest version 7.13.0 or higher, but lower than 8.0.0
- pack:   Keil::TFM                        # 'TFM' Pack from vendor Keil, latest installed version
- pack:   AWS                              # All Software Packs from vendor 'AWS', latest version
- pack:   Keil::STM*                       # Software Packs that start with 'STM' from vendor 'Keil'
- pack:   Keil::MDK-Middleware@>=8.0.0-0   # version 8.0.0 or higher including pre-release versions
```

For example, if one input file specifies `ARM::CMSIS` and another specifies `ARM::CMSIS@6.1.0`, both requirements resolve to `ARM::CMSIS@6.1.0`; a separately installed version 6.2.0 does not override the exact selection.

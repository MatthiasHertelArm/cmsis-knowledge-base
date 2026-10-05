---
id: "aig-install-guides-arm-toolchains-repositor-previous-repository-locations"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: Previous repository locations"
summary: "The current Arm Toolchains repository at https://developer.arm.com/packages/arm-toolchains/ replaces the earlier repository structure that was based on repositories built using the SUSE Open Build Service."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#previous-repository-locations"
license: "CC-BY-SA-4.0"
mode: "V"
---

The current Arm Toolchains repository at [https://developer.arm.com/packages/arm-toolchains/](https://developer.arm.com/packages/arm-toolchains/) replaces the earlier repository structure that was based on repositories built using the SUSE Open Build Service.

Earlier repositories were published under the top-level package URL [https://developer.arm.com/packages/](https://developer.arm.com/packages/) and used repository prefixes such as:

```output
ACfL:<distro>
arm-toolchains:<distro>
```

These earlier repositories are deprecated but will continue to work until further notice.

Don't configure new systems to use the deprecated `ACfL:` or `arm-toolchains:` repository paths. Migrate existing systems to the current Arm Toolchains Linux repositories and install the current `arm-toolchains-repository` package.

The deprecated repositories will be removed in a future update.

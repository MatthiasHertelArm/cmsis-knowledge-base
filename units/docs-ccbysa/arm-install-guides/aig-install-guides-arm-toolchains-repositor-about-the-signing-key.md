---
id: "aig-install-guides-arm-toolchains-repositor-about-the-signing-key"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: About the signing key"
summary: "Linux package managers use cryptographic signing keys to verify that repository metadata and packages are authentic and come directly from Arm."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#about-the-signing-key"
license: "CC-BY-SA-4.0"
mode: "V"
---

Linux package managers use cryptographic signing keys to verify that repository metadata and packages are authentic and come directly from Arm.

In July 2026, Arm reviewed and strengthened the repository management and publication processes used for the Arm Toolchains repository. As part of the continuing evolution of this release channel, Arm revoked and replaced the signing key.

If you're setting up a new system after July 2026, installing the `arm-toolchains-repository` package automatically configures the current repository signing key for you. You don't need to install the key manually or verify fingerprints.

However, if you're upgrading a system that configured the Arm Toolchains repository for Linux before July 2026, you need to update the repository configuration to use the new key.
Otherwise, your package manager might refuse to refresh repository metadata or install packages.

Existing installed copies of Arm Toolchain for Linux and Arm Performance Libraries continue to work.

---
id: "aig-install-guides-arm-toolchains-repositor"
type: "concept"
domain: "project"
title: "Arm Toolchains repository"
summary: "The Arm Toolchains repository provides a native and convenient way to install selected Arm software products on supported Linux hosts using the host operating system package manager."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/"
license: "CC-BY-SA-4.0"
mode: "V"
---

The [Arm Toolchains repository](https://developer.arm.com/packages/arm-toolchains/) provides a native and convenient way to install selected Arm software products on supported Linux hosts using the host operating system package manager.

The repository files are used to distribute Linux packages for Arm Toolchains, including:

- Arm Toolchain for Linux
- Arm Performance Libraries for supported compilers on Linux

Using the repository, you can install, upgrade, and manage these packages using standard Linux package-management tools such as `apt`, `dnf`, `yum`, and `zypper`.

To use the repository, you'll need to install the repository package. Arm provides an `arm-toolchains-repository` package for each supported Linux distribution. The package installs:

- the Arm Toolchains repository definition for your Linux distribution
- the Arm Toolchains repository signing public key
- package manager configuration that associates the repository with the correct signing key

**Signing-key update:**
If you configured the Arm Toolchains repository before July 2026, package manager operations might report a signing-key error or ask you to trust a new key. Existing installations of Arm Toolchain for Linux and Arm Performance Libraries continue to work. See [Recognize package manager signing-key errors](#recognize-package-manager-signing-key-errors).

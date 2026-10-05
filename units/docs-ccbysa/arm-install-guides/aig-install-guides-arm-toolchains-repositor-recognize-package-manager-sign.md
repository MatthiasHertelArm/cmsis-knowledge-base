---
id: "aig-install-guides-arm-toolchains-repositor-recognize-package-manager-sign"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: Recognize package manager signing-key errors"
summary: "You only need this section if you configured the Arm Toolchains repository before July 2026, or if a package manager reports a signing-key problem. New systems that install arm-toolchains-repository version 2-2 or later already use the current key."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#recognize-package-manager-signing-key-errors"
license: "CC-BY-SA-4.0"
mode: "V"
---

You only need this section if you configured the Arm Toolchains repository before July 2026, or if a package manager reports a signing-key problem. New systems that install `arm-toolchains-repository` version `2-2` or later already use the current key.

These messages don't mean that your installed copy of Arm Toolchain for Linux or Arm Performance Libraries is damaged. They mean that the package manager can't verify new repository metadata or packages until you update the repository configuration.

### Ubuntu

Running `sudo apt update` might report:

```output
The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 8144CA1611A0BD71
```

### RHEL and Amazon Linux

`dnf` or `yum` might report:

```output
The GPG keys listed for the "Arm Toolchains" repository are already installed but they are not correct for this package.
Error: GPG check FAILED
```

### SLES

Rather than reporting an error, `zypper refresh` might ask you to trust the current signing key:

```output
New repository or package signing key received:

Key Fingerprint: A406 5BCE 9386 DD1E 62FD E03B 8144 CA16 11A0 BD71

Do you want to reject the key, trust temporarily, or trust always? [r/t/a/?] (r):
```

Confirm that the fingerprint matches the value shown above before entering `a` to trust the key permanently.

To update the repository configuration, [install the repository package directly](#install-the-repository-package-directly). If you can't install the package, see [Use manual recovery](#use-manual-recovery).

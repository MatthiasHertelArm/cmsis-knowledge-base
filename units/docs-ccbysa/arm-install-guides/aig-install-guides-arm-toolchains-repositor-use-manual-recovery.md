---
id: "aig-install-guides-arm-toolchains-repositor-use-manual-recovery"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: Use manual recovery"
summary: "The recommended method is to install arm-toolchains-repository version 2-2 or later directly."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#use-manual-recovery"
license: "CC-BY-SA-4.0"
mode: "V"
---

The recommended method is to install `arm-toolchains-repository` version `2-2` or later directly.

Use manual recovery only if you cannot install the repository package directly.

### Ubuntu manual recovery

Remove previous Arm Linux Toolchains Repository key material if present:

```bash
sudo rm -f /usr/share/keyrings/arm-toolchains-archive-keyring.gpg
sudo rm -f /etc/apt/keyrings/arm-toolchains-archive-keyring.gpg
sudo rm -f /etc/apt/trusted.gpg.d/arm-toolchains.gpg
sudo rm -f /etc/apt/trusted.gpg.d/arm-toolchains.asc
```

Install the current Arm Toolchains repository signing key:

```bash
curl -O https://developer.arm.com/packages/arm-toolchains/arm-toolchains.gpg
sudo install -D -m 0644 arm-toolchains.gpg \
  /usr/share/keyrings/arm-toolchains-archive-keyring.gpg
```

Check the fingerprint:

```bash
gpg --show-keys --fingerprint /usr/share/keyrings/arm-toolchains-archive-keyring.gpg
```

The output should include:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

Find any existing Arm Toolchains repository entries:

```bash
grep -Rns "developer.arm.com/packages/arm-toolchains/ubuntu" \
  /etc/apt/sources.list /etc/apt/sources.list.d 
```

If the command finds an existing entry, edit that entry so it references `/usr/share/keyrings/arm-toolchains-archive-keyring.gpg` using `signed-by`. Don't create a second entry for the same repository because `apt` might report conflicting `Signed-By` values.

If the command doesn't find an entry, create `/etc/apt/sources.list.d/arm-toolchains.list` using one of the following commands:

For Ubuntu 24.04, run:

```bash
echo "deb [signed-by=/usr/share/keyrings/arm-toolchains-archive-keyring.gpg] https://developer.arm.com/packages/arm-toolchains/ubuntu noble main" | \
  sudo tee /etc/apt/sources.list.d/arm-toolchains.list
```

For Ubuntu 22.04, run:

```bash
echo "deb [signed-by=/usr/share/keyrings/arm-toolchains-archive-keyring.gpg] https://developer.arm.com/packages/arm-toolchains/ubuntu jammy main" | \
  sudo tee /etc/apt/sources.list.d/arm-toolchains.list
```

After creating `arm-toolchains.list`, refresh package metadata:

```bash
sudo apt update
```

### RPM-based manual recovery

Remove the previous Arm Toolchains public key if present:

```bash
sudo rpm -e gpg-pubkey-7a05af82* || true
```

Install the current Arm Toolchains repository signing key:

```bash
curl -O https://developer.arm.com/packages/arm-toolchains/arm-toolchains.gpg
sudo rpm --import arm-toolchains.gpg
```

Check that the key is installed:

```bash
rpm -qa gpg-pubkey*
```

Refresh package metadata by running one of the following set of commands.

For RHEL, Amazon Linux, and compatible RPM-based distributions:

```bash
sudo dnf clean all
sudo dnf makecache
```

For SLES:

```bash
sudo zypper clean
sudo zypper refresh
```

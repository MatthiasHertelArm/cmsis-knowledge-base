---
id: "aig-install-guides-arm-toolchains-repositor-signing-key-reference"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: Signing key reference"
summary: "For reference or manual verification, the fingerprints of the previous and current Arm Toolchains signing keys are as follows."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#signing-key-reference"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Repository signing key fingerprints

For reference or manual verification, the fingerprints of the previous and current Arm Toolchains signing keys are as follows.

Previous fingerprint:

```output
EE37 7ACD D5AD 4AB6 BD79  9B8A B83D 741E 7A05 AF82
```

Current fingerprint:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

### (Optional) Manually verify the signing key

If you want to manually verify the signing key, ensure the `gpg` utility (part of GnuPG) is installed on your system, then download the key file and display its fingerprint:

```bash
curl -O https://developer.arm.com/packages/arm-toolchains/arm-toolchains.gpg
gpg --show-keys --fingerprint arm-toolchains.gpg
```

The output should show the current fingerprint:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

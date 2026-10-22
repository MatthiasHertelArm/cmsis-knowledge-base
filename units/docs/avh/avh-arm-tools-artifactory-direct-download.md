---
id: "avh-arm-tools-artifactory-direct-download"
type: "concept"
domain: "test"
title: "Arm Tools Artifactory: Direct download"
summary: "You can download individual tool artifacts directly using the URL."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:DoxyGen/infrastructure/src/avh_artifactory.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/infrastructure/src/avh_artifactory.md#direct-download"
license: "Apache-2.0"
mode: "V"
---

You can download individual tool artifacts directly using the URL. The Arm FVPs can be found at
[https://artifacts.tools.arm.com/avh/](https://artifacts.tools.arm.com/avh/) and are organized by release version and
packaged for supported host operating systems such as Linux on Arm (AArch64), Windows on x86, and Linux on x86.

For example to download AVH FVP v11.30.29 for use on Linux with Arm-based CPUs, run the following commands:

```sh
wget https://artifacts.tools.arm.com/avh/11.30.29/avh-linux-aarch64_11.30_29_Linux64_armv8l.tgz
tar zxvf avh-linux-aarch64_11.30_29_Linux64_armv8l.tgz
```

In this example, the artifact is downloaded with `wget` and extracted. The models are then available locally in
`./avh-linux-aarch64/bin/models/` directory.

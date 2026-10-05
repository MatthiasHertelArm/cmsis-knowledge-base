---
id: "aig-install-guides-arm-toolchains-repositor-verify-the-repository-package"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: Verify the repository package version"
summary: "After installing the repository package, verify the installation:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#verify-the-repository-package-version"
license: "CC-BY-SA-4.0"
mode: "V"
---

After installing the repository package, verify the installation:


  **Ubuntu:**
dpkg -l arm-toolchains-repository
  
  **RPM-based distributions:**
rpm -q arm-toolchains-repository
  


The installed version should be `2-2` or later.

---
id: "aig-install-guides-arm-toolchains-repositor-install-the-repository-package"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: Install the repository package directly"
summary: "Use one of the following commands to install the repository package directly. This allows you to update the repository configuration even if your package manager can't currently refresh the Arm Toolchains repository metadata."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#install-the-repository-package-directly"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use one of the following commands to install the repository package [directly](https://developer.arm.com/packages/arm-toolchains/). This allows you to update the repository configuration even if your package manager can't currently refresh the Arm Toolchains repository metadata.


  **Ubuntu 24.04:**
curl -O https://developer.arm.com/packages/arm-toolchains/ubuntu/pool/arm-toolchains-repository_2-2~noble_all.deb
sudo dpkg -i arm-toolchains-repository_2-2~noble_all.deb
sudo apt update
  
  **Ubuntu 22.04:**
curl -O https://developer.arm.com/packages/arm-toolchains/ubuntu/pool/arm-toolchains-repository_2-2~jammy_all.deb
sudo dpkg -i arm-toolchains-repository_2-2~jammy_all.deb
sudo apt update
  
  **RHEL 10:**
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el10/aarch64/arm-toolchains-repository-2-2.el10.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  
  **RHEL 9:**
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el9/aarch64/arm-toolchains-repository-2-2.el9.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  
  **RHEL 8:**
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el8/aarch64/arm-toolchains-repository-2-2.el8.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  
  **Amazon Linux 2023:**
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/amazonlinux/al2023/aarch64/arm-toolchains-repository-2-2.al2023.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  
  **SLES 15:**
sudo zypper install -y https://developer.arm.com/packages/arm-toolchains/sles/sles15/aarch64/arm-toolchains-repository-2-2.sles15.noarch.rpm
sudo zypper clean
sudo zypper refresh
  
  **SLES 16:**
sudo zypper install -y https://developer.arm.com/packages/arm-toolchains/sles/sles16/aarch64/arm-toolchains-repository-2-2.sles16.noarch.rpm
sudo zypper clean
sudo zypper refresh

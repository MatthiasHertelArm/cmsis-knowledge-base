---
id: "alp-avh-matter-2setup-install-necessary-software-com"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Prepare AVH instances of Raspberry Pi 4: Install necessary software components"
summary: "You'll build the Matter examples on the virtual Raspberry Pi 4 instances. To prepare for this, install the necessary dependencies on each instance. You can do this in parallel on both instances."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/2setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/2setup/#install-necessary-software-components"
license: "CC-BY-SA-4.0"
mode: "V"
---

You'll build the Matter examples on the virtual Raspberry Pi 4 instances. To prepare for this, install the necessary dependencies on **each** instance. You can do this in parallel on both instances.
```console
sudo apt-get update
sudo apt-get install -y git gcc g++ pkg-config libssl-dev libdbus-1-dev libglib2.0-dev libavahi-client-dev ninja-build python3-venv python3-dev python3-pip unzip libgirepository1.0-dev libcairo2-dev libreadline-dev libpango1.0-dev
```
You'll also build ZAP from source on your instances. ZAP is generally installed as a third-party tool via CIPD during the build environment bootstrap, but ZAP packages aren't currently available for arm64.
```console
git clone https://github.com/project-chip/zap.git ~/zap
cd ~/zap
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo src-script/install-packages-ubuntu
npm ci
export ZAP_DEVELOPMENT_PATH=~/zap
cd ~
```
This will also verify that your instances are working correctly.

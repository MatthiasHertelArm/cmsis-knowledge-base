---
id: "alp-avh-matter-4cicdsh-create-github-self-hosted-runn"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Manage development in a CI/CD workflow with Self-Hosted Runner: Create GitHub self-hosted runner"
summary: "Browse to the forked Matter repository in your personal GitHub space."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh/#create-github-self-hosted-runner"
license: "CC-BY-SA-4.0"
mode: "V"
---

Browse to the forked Matter repository in your personal GitHub space.

Navigate to `Settings` > `Actions` > `Runners`, and then click on `New self-hosted runner`.

Configure for `Linux` host on `ARM64` Architecture (the `host` of the runner will be the `lighting-app` Virtual Raspberry Pi 4 instance).

You'll see a set of commands (unique to you) to download and configure the `runner`.

In the `lighting-app` console, return to your home directory:
```console
cd ~
```
Copy and paste the `Download` and `Configure` commands (from GitHub) for your `self-hosted runner`.

It's OK to select the default options when prompted during configuration.

To keep the console available for later use, run the `self-hosted runner agent` as a background service (if started, first stop with `Ctrl+C`):
```console
sudo ./svc.sh install pi
sudo ./svc.sh start
sudo ./svc.sh status
```
In your GitHub repository, you'll see your runner listed (`Settings` > `Actions` > `Runners`), with `Idle` status.

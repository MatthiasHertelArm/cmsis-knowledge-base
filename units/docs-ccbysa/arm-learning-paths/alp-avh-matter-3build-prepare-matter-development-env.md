---
id: "alp-avh-matter-3build-prepare-matter-development-env"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Build and run Matter examples on Arm Virtual Hardware: Prepare Matter development environment"
summary: "Configure the Matter development environment on each instance, which again can be done with a provided script(s):"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/3build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/3build/#prepare-matter-development-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Configure the Matter development environment on each instance, which again can be done with a provided script(s):
```console
./scripts/build/gn_bootstrap.sh
source scripts/activate.sh
```
These will take a few minutes to complete. Don't forget to run scripts on each instance, which you can perform in parallel. You should see
```output
Environment looks good, you are ready to go!
```
when complete.

Full [documentation](https://github.com/project-chip/connectedhomeip/blob/master/docs/guides/BUILDING.md) on the build environment is provided in the Matter repository.

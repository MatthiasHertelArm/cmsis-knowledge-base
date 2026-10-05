---
id: "alp-nav-mlek-sw-using-docker"
type: "concept"
domain: "edge-ai"
title: "Navigate Machine Learning development with Ethos-U processors: Software development considerations: Using Docker"
summary: "You may want to use Docker to simplify ML development environment creation."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/nav-mlek/sw.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/nav-mlek/sw/#using-docker"
license: "CC-BY-SA-4.0"
mode: "V"
---

You may want to use [Docker](https://learn.arm.com/install-guides/docker/) to simplify ML development environment creation. 

As an example, clone the MLEK repository and look at the `Dockerfile` at the top of the repository to see one way to use Docker in ML application development:

```console
git clone "https://git.gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit.git"
cd ml-embedded-evaluation-kit
git submodule update --init
```

Use an editor or program such as `more` or `cat` to view the Dockerfile.

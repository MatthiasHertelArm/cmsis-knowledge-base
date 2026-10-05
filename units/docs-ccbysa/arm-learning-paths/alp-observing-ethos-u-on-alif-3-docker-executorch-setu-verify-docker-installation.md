---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-verify-docker-installation"
type: "concept"
domain: "edge-ai"
title: "3 docker executorch setup: Verify Docker installation"
summary: "After installation, start Docker Desktop and verify that Docker is available from your terminal:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#verify-docker-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

After installation, start Docker Desktop and verify that Docker is available from your terminal:

```bash
docker --version
```
The output is similar to:

```output
Docker version 24.0.7, build afdd53b
```

Test Docker is working:

```bash
docker run hello-world
```

The output is similar to:
```output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

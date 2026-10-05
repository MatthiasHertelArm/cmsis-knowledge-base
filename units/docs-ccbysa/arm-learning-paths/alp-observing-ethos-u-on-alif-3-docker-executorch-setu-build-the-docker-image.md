---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-build-the-docker-image"
type: "concept"
domain: "edge-ai"
title: "3 docker executorch setup: Build the Docker image"
summary: "Build the image from the executorch-alif directory:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#build-the-docker-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

Build the image from the `executorch-alif` directory:

```bash
docker build -t executorch-alif:latest .
```

**Note:**
The build can take 5 to 10 minutes.


The output is similar to:
```output
[+] Building 320.5s (12/12) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 1.2kB
 => [internal] load .dockerignore
 ...
 => => naming to docker.io/library/executorch-alif:latest
```

Verify the image:

```bash
docker images
```

The output is similar to:
```output
executorch-alif    latest
```

---
id: "armsw-foundation-components-for-mlops-sy-multi-architecture-support"
type: "concept"
domain: "edge-ai"
title: "Foundation Components for MLOps Systems: Multi-architecture support"
summary: "The Docker images support both x86_64 (amd64) and aarch64 (arm64) host architectures."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/AVH-MLOps@4a1c76f:README.md"
doc_source: "https://github.com/ARM-software/AVH-MLOps/blob/4a1c76f/README.md#multi-architecture-support"
license: "Apache-2.0"
mode: "V"
---

The Docker images support both **x86_64 (amd64)** and **aarch64 (arm64)** host architectures.

### Local builds
When building locally, Docker automatically targets the host architecture:
```bash
docker build -t arm-mlops-base ./docker_base
```
No additional flags are needed — this works on both x86_64 and aarch64 hosts (e.g., Apple Silicon, AWS Graviton).

To explicitly cross-build for a different architecture:
```bash
docker build --platform=linux/arm64 -t arm-mlops-base-arm64 ./docker_base
```

### CI images
CI workflows produce architecture-specific image tags:
- `arm-mlops-docker-base:latest-amd64` / `arm-mlops-docker-base:latest-arm64`
- `arm-mlops-docker-licensed:latest-amd64` / `arm-mlops-docker-licensed:latest-arm64`
- `arm-mlops-docker-licensed-community:latest-amd64` / `arm-mlops-docker-licensed-community:latest-arm64`

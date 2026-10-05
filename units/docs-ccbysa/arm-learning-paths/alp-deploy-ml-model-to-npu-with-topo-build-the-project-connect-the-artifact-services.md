---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-connect-the-artifact-services"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: Connect the artifact services"
summary: "Add pte-artifacts and runner-artifacts as siblings of the existing webapp service in the root compose.yaml:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#connect-the-artifact-services"
license: "CC-BY-SA-4.0"
mode: "V"
---

Add `pte-artifacts` and `runner-artifacts` as siblings of the existing `webapp` service in the root `compose.yaml`:

```yaml
services:
  pte-artifacts:
    platform: linux/arm64
    scale: 0
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: pte-artifacts
      cache_from:
        - ${EXECUTORCH_BASE_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04}

  runner-artifacts:
    platform: linux/arm64
    scale: 0
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: runner-artifacts
      cache_from:
        - ${IMX93_RUNNER_BUILD_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04}
```

Don't replace the existing root `webapp` service with this snippet. The root file should now have three service names under the same top-level `services:` map: `webapp`, `pte-artifacts`, and `runner-artifacts`.

These services are used only to build artifacts. They don't run as part of the deployed application. `scale: 0` tells Compose not to start containers for them, while still allowing other services to copy files from their build outputs.

Replace `webapp/compose.yaml` with the following version so the Flask image imports the `.pte` artifact:

```yaml
services:
  webapp:
    platform: linux/arm64
    build:
      context: .
      dockerfile: Dockerfile
      additional_contexts:
        pte_artifacts: service:pte-artifacts
    privileged: true
    ports:
      - "${WEBAPP_PORT:-3001}:3000"
    volumes:
      - /sys:/sys
      - /dev:/dev
    restart: unless-stopped
```

Then add the `.pte` copy line to `webapp/Dockerfile` with the other `COPY` commands:

```Dockerfile
COPY --from=pte_artifacts /artifacts/mv2_ethosu65_256.pte /opt/mv2-imx93/mv2_ethosu65_256.pte
```

The `/opt/mv2-imx93/` path is the location the Flask application expects for its MobileNetV2 support files. At run time, the app reads the `.pte` file from this path before copying it into reserved memory for the Cortex-M33 runner.

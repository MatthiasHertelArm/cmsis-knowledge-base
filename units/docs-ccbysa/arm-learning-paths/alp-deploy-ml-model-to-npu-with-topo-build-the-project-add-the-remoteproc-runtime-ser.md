---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-add-the-remoteproc-runtime-ser"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: Add the Remoteproc Runtime se"
summary: "Add the Cortex-M33 runner as another sibling under the top-level services: map in the root compose.yaml:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#add-the-remoteproc-runtime-service"
license: "CC-BY-SA-4.0"
mode: "V"
---

Add the Cortex-M33 runner as another sibling under the top-level `services:` map in the root `compose.yaml`:

```yaml
services:
  cm33-runner:
    platform: linux/arm64
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: runner-runtime
      cache_from:
        - ${IMX93_RUNNER_BUILD_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04}
    runtime: io.containerd.remoteproc.v1
    annotations:
      remoteproc.name: imx-rproc
```

Keep the existing `webapp`, `pte-artifacts`, and `runner-artifacts` services in the same file. This step adds one more service and doesn't replace any of the previous services.

This is the heterogeneous deployment hook. Docker still builds an image, but the service doesn't start as a Linux userspace process. The runtime `io.containerd.remoteproc.v1` selects Remoteproc Runtime, and the `remoteproc.name` annotation tells the shim to use the i.MX remote processor driver.

Update the existing root `webapp` service so it depends on the CM33 runner and passes the cache image values into the build. Keep the existing `extends` block, then add `depends_on` and `build.args` as shown:

```yaml
services:
  webapp:
    platform: linux/arm64
    extends:
      file: webapp/compose.yaml
      service: webapp
    depends_on:
      - cm33-runner
    build:
      args:
        EXECUTORCH_BASE_CACHE_IMAGE: ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04
        IMX93_RUNNER_BUILD_CACHE_IMAGE: ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04
```

The web app is privileged and mounts `/sys` and `/dev` because it checks the device tree, reads remoteproc state through `/sys/class/remoteproc`, talks to `/dev/ttyRPMSG*`, writes shared memory through `/dev/mem`, and checks for `/dev/ethosu0`.

Keep the web app build context in `webapp/compose.yaml`. The root `webapp.build.args` block supplies only Topo-collected build arguments. It shouldn't replace the extended build context and Dockerfile from `webapp/compose.yaml`.

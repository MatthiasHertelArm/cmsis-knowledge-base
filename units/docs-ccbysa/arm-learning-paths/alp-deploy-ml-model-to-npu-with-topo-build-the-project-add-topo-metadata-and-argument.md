---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-add-topo-metadata-and-argument"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: Add Topo metadata and argumen"
summary: "After the Compose services are complete, add the root-level x-topo block. Keep it at the root of compose.yaml, as a sibling of services, not under services."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#add-topo-metadata-and-arguments"
license: "CC-BY-SA-4.0"
mode: "V"
---

After the Compose services are complete, add the root-level `x-topo` block.
Keep it at the root of `compose.yaml`, as a sibling of `services`, not under `services`.

If you want to use an agent skill to perform this step, skip to the optional step.

```yaml
x-topo:
  name: "i.MX93 ExecuTorch runner"
  description: "Runs a Cortex-A web application that sends image inference commands to a resident CM33 ExecuTorch runner over RPMsg."
  features:
    - "remoteproc-runtime"
  parameters:
    EXECUTORCH_BASE_CACHE_IMAGE:
      description: Optional GHCR image used as a BuildKit cache source for the ExecuTorch PTE build.
      required: false
      default: ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04
    IMX93_RUNNER_BUILD_CACHE_IMAGE:
      description: Optional GHCR image used as a BuildKit cache source for the CM33 runner build.
      required: false
      default: ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04
```

The `features` value tells Topo that this project requires `remoteproc-runtime` support on the target. This is useful when checking for project compatibility with the `topo projects --target <target>` command.

The `parameters` entries describe configurable build inputs. Compose consumes those values through the `cache_from` interpolation that you added earlier:

```output
cache_from:
  - ${EXECUTORCH_BASE_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04}
```

The root `webapp.build.args` block also makes the Topo-provided values visible in the Compose build model while preserving the `webapp/` build context inherited through `extends`.

Keep runtime settings such as `WEBAPP_PORT` as normal Compose interpolation unless you intentionally want Topo to collect them as Topo Project setup arguments.

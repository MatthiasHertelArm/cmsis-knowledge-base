---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-add-the-executorch-artifact-pi"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: Add the ExecuTorch artifact p"
summary: "The web application needs an ExecuTorch .pte model, and the target needs a Cortex-M33 ELF image. Both artifacts are built by executorch-runner/Dockerfile."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#add-the-executorch-artifact-pipeline"
license: "CC-BY-SA-4.0"
mode: "V"
---

The web application needs an ExecuTorch `.pte` model, and the target needs a Cortex-M33 ELF image. Both artifacts are built by `executorch-runner/Dockerfile`.

Copy the Dockerfile into the runner build context:

```bash
cp ../topo-imx93-npu-deployment/executorch-runner/Dockerfile executorch-runner/
```

For this multi-stage Dockerfile:

- `build-base`: installs the common Ubuntu build tools.
- `executorch-base`: clones ExecuTorch, installs the Arm backend dependencies, and copies `export_mv2_imx93.py` and `docker-entrypoint.sh`.
- `pte-builder`: exports `mv2_ethosu65_256.pte`.
- `pte-artifacts`: packages the `.pte` file as a BuildKit artifact context.
- `runner-base`: installs the Arm GNU toolchain, MCUX SDK, RPMsg-Lite dependencies, runner sources, and local patches.
- `runner-builder`: builds `executorch_runner_cm33.elf`.
- `runner-artifacts`: packages the ELF for inspection or reuse.
- `runner-runtime`: produces a `scratch` image whose entrypoint is the ELF file.

The important artifact stages look like this:

```Dockerfile
FROM busybox:1.36 AS pte-artifacts
COPY --from=pte-builder /workspace/build/mv2-imx93/mv2_ethosu65_256.pte /artifacts/mv2_ethosu65_256.pte

FROM busybox:1.36 AS runner-artifacts
COPY --from=runner-builder /artifacts/executorch_runner_cm33.elf /artifacts/executorch_runner_cm33.elf

FROM scratch AS runner-runtime
COPY --from=runner-builder /artifacts/executorch_runner_cm33.elf /executorch_runner_cm33.elf
ENTRYPOINT ["/executorch_runner_cm33.elf"]
```

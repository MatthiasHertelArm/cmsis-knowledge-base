---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-validate-the-final-topo-projec"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: Validate the final Topo Proje"
summary: "Check the Compose model and check that the Topo metadata is present:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#validate-the-final-topo-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Check the Compose model and check that the Topo metadata is present:

```bash
docker compose config
```

In the `docker compose config` output, check that the resolved `webapp` service has:

- `build.context` ending in `/webapp`
- `build.dockerfile` set to `Dockerfile`
- `build.additional_contexts.pte_artifacts` set to `service:pte-artifacts`

Install `check-jsonschema` if it's not already available:


  **macOS:**
brew install check-jsonschema
  
  **Linux / WSL:**
sudo apt update
sudo apt install -y pipx
pipx ensurepath
pipx install check-jsonschema
export PATH="$HOME/.local/bin:$PATH"
  


Validate the root Compose file with the schema in the Topo Project specification:

```bash
check-jsonschema \
  --schemafile ../topo/docs/project-specification/schema/topo-project-specification.json \
  compose.yaml
```

Review these points:

- `compose.yaml` contains root-level `x-topo` metadata.
- `x-topo.features` includes `remoteproc-runtime`.
- non-remoteproc services set `platform: linux/arm64`.
- `pte-artifacts` and `runner-artifacts` use `scale: 0`.
- `cm33-runner` uses `runtime: io.containerd.remoteproc.v1`.
- `cm33-runner` has `remoteproc.name: imx-rproc`.
- `webapp` depends on `cm33-runner`.
- `webapp` imports the `.pte` file through `additional_contexts`.
- every `x-topo.parameters` entry is consumed by Compose interpolation.

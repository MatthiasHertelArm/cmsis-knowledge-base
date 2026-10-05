---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-create-the-repository-from-the"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: Create the repository from th"
summary: "Start by copying the original base projects from the Topo Project."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#create-the-repository-from-the-base-projects"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start by copying the original base projects from the Topo Project. 

Clone the Topo repository for the Topo Project specification and validation schema, clone the original Topo Project for the source files, and start a new empty repository:

```bash
git clone https://github.com/arm/topo.git
git clone https://github.com/Arm-Examples/topo-imx93-npu-deployment.git
mkdir new-topo-npu-template
cd new-topo-npu-template
```

Create the project layout:

```bash
mkdir -p webapp executorch-runner licenses
```

Copy the relevant `webapp` files:

```bash
cp -R ../topo-imx93-npu-deployment/webapp/src webapp
```

Copy the Cortex-M33 runner build inputs from the firmware project:

```bash
cp ../topo-imx93-npu-deployment/executorch-runner/build-runner.sh executorch-runner/build-runner.sh
cp ../topo-imx93-npu-deployment/executorch-runner/export_mv2_imx93.py executorch-runner/export_mv2_imx93.py
cp ../topo-imx93-npu-deployment/executorch-runner/docker-entrypoint.sh executorch-runner/docker-entrypoint.sh
cp -R ../topo-imx93-npu-deployment/executorch-runner/patches executorch-runner
```

Add the licenses and ignore rules used by the source projects:

```bash
cp ../topo-imx93-npu-deployment/LICENSE.md .
cp -R ../topo-imx93-npu-deployment/licenses .
cp ../topo-imx93-npu-deployment/.gitignore .
```

You have two sets of source code combined into one repository. It's not a Compose project and it's not a Topo Project. 

You'll now create a Compose project and Topo Project around the source code.

The Compose project provides the container build and runtime structure. A Dockerfile describes how to build one image. A Compose file describes the services that use those images, their build contexts, ports, volumes, dependencies, and runtime settings. In this Topo Project:

- `webapp/Dockerfile` builds the Flask image.
- `webapp/compose.yaml` keeps the web app's build context and Linux runtime settings close to the web app source.
- `executorch-runner/Dockerfile` builds the ExecuTorch `.pte` model and Cortex-M33 runner ELF through multi-stage Docker builds.
- the root `compose.yaml` is the Topo Project entry point. It combines the web app, artifact build services, the Remoteproc Runtime service, and the root-level `x-topo` metadata.

For a general introduction to Compose projects, services, and the `compose.yaml` file, see Docker's [How Compose works](https://docs.docker.com/compose/intro/compose-application-model/) documentation.

**Note:**
When you creating a file for any of the following steps, paste the complete file contents as shown.

When you update part of an existing Compose file for a step, merge the YAML into the existing top-level key shown by the snippet. For example, if a snippet starts with `services:`, add the named service under the existing top-level `services:` map. Don't create a second `services:` block in the same file.

---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-optional-use-an-agent-skill-to"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: (Optional) Use an Agent Skill"
summary: "Topo currently provides the following skills:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#optional-use-an-agent-skill-to-add-the-topo-metadata"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Topo](https://github.com/arm/topo) currently provides the following skills:

- `topo-project-context`: provides Topo and Topo Project reference context for questions about x-topo metadata, schema, docs, and CLI project behavior.
- `topo-project-bootstrap`: converts a repository into a Topo Project by adding or improving `compose.yaml` and `x-topo` metadata.
- `topo-project-lint`: reviews an existing Topo Project for correctness, consistency, and authoring best practices.
- `topo-project-optimize-deployment`: optimizes feedback loop by measuring and applying the highest-leverage Docker build improvement.

Install the skills with `npx skills`:

```bash
npx skills add arm/topo
```

If your agent doesn't use `npx skills`, manually copy or symlink the skill directories from Topo into your agent's skills directory.

Restart your agent after installing or updating the skills.

From the root of the Compose project, ask your agent to use `topo-project-bootstrap`:

```
Use topo-project-bootstrap on this repository.
Treat the root compose.yaml as the project root.
Preserve plain docker compose behavior.
Add x-topo metadata only where it reflects the actual services, hardware requirements, and build arguments.
```

After bootstrap, ask the agent to use `topo-project-lint`:

```
Use topo-project-lint on this repository.
Validate compose.yaml against the Topo Project specification schema.
Check README alignment, Remoteproc Runtime metadata, and x-topo.parameters wiring.
```

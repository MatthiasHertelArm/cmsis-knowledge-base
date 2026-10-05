---
id: "alp-observing-ethos-u-on-nxp-4-environment-setup-get-the-executorch-source-code"
type: "concept"
domain: "edge-ai"
title: "4 environment setup: Get the ExecuTorch source code"
summary: "Clone ExecuTorch and initialize its submodules:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/4-environment-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/4-environment-setup/#get-the-executorch-source-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

Clone ExecuTorch and initialize its submodules:

   ```bash
   git clone https://github.com/pytorch/executorch.git
   cd executorch
   git fetch --tags
   git checkout c70a742344e30158dc370d7d35d60ed07660fee0
   git submodule sync
   git submodule update --init --recursive
   ```

**EthosUCompileSpec parameters:**
The `EthosUCompileSpec` parameters used in this guide:

| Parameter         | Value                 | Description                                    |
| ----------------- | --------------------- | ---------------------------------------------- |
| `target`          | `ethos-u65-256`       | Targets the Ethos-U65 with 256 MAC units       |
| `system_config`   | `Ethos_U65_High_End`  | High-end system configuration for optimal performance |
| `memory_mode`     | `Shared_Sram`         | Uses shared SRAM memory mode                   |

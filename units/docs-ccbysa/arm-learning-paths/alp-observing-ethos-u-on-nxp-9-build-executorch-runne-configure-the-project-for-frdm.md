---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-configure-the-project-for-frdm"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: Configure the project for FRDM-MIMX93"
summary: "If the MCUXpresso extension doesn't automatically pick up the project, import it:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#configure-the-project-for-frdm-mimx93"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open the project in VS Code:

```bash
code .
```

If the MCUXpresso extension doesn't automatically pick up the project, import it:

1. Open the Command Palette
2. Run **MCUXpresso for VS Code: Import Project**
3. Select the `Executorch_runner_cm33` folder
4. When prompted, choose **Arm GNU Toolchain**

(figure: Import Project dialog showing project path, repository, and toolchain selection#center)

---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-update-the-solution-file"
type: "concept"
domain: "edge-ai"
title: "6 alif cmsis project: Update the solution file"
summary: "The alif.csolution.yml file describes the whole CMSIS workspace: available projects, targets, devices, packs, and flash settings."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#update-the-solution-file"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `alif.csolution.yml` file describes the whole CMSIS workspace: available projects, targets, devices, packs, and flash settings.

Open the file and make the following changes.

Update the `created-for` field to match your CMSIS Toolbox version:

```yaml
  created-for: CMSIS-Toolbox@2.12.0
```

Add the required packs under the `packs:` section:

```yaml
  packs:
    - pack: AlifSemiconductor::Ensemble@2.0.4
    - pack: ARM::CMSIS@6.0.0
    - pack: ARM::CMSIS-Compiler@2.1.0
    - pack: Keil::MDK-Middleware@8.2.0
    - pack: ARM::ethos-u-core-driver
```

Add a `target-set` block to the `E8-HP` target type so the Security Toolkit knows which binary to flash. Find the `type: E8-HP` section and add the following:

```yaml
    - type: E8-HP
      device: Alif Semiconductor::AE822FA0E5597LS0:M55_HP
      board: Alif Semiconductor::DevKit-E8
      define:
        - "CORE_M55_HP"
      target-set:
        - set:
          images:
            - project-context: mnist_executorch.debug
```

For all other target types (E7-HE, E7-HP, E1C-HE, E8-HE), add a `target-set` pointing to `blinky.debug` instead.

Add `mnist_executorch` to the projects list at the end of the file:

```yaml
  projects:
    - project: blinky/blinky.cproject.yml
    - project: hello/hello.cproject.yml
    - project: hello_rtt/hello_rtt.cproject.yml
    - project: mnist_executorch/mnist_executorch.cproject.yml
```

---
id: "alp-alif-image-classification-create-project-update-the-solution-file"
type: "concept"
domain: "edge-ai"
title: "create project: Update the solution file"
summary: "Open alif.csolution.yml and make the following changes."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/create-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/create-project/#update-the-solution-file"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open `alif.csolution.yml` and make the following changes.

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

Add a `target-set` block to the `E8-HP` target type so the Security Toolkit knows which binary to flash. Find the `type: E8-HP` section and add:

```yaml
    - type: E8-HP
      device: Alif Semiconductor::AE822FA0E5597LS0:M55_HP
      board: Alif Semiconductor::DevKit-E8
      define:
        - "CORE_M55_HP"
      target-set:
        - set:
          images:
            - project-context: mv2_runner.debug
```

For all other target types (E7-HE, E7-HP, E1C-HE, E8-HE), add a `target-set` pointing to `blinky.debug` instead.

Add `mv2_runner` to the projects list:

```yaml
  projects:
    - project: blinky/blinky.cproject.yml
    - project: hello/hello.cproject.yml
    - project: hello_rtt/hello_rtt.cproject.yml
    - project: mv2_runner/mv2_runner.cproject.yml
```

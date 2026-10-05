---
id: "alp-avh-matter-4cicdsh-follow-the-workflow-progress-i"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Manage development in a CI/CD workflow with Self-Hosted Runner: Follow the workflow progress in GitHub Actions"
summary: "The workflow does not output on the target, but rather logs to GitHub."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh/#follow-the-workflow-progress-in-github-actions"
license: "CC-BY-SA-4.0"
mode: "V"
---

The workflow does not output on the target, but rather logs to GitHub.

You can follow the workflow steps, and see the output logs in your GitHub repository, under the `Actions` tab.

After `lighting-app` is initialized, you can toggle the light with your `chip-tool` instance as before:
```console
./out/debug/chip-tool onoff on 0x11 1
./out/debug/chip-tool onoff off 0x11 1
```
Observer your new message in the `run_lighting_app` log, for example:
```output
[TIMESTAMP][INSTANCEID] CHIP:ZCL: HELLO WORLD! Toggle ep1 on/off from state 1 to 0
```
The workflow will cleanly terminate `lighting-app` after 120 seconds.

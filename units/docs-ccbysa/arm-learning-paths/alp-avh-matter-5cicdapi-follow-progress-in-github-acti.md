---
id: "alp-avh-matter-5cicdapi-follow-progress-in-github-acti"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Control Arm Virtual Hardware with API: Follow progress in GitHub Actions"
summary: "Navigate to the Actions tab of your GitHub repository, and open the current workflow to follow progress. Observe that there are now three jobs, with the jobs to run lighting-app and chip-tool executing in parallel."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/5cicdapi.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/5cicdapi/#follow-progress-in-github-actions"
license: "CC-BY-SA-4.0"
mode: "V"
---

Navigate to the `Actions` tab of your GitHub repository, and open the current workflow to follow progress. Observe that there are now three `jobs`, with the jobs to run `lighting-app` and `chip-tool` executing in parallel. You can follow progress in the GitHub Actions log, and observe `chip-tool` toggling `lighting-app` automatically. You'll also see the commands appear in the `chip-tool` console.

Congratulations! You've entirely automated the process to build and test your applications.

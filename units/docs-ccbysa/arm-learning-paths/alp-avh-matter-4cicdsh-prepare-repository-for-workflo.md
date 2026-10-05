---
id: "alp-avh-matter-4cicdsh-prepare-repository-for-workflo"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Manage development in a CI/CD workflow with Self-Hosted Runner: Prepare repository for workflows"
summary: "The Matter repository from where the examples are sourced contains many workflows for rebuilding different configurations. For convenience, remove these, and install only the new workflow."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh/#prepare-repository-for-workflows"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Matter repository from where the examples are sourced contains many workflows for rebuilding different configurations. For convenience, remove these, and install only the new workflow.

In the `lighting-app` console, navigate to the `.github/workflows` directory, and delete all.
```console
cd ~/connectedhomeip/.github/workflows
rm -rf *.yaml
rm -rf *.yml
ls
```
Create a `.yml` textfile, and copy the below to that file.
```yml
name: Matter_CICD_Demo

on:
  push:
  workflow_dispatch:

jobs:
  rebuild_lighting_app:
    runs-on: self-hosted
    steps:
     - uses: actions/checkout@v2
     
     - name: submodules
       run: ./scripts/checkout_submodules.py --shallow --platform linux
       
     - name: bootstrap and build
       run: |
         ./scripts/build/gn_bootstrap.sh
         source scripts/activate.sh
         git clone https://github.com/project-chip/zap.git ./zap
         cd ./zap
         sudo src-script/install-packages-ubuntu
         npm ci
         export ZAP_DEVELOPMENT_PATH=$PWD
         cd ../examples/lighting-app/linux
         gn gen out/debug
         ninja -C out/debug
         
  run_lighting_app:
    needs: rebuild_lighting_app
    runs-on: self-hosted
    steps:
      - name: Run lighting-app for 3 minutes
        run: |
          cd examples/lighting-app/linux
          timeout 180s ./out/debug/chip-lighting-app || code=$?; if [[ $code -ne 124 && $code -ne 0 ]]; then exit $code; fi
```

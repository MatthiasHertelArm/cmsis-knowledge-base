---
id: "csx-continuous-integration-ci-test-for-github-action-workflows"
type: "concept"
domain: "project"
title: "Continuous Integration (CI) test for csolution-examples: GitHub Action Workflows"
summary: "The GitHub Actions workflows in the directory .github/workflows run the CI tests. The examples use the Arm Compiler (AC6), GCC, and CLANG toolchains. The toolchains tested depend on the example."
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:.ci/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/.ci/README.md#github-action-workflows"
license: "Apache-2.0"
mode: "V"
---

The [**GitHub Actions**](https://docs.github.com/en/actions) workflows in the directory `.github/workflows` run the CI tests. The examples use the **Arm Compiler (AC6)**, **GCC**, and **CLANG** toolchains. The toolchains tested depend on the example.

- **`Hello-CI.yml`** builds and executes the Debug and Release variants with **AC6**, **GCC**, and **CLANG**. The execution tests run on an [Arm Virtual Hardware Fixed Virtual Platform (AVH FVP)](https://arm-software.github.io/AVH/main/simulation/html/index.html). The directory `FVP` contains the simulation model configuration.

- **`DualCore-CI.yml`** builds the dual-core Cortex-M0+ and Cortex-M4 project with **AC6**. The build output is stored as a downloadable artifact.

- **`SimpleTZ-CI.yml`** builds and executes the Debug and Release target sets of the TrustZone project with **AC6**. The execution tests run on an [Arm Virtual Hardware Fixed Virtual Platform (AVH FVP)](https://arm-software.github.io/AVH/main/simulation/html/index.html) using the configuration in the `FVP` directory.

- **`CubeMX-CI.yml`** builds the CubeMX-generated project with **AC6**.

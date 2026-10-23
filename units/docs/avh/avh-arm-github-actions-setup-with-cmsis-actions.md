---
id: "avh-arm-github-actions-setup-with-cmsis-actions"
type: "concept"
domain: "test"
title: "Arm GitHub Actions: Setup with CMSIS-Actions"
summary: "Arm provides several GitHub Actions that simplify installation of Arm FVPs and other Arm Tools within your GitHub CI workflows. The following actions are maintained in the cmsis-actions repository:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:DoxyGen/infrastructure/src/avh_gh_actions.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/infrastructure/src/avh_gh_actions.md#setup-with-cmsis-actions"
license: "Apache-2.0"
mode: "V"
---

Arm provides several GitHub Actions that simplify installation of Arm FVPs and other Arm Tools within your GitHub CI
workflows. The following actions are maintained in the [cmsis-actions](https://github.com/ARM-software/cmsis-actions)
repository:

- The **vcpkg** action performs the environment setup from Arm Tools Artifactory based on vcpkg configuration (refer to
  avh_fvp_vcpkg).

  The following step can be added to the workflow to execute this action:

 ```yml
 - name: Setup vcpkg environment
   uses: ARM-software/cmsis-actions/vcpkg@v1
   with:
     config: "./vcpkg-configuration.json"
     vcpkg-downloads: "${{ github.workspace }}/.vcpkg/downloads"
     cache: "-"
 ```

- The **armlm** action activates an Arm user based license (UBL) for Arm Tools on your GitHub Runner.

  For example, add the following step to your workflow to activate an MDK-Community license that allows evaluation and
  open-source usage of Arm Tools:

```yml
- name: Activate Arm license
  uses: ARM-software/cmsis-actions/armlm@v1
```

The activated environment is preserved into `$GITHUB_PATH` and `$GITHUB_ENV` so that it can be used by subsequent steps.

The actions execute on the GitHub Runner operations for vcpkg-based tool download and license activation as explained
in the avh_fvp_artifactory.

---
id: "avh-arm-github-actions-program-execution"
type: "concept"
domain: "test"
title: "Arm GitHub Actions: Program Execution"
summary: "After Arm FVPs and other tools are installed and activated on the GitHub Runner (see armcmsisactions), you can use the command line interface for building your project (e.g with cbuild utility) and run the firmware on an Arm …"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_gh_actions.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_gh_actions.md#program-execution"
license: "Apache-2.0"
mode: "V"
---

After Arm FVPs and other tools are installed and activated on the GitHub Runner (see arm_cmsis_actions), you can
use the command line interface for building your project (e.g with `cbuild` utility) and run the firmware on an Arm FVP
target (see [Running User Applications in CLI](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/using.html#Execution)).

For example, the code snippet below adds to a GitHub Actions workflow a step with program execution on Corstone-320 FVP
target:

```yml
name: Execute
        run: |
          echo "Running project example ..."
          FVP_Corstone_SSE-320 -f fvp_config.txt -a Project.axf | tee Project.avh.log
```

Also see [Execution in CI frameworks](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/hints.html#ci_frameworks) for useful hints about running
FVPs in CI workflows.

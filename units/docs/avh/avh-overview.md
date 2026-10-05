---
id: "avh-overview"
type: "concept"
domain: "test"
title: "Overview"
summary: "Following methods of accessing and using Arm FVPs are explained in this section:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/main.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/main.md"
license: "Apache-2.0"
mode: "V"
---

**Arm Virtual Hardware** provides a cloud-native infrastructure with
[FVP simulation models](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/../../simulation/html/index.html) and necessary software tooling. It integrates well into
various CI/CD and MLOps workflows ranging from GitHub to on-premise IT infrastructure.

Following methods of accessing and using Arm FVPs are explained in this section:

- avh_fvp_artifactory gives universal access to Arm FVP models that can be used in different workflows.
- avh_gh_actions simplifies use of Arm FVPs from Arm Tools Artifactory for building and testing embedded projects
  maintained in GitHub repositories.
- avh_desktop is useful for local development and program debugging.

(figure: Create, debug, and test)

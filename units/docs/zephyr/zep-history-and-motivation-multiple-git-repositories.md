---
id: "zep-history-and-motivation-multiple-git-repositories"
type: "concept"
domain: "project"
title: "History and Motivation: Multiple Git Repositories"
summary: "Zephyr intends to provide all required building blocks needed to deploy complex IoT applications. This in turn means that the Zephyr project is much more than an RTOS kernel, and is instead a collection of components that work together."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/why.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/why.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr intends to provide all required building blocks needed to deploy complex
IoT applications. This in turn means that the Zephyr project is much more than
an RTOS kernel, and is instead a collection of components that work together.
In this context, there are a few reasons to work with multiple Git
repositories in a standardized manner within the project:

* Clean separation of Zephyr original code and imported projects and libraries
* Avoidance of license incompatibilities between original and imported code
* Reduction in size and scope of the core Zephyr codebase, with additional
  repositories containing optional components instead of being imported
  directly into the tree
* Safety and security certifications
* Enforcement of modularization of the components
* Out-of-tree development based on subsets of the supported boards and SoCs

See west-basics for information on how west workspaces manage multiple
git repositories.

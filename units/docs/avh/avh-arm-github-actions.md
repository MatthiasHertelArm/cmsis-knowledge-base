---
id: "avh-arm-github-actions"
type: "concept"
domain: "test"
title: "Arm GitHub Actions"
summary: "GitHub Actions allow you to automate build, test, and deployment pipelines for GitHub-based projects."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:DoxyGen/infrastructure/src/avh_gh_actions.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/infrastructure/src/avh_gh_actions.md"
license: "Apache-2.0"
mode: "V"
---

GitHub Actions allow you to automate build, test, and deployment pipelines for GitHub-based projects.

A GitHub Actions workflow executes your commands on a virtual machine (GitHub Runner) that is hosted either directly by
GitHub or can be self-hosted. It is event-driven, meaning that you can run a series of commands on a specified event
such as push of a new commit or creation of a pull request. Refer to
[Introduction to GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions)
for information about the components of GitHub Actions.

This section explains how to setup your GitHub Actions environment for executing programs on Arm FVPs.

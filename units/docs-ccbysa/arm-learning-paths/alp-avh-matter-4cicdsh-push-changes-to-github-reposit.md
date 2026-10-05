---
id: "alp-avh-matter-4cicdsh-push-changes-to-github-reposit"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Manage development in a CI/CD workflow with Self-Hosted Runner: Push changes to GitHub repository and invoke workf"
summary: "The workflow contains the below, which tells GitHub to invoke this workflow whenever there's a push to the repository."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh/#push-changes-to-github-repository-and-invoke-workflow"
license: "CC-BY-SA-4.0"
mode: "V"
---

The workflow contains the below, which tells GitHub to invoke this workflow whenever there's a `push` to the repository.
```yml
on:
  push:
```
To push the changes, in `lighting-app` console, first enter your GitHub credentials.
```console
git config --global user.name "YOUR_GITHUB_USERNAME"
git config --global user.email YOUR_EMAIL_ADDRESS
```
Ensure you are pushing these changes to your personal forked repository.
```console
git remote -v 
```
Commit the changes to your repository.
```console
cd ~/connectedhomeip
git add .
git commit -m "delete other workflows, update output message"
git push
```
You'll be prompted for your GitHub username and `Personal Access Token` (password).

The workflow contains two `jobs`, which rebuild, and then run `lighting-app`:
```yml
jobs:
  rebuild_lighting_app:
...
  run_lighting_app:
```
Note that `rebuild_lighting_app` will take a few minutes to complete, as it must repeat all the initialization steps for the Matter build system.

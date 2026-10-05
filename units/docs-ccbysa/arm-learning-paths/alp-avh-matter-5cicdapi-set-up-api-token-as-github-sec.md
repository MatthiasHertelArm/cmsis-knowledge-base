---
id: "alp-avh-matter-5cicdapi-set-up-api-token-as-github-sec"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Control Arm Virtual Hardware with API: Set up API Token as GitHub secret"
summary: "In either Arm Virtual Hardware browser, navigate to Profile > API."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/5cicdapi.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/5cicdapi/#set-up-api-token-as-github-secret"
license: "CC-BY-SA-4.0"
mode: "V"
---

In either `Arm Virtual Hardware` browser, navigate to `Profile` > `API`.

Generate and copy your `API Token`. This is a unique key that enables remote access to your instance(s).

In the GitHub browser, go to your forked repository, and navigate to `Settings` > `Secrets` > `Actions`.

Create a `New repository secret`. Name the secret:
```console
API_TOKEN
```
Paste the above `API Token` as the secret value.

The secret name must be exactly `API_TOKEN`, as this is used by the workflow later.

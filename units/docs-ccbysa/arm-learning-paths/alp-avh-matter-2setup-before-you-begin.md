---
id: "alp-avh-matter-2setup-before-you-begin"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Prepare AVH instances of Raspberry Pi 4: Before you begin"
summary: "You need a user account for Arm Virtual Hardware 3rd Party Hardware. Refer to the Arm Virtual Hardware install guide for more information."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/2setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/2setup/#before-you-begin"
license: "CC-BY-SA-4.0"
mode: "V"
---

You need a user account for [Arm Virtual Hardware 3rd Party Hardware](https://avh.arm.com/). Refer to the [Arm Virtual Hardware install guide](https://learn.arm.com/install-guides/avh/#thirdparty) for more information.

A [GitHub](https://github.com) account is also required.

GitHub requires that a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) be set. If you don't have this on your account already, navigate to `Settings` > `Developer Settings` > `Personal Access Tokens`, click on `Generate new token`, and save the token locally.

Ensure you have enabled the token to `Update GitHub Action workflows`.

You may wish to create a local scratch pad text file containing the below details (which will be unique to you), so that you can easily copy and paste from.

```
YOUR_GITHUB_USERNAME
YOUR_PERSONAL_ACCESS_TOKEN
git config --global user.name "YOUR_GITHUB_USERNAME"
git config --global user.email YOUR_EMAIL_ADDRESS
```

---
id: "mbedtls-mbed-tls-ci-dco"
type: "concept"
domain: "security"
title: "Mbed TLS CI: DCO"
summary: "This job checks that all commits have a Signed-off-by: line."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/testing-ci.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-ci.md#dco"
license: "Apache-2.0"
mode: "V"
---

This job checks that all commits have a `Signed-off-by:` line. The presence of this line indicates that the author of the commit certifies that the commit is covered by the [Developer Certificate of Origin](https://github.com/Mbed-TLS/mbedtls/blob/development/dco.txt) and contributed according to the [project license](https://github.com/Mbed-TLS/mbedtls/blob/development/README.md#License).

All commits must have such a line, otherwise the commit cannot be accepted for legal reasons. For Arm employees or other contributors who already have a contributor license agreement (CLA), we can legally accept contributions without a DCO, however depending on the repository it may be technically impossible to merge a pull request with a failed DCO check.

If the DCO job fails, please reword all commit messages that are missing a `Signed-off-by:` line. If you have multiple commit messages to rewrite, [How to use git interactive rebase for signing off a series of commits](https://stackoverflow.com/questions/25570947/how-to-use-git-interactive-rebase-for-signing-off-a-series-of-commits) may help.

### Retrying a stuck DCO check

GitHub triggers a DCO check whenever a pull request is updated. This check is required: a pull request cannot be merged unless it passes.

If the DCO check doesn't report back to GitHub (the status remains “Pending” and no “Details” link appears), the only known solution is to change the commit ID at the head of the pull request. You can amend the head commit without changing its commit message: this changes the commit date, so it changes the commit ID. Force-pushing such an amended commit triggers all new CI checks, but does not invalidate review approvals.

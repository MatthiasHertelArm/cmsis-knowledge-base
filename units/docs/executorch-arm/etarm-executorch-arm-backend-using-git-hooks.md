---
id: "etarm-executorch-arm-backend-using-git-hooks"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend: Using git hooks"
summary: "The repo-wide pre-commit hook (lintrunner + torch_pin sync) is installed automatically by ./install_executorch.sh. To install the Arm-specific pre-push hook (license checks, commit message format, docgen):"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/backends/arm/README.md#using-git-hooks"
license: "BSD-3-Clause"
mode: "V"
---

The repo-wide pre-commit hook (lintrunner + torch_pin sync) is installed automatically
by `./install_executorch.sh`. To install the Arm-specific pre-push hook (license checks,
commit message format, docgen):

```
cp backends/arm/scripts/pre-push .git/hooks/
```

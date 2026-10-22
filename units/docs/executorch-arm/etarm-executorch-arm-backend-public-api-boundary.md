---
id: "etarm-executorch-arm-backend-public-api-boundary"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend: Public API Boundary"
summary: "The Arm backend public Python API is the set of symbols tracked in backends/arm/public_api_manifests/api_manifest_running.toml. Other modules, helpers, scripts, and directory layouts in this subtree are implementation details and may change without deprecation."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/backends/arm/README.md#public-api-boundary"
license: "BSD-3-Clause"
mode: "V"
---

The Arm backend public Python API is the set of symbols tracked in
`backends/arm/public_api_manifests/api_manifest_running.toml`. Other modules,
helpers, scripts, and directory layouts in this subtree are implementation
details and may change without deprecation.

In particular, `backends/arm/tosa` contains shared lowering implementation for
Arm backends. It is not a stable public package except for symbols explicitly
listed in the public API manifest. Prefer the target-specific public APIs in
`executorch.backends.arm.ethosu` and `executorch.backends.arm.vgf` for
application code.

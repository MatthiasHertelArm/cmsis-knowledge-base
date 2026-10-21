---
id: "x-fvp-debug-setup-3"
type: "troubleshooting"
domain: "debug"
title: "Arm FVP license refused inside a Docker container"
status: "draft"
symptoms: ["Fatal: license error: The license found is assigned to another user."]
extracted_from: "proc-fvp-debug-setup"
source: "fvp-debug-setup/SKILL.md"
license: "Apache-2.0"
---

The container must run as the **host user name and uid** (`groupadd`/`useradd` from build args), with `~/.armlm` mounted and `ARMLM_CACHED_LICENSES_LOCATION` set — the Arm user-based license is bound to the account that activated it, otherwise: `Fatal: license error: The license found is assigned to another user.`

---
id: "x-fvp-debug-setup-4"
type: "concept"
domain: "debug"
title: "No macOS build of the Arm FVP"
status: "draft"
extracted_from: "proc-fvp-debug-setup"
source: "fvp-debug-setup/SKILL.md"
---

**Host support.** The artifact has demands for `windows and x64`, `linux and x64`, `linux and arm64` — **no darwin**. On macOS `vcpkg activate` silently installs nothing (you get an artifact dir containing only `artifact.json`), so the model has to run in Docker. Check `docker info` there.

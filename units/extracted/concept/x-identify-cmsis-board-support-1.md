---
id: "x-identify-cmsis-board-support-1"
type: "concept"
domain: "project"
title: "Installed-pack queries are supporting evidence only"
status: "draft"
extracted_from: "proc-identify-cmsis-board-support"
source: "project/identify-cmsis-board-support/SKILL.md"
---

When the CMSIS-Toolbox environment is active, cross-check installed packs with `csolution list boards --filter <terms>` or `csolution list devices --filter <terms>`. Installed-pack results are supporting evidence only: they may be a subset of the online catalog and therefore cannot establish uniqueness or eliminate other candidates. An empty local result does not prove that the online catalog lacks a BSP or DFP.

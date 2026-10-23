---
id: "cda-cmsis-developer-assistant-tool-con"
type: "concept"
domain: "debug"
title: "CMSIS Developer Assistant tool contract"
summary: "The rules that keep agents on the MCP tools instead of pyOCD, GDB, cbuild or a serial terminal in the shell, and the shell commands with the tool that replaces each (#50)."
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/tool-contract.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/tool-contract.md"
license: "Apache-2.0"
mode: "V"
---

The rules that keep agents on the MCP tools instead of pyOCD, GDB, cbuild or a
serial terminal in the shell, and the shell commands with the tool that
replaces each (#50). This file is the only place they are written:

- The MCP server starts its `instructions` with the rules block.
- `npm run skills:sync -- --offline` copies the blocks between their markers
  into the bundled skills `cmsis-debug-live`, `cmsis-pack-docs`,
  `add-board-layer` and `cmsis-help`, and into `debug_instructions.md`.
  `src/test/toolContract.test.ts` fails when a copy differs.
- *Configure Agent* offers to write the rules block into the
  agents' rule files (`CLAUDE.md`, `AGENTS.md`, …), each change previewed,
  and activation brings the blocks it wrote up to date
  (`src/core/agentRules.ts`).

Edit the text between the markers here, then run that command. The rules
stay at ten lines and under 1 600 bytes: clients keep them in every turn.

<!-- cmsis-developer-assistant:rules:begin -->

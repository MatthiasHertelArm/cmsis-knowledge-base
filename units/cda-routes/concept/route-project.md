---
type: "concept"
domain: "project"
title: "CMSIS project setup: which procedure"
summary: "Create, extend or retarget CMSIS csolution and Zephyr projects: which procedure fits a task, and the usual order."
triggers: ["Set up and extend CMSIS csolution projects and Zephyr-based CMSIS solutions: verify the CMSIS-Toolbox, CMake, Ninja and compiler environment or a Zephyr west workspace; resolve a fuzzy board or device name to its exact CMSIS identity and BSP/DFP, or to its Zephyr board target; add a verified target to an existing *.csolution.yml; find compatible packaged board layers; or create an initial west-integrated CMSIS Zephyr Blinky solution. Use when the user wants to create, extend or retarget a csolution, check their build tools, or identify board, device and pack identifiers; it routes to the specialised project procedures of the knowledge index. Not for debugging a running target (cmsis-debug-live) or for PDSC authoring (cmsis-pack)."]
status: "draft"
source: "CMSIS-Developer-Assistant/scripts/skills.config.json"
license: "Apache-2.0"
id: "route-project"
references: ["proc-add-board-layer", "proc-add-cmsis-target", "proc-check-cmsis-environment", "proc-check-zephyr-environment", "proc-cmsis-bootstrap", "proc-cmsis-debugger-setup", "proc-identify-cmsis-board-layer", "proc-identify-cmsis-board-support", "proc-identify-zephyr-board", "proc-start-cmsis-project", "proc-start-zephyr-project"]
---

# CMSIS project setup: which procedure

Read the procedure with `knowledge_get` before acting on it, and follow its own prerequisites and guardrails. A `$name` inside a procedure is the procedure `proc-<name>`.

| If the task is to … | Procedure |
|---|---|
| Add a board layer to an existing csolution by asking for the few open decisions, then build it | `proc-add-board-layer` |
| Add a verified board or device target to an existing CMSIS solution, declare its support packs, and offer compatible packaged board layers when the project uses them. | `proc-add-cmsis-target` |
| Verify the CMSIS tools environment exported by the CMSIS Solution extension, CMSIS-Toolbox, CMake, Ninja, and available compiler toolchains, and return a `PASS` or `FAIL` report without installing or reconfiguring tools. | `proc-check-cmsis-environment` |
| Verify an existing Zephyr workspace, its Python virtual environment, and the venv-local west installation, returning a `PASS` or `FAIL` report without installing, upgrading, repairing, or reconfiguring Zephyr, Python, or west. | `proc-check-zephyr-environment` |
| Go from an empty VS Code window to a CMSIS solution that builds and debugs | `proc-cmsis-bootstrap` |
| Wire the debug adapter of a csolution target and verify Load & Debug | `proc-cmsis-debugger-setup` |
| Identify packaged CMSIS board layers compatible with an existing solution target and its required connections, returning `MATCHES`, `NO MATCH`, or `NOT REQUIRED` with exact command evidence. | `proc-identify-cmsis-board-layer` |
| Resolve a supplied board or device to exactly one verified CMSIS identity, identify its BSP or DFP, and ask the user when multiple candidates remain. | `proc-identify-cmsis-board-support` |
| Resolve a user-supplied physical board to its exact Zephyr board target and fitted MCU or SoC using the installed west board catalog. | `proc-identify-zephyr-board` |
| Create the first csolution for a board or device: a minimal project, or an example or template of its pack | `proc-start-cmsis-project` |
| Create and validate one initial west-integrated CMSIS Zephyr Blinky solution for a board already supported by Zephyr, from verified environment, board, and pack information, using `cbuild setup` and `cbuild`. | `proc-start-zephyr-project` |

## Typical order

1. No folder open or no solution yet: `proc-cmsis-bootstrap` first; it opens or creates the project folder and hands over to `proc-start-cmsis-project`, which writes a minimal project (CMSIS CORE, the DFP's startup, a bare `main`; Arm Compiler 6 unless the user prefers another compiler) or copies an example of the board's pack, then builds it with `cmsis_action build`.
2. `proc-check-cmsis-environment` (or `proc-check-zephyr-environment`) to confirm the toolchain before anything is created or built.
3. `proc-identify-cmsis-board-support` (or `proc-identify-zephyr-board`) to resolve the hardware to exactly one verified identity and its BSP/DFP.
4. `proc-add-cmsis-target` to extend the solution, then `proc-identify-cmsis-board-layer` for a packaged board layer — or `proc-start-zephyr-project` for a new west-integrated solution.
5. `proc-add-board-layer` when no packaged layer fits: interview for the few open decisions, then author Board.clayer.yml with its startup, stdio and memory files — or integrate the DFP's configuration generator — and build to green.
6. `proc-cmsis-debugger-setup` once the solution builds: set the debug adapter of the target set, let the CMSIS Solution extension write launch.json, and verify Load & Debug on the target.

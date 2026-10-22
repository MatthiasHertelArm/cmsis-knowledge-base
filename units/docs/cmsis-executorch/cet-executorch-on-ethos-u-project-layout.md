---
id: "cet-executorch-on-ethos-u-project-layout"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: Project layout"
summary: "ExecuTorch on Ethos-U: Project layout"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#project-layout"
license: "Apache-2.0"
mode: "V"
---

| Path | Purpose |
| ------ | --------- |
| `cmsis-executorch.csolution.yml` | Corstone-320 / Ethos-U85 solution and MLOps configuration |
| `cmsis-executorch-u55.csolution.yml` | Corstone-300 / Ethos-U55-128 solution and MLOps configuration |
| `cmsis-executorch.cproject.yml` | Application project: sources plus the Board and AI layers |
| `model/model.py` | Starter TinyCNN ML model |
| `create_ai_layer.py` | Exports the ML model for the target and writes the AI layer |
| `ai_layer/` | Generated: component selection and the embedded ML model data |
| `setup_venv.py` (`.sh` / `.bat`) | Creates the Python environment for the export |
| `.vscode.d/tasks.json` | The VS Code tasks (venv setup, Create AI layer) merged by the CMSIS Solution extension |
| `.vscode/fvp.sh`, `.vscode/fvp.Dockerfile`, `.vscode/launch.json.mac` | macOS only: runs the FVP in Docker, and the debug configuration that waits for it |
| `board/Corstone-300/`, `board/Corstone-320/` | Platform support and FVP configurations |
| `src/app_main.cpp` | Loads the ML model, runs inference, and prints the result; pool sizes overridable with `APP_METHOD_POOL_SIZE`, `APP_TEMP_POOL_SIZE`, `APP_POOL_SECTION` |
| `src/arm_embedded_module.*` | `EmbeddedModule`: ExecuTorch's `Module` class without the POSIX file loading (BSD-3-Clause, `src/LICENSE-ExecuTorch`) |
| `documentation/mlops-flow.md` | The MLOps flow in detail |
| `documentation/executorch-pack-maintenance.md` | Where the ExecuTorch pack comes from, how to update it |

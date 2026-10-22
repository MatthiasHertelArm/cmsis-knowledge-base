---
id: "dbgx-component-viewer-architecture-diagrams"
type: "concept"
domain: "debug"
title: "Component Viewer — Architecture: Diagrams"
summary: "The remaining draw.io files cover individual subsystems in more detail."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:docs/component-viewer/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/README.md#diagrams"
license: "Apache-2.0"
mode: "V"
---

The remaining draw.io files cover individual subsystems in more detail.

| Diagram | Description |
| --------- | ------------- |
| [architecture.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/architecture.png) | High level overview. |
| [all-subsystems.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/all-subsystems.drawio) | Single-canvas overview of all subsystems and their connections. |
| [instance.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/instance.drawio) | Detail of `ComponentViewerInstance`: `readModel()` and `update()` call paths. |
| [scvd-model.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/scvd-model.drawio) | Class hierarchy of the SCVD model (`model/`). |
| [statement-engine.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/statement-engine.drawio) | Statement Engine internals and statement type hierarchy. |
| [evaluation-layer.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/evaluation-layer.drawio) | Evaluation layer: eval context, eval interface, parser/evaluator pipeline. |
| [data-host-caches.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/data-host-caches.drawio) | Data hosts and caching strategy (memory, registers, symbols). |
| [scvd-gui-tree.drawio](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/docs/component-viewer/scvd-gui-tree.drawio) | `ScvdGuiTree` node structure and `ScvdGuiInterface` contract. |

*Note: Program is avaliable here: https://www.drawio.com/ or as VS Code extension.*

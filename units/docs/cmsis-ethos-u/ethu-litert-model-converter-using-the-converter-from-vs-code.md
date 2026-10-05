---
id: "ethu-litert-model-converter-using-the-converter-from-vs-code"
type: "concept"
domain: "edge-ai"
title: "LiteRT model converter: Using the converter from VS Code"
summary: "The example contains a .vscode.d/tasks.json drop-in for the CMSIS Solution extension. After opening or updating the solution, run Tasks: Run Task from the Command Palette and select Convert LiteRT models."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/script/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/script/README.md#using-the-converter-from-vs-code"
license: "Apache-2.0"
mode: "V"
---

The example contains a `.vscode.d/tasks.json` drop-in for the CMSIS Solution
extension. After opening or updating the solution, run **Tasks: Run Task** from
the Command Palette and select **Convert LiteRT models**. Choose the generated
MLOps configuration for U55, U65, or U85 when prompted.

If the task is not visible yet, run **Update Debug Tasks and Launch
Configurations** from the Command Palette. The extension merges the drop-in
task into the generated workspace `.vscode/tasks.json` file.

Generate the selected `*.cbuild-mlops.yml` file by setting up or building the
corresponding solution before running the conversion task.

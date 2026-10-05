---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-duplicate-an-existing-blinky-p"
type: "concept"
domain: "edge-ai"
title: "6 alif cmsis project: Duplicate an existing Blinky project"
summary: "Start by copying a working Blinky project as a template, and renaming the project file inside the new directory:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#duplicate-an-existing-blinky-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start by copying a working Blinky project as a template, and renaming the project file inside the new directory:


  **macOS and Linux:**
cd ~/mnist_alif/alif_vscode-template
cp -R blinky/ mnist_executorch
mv mnist_executorch/blinky.cproject.yml mnist_executorch/mnist_executorch.cproject.yml
  

  **Windows (PowerShell):**
cd ~\mnist_alif\alif_vscode-template
Copy-Item .\blinky .\mnist_executorch -Recurse
Rename-Item .\mnist_executorch\blinky.cproject.yml mnist_executorch.cproject.yml
  


Next, replace all internal references from `blinky` to `mnist_executorch`:

  **macOS and Linux:**
perl -pi -e 's/\bblinky\b/mnist_executorch/g' $(grep -RIl "blinky" mnist_executorch)
  

  **Windows (PowerShell):**
Get-ChildItem .\mnist_executorch -Recurse -File | Where-Object { Select-String -Path $_.FullName -Pattern '\bblinky\b' -Quiet } | ForEach-Object { $text = Get-Content $_.FullName -Raw; $text = $text -replace '\bblinky\b', 'mnist_executorch'; Set-Content $_.FullName $text -NoNewline }

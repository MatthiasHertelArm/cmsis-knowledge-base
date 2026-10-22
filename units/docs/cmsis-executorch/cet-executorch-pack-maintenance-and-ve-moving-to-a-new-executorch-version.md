---
id: "cet-executorch-pack-maintenance-and-ve-moving-to-a-new-executorch-version"
type: "concept"
domain: "pack"
title: "ExecuTorch pack maintenance and versioning: Moving to a new ExecuTorch version"
summary: "The pack's C++ runtime and the Python exporter must come from the same ExecuTorch version — a .pte produced by a different version than the runtime that loads it will fail at load time, or worse, at inference time."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/executorch-pack-maintenance.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/executorch-pack-maintenance.md#moving-to-a-new-executorch-version"
license: "Apache-2.0"
mode: "V"
---

The pack's C++ runtime and the Python exporter must come from the *same*
ExecuTorch version — a `.pte` produced by a different version than the runtime
that loads it will fail at load time, or worse, at inference time. Four steps,
in order:

1. **Install the new pack** — `cpackget add PyTorch::ExecuTorch@<new>`, or
   build one yourself (above) if the version is not published.
2. **Update both pins** — `PyTorch::ExecuTorch@<new>` in the csolution and in
   the cproject.
3. **Update the Python pins**: `executorch`, `torch` and `torchao` in
   `requirements.txt`, following the new release's `torch_pin.py` and
   `install_requirements.py`;
   `requirements-arm-tosa.txt` (the TOSA serializer and its flatbuffers pin)
   only changes when the Arm backend's `requirements-arm-tosa.txt` does.
4. **Rebuild the venv, the AI layer and the project:**

   ```bash
   ./setup_venv.sh --recreate
   cbuild setup cmsis-executorch.csolution.yml --active SSE-320-U85 --packs
   python3 create_ai_layer.py cmsis-executorch.cbuild-mlops.yml
   cbuild cmsis-executorch.csolution.yml --active SSE-320-U85
   ```

   A changed operator set simply shows up in the regenerated
   `ai_layer/ai_layer.clayer.yml`.

Finally, update the version wherever it appears in prose: the README
(Prerequisites and the pack-version note), the csolution header comment and
this page.

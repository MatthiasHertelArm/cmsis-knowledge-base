---
id: "cet-executorch-pack-maintenance-and-ve-where-it-comes-from"
type: "concept"
domain: "pack"
title: "ExecuTorch pack maintenance and versioning: Where it comes from"
summary: "The pack is published as an asset of the matching ExecuTorch GitHub release, which is also what its .pdsc declares as its download location:"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/executorch-pack-maintenance.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/executorch-pack-maintenance.md#where-it-comes-from"
license: "Apache-2.0"
mode: "V"
---

The pack is published as an asset of the matching ExecuTorch GitHub release,
which is also what its `.pdsc` declares as its download location:

```xml
<url>https://github.com/pytorch/executorch/releases/download/v1.5.1/</url>
```

So the normal acquisition routes work, and `cbuild setup ... --packs` takes
care of it on a fresh clone. To install it by hand:

```bash
cpackget add PyTorch::ExecuTorch@1.5.1
```

The version is pinned exactly, in `cmsis-executorch.csolution.yml` and
`cmsis-executorch.cproject.yml`:

```yaml
packs:
  - pack: PyTorch::ExecuTorch@1.5.1
```

Both must agree. The pin is exact rather than a `@^1.5.1` range because the
pack's C++ runtime and the Python exporter have to be the *same* ExecuTorch
version — see [Moving to a new ExecuTorch version](#moving-to-a-new-executorch-version).

`create_ai_layer.py` reads the installed pack's `.pdsc` out of the pack root
(`$CMSIS_PACK_ROOT`, or cpackget's default) to find out which operator
components exist. It reads the version `cbuild setup` resolved, taken from
`cmsis-executorch.cbuild-pack.yml`, so a pack root holding several
ExecuTorch versions cannot make it read the wrong one.

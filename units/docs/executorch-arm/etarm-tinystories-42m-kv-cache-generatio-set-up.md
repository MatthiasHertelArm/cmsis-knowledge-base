---
id: "etarm-tinystories-42m-kv-cache-generatio-set-up"
type: "concept"
domain: "edge-ai"
title: "TinyStories-42M KV-cache generation on Ethos-U85: Set up"
summary: "The checkpoint is available from https://huggingface.co/karpathy/tinyllamas/resolve/main/stories42M.pt. Set TINYSTORIES42M_ARTIFACT_DIR when the files live elsewhere."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/tinystories42m_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/tinystories42m_example_ethos_u/README.md#set-up"
license: "BSD-3-Clause"
mode: "V"
---

From the ExecuTorch repository root:

```bash
source ../optimum-executorch/.venv_et/bin/activate
source examples/arm/arm-scratch/setup_path.sh

export CC=/usr/bin/gcc-12
export CXX=/usr/bin/g++-12
export CUDAHOSTCXX="${CXX}"
```

Place these files in one directory:

```text
data/tinystories42m/stories42M.pt
data/tinystories42m/params.json
data/tinystories42m/tokenizer.model
```

The checkpoint is available from
`https://huggingface.co/karpathy/tinyllamas/resolve/main/stories42M.pt`.
Set `TINYSTORIES42M_ARTIFACT_DIR` when the files live elsewhere.

Use these parameters for the 42M checkpoint:

```json
{
  "dim": 512,
  "multiple_of": 32,
  "n_heads": 8,
  "n_kv_heads": 8,
  "n_layers": 8,
  "norm_eps": 1e-05,
  "vocab_size": 32000
}
```

---
id: "etarm-executorch-arm-backend-building"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend: Building"
summary: "The Arm backend can be built using the following command:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/backends/arm/README.md#building"
license: "BSD-3-Clause"
mode: "V"
---

The Arm backend can be built using the following command:

```
./install_executorch.sh
```

**NOTE:** While developing, it can be convenient to use `./install_executorch.sh --editable`, which creates an editable installation of ExecuTorch.

### Target-specific setup and build

Pick one of the target flows below. Each flow has a one-time setup step and a build command.

### Baremetal (Ethos-U) workflow

Builds ExecuTorch runtime libraries for Cortex-M with Ethos-U acceleration.

Setup:

```
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

Build:

```
./backends/arm/scripts/build_executorch.sh
```

### VGF (Vulkan ML extensions) workflow

Setup:

```
./examples/arm/setup.sh --disable-ethos-u-deps --enable-mlsdk-deps
```

This is the default setup path and installs the MLSDK components from pip.
Developers who need local source builds can use:

```
./backends/arm/scripts/setup-mlsdk-from-source.sh
```

The current flow lowers to TOSA and converts to VGF for use in external projects,
so the `executor_runner` is not typically used here.

### Compiling models with the Python API

Use the Python API as the primary way to compile your own models. It lets you
keep model construction, export inputs, quantization, custom passes, and artifact
generation in your application code. The `aot_arm_compiler.py` script is useful
for simple examples and smoke tests, but production code should call the
ExecuTorch and Arm backend APIs directly.

The delegated Python API flow is:

1. Prepare the model and representative example inputs.
2. Create a target-specific Arm compile spec.
3. Export the model with `torch.export.export`.
4. Optionally quantize with the target-specific Arm quantizer and re-export the
   quantized graph.
5. Create the matching Arm partitioner from the compile spec.
6. Lower with `to_edge_transform_and_lower`.
7. Convert to an ExecuTorch program and save the PTE file.

For complete examples of that flow, including quantization and target-specific
compile specs, see:

- [Arm Ethos-U tutorial](https://github.com/pytorch/executorch/blob/6368414/backends/arm/../../docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md)
- [Arm VGF tutorial](https://github.com/pytorch/executorch/blob/6368414/backends/arm/../../docs/source/backends/arm-vgf/tutorials/vgf-getting-started.md)
- [Arm Cortex-M backend overview](https://github.com/pytorch/executorch/blob/6368414/backends/arm/../../docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md)
- [Ethos-U porting guide](https://github.com/pytorch/executorch/blob/6368414/backends/arm/../../examples/arm/ethos-u-porting-guide.md)

Additional examples are available in `examples/arm`.

#### Fast model operator-support pre-check

For a quick pre-backend operator-list comparison before running the full Arm
export and backend toolchain, use `backends/arm/scripts/check_model_support.py`.
The script exports the model to ATen and compares operators visible in the
`torch.export` graph with the generated support table committed in the
**current checkout**.

It uses the same external-model convention as `aot_arm_compiler.py`: the model
file defines `ModelUnderTest` and `ModelInputs`, with optional `ModelKwargs`.
Choose the backend with `--backend vgf`, `--backend u55`, or `--backend u85`:

```bash
python backends/arm/scripts/check_model_support.py \
  --backend u85 \
  --model examples/arm/example_modules/add.py
```

The backend tables used by the checker are:

- VGF: `docs/source/backends/arm-vgf/VGF_op_support.md`
- Ethos-U55: `docs/source/backends/arm-ethos-u/U55_op_support.md`
- Ethos-U85: `docs/source/backends/arm-ethos-u/U85_op_support.md`

A small demo deliberately combines table-matched operators with `torch.sort`,
which is not in these support lists at the time the example is added:

```bash
python backends/arm/scripts/check_model_support.py \
  --backend u85 \
  --model backends/arm/scripts/examples/fast_model_support_demo.py
```

The expected result is inconclusive rather than a hard backend rejection:

```text
Unmatched pre-backend export operators (1):
  - torch.sort [torch.ops.aten.sort.default]

Result: INCONCLUSIVE
```

**Important:** A `PASS` only means that no operator-list gap was found in the
pre-backend export graph. It does **not** guarantee that the model is supported
end to end: the fast checker does not validate shapes, ranks, dtypes,
quantization configuration, operator attributes, partitioning constraints,
backend compiler constraints, memory requirements, or runtime behavior.

`INCONCLUSIVE` means that one or more operators visible in the pre-backend
`torch.export` graph are absent from the generated support table. This is not a
definitive unsupported result because normal ExecuTorch/Arm lowering may
decompose, rewrite, canonicalize, or remove those operators before backend
support checking. Known export-only infrastructure operators, such as
`aten._assert_tensor_metadata.default`, are ignored when they are known to be
removed before backend lowering.

#### Export recipes

An `ExportRecipe` bundles those steps for a target, so a standard export needs
no compile spec, quantizer or partitioner of its own. Each recipe carries the
settings its target expects:

```python
from executorch.backends.arm.recipes.arm_recipe_types import ArmRecipeType
from executorch.export import export, ExportRecipe

session = export(
    model=model,
    example_inputs=[example_inputs],
    export_recipe=ExportRecipe.get_recipe(ArmRecipeType.ETHOS_U55_INT8),
)
session.save_to_pte("model")
```

The recipe quantizes the model, so pass `example_inputs` that are representative
of real data; they are used to calibrate.

Available recipes:

| Recipe | Target |
| --- | --- |
| `ETHOS_U55_INT8`, `ETHOS_U65_INT8`, `ETHOS_U85_INT8` | Ethos-U NPUs, int8 |
| `TOSA_FP`, `TOSA_INT8`, `TOSA_A16W8` | TOSA, for testing without hardware |
| `VGF_FP`, `VGF_INT8` | VGF, for the ML SDK for Vulkan |

The Ethos-U recipes accept `macs`, `system_config`, `memory_mode`,
`extra_flags` and `config_ini`, matching the corresponding Vela options:

```python
ExportRecipe.get_recipe(ArmRecipeType.ETHOS_U85_INT8, macs=512)
```

`macs` is validated against the accelerator configurations the installed Vela
accepts, so an unsupported count fails at recipe construction rather than during
compilation.

Reach for the step-by-step flow above when a recipe does not fit -- a custom
quantization scheme, extra passes, or a compile spec the recipe does not expose.

#### TopK support

The `to_edge_transform_and_lower` flow handles supported `torch.topk` calls
automatically. Supported configurations are:

- FP16 or FP32 input with positive static shape `[T, E]`, where
  `E <= 2^31 - 1`.
- Constant `1 <= K <= min(4, E)`, `dim=-1` or `dim=1`, `largest=True`, and
  `sorted=True`.
- The TOSA FP profile for K=1, or FP+INT for K>1. The scores remain
  floating-point in both cases.

**Input scores must be finite.** This condition is not checked at runtime;
non-finite scores can produce incorrect results without triggering automatic
fallback. Equal scores are selected in increasing index order, so tied indices
may differ from PyTorch's results. Dynamic shapes or K, BF16, and quantized TopK
are unsupported.

### Direct Drive (experimental, Ethos-U85 on Linux) workflow

Direct Drive enables execution on Ethos-U85 via the Linux driver stack.

Driver stack (Linux) and API:

```
https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-linux-driver-stack
```

An FVP with Linux is available for Direct Drive, but it must be built and run
manually. See:

```
https://corstone1000.docs.arm.com/en/corstone1000-2025.12/
```

Setup:

```
./examples/arm/setup.sh --i-agree-to-the-contained-eula --target-toolchain linux-musl
source ./examples/arm/arm-scratch/setup_path.sh
```

Build:

```
./backends/arm/scripts/build_executorch.sh \
  --toolchain=aarch64-linux-musl-gcc \
  --build_type=Debug
```

Note: setup selects the linux-musl toolchain; build uses the aarch64-linux-musl GCC toolchain name.

If your Yocto image enables the dropbear SSH server, you can copy the
`executor_runner` binary into the running FVP via scp:

```
scp -P 2222 arm_test/cmake-out/executor_runner root@127.0.0.1:/tmp/
```

#### Direct Drive model (PTE) workflow

For a quick test with the example `add` model,
`aot_arm_compiler.py` can be used:

```
python3 -m backends.arm.scripts.aot_arm_compiler \
  --model_name examples/arm/example_modules/add.py \
  --delegate \
  --quantize \
  --target ethos-u85-256 \
  --direct_drive
```

For production use, the Python API described in
[Compiling models with the Python API](#compiling-models-with-the-python-api)
should be used. Use an Ethos-U85 target and set the Direct Drive `extra_flags` when creating the `EthosUCompileSpec`:

```python
compile_spec = EthosUCompileSpec(
    target="ethos-u85-256",
    extra_flags=["--separate-io-regions", "--cop-format=COP2"],
)
```

Then save the generated program as e.g. `model.pte` or
update the copy and run commands below to match your output file name.

Copy the `executor_runner` binary and the generated PTE file to the running FVP:

```
scp -P 2222 arm_test/cmake-out/executor_runner model.pte root@127.0.0.1:/tmp/
```

Run the model on the FVP:

```
ssh -p 2222 root@127.0.0.1 -t "/tmp/executor_runner -model_path /tmp/model.pte -num_executions 1"
```

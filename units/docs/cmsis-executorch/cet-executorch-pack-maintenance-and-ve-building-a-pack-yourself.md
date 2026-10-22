---
id: "cet-executorch-pack-maintenance-and-ve-building-a-pack-yourself"
type: "concept"
domain: "pack"
title: "ExecuTorch pack maintenance and versioning: Building a pack yourself"
summary: "Worth knowing if you need a version that has no published pack yet, or want to carry a local ExecuTorch change into the firmware. The generator lives in the ExecuTorch tree at backends/arm/cmsis_pack/scripts/build_pack.sh."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/executorch-pack-maintenance.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/executorch-pack-maintenance.md#building-a-pack-yourself"
license: "Apache-2.0"
mode: "V"
---

Worth knowing if you need a version that has no published pack yet, or want to
carry a local ExecuTorch change into the firmware. The generator lives in the
ExecuTorch tree at `backends/arm/cmsis_pack/scripts/build_pack.sh`.

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout release/1.5          # or the tag matching your target version
git submodule update --init --recursive
```

> **Run the CMake cross-compile before `build_pack.sh`.**
>
> This is the one trap worth knowing about. If `build_pack.sh` runs without the
> prior cross-compile, it completes successfully but **silently omits**:
>
> - the bundled `include/flatbuffers/` headers, and
> - the flatc-generated `program_generated.h` and `scalar_type_generated.h`.
>
> The resulting pack looks complete and fails at compile time with missing-header
> errors that point nowhere useful. Those two headers are generated with:
>
> ```bash
> flatc --cpp --cpp-std c++11 --gen-mutable --scoped-enums <schema>.fbs
> ```
>
> `flatc` ships inside the executorch wheel — after `./setup_venv.sh` it is at
> `.venv/bin/flatc`.

The cross-compile that produces those headers is a plain CMake build of the
runtime for Cortex-M; the host executor runner is not needed and its link
fails without the Ethos-U driver, so leave it off:

```bash
cmake -S . -B cmake-out-arm \
    -DCMAKE_TOOLCHAIN_FILE=examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
    -DEXECUTORCH_BUILD_ARM_BAREMETAL=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_FLATC=ON \
    -DEXECUTORCH_BUILD_EXECUTOR_RUNNER=OFF \
    -DPYTHON_EXECUTABLE=/path/to/this/template/.venv/bin/python
cmake --build cmake-out-arm --config Release -j4
```

`arm-none-eabi-gcc` must be on `PATH` (the one from `vcpkg-configuration.json`
does); `PYTHON_EXECUTABLE` points at this template's `.venv`, which has the
Python packages the generators import.

Then run the generator with all four arguments (it refuses to run without
them); the pack lands in the output directory:

```bash
backends/arm/cmsis_pack/scripts/build_pack.sh \
    --executorch-root "$PWD" \
    --build-dir cmake-out-arm \
    --version 1.5.1-local \
    --output-dir pack-output
```

### Verifying a pack you built

Before trusting a freshly built pack, check the parts that go missing quietly:

```bash
VERSION=1.5.1-local
PACK=pack-output/PyTorch.ExecuTorch.$VERSION
set -e

# 1. The bundled flatbuffers headers must be present.
test -d "$PACK/include/flatbuffers"

# 2. The flatc-generated headers must be present.
for h in program_generated.h scalar_type_generated.h; do
    find "$PACK/include" -name "$h" | grep .
done

# 3. The pack must pass the structural check the generator ships.
python3 backends/arm/cmsis_pack/test/validate_pack.py "$PACK.pack"
```

These checks catch the parts that go missing quietly; they do not prove that
the operators a model needs are present or that the pack compiles. Install it
and build this template against it, with the pack version pinned in the
csolution and the cproject:

```bash
cpackget add --agree-embedded-license pack-output/PyTorch.ExecuTorch.$VERSION.pack
cpackget list | grep "PyTorch::ExecuTorch@$VERSION"   # cpackget exits 0 even when it declined
```

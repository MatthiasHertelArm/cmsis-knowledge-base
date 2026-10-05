---
id: "mlek-building-the-ml-embedded-code-samp-optimize-custom-model-with-vela-compiler"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Optimize custom model with Vela compiler"
summary: "The Vela compiler is a tool that can optimize a neural network model into a version that can run on an embedded system containing an Ethos-U NPU."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/building.md#optimize-custom-model-with-vela-compiler"
license: "Apache-2.0"
mode: "V"
---

> **Note:** This tool is not available within this project. It is a Python tool available from
> <https://pypi.org/project/ethos-u-vela/>.
> The source code is hosted on <https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela>.

> **Note:** The correct version of Vela should be used and this depends on the versions of software dependencies used
> or you may encounter issues when trying to run applications on different variants of Ethos-U NPUs.
> See <https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela> for more details of which versions align.

The Vela compiler is a tool that can optimize a neural network model into a version that can run on an embedded system
containing an *Ethos-U* NPU.

The optimized model contains custom operators for sub-graphs of the model that can be accelerated by the *Ethos-U*
NPU. The remaining layers that cannot be accelerated, are left unchanged and are run on the CPU using optimized, or
`CMSIS-NN`, or reference kernels that are provided by the inference engine.

After the compilation, the optimized model can only be executed on a system using an *Ethos-U* NPU.

> **Note:** The NN model provided during the build and compiled into the application executable binary defines whether
the CPU or NPU is used to execute workloads. If an unoptimized model is used, then inference runs on the *Cortex-M* CPU.

The Vela compiler accepts parameters to influence a model optimization. The model provided within this project has been
optimized with the following parameters:

```commandline
vela \
    --accelerator-config=ethos-u55-128 \
    --optimise Performance \
    --config my_vela_cfg.ini \
    --memory-mode Shared_Sram \
    --system-config Ethos_U55_High_End_Embedded \
    <model>.tflite
```

The Vela command contains the following:

- `--accelerator-config`: Specifies the accelerator configuration to use between `ethos-u55-256`, `ethos-u55-128`,
  `ethos-u55-64`, `ethos-u55-32`, `ethos-u65-256`, `ethos-u65-512`, `ethos-u85-128`, `ethos-u85-256`, `ethos-u85-512`,
  `ethos-u85-1024` and `ethos-u85-2048`.
- `--optimise`: Sets the optimisation strategy to Performance or Size. The Size strategy results in a model minimising
  the SRAM usage whereas the Performance strategy optimises the neural network for maximal performance.
  Note that if using the Performance strategy, you can also pass the `--arena-cache-size` option to Vela.
- `--config`: Specifies the path to the Vela configuration file. The format of the file is a Python ConfigParser `.ini`
    file. An example can be found in the `dependencies` folder [default_vela.ini](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../scripts/vela/default_vela.ini).
- `--memory-mode`: Selects the memory mode to use as specified in the Vela configuration file.
- `--system-config`: Selects the system configuration to use as specified in the Vela configuration file:
  `Ethos_U55_High_End_Embedded`for *Ethos-U55*, `Ethos_U65_High_End` for *Ethos-U65*,
  `Ethos_U85_SYS_DRAM_Low` for *Ethos-U85* with 128 or 256 MACs configurations,
  `Ethos_U85_SYS_DRAM_Mid_512` for *Ethos-U85* with 512 MACs configuration,
  `Ethos_U85_SYS_DRAM_Mid_1024` for *Ethos-U85* with 1024 MACs configuration and
  `Ethos_U85_SYS_DRAM_Mid_2048` for *Ethos-U85* with 2048 MACs configuration.

Vela compiler accepts `.tflite` file as input and saves optimized network model as a `.tflite` file.

Using `--show-cpu-operations` and `--show-subgraph-io-summary` shows all the operations that fall back to the CPU. And
includes a summary of all the subgraphs and their inputs and outputs.

To see Vela helper for all the parameters use: `vela --help`.

> **Note:** By default, use of the *Ethos-U* NPU is enabled in the CMake configuration. This can be changed by passing
> `-DETHOS_U_NPU_ENABLED`.

> **Note:** The performance summary produced by Vela compiler for any model are **estimates only**. Vela computes
> these figures from a very simplistic approximation. To get accurate performance numbers for the Arm Ethos-U NPU, use
> of FVP or FPGA platforms is recommended.

---
id: "ethu-integration-step-2-select-and-verify-the-vela-config"
type: "concept"
domain: "edge-ai"
title: "Integration: Tutorial: Create an Ethos-U application / Step 2: Select and verify the Vela configuration"
summary: "Part of: Tutorial: Create an Ethos-U application"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/integration/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/integration/src/main.md#step-2-select-and-verify-the-vela-configuration"
license: "Apache-2.0"
mode: "V"
---

_Part of: Tutorial: Create an Ethos-U application_

#### Update MLOps information

The [`mlops:` information in the `*.csolution.yml` file](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information)
describes the NPU, Vela configuration, model layer, and test targets used by an
MLOps system. Update this information in two stages.

##### Stage 1: Update the Ethos-U configuration

First select the NPU independently of its memory configuration. The Alif E7
`M55_HP` processor integrates an Ethos-U55 with 256 MACs, so change `macs:` from
`128` to `256` in `Test-Ethos-U55.csolution.yml`:

```yml
  mlops:
    description: TinyCNN int8 image classifier for Ethos-U55
    npu:
      type: Ethos-U55
      macs: 256      # Must match the hardware target
```

> [!NOTE]
> For the complete syntax of the `mlops:` node, see [MLOps Management](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#mlops-management) in the CMSIS-Toolbox manual.

In Keil Studio, saving the solution runs `cbuild setup` and regenerates
`Test-Ethos-U55.cbuild-mlops.yml`. CMSIS-Toolbox combines the MLOps settings
with the NPU and processor information published by the selected device and DFP.

##### Stage 2: Verify and update the Vela configuration

Inspect the `vela:` section of the generated `*.cbuild-mlops.yml` file. Its
`ini:` entry identifies the device-specific `vela.ini` supplied by the DFP. For
example:

```yml
cbuild-mlops:
  generated-by: csolution version 2.14.1+p55-g119b477e
  description: TinyCNN int8 image classifier for Ethos-U55
  processor:
    type: Cortex-M55
  npu:
    type: Ethos-U55
    macs: 256
  vela:
    ini: .cmsis/ensemble_vela.ini    # Device-specific vela.ini file
    options: --accelerator-config ethos-u55-256 --system-config Ethos_U55_High_End_Embedded --memory-mode Shared_Sram
```

> [!NOTE]
> If the `vela:` section does not contain an `ini:` entry, check the DFP
> documentation or contact the silicon vendor for a configuration that
> describes the device.

The generated `options:` entry might initially contain a system configuration
or memory mode inherited from the original example. List the configurations and
memory modes that the device-specific `vela.ini` actually provides:

```console
vela --list-configs .cmsis/ensemble_vela.ini
```

Choose from the reported values by comparing the memory types, bandwidths,
clock frequency, and AXI mappings with the target hardware and intended model
placement. In the `*.csolution.yml` file, update the `vela:` node under
`mlops:` with selectors that are present in the device-specific `vela.ini`:

```yml
  mlops:
    description: TinyCNN int8 image classifier for Ethos-U55
    npu:
      type: Ethos-U55
      macs: 256
    vela:
      system: RTSS_HP_SRAM_MRAM # System configuration from the device-specific vela.ini
      memory: Shared_Sram       # Memory mode from the device-specific vela.ini
      misc: --optimise Performance --verbose-config # Additional Vela options
    model:
      clayer: ./Model/ML-MyModels.clayer.yml
      name: tiny_cnn_int8
#     path: Model/tiny_cnn      # feature to be added in CMSIS-Toolbox 2.15
```

Save the solution again. In the regenerated `*.cbuild-mlops.yml`, verify that
the `ini:` and `options:` entries under `vela:` contain the intended
configuration.

#### Configure 256 MACs for FVP simulation

The supplied Corstone-300 simulator target uses Ethos-U55-128 by default. To
test the same Ethos-U55-256 model that runs on the Alif E7, update the simulator
configuration as follows:

- In `Board/Corstone-300/Board-U55.clayer.yml`, set the compile-time driver
   configuration to:

   ```yml
   - ETHOSU_MACS: 256
   ```

- In `Board/Corstone-300/fvp_config_u55.txt`, configure the simulated NPU:

   ```ini
   ethosu.num_macs=256
   ```

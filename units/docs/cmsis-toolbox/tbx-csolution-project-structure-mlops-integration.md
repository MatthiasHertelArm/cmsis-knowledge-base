---
id: "tbx-csolution-project-structure-mlops-integration"
type: "concept"
domain: "project"
title: "CSolution Project Structure: MLOps Integration"
summary: "An MLOps (Machine Learning Operations) system automates the process of generating and maintaining machine learning (ML) models."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-integration"
license: "Apache-2.0"
mode: "V"
---

An MLOps (Machine Learning Operations) system automates the process of generating and maintaining machine learning (ML) models. Often described as "DevOps for ML", it bridges the gap between data scientists who build ML models and embedded developers that integrate these models into real-world applications.

The CMSIS-Toolbox generates the file [`*.cbuild-mlops.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-mlopsyml) as the interface between a *csolution project* and an MLOps system. It combines DFP information about the processor and NPU with project settings so that model conversion does not duplicate target-specific configuration.

(figure: MLOps Integration)

The `*.cbuild-mlops.yml` file provides information about:

- Processor type
- NPU type with MAC configuration
- Vela INI file and parameters (only for Ethos-U NPUs)
- Location of the `*.clayer.yml` file that contains the ML model under development
- Custom model properties, including simple values, lists, and grouped settings with additional levels
- Build information (using `cbuild` with hardware target) for testing on hardware
- Build information (using `cbuild` with simulator target) for testing on FVP simulation models along with information for FVP invocation

The [`*.cbuild-mlops.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-mlopsyml) file is designed for applications that use one or more ML models and optional NPUs. Custom properties in the [`model:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#model) node can describe framework-specific inputs as simple values, lists, or grouped settings with additional levels. This allows a model integration script to process several models or related artifacts in one workflow. When [`mlops:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#mlops) is used, the CMSIS-Toolbox generates the `*.cbuild-mlops.yml` file with the base name of the `*.csolution.yml` file in the same folder.

### Model Integration Workflow

Model creation is separate from the application build. A typical command-line workflow is:

1. Generate the resolved MLOps information for the selected target:

    ```bash
    cbuild setup MyApp.csolution.yml --active SSE-320-U85@FVP-Test --packs
    ```

    This creates `MyApp.cbuild-mlops.yml` with the processor, NPU, Vela options, model metadata, AI-layer location, and test target information.

2. Pass that file to the framework-specific model integration script:

    ```bash
    python create_ai_layer.py MyApp.cbuild-mlops.yml
    ```

    The script performs model export or conversion and writes a complete AI layer, including the generated C/C++ model data and the `*.clayer.yml` file with the required software components. The script is part of the framework integration, not the CMSIS-Toolbox.

3. Build the application with the generated layer:

    ```bash
    cbuild MyApp.csolution.yml --active SSE-320-U85@FVP-Test
    ```

    This is a normal application build and does not run the model conversion. After changing the model or target, repeat the setup and AI-layer creation steps before rebuilding.

**Example:**

`MyApp.csolution.yml` input:

```yml
solution:
   :
  mlops:
    description: ML model for detecting Rock/Paper/Scissors images
    npu:
      type: Ethos-U85           # Select NPU as the Alif E8 Device has multiple NPUs
    vela:
      system: RTSS_HE_SRAM_MRAM # Choose system configuration from Vela.ini file
      memory: Shared_Sram       # Choose memory configuration from Vela.ini file
    model:
      clayer: $AI-Layer$        # Layer that contains the ML model
      framework: ExecuTorch     # Custom metadata passed to the MLOps system
      source:                   # Lists support workflows with multiple models
        - models/rps_detector.pte
        - $Model-Source$        # Undefined variables produce an empty string
      settings:                 # Nested maps are also preserved
        delegate: Ethos-U
        quantize: true
    hardware:
      target: AppKit-E8-U85@HIL # Hardware target used for testing
    simulator:
      target: SSE-320-U85@FVP-Test # FVP target used for testing
    :
  # List different hardware targets that are used to deploy the solution.
  target-types:
    - type: AppKit-E8-U85
      device: AE822FA0E5597BS0
      board: AppKit-E8-AIML
      variables:
        - Board-Layer: $SolutionDir()$/Board/AppKit-E8_M55_HP/Board_HP-U85.clayer.yml
        - SDSIO-Layer: $SolutionDir()$/sdsio/usb/sdsio_usb.clayer.yml
        - AI-Layer: $SolutionDir()$/ai_layer/ai_layer.clayer.yml
      target-set:
        - set: J-Link           # Debug setup for desktop (IDE workflow)
          debugger:
            name: J-Link Server
            clock: 4000000
            protocol: swd
            start-pname: M55_HP
          images:
            - project-context: AlgorithmTest.Debug
        - set: HIL              # Debug setup for test automation (HIL workflow)
          debugger:
            name: ULINKplus@pyOCD
            clock: 10000000
            protocol: swd
            start-pname: M55_HP
            stdio:
              - pname: M55_HP
                mode: console
          images:
            - project-context: AlgorithmTest.Debug

    - type: SSE-320-U85 # Simulator (Cortex-M85 + Ethos-U85)
      board: SSE-320
      device: SSE-320-FVP
      define:
        - SIMULATOR
      variables:
        - Board-Layer: $SolutionDir()$/Board/Corstone-320/Board-U85.clayer.yml
        - SDSIO-Layer: $SolutionDir()$/sdsio/fvp/sdsio_fvp.clayer.yml
        - AI-Layer: $SolutionDir()$/ai_layer/ai_layer.clayer.yml
      target-set:
        - set: FVP-Test          # Debug setup for test automation (FVP simulation)
          debugger:
            name: Arm-FVP
            model: FVP_Corstone_SSE-320
            config-file: Board/Corstone-320/fvp_config.txt
          images:
            - project-context: AlgorithmTest.Debug
```

`MyApp.cbuild-mlops.yml` output. Paths are relative to the location of the `*.cbuild-mlops.yml` file (which is in the same directory as the `*.csolution.yml` file).

```yml
cbuild-mlops:
  description: ML model for detecting Rock/Paper/Scissors images
  processor:
    type: Cortex-M55
  npu:
    type: Ethos-U85
    macs: 256
  vela:
    ini: .cmsis/ensemble_vela.ini
    options: --accelerator-config ethos-u85-256 --system-config RTSS_HE_SRAM_MRAM --memory-mode Shared_Sram
  model:
    clayer: ai_layer/ai_layer.clayer.yml
    framework: ExecuTorch
    source:
      - models/rps_detector.pte
      - ""
    settings:
      delegate: Ethos-U
      quantize: true
  hardware:
    active: AppKit-E8-U85@HIL
    cbuild-run: out/MyApp+AppKit-E8-U85.cbuild-run.yml
    output:
      - file: out/AlgorithmTest/AppKit-E8-U85/Debug/AlgorithmTest.axf
        type: elf
  simulator:
    active: SSE-320-U85@FVP-Test
    cbuild-run: out/MyApp+SSE-320-U85.cbuild-run.yml
    output:
      - file: out/AlgorithmTest/SSE-320-U85/Debug/AlgorithmTest.axf
        type: elf
    model: FVP_Corstone_SSE-320
    config-file: Board/Corstone-320/fvp_config.txt
```

Using the information in the `*.cbuild-mlops.yml` file, the MLOps system can create the AI layer and execute tests on hardware or simulation targets.

### Framework Integration Examples

The [`CMSIS-ExecuTorch` preview workflow](https://github.com/Arm-Examples/CMSIS-Executorch/tree/preview) uses an isolated `model/model.py`. A new model can replace this file without changing the build environment. Its `create_ai_layer.py` script exports and delegates the model, selects the required ExecuTorch CMSIS components, and writes the ExecuTorch program as C source into the AI layer.

The [`CMSIS-LiteRT` preview workflow](https://github.com/MatthiasHertelArm/cmsis-litert/tree/preview) applies the same interface to LiteRT. Its `create_ai_layer.py` consumes the Vela parameters, converts the model data to C source, and selects either the Ethos-U or CMSIS-NN kernel components for the generated layer.

Both examples keep target and NPU settings in the *csolution project* and pass framework-specific model parameters as custom keys under `mlops.model:`. This separation allows a framework pack to supply the integration script while the application supplies only its model and target configuration. For ExecuTorch with Zephyr, refer also to [`CMSIS-Zephyr-ExecuTorch`](https://github.com/Arm-Examples/CMSIS-Zephyr-Executorch).

### Test on Hardware

Build and test the ML model (in context with the application) with these commands.

```bash
>cbuild MyApp.csolution.yml --active AppKit-E8-U85@HIL --packs
>pyOCD load --cbuild-run out/MyApp+AppKit-E8-U85.cbuild-run.yml
>pyOCD run --cbuild-run out/MyApp+AppKit-E8-U85.cbuild-run.yml --eot --timelimit 30
```

### Test on Simulator

Build and test the ML model (in context with the application) with these commands.

```bash
>cbuild MyApp.csolution.yml --active SSE-320-U85@FVP-Test --packs
>FVP_Corstone_SSE-320 -f Board/Corstone-320/fvp_config.txt -a out/AlgorithmTest/SSE-320-U85/Debug/AlgorithmTest.elf --simlimit 30
```

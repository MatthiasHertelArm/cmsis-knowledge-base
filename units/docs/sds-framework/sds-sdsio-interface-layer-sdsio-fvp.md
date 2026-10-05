---
id: "sds-sdsio-interface-layer-sdsio-fvp"
type: "concept"
domain: "test"
title: "SDSIO Interface: Layer: sdsio_fvp"
summary: "The template/sdsio/fvp/sdsiofvp.clayer.yml targets AVH FVP simulation and is configured for playback from the host computer or a CI system. It uses the SDSIO VSI interface implemented by the file vsi/python/armvsi3.py, which is loaded by the FVP simulation model."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/sdsio.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/sdsio.md#layer-sdsio-fvp"
license: "Apache-2.0"
mode: "V"
---

The [`template/sdsio/fvp/sdsio_fvp.clayer.yml`](https://github.com/ARM-software/SDS-Framework/tree/main/template/sdsio/fvp) targets AVH FVP simulation and is configured for playback from the host computer or a CI system. It uses the [SDSIO VSI interface](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi.html) implemented by the file `vsi/python/arm_vsi3.py`, which is loaded by the FVP simulation model. Since the SDSIO-Server functionality is implemented in `arm_vsi3.py`, no separate SDSIO-Server is required.

The VSI3 Python script (`arm_vsi3.py`) is tested with Python 3.13 and has requirements to the modules `pyyaml` and `asyncio` that can be installed with:

```bash
pip install pyyaml asyncio
```

### Using FVP Simulation Models

VSI3 implements the SDSIO VSI interface and is designed for regression testing on host computer and CI systems. The tests cases are configured using a [`*.sdsio.yml` control file](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-control-file-sdsioyml). 

VSI3 locates a [`*.sdsio.yml` control file](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sdsio-control-file-sdsioyml) as follows:

- If the environment variable `SDSIO_FVP` is set, it must be an **absolute path** to either a config file or a directory:
    - **File** — used directly as the config file.
    - **Directory** — searched for a config file in this order: `sdsio.yml`, `sdsio.yaml`, first `*.sdsio.yml` (alphabetical), first `*.sdsio.yaml` (alphabetical).
    - If the path does not exist or is not absolute, the search falls back to the working directory.
- If `SDSIO_FVP` is not set (or falls back), the **simulator working directory** is searched using the same file order: `sdsio.yml`, `sdsio.yaml`, first `*.sdsio.yml` (alphabetical), first `*.sdsio.yaml` (alphabetical).

!!! Tip
    In Keil Studio you may set the [environment variable `SDSIO_FVP`](https://mdk-packs.github.io/vscode-cmsis-solution-docs/zephyr.html#set-environment-variables) using the Settings dialog with id `cmsis-csolution.environmentVariables`.

If a control file is found, the script reads the `sdsio:` root node. If `workdir:` is a relative path, it is interpreted relative to the simulator working directory.

**Console output:**

This is a example console output during simulation

```txt
FVP_Corstone_SSE-300_Ethos-U55 -f Board/Corstone-300/fvp_config.txt -a out/DataTest/SSE-300-U55/Debug/DataTest.hex  

Ethos-U version info:
        Arch:       v1.1.0
        MACs/cc:    128
        Cmd stream: v0
SDSIO VSI interface initialized successfully
==== SDS playback started
==== SDS playback stopped

Info: /OSCI/SystemC: Simulation stopped by user.
Fatal Python error: _Py_GetConfig: the function must be called with the GIL held ...
```

!!! Note
    - It might be required to enable access permissions for the FVP simulation model.
    - The Fatal Python error at exit is a known problem that will be solved in a future version of the FVP simulation models. It has no impact on the actual test results.

**Log File: `sdsio.log`:**

During FVP simulation, an `sdsio.log` file is generated that records all [SDS data file](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#sds-data-files) access operations. This file is located in the folder that is configured the `workdir:` in the `*.sdsio.yml` file.

**Example:**

```txt
Created by ...\Board\Corstone-300\vsi\python\arm_vsi3.py

SDSIO VSI version 3.1.0
SDSIO_FVP environment variable not set.
Working directory: ...\datatest\SDS Recordings.
SDSIO configuration YAML: ...\SDS\datatest.sdsio.yml.
sdsFlags = 0xB0000000.
Playback step 0: Test 0.
Playback: Test_In (Test_In.0.sds).
Record:   Test_Out (Test_Out.0.p.sds).
Closed:   Test_In (Test_In.0.sds).
Closed:   Test_Out (Test_Out.0.p.sds).
Playback complete - no more steps remaining.
sdsFlags = 0x30000000.
sdsFlags = 0x70000000.
sdsFlags = 0x30000000.
```

**FVP Model Configuration:**

The FVP model is configured with the file `./Board/Corstone-300/fvp_config.txt` or `./Board/Corstone-320/fvp_config.txt`.
When using an Ethos-U NPU it is important that the MAC configuration matches the settings that were used when generating the ML model.

Refer to [Arm FVP Simulation Models - Model Configuration](https://arm-software.github.io/AVH/main/simulation/html/using.html#Config) for further information.

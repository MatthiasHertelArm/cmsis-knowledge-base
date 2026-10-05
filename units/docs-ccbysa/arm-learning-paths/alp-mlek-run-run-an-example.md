---
id: "alp-mlek-run-run-an-example"
type: "concept"
domain: "edge-ai"
title: "Build and run the Arm Machine Learning Evaluation Kit examples: Run the examples on the FVP: Run an example"
summary: "Navigate to the evaluation kit repository."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/mlek/run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/mlek/run/#run-an-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Navigate to the evaluation kit repository.

```bash
cd ml-embedded-evaluation-kit/
```

The built examples (`.axf` files) will be located in a `cmake-*/bin` folder based on the build configuration used.

Navigate into that folder, and list the images. For example:

```bash
cd cmake-build-mps4-sse-320-ethos-u85-256-gnu/bin/
 
ls *.axf
```

Use `-a` to specify the application to load to the FVP.

Use `-C mps4_board.subsystem.ethosu.num_macs` to configure the Ethos-U component of the model.

**Note:**
The number of NPU MACs specified in the build MUST match the number specified in the FVP. Else an error similar to the below will be emitted.

```
E: NPU config mismatch. npu.macs_per_cc=E: NPU config mismatch..
```


You can list all available parameters by running the FVP executable with the `--list-params` option, for example:

```console
FVP_Corstone_SSE-320 --list-params > parameters.txt
```


### Run the application

```console
FVP_Corstone_SSE-320								\
    -C mps4_board.subsystem.ethosu.num_macs=256			\
    -C mps4_board.visualisation.disable-visualisation=1	\
    -C vis_hdlcd.disable_visualisation=1				\
    -a ethos-u-kws.axf
```

If adding configuration options becomes cumbersome, it can be easier to specify them in a configuration file (remove the `-C` option) and then use that on the command line (`-f`).

#### config.txt
```
mps4_board.subsystem.ethosu.num_macs=256
mps4_board.visualisation.disable-visualisation=1
vis_hdlcd.disable_visualisation=1
```

The command line becomes:
```console
FVP_Corstone_SSE-320 -f config.txt -a ethos-u-kws.axf
```

The application executes and identifies words spoken within audio files.

Repeat with any of the other built applications.

Full instructions are provided in the evaluation kit [documentation](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/main/docs/quick_start.md).

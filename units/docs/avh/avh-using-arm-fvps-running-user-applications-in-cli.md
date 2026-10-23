---
id: "avh-using-arm-fvps-running-user-applications-in-cli"
type: "concept"
domain: "test"
title: "Using Arm FVPs: Running User Applications in CLI"
summary: "The FVP models can be executed from command prompt by using the model name followed by the model options. Development tools may abstract the execution with GUI, but the underlying approach stays the same."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:DoxyGen/simulation/src/using.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/simulation/src/using.md#running-user-applications-in-cli"
license: "Apache-2.0"
mode: "V"
---

The FVP models can be executed from command prompt by using the model name followed by the model options. Development
tools may abstract the execution with GUI, but the underlying approach stays the same.

Below is an example of the command for running a program on the FVP model for Corstone-300 with Ethos-U55 in a Linux
environment:

```sh
FVP_Corstone_SSE-300_Ethos-U55 -a project.axf -C mps3_board.v_path=./vsi_py/ -f fvp_config.txt --simlimit 24 --stat
```

Where:

- `FVP_Corstone_SSE-300_Ethos-U55` is the simulation model name. Note that on Windows the executable files shall be
  used, for example `FVP_Corestone_SSE-300_Ethos-U55.exe`. 
- `-a` (or `--application`) option specifies the application binary file to run on the model (`project.axf` in this
  example).
- `-f` (or `--config-file`) specifies the configuration file for the simulation model (`fvp_config.txt` in this case).
  See Config.
- `-C mp3_board.v_path` specifies model configuration parameter for VSI python scripts for arm_cmvp
  (`"./vsi_py/"` here). Use `mp2_board.v_path`, `mps3_board.v_path` or `mps4_board.v_path`, depending on the underlying
  board.
- `--stat` instructs to print run statistics on simulation exit.
- `--simlimit` specifies the maximum number of seconds to simulate.

The available command options can be listed using the `--help` option. Refer to
[FVP command line options](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/FVP-command-line-options).

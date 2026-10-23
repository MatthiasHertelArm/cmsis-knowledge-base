---
id: "mlek-deployment-deploying-on-an-fvp"
type: "concept"
domain: "edge-ai"
title: "Deployment: Fixed Virtual Platform / Deploying on an FVP"
summary: "This section assumes that the FVP has been installed (see Installing an FVP) to the home directory of the user: ~/FVP_Corstone_SSE-300. The installation, typically, has the executable under ~/FVP_Corstone_SSE-300/model/<OS><compiler-version>/ directory. For the example below, we assume it is: ~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/deployment.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/deployment.md#deploying-on-an-fvp"
license: "Apache-2.0"
mode: "V"
---

_Part of: Fixed Virtual Platform_

This section assumes that the FVP has been installed (see
[Installing an FVP](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./deployment.md#installing-an-fvp))
to the home directory of the user: `~/FVP_Corstone_SSE-300`. The installation, typically, has the
executable under `~/FVP_Corstone_SSE-300/model/<OS>_<compiler-version>/` directory. For the example
below, we assume it is: `~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4`.

> **NOTE**: The commandline arguments for the FVP mentioned below are valid for FVPs (and AVH) for
> Arm® Corstone™-300, Corstone™-310, Corstone™-315 and Corstone™-320.

To run a use-case on the FVP, from the [Build directory](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../sections/building.md#create-a-build-directory):

```commandline
~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 -a ./bin/mlek_<use_case>.axf
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003

    Ethos-U rev 0 --- Oct 13 2020 11:27:45
    (C) COPYRIGHT 2019-2020 Arm Limited
    ALL RIGHTS RESERVED
```

This also launches a telnet window with the standard output from the sample application.
And also error log entries containing information about the pre-built application version,
TensorFlow Lite Micro or ExecuTorch library version used, and data type.
It also includes the input and output tensor sizes of the model that are compiled into the executable binary.

> **Note:** For details on the specific use-case, follow the instructions in the corresponding documentation.

After starting, the application outputs a menu and waits for the user-input from the telnet terminal.

For example, the image classification use-case on *Ethos-U55* processor can be started by using:

```commandline
~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 -a ./bin/mlek_img_class.axf
```

Meanwhile, for *Ethos-U65*:

```commandline
~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U65 -a ./bin/mlek_img_class.axf
```

(figure: FVP)

(figure: FVP Terminal)

The FVP supports many command-line parameters, such as:

- Those passed by using `-C <param>=<value>`. The most important ones are:

  | Arm® Corstone™-300 FVP and Arm® Corstone™-310 FVP | Arm® Corstone™-315 FVP and Arm® Corstone™-320 FVP                                      | Description                                                                                                                                                                                                                                                                |
  |---------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | `ethosu.num_macs`                                 | `mps4_board.subsystem.ethosu.num_macs`                                                 | Sets the *Ethos-U* configuration for the model. The valid parameters are:
- *Ethos-U55*: `32`, `64`, `256`, and the default one `128`.
- *Ethos-U65*: `256`, and the default one `512`.
- *Ethos-U85*: `128`, `512`, `1024`, `2048`, and the default one `256`. |
  | `cpu0.CFGITCMSZ`                                  | `mps4_board.subsystem.cpu0.CFGITCMSZ`                                                  | The ITCM size for the *Cortex-M* CPU. The size of ITCM is *pow(2, CFGITCMSZ - 1)* KB                                                                                                                                                                                       |
  | `cpu0.CFGDTCMSZ`                                  | `mps4_board.subsystem.cpu0.CFGDTCMSZ`                                                  | The DTCM size for the *Cortex-M* CPU. The size of DTCM is *pow(2, CFGDTCMSZ - 1)* KB                                                                                                                                                                                       |
  | `mps3_board.telnetterminal0.start_telnet`         | `mps4_board.telnetterminal0.start_telnet`                                              | Starts the telnet session if nothing connected.                                                                                                                                                                                                                            |
  | `mps3_board.uart0.out_file`                       | `mps4_board.uart0.out_file`                                                            | Sets the output file to hold the data written by the UART. Use `'-'` to send all output to `stdout` and is empty by default).                                                                                                                                              |
  | `mps3_board.uart0.shutdown_on_eot`                | `mps4_board.uart0.shutdown_on_eot`                                                     | Shut down the simulation when an `EOT (ASCII 4)` char is transmitted.                                                                                                                                                                                                      |
  | `mps3_board.visualisation.disable-visualisation`  | `mps4_board.visualisation.disable-visualisation`
`vis_hdlcd.disable_visualisation` | Enables, or disables, visualization and is disabled by default.                                                                                                                                                                                                            |
  | `ethosu.extra_args="--fast"`                      | `mps4_board.subsystem.ethosu.extra_args="--fast"`                                      | Run the FVP in fast mode.  This is useful for functionally testing your application, but should *not* be used for performance testing.                                                                                                                                     |
  | `cpu0.semihosting-enable`                         | `mps4_board.subsystem.cpu0.semihosting-enable`                                         | Toggles semihosting. Default value is `0` and to enable semihosting, it can be set to `1`                                                                                                                                                                                  |

  To start the model in `128` mode for *Ethos-U55*:

    ```commandline
    ~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 -a ./bin/mlek_img_class.axf -C ethosu.num_macs=128
    ```

  To start the model in `512` mode for *Ethos-U65*:

    ```commandline
    ~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U65 -a ./bin/mlek_img_class.axf -C ethosu.num_macs=512
    ```

- `-l`: shows the full list of supported parameters

    ```commandline
    ~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 -l
    ```

- `--stat`: prints some run statistics on simulation exit

    ```commandline
    ~/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 --stat
    ```

- `--timelimit`: sets the number of wall clock seconds for the simulator to run, excluding startup and shutdown.

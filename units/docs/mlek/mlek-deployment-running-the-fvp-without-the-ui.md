---
id: "mlek-deployment-running-the-fvp-without-the-ui"
type: "concept"
domain: "edge-ai"
title: "Deployment: Fixed Virtual Platform / Running the FVP without the UI"
summary: "If there is a need to run the FVP without the UI (e.g. running the FVP inside a Docker container), it can be done as follows."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/deployment.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/deployment.md#running-the-fvp-without-the-ui"
license: "Apache-2.0"
mode: "V"
---

_Part of: Fixed Virtual Platform_

If there is a need to run the FVP without the UI (e.g. running the FVP inside a Docker container),
it can be done as follows.

#### Arm® Corstone™-300 and Arm® Corstone™-310

Add `-C mps3_board.visualisation.disable-visualisation=1` and `-C mps3_board.telnetterminal0.start_telnet=0`
to the command line arguments when starting the FVP. For example:

```commandline
FVP_install_location/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55 \
    -C mps3_board.visualisation.disable-visualisation=1 \
    -C mps3_board.telnetterminal0.start_telnet=0 \
    ./bin/mps3-sse-300/mlek_<use_case>.axf
   ```

#### Arm® Corstone™-315 and Arm® Corstone™-320

For an `MPS4` FVP, the arguments are similar. For example:

```commandline
FVP_install_location/models/Linux64_GCC-9.3/FVP_Corstone_SSE-315 \
    -C mps4_board.visualisation.disable-visualisation=1 \
    -C vis_hdlcd.disable_visualisation=1 \
    -C mps4_board.telnetterminal0.start_telnet=0 \
    ./bin/mps4-sse-315/mlek_<use_case>.axf
   ```

By default, there is no interaction on telnet needed and the application output can be directed to standard output by
using an FVP option:

- `-C mps3_board.uart0.out_file='-'` for MPS3 based FVPs, OR
- `-C mps4_board.uart0.out_file='-'` for MPS4 based FVPs.

Otherwise, once the FVP reports waiting on telnet connections, connect to the first server port from another terminal.
Assuming the FVP has the telnet server running at the default port 5000, connect to it by:

```commandline
telnet localhost 5000
```


> **NOTE**: Dockerfile, provided within the repository, contains useful environment variables pre-assigned with
> above arguments. These can be used directly from command-line. For example, to run MPS4 Arm® Corstone™-315 based
> application within the Docker container, the following command can be used to run the FVP in headless mode.
>
> ```commandline
> ${FVP_315_U65} -a <path/to/mlek_<use_case>.axf> ${FVP_315_ARGS}
> ```

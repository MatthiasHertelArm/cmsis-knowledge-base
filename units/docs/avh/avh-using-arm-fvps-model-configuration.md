---
id: "avh-using-arm-fvps-model-configuration"
type: "concept"
domain: "test"
title: "Using Arm FVPs: Model Configuration"
summary: "The operation of the FVP models can be configured at start-time by providing following command-line options:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/simulation/src/using.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/simulation/src/using.md#model-configuration"
license: "Apache-2.0"
mode: "V"
---

The operation of the FVP models can be configured at start-time by providing following command-line options:

- using `-C` (or `--parameter`) option to configure individual parameters.
- using option `-f` (or `--config-file`) followed by path to the text file with configuration parameters.

The configuration parameters are model-specific and follow syntax `instance.parameter= <value>`, where `instance`
specifies a simulated instance, such as CPU, interface, bus, memory, peripheral,  etc. and can be also hierarchical.

All parameters available for a target model including default setting and brief description can be obtained with the
command option `-l` (or `--list-params`). Because of the large number of parameters, it is convenient to print them
into a text file. For example:

```sh
FVP_Corstone_SSE-300_Ethos-U55 --list-params > config.txt
```

In a simple case, the configuration file for a Corstone-300 target could look like this:

```txt
# Parameters:
# instance.parameter=value       #(type, mode) default = 'def value' : description : [min..max]
#------------------------------------------------------------------------------
core_clk.mul=100000000                              # (int   , init-time) default = '0x17d7840' : Clock Rate Multiplier. This parameter is not exposed via CADI and can only be set in LISA
mps3_board.telnetterminal0.start_telnet=0           # (bool  , init-time) default = '1'      : Start telnet if nothing connected
mps3_board.uart0.out_file=-                         # (string, init-time) default = ''       : Output file to hold data written by the UART (use '-' to send all output to stdout)
mps3_board.visualisation.disable-visualisation=1    # (bool  , init-time) default = '0'      : Enable/disable visualisation
cpu0.semihosting-enable=1                           # (bool  , init-time) default = '0'      : Enable semihosting SVC traps. Applications that do not use semihosting must set this parameter to false.
#------------------------------------------------------------------------------
```

Where:

- `core_clk.mul=100000000` specifies the virtual time, in this case 100 MHz CPU clock.
- `mps3_board.telnetterminal0.start_telnet=0` disables the Telnet connectivity.
- `mps3_board.uart0.out_file=-` UART output is send to stdout.
- `mps3_board.visualisation.disable-visualisation=1` disables the graphical user interface of the FVP.
- `cpu0.semihosting-enable=1` enables semihosting in the FVP.

Note that instances implemented in the model can be obtained with the command option `--list-instances` that returns
instance names and corresponding model component type, version and brief description. Section
[Fast Models components](https://developer.arm.com/documentation/100964/latest/Fast-Models-components) explains all the
components available with Fast Model technology and can be used for finding more information about a specific instance
in the FVP.

For additional details, see chapter
[Configuring the model](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/Configuring-the-model)
in the Getting Started with Fixed Virtual Platforms Guide.

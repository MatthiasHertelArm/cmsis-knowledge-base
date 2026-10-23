---
id: "pyocd-target-support-target-types"
type: "concept"
domain: "debug"
title: "Target support: Target types"
summary: "When pyOCD connects to a device, it needs to know what type of device (target) it is controlling. The type of device is known as the \"target type\"."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/target_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/target_support.md#target-types"
license: "Apache-2.0"
mode: "V"
---

When pyOCD connects to a device, it needs to know what type of device (target) it is controlling.
The type of device is known as the "target type". The target type defines the flash programming
algorithm and determine the device's memory map and other important information. Each target type is
identified by a short string that is either the full or partial part number for the device. For
example, "k64f" or "stm32l072".

Target types are either built-in to pyOCD or come from CMSIS-Packs. The sections below describe more
about the sources of target support.

To see the available target types you can run `pyocd list --targets`. This command will print a
table of supported target types, including the target name, vendor, and part number. In addition, it
prints whether each target target is built-in or comes from a CMSIS-Pack.


### Generic target type

PyOCD furnishes a generic target type named "cortex_m". This target type will be able to connect to
and debug almost any Cortex-M device that correctly implements the CoreSight architecture. However,
flash memory cannot be programmed, and a memory map is not provided. In addition, it may not work
for certain devices that require special handling of operations such as reset and halt.

Because of the limitations of the generic "cortex_m" target, the warning shown below will be logged
if the target type is "cortex_m".

    0000183:WARNING:board:Generic cortex_m target type is selected; is this intentional? You will be
    able to debug but not program flash. To set the target type use the '--target' argument or
    'target_override' option. Use 'pyocd list --targets' to see available targets.


### Setting the target type

There are two ways to specify the target type.

The first is to pass the `--target` command line argument to the `pyocd` tool and pass the target
type name. This argument must be passed every time you run `pyocd` with a subcommand that connects
to the target.

Another method is to set the `target_override` session option in a `pyocd.yaml` configuration file. The
[configuration file documentation]({% link _docs/configuration.md %}) describes how to do this for a specific debug
probe instead of globally.


### Target type auto-detection

Certain on-board debug probes know the type of target with which they are connected. The Arm DAPLink
and STLinkV2-1 firmwares both support this feature. When using a probe with target type
auto-detection, you do not need to tell pyOCD

To check whether your debug probe supports auto-detection, run `pyocd list`. This command prints
a list of all connected debug probes. If a probe does not support auto-detection, the name of the
probe firmware is printed. Whereas probes that do support auto-detection will show up with the
name of the board plus the target type in brackets.

Example probe listing:

      #   Probe/Board                       Unique ID                                          Target
    --------------------------------------------------------------------------------------------------------------------
      0   Arm DAPLink CMSIS-DAP             02400b0129164e4500440012706e0007f301000097969900   ✔︎ k64f
          NXP                               FRDM-K64F

      1   STLINK-V3                         002500074741500420383733                           ✖︎ stm32u585aiix
          B-U585I-IOT02A

      2   STM32 STLink                      066EFF555051897267233656                           ✔︎ stm32l475xg
          DISCO-L475VG-IOT01A

      3   Segger J-Link OB-K22-NordicSemi   960177309                                          n/a


This example shows several connected debug probes. The first supports extended auto-detection with automatic target type reporting. The second and third support board type detection using pyOCD's built-in table of board types, and show both an installed and uninstalled target type. Finally, the fourth probe does not support auto-detection.
Note how the descriptions of all but the last probe show the name of the board and the target type, for instance
"stm32l475xg" in the "Target" column.

If the target type is *not* auto-detected, it will default to "cortex_m" unless specified as
described above (see [Generic target type](#generic_target_type) above). In this case, the "Target" column will show "n/a".

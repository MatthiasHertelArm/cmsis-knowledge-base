---
id: "pyocd-debug-probes-listing-available-debug-probes"
type: "concept"
domain: "debug"
title: "Debug probes: Listing available debug probes"
summary: "To view the connected probes and their unique IDs, run pyocd list. This command will produce output looking like this:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/debug_probes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/debug_probes.md#listing-available-debug-probes"
license: "Apache-2.0"
mode: "V"
---

To view the connected probes and their unique IDs, run `pyocd list`. This command will produce output looking like this:

      #   Probe/Board                       Unique ID                                          Target
    --------------------------------------------------------------------------------------------------------------------
      0   Arm DAPLink CMSIS-DAP             02400b0129164e4500440012706e0007f301000097969900   ✔︎ k64f
          NXP                               FRDM-K64F

      1   STLINK-V3                         002500074741500420383733                           ✖︎ stm32u585aiix
          B-U585I-IOT02A

      2   STM32 STLink                      066EFF555051897267233656                           ✔︎ stm32l475xg
          DISCO-L475VG-IOT01A

      3   Segger J-Link OB-K22-NordicSemi   960177309                                          n/a


The output is divided into columns for the probe number, probe name, unique ID, and default target type name.
Probes that have additional board identification will have a second row with the board name and possibly board
vendor.

The "Target" column shows the debug probe's default target type for debug probes that support automatic target
type reporting. Whether that target type is installed and available for use is shown by a check or "X" mark
before the target type name (and in different colours, if colour output is enabled). If an "X" mark is
displayed, see the [target support documentation]({% link _docs/target_support.md %}) for information about
how you can install that the target type.

For debug probes that do not support automatic target type reporting, the Target column will simply display
"n/a". This can be seen above for the "Segger J-Link OB-K22-NordicSemi" probe. The target type must be
specified manually in such cases, otherwise full functionality, such as flash programming, will not be
available.

In any case, whether required because the probe doesn't have a default, or to override the default, the target
type can be specified either on the command line with the `-t` / `--target` argument, or by setting the
`target_override` session option (e.g., in a [config file]({% link _docs/configuration.md %}#config_file)).

Note that the printed list includes only those probes that pyOCD can actively query for, which currently means
only USB based probes.

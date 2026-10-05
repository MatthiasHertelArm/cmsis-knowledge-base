---
id: "zep-input-and-output-files-input-files"
type: "concept"
domain: "project"
title: "Input and output files: Input files"
summary: "There are four types of devicetree input files:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/intro-input-output.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/intro-input-output.rst"
license: "Apache-2.0"
mode: "V"
---

There are four types of devicetree input files:

- sources (`.dts`)
- includes (`.dtsi`)
- overlays (`.overlay`)
- bindings (`.yaml`)

The devicetree files inside the `zephyr` directory look like this:

```none

boards/<ARCH>/<BOARD>/<BOARD>.dts
dts/common/skeleton.dtsi
dts/<ARCH>/.../<SOC>.dtsi
dts/bindings/.../binding.yaml
```
Generally speaking, every supported board has a `BOARD.dts` file
describing its hardware. For example, the `reel_board` has
`boards/phytec/reel_board/reel_board.dts`.

`BOARD.dts` includes one or more `.dtsi` files. These `.dtsi` files
describe the CPU or system-on-chip Zephyr runs on, perhaps by including other
`.dtsi` files. They can also describe other common hardware features shared by
multiple boards. In addition to these includes, `BOARD.dts` also describes
the board's specific hardware.

The `dts/common` directory contains `skeleton.dtsi`, a minimal
include file for defining a complete devicetree. Architecture-specific
subdirectories (`dts/<ARCH>`) contain `.dtsi` files for CPUs or SoCs
which extend `skeleton.dtsi`.

The C preprocessor is run on all devicetree files to expand macro references,
and includes are generally done with `#include <filename>` directives, even
though DTS has a `/include/ "<filename>"` syntax.

`BOARD.dts` can be extended or modified using *overlays*. Overlays are
also DTS files; the `.overlay` extension is just a convention which makes
their purpose clear. Overlays adapt the base devicetree for different purposes:

- Zephyr applications can use overlays to enable a peripheral that is disabled
  by default, select a sensor on the board for an application specific purpose,
  etc. Along with kconfig, this makes it possible to reconfigure the
  kernel and device drivers without modifying source code.

- Overlays are also used when defining shields.

The build system automatically picks up `.overlay` files stored in
certain locations. It is also possible to explicitly list the overlays to
include, via the `DTC_OVERLAY_FILE` CMake variable. See
set-devicetree-overlays for details.

The build system combines `BOARD.dts` and any `.overlay` files by
concatenating them, with the overlays put last. This relies on DTS syntax which
allows merging overlapping definitions of nodes in the devicetree. See
dt_k6x_example for an example of how this works (in the context of
`.dtsi` files, but the principle is the same for overlays). Putting the
contents of the `.overlay` files last allows them to override
`BOARD.dts`.

dt-bindings (which are YAML files) are essentially glue. They describe
the contents of devicetree sources, includes, and overlays in a way that allows
the build system to generate C macros usable by device drivers and
applications. The `dts/bindings` directory contains bindings.

---
id: "zep-board-porting-guide-transition-to-the-current-hardware-model"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Transition to the current hardware model"
summary: "Shortly after Zephyr 3.6.0 was released, a new hardware model was introduced to Zephyr."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Shortly after Zephyr 3.6.0 was released, a new hardware model was introduced to
Zephyr. This new model overhauls the way both SoCs and boards are named and
defined, and adds support for features that had been identified as important
over the years. Among them:

- Support for multi-core, multi-arch AMP (Asymmetrical Multi Processing) SoCs
- Support for multi-SoC boards
- Support for reusing the SoC and board Kconfig trees outside of the Zephyr
  build system
- Support for advanced use cases with sysbuild
- Removal of all existing arbitrary and inconsistent uses of Kconfig and folder
  names

All the documentation in this page refers to the current hardware model. Please
refer to the documentation in Zephyr v3.6.0 (or earlier) for information on the
previous, now obsolete, hardware model.

More information about the rationale, development and concepts behind the new
model can be found in the `original issue <51831>`, the
`original Pull Request <50305>` and, for a complete set of changes
introduced, the hardware model v2 commit.

Some non-critical features, enhancements and improvements of the new hardware
model are still in development. Check the
`hardware model v2 enhancements issue <69546>` for a complete list.

The transition from the previous hardware model to the current one (commonly
referred to as "hardware model v2") requires modifications to all existing board
and SoC definitions. A decision was made not to provide direct backwards
compatibility for the previous model, which leaves users transitioning from a
previous version of Zephyr to one including the new model (v3.7.0 and onwards)
with two options if they have an out-of-tree board (or SoC):

#. Convert the out-of-tree board to the current hardware model (recommended)
#. Take the SoC definition from Zephyr v3.6.0 and copy it to your downstream
   repository (ensuring that the build system can find it via a
   zephyr module or `SOC_ROOT`). This will allow your board,
   defined in the previous hardware model, to continue to work

When converting your board from the previous to the current hardware model, we
recommend first reading through this page to understand the model in detail. You
can then use the example-application conversion Pull Request as an example on
how to port a simple board. Additionally, a conversion script is available
and works reliably in many cases (though multi-core SoCs may not be handled
entirely). Finally, the hardware model v2 commit contains the full conversion
of all existing boards from the old to the current model, so you can use it as a
complete conversion reference.

---
id: "zep-arm-cortex-m-developer-guide-floating-point-services"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / Floating point Services"
summary: "Both unshared and shared FP registers mode are supported in Cortex-M (see float_v2 for more details)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

Both unshared and shared FP registers mode are supported in Cortex-M (see
float_v2 for more details).

When FPU support is enabled in the build
(`CONFIG_FPU` is enabled), the
sharing FP registers mode (`CONFIG_FPU_SHARING`)
is enabled by default. This is done as some compiler configurations
may activate a floating point context by generating FP instructions
for any thread, regardless of whether floating point calculations are
performed, and that context must be preserved when switching such
threads in and out.

The developers can still disable the FP sharing mode in their
application projects, and switch to Unshared FP registers mode,
if it is guaranteed that the image code does not generate FP
instructions outside the single thread context that is allowed
(and supposed) to do so.

Under FPU sharing mode, the callee-saved FPU registers are saved
and restored in context-switch, if the corresponding threads have
an active FP context. This adds some runtime overhead on the swap
routine. In addition to the runtime overhead, the sharing FPU mode

* requires additional memory for each thread to save the callee-saved
  FP registers
* requires additional stack memory for each thread, to stack the caller-saved
  FP registers, upon exception entry, if an FP context is active. Note, however,
  that since lazy stacking is enabled, there is no runtime overhead of FP context
  stacking in regular interrupts (FP state preservation is only activated in the
  swap routine in PendSV interrupt).

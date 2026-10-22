---
id: "ethu-driver-driver-bring-up-checklist"
type: "concept"
domain: "edge-ai"
title: "Driver: Driver bring-up checklist"
summary: "Use this checklist after initializing the driver and before integrating large application graphs:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/driver/src/main.md#driver-bring-up-checklist"
license: "Apache-2.0"
mode: "V"
---

Use this checklist after initializing the driver and before integrating large
application graphs:

- Confirm the NPU identity and MAC configuration reported by
  ethosu_get_hw_info() match the target used to
  compile the ML model for the device.
- Confirm the command stream and every used base-pointer region are accessible
  to the NPU. Review Command
  stream regions and base pointers
  and Configure memory placement and the linker script.
- Route the NPU interrupt to
  ethosu_irq_handler() and exercise an inference
  timeout. If the wait does not complete, follow
  Troubleshoot an inference that does not complete.
- Verify cache cleaning and invalidation with caches enabled, not only disabled.
  See Data caching.
- Check ethosu_address_remap() for TCM or aliased
  memory windows. See Platform-specific functions.
- Start with one known-good, fully supported model before testing a large graph.
  Use the recovery and isolation guidance in
  Troubleshoot an inference that does not complete.
- Use PMU cycle, activity, stall,
  and memory events when validating performance or investigating a difference
  from compiler estimates.
- Enable driver logging and capture fault information
  before resetting the NPU after an error.

After these driver checks, continue with the end-to-end
Integration workflow
and Validate and tune
before treating platform bring-up as complete.

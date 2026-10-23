---
id: "x-cmsis-debug-live-4"
type: "troubleshooting"
domain: "debug"
title: "Reads rejected while target is running"
status: "draft"
symptoms: ["[TARGET_RUNNING]"]
extracted_from: "proc-cmsis-debug-live"
source: "cmsis-debug-live/SKILL.md"
license: "Apache-2.0"
---

running rejects step_over, step_into, step_out, continue_execution, read_memory, read_core_registers, read_peripheral_register, read_cycle_counter, get_fault_info, diagnose_fault, evaluate_expression, get_call_stack, get_frame_variables, get_threads, list_variable_names and get_variables_values: call pause_execution first.

---
id: "etarm-executorch-arm-backend-profiling-of-vgf-backend"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend: Profiling of VGF Backend"
summary: "VGF profiling now emits both host-side ExecuTorch event tracer ranges and Vulkan timestamp-query measurements. The host ranges split init into VGF_INIT phases, including VGF_INIT_CREATE_DATA_GRAPH_PIPELINE, and split execute into VGF_COPY_INPUTS, VGF_QUEUE_SUBMIT, VGF_QUEUE_WAIT_IDLE, VGF_TIMESTAMP_QUERY_READBACK, VGF_DISPATCH_AND_WAIT, and VGF_COPY_OUTPUTS."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/backends/arm/README.md#profiling-of-vgf-backend"
license: "BSD-3-Clause"
mode: "V"
---

VGF profiling now emits both host-side ExecuTorch event tracer ranges and Vulkan timestamp-query measurements. The host ranges split init into `VGF_INIT_*` phases, including `VGF_INIT_CREATE_DATA_GRAPH_PIPELINE`, and split execute into `VGF_COPY_INPUTS`, `VGF_QUEUE_SUBMIT`, `VGF_QUEUE_WAIT_IDLE`, `VGF_TIMESTAMP_QUERY_READBACK`, `VGF_DISPATCH_AND_WAIT`, and `VGF_COPY_OUTPUTS`. Vulkan timestamp queries are inserted into the recorded VGF command buffer around `vkCmdDispatchDataGraphARM()`, producing `VGF_DATA_GRAPH_DEVICE_TIME`, which measures device-side elapsed time for the submitted data-graph command buffer region. To collect a profile, build the VGF runner with event tracing enabled, run the model with an ETDump path, then convert the ETDump to Chrome trace JSON:

```bash
mkdir -p etdumps traces

./cmake-out-vgf/executor_runner \
  --model_path vgf_mobilenetv2_out/mobilenet_v2_vgf_int8.pte \
  --num_executions 10 \
  --etdump_path ./etdumps/vgf_timestamps.etdp \
  --print_output none

python ./backends/arm/scripts/etdump_to_chrome_trace.py \
  --etdump_path ./etdumps/vgf_timestamps.etdp \
  --output ./etdumps/vgf_timestamps_trace.json
```

Open the result in Chrome by navigating to `chrome://tracing`, selecting **Load**, and choosing `./traces/vgf_timestamps_trace.json`. The key fields to inspect are `VGF_INIT_CREATE_DATA_GRAPH_PIPELINE` for pipeline creation/init cost, `VGF_QUEUE_SUBMIT` and `VGF_QUEUE_WAIT_IDLE` for host-side submission/wait overhead, and `VGF_DATA_GRAPH_DEVICE_TIME` for device-side data-graph execution time.

VGF profiling can emit optional Vulkan timestamp-query measurements. Vulkan timestamp queries are controlled by the `EXECUTORCH_VGF_ENABLE_TIMESTAMP_QUERIES` environment variable. Set it to `1` to insert timestamp queries into the recorded VGF command buffer around `vkCmdDispatchDataGraphARM()`. When enabled, the backend emits `VGF_DATA_GRAPH_DEVICE_TIME`, which measures device-side elapsed time for the submitted data-graph command buffer region. If `EXECUTORCH_VGF_ENABLE_TIMESTAMP_QUERIES` is unset or set to `0`, only host-side ExecuTorch event tracer ranges are collected and no Vulkan timestamp-query readback is performed. Note that the timestamp-query measurements will be printed out and not included into `.etdp`.

So, in this case the command is:

```bash
EXECUTORCH_VGF_ENABLE_TIMESTAMP_QUERIES=1 \
./cmake-out-vgf/executor_runner \
  --model_path vgf_mobilenetv2_out/mobilenet_v2_vgf_int8.pte \
  --num_executions 10 \
  --etdump_path ./etdumps/vgf_timestamps.etdp \
  --print_output none
```

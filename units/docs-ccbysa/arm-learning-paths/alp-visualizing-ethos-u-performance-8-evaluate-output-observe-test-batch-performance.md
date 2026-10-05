---
id: "alp-visualizing-ethos-u-performance-8-evaluate-output-observe-test-batch-performance"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Evaluate Ethos-U Performance: Observe Test Batch Performance"
summary: "By default, run.sh (and the underlying ethos_u_runner) uses: - A constant input tensor, usually filled with zeros, ones, or random-ish synthetic data - Input shape matches MobileNet V2: typically [1, 3, 224, 224] (batch size 1, 3 RGB …"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output/#observe-test-batch-performance"
license: "CC-BY-SA-4.0"
mode: "V"
---

By default, `run.sh` (and the underlying ethos_u_runner) uses:
- A constant input tensor, usually filled with zeros, ones, or random-ish synthetic data
- Input shape matches MobileNet V2: typically `[1, 3, 224, 224]` (batch size 1, 3 RGB channels, 224×224 image)
- Input tensor size: `1 × 3 × 224 × 224 × 1 byte = 150528 bytes ≈ 147 KB`
  ```bash { output_lines = "1" }
  Input   SRAM bandwidth = 15.49 MB/batch
  ```
- `Batch Inference time` gives you a single performance metric for the Ethos-U85 (versus other [Ethos-U NPUs](https://developer.arm.com/Processors#q=Ethos-U&aq=%40navigationhierarchiescategories%3D%3D%22Processor%20products%22%20AND%20%40navigationhierarchiescontenttype%3D%3D%22Product%20Information%22&numberOfResults=48))
   ```bash { output_lines = "1" }
   Batch Inference time                 4.94 ms,  202.34 inferences/s (batch size 1)
   ```

**Test Batch Performance:**
```bash { output_lines = "1-34" }
Network summary for out
Accelerator configuration               Ethos_U85_128
System configuration             Ethos_U85_SYS_DRAM_Mid
Memory mode                                 Sram_Only
Accelerator clock                                1000 MHz
Design peak SRAM bandwidth                      29.80 GB/s

Total SRAM used                               5178.77 KiB

CPU operators = 0 (0.0%)
NPU operators = 64 (100.0%)

Average SRAM bandwidth                           7.21 GB/s
Input   SRAM bandwidth                          15.49 MB/batch
Weight  SRAM bandwidth                          11.87 MB/batch
Output  SRAM bandwidth                           6.66 MB/batch
Total   SRAM bandwidth                          35.65 MB/batch
Total   SRAM bandwidth            per input     35.65 MB/inference (batch size 1)

Neural network macs                         300836992 MACs/batch

Info: The numbers below are internal compiler estimates.
For performance numbers the compiled network should be run on an FVP Model or FPGA.

Network Tops/s                                   0.12 Tops/s

NPU cycles                                    4832315 cycles/batch
SRAM Access cycles                            1168037 cycles/batch
DRAM Access cycles                                  0 cycles/batch
On-chip Flash Access cycles                         0 cycles/batch
Off-chip Flash Access cycles                        0 cycles/batch
Total cycles                                  4942076 cycles/batch

Batch Inference time                 4.94 ms,  202.34 inferences/s (batch size 1)
```

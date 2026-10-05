---
id: "vela-vela-performance-estimations"
type: "concept"
domain: "edge-ai"
title: "Vela Performance Estimations"
summary: "A performance estimation summary is reported after compilation."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:PERFORMANCE.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/PERFORMANCE.md"
license: "Apache-2.0"
mode: "V"
---

A performance estimation summary is reported after compilation.  The cycle and
bandwidth numbers should not be taken as accurate representations of real
performance numbers and they should not be compared against those from other
compilations that use different settings or configurations.  The numbers
reported allow the compiler to make its optimisation decisions only.  For
accurate performance numbers the network should be run and profiled on an FPGA.
For approximate performance numbers the network can be run on a Fixed
Virtual Platform (FVP) Model.

The following is a description of the fields reported in the performance
estimation summary.  This summary is also printed to a csv in the output
directory.

The following is an example of the output.
```
$ vela my_network.tflite

Network summary for my_network
Accelerator configuration               Ethos_U55_256
System configuration                 internal-default
Memory mode                          internal-default
Accelerator clock                                 500 MHz
Design peak SRAM bandwidth                       4.00 GB/s
Design peak Off-chip Flash bandwidth             0.50 GB/s

Total SRAM used                                  0.95 KiB
Total Off-chip Flash used                      106.98 KiB

CPU operators = 0 (0.0%)
NPU operators = 44 (100.0%)

Average SRAM bandwidth                           0.04 GB/s
Input   SRAM bandwidth                           0.01 MB/batch
Weight  SRAM bandwidth                           0.00 MB/batch
Output  SRAM bandwidth                           0.00 MB/batch
Total   SRAM bandwidth                           0.01 MB/batch
Total   SRAM bandwidth            per input      0.01 MB/inference (batch size 1)

Average Off-chip Flash bandwidth                 0.46 GB/s
Input   Off-chip Flash bandwidth                 0.01 MB/batch
Weight  Off-chip Flash bandwidth                 0.09 MB/batch
Output  Off-chip Flash bandwidth                 0.00 MB/batch
Total   Off-chip Flash bandwidth                 0.10 MB/batch
Total   Off-chip Flash bandwidth  per input      0.10 MB/inference (batch size 1)

Neural network macs                             86952 MACs/batch
```

To display internal cycle estimates for the network use the CLI option
`--verbose-cycle-estimate`.  

```
Info: The numbers below are internal compiler estimates.
For performance numbers the compiled network should be run on an FVP Model or FPGA.

Network Tops/s                                   0.00 Tops/s

NPU cycles                                      21298 cycles/batch
SRAM Access cycles                               2261 cycles/batch
DRAM Access cycles                                  0 cycles/batch
On-chip Flash Access cycles                         0 cycles/batch
Off-chip Flash Access cycles                   112755 cycles/batch
Total cycles                                   114098 cycles/batch

Batch Inference time                 0.23 ms, 4382.18 inferences/s (batch size 1)
```

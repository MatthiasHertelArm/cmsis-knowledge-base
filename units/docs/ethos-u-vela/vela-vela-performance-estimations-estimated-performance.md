---
id: "vela-vela-performance-estimations-estimated-performance"
type: "concept"
domain: "edge-ai"
title: "Vela Performance Estimations: Estimated performance"
summary: "_NOTE: This is only an estimate. For performance numbers we recommend running the compiled network on an FVP Model or FPGA."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:PERFORMANCE.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/PERFORMANCE.md#estimated-performance"
license: "Apache-2.0"
mode: "V"
---

__NOTE: This is only an estimate. For performance numbers we recommend running
the compiled network on an FVP Model or FPGA.__  

The final sections show the estimated required compute power and performance
for the network.  

This section is only visible if the CLI option `--verbose-cycle-estimate` is provided.  

```
Network Tops/s                                   0.00 Tops/s

NPU cycles                                      21298 cycles/batch
SRAM Access cycles                               2261 cycles/batch
DRAM Access cycles                                  0 cycles/batch
On-chip Flash Access cycles                         0 cycles/batch
Off-chip Flash Access cycles                   112755 cycles/batch
Total cycles                                   114098 cycles/batch

Batch Inference time                 0.23 ms, 4382.18 inferences/s (batch size 1)
```

### Network Tops/s

This shows the estimated TOPs/s for the network, which is an alternative
representation of [Neural network MACs](#Neural-network-MACs)

### Cycles

This shows the estimated number of cycles per batch for NPU, memory accesses
and in total. The total is the sum of the single action that consumes the most
cycles per pass, i.e. if memory access consumes the most cycles for a pass
only that will account for the pass cycles in the total.  
To clarify: for each type of cycle counts, the number of cycles per batch is the
sum of cycle counts for each layer, where each layer's cycle count is based on
the maximal processing path.  
A layer consists of a feature map and an operator. For example, if the DMA
transfer for a feature map requires less cycles than the cycles for the
operation, then the DMA cycles will not contribute to the layer cycle count.
As a result, it will not be part of the summed SRAM or DRAM access cycles.  
Looking at the example above in [Estimated performance](#Estimated-performance),
the zero cycle count for DRAM Access cycles means that either there was no DRAM
access or, like in our previously described example, the DMA cycles were fewer
than for the operation for every layer that required a DMA transfer.

### Batch Inference time

This shows the estimated inference time and inferences per second per batch.

# Vela Performance Estimation Per-Layer

This section describes the per-layer performance output that is printed when the
--verbose-performance option is used. This is also printed to a csv file in the
output directory.

The following is an example of the output:

```
################################################################################
Performance for NPU Subgraph _split_1
TFLite_operator      NNG Operator         NPU_OP                   SRAM Usage  Peak%  Op Cycles Network%        NPU    SRAM AC    DRAM AC OnFlash AC OffFlash AC  MAC Count Network%  Util% Name
-------------------- -------------------- ------------------------ ---------- ------ ---------- -------- ---------- ---------- ---------- ---------- ----------- ---------- -------- ------ --------------------
CONV_2D              Conv2DBias           NPU_OP_CONV                  629616  86.18    1889913    46.80    1889913      21504          0          0           0   99090432    49.99  20.48 ResNet18/activation_32/Relu;ResNet18/batch_normalization_32/FusedBatchNormV3;ResNet18/conv2d_38/BiasAdd/ReadVariableOp/resource;ResNet18/conv2d_38/BiasAdd;ResNet18/conv2d_39/Conv2D;ResNet18/conv2d_38/Conv2D1
CONV_2D              Conv2DBias           NPU_OP_CONV                  730624 100.00    2127584    52.69    2127584      21504          0          0           0   99090432    49.99  18.19 ResNet18/batch_normalization_33/FusedBatchNormV3;ResNet18/conv2d_39/BiasAdd/ReadVariableOp/resource;ResNet18/conv2d_39/BiasAdd;ResNet18/conv2d_39/Conv2D
ADD                  Add                  NPU_OP_ELEMENTWISE            43008   5.89      16128     0.40      16128       8064          0          0           0          0     0.00   0.00 ResNet18/activation_33/Relu;ResNet18/add_15/add
AVERAGE_POOL_2D      AvgPool              NPU_OP_POOL                   27648   3.78       4224     0.10       2200       4224          0          0           0      24576     0.01   2.27 ResNet18/average_pooling2d_1/AvgPool
```

The columns in the above output have the following meaning:

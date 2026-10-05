---
id: "mlek-memory-considerations-memory-constraints"
type: "concept"
domain: "edge-ai"
title: "Memory considerations: Memory constraints"
summary: "Both the MPS3 Fixed Virtual Platform (FVP) and the MPS3 FPGA platform share the linker script for Arm® Corstone™-300 design. The CMake configuration parameter TARGET_SUBSYSTEM sets the design, which is described in: build options."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/memory_considerations.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/memory_considerations.md#memory-constraints"
license: "Apache-2.0"
mode: "V"
---

Both the MPS3 Fixed Virtual Platform (FVP) and the MPS3 FPGA platform share the linker script for Arm® *Corstone™-300*
design. The CMake configuration parameter `TARGET_SUBSYSTEM` sets the design, which is described in:
[build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./building.md#build-options).

The memory map exposed by this design is located in the [Appendix](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./appendix.md#appendix), and can be used as a reference when
editing the linker script. This is useful to make sure that the region boundaries are respected. The snippet from the
scatter file is as follows:

```log
;---------------------------------------------------------
; First load region (ITCM)
;---------------------------------------------------------
LOAD_REGION_0       0x00000000                  0x00080000
{

...

    ;-----------------------------------------------------
    ; SSE-300's internal SRAM of 4MiB - reserved for
    ; activation buffers.
    ; This region should have 3 cycle read latency from
    ; both Cortex-M55 and Ethos-U NPU
    ;-----------------------------------------------------
    isram.bin       0x31000000  UNINIT ALIGN 16 0x00400000
    {
        ; Cache area (if used)
        *.o (.bss.NoInit.ethos_u_cache)

        ; activation buffers a.k.a tensor arena when memory mode sram only
        *.o (.bss.NoInit.activation_buf_sram)
    }
}

;---------------------------------------------------------
; Second load region (DDR)
;---------------------------------------------------------
LOAD_REGION_1       0x70000000                  0x02000000
{
    ;-----------------------------------------------------
    ; 32 MiB of DDR space for neural network model,
    ; input vectors and labels. If the activation buffer
    ; size required by the network is bigger than the
    ; SRAM size available, it is accommodated here.
    ;-----------------------------------------------------
    ddr.bin        0x70000000 ALIGN 16         0x02000000
    {
        ; nn model's baked in input matrices
        *.o (ifm)

        ; nn model's default space
        *.o (nn_model)

        ; labels
        *.o (labels)

        ; activation buffers a.k.a tensor arena when memory mode dedicated sram
        *.o (activation_buf_dram)
    }

...

}

```

> **Note:** With Arm® *Corstone™-300* FPGA and FVP implementations, only the BRAM, internal SRAM, and DDR memory regions
> are accessible to the Arm® Ethos™-U NPU block.

In the preceding snippet, the internal SRAM region memory is utilized by the activation buffers with a limit of 4MiB. If
used by a Vela optimized neural network model, then the Arm® *Ethos™-U* NPU writes to this block frequently.

A bigger region of memory for storing the neural network model is placed in the DDR, or flash, region under
`LOAD_REGION_1`. The two load regions are necessary as the motherboard configuration controller of the MPS3 limits the
load size at address `0x00000000` to 1MiB. This has implications on how the application **is deployed** on MPS3, as
explained under the following section: [Deployment on MPS3](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./deployment.md#mps3-fpga-board).

The next section of the documentation covers: [Troubleshooting](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/troubleshooting.md).

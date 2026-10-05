---
id: "alp-alif-dual-npu-vision-understand-architecture-understand-the-memory-layout"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: Understand the memory layout"
summary: "The application separates persistent artifacts, CPU-private state, display and video buffers, and U85-visible working memory."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#understand-the-memory-layout"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application separates persistent artifacts, CPU-private state, display and video buffers, and U85-visible working memory.

(figure: Memory diagram showing models and firmware in MRAM, U55 state in HP DTCM, U55 temporary storage in SRAM0, and the display, U85 working memory, and camera buffers in SRAM1.#center)

### Persistent MRAM payload

SETOOLS writes `model_assets.bin` at `0x80008000` and the execute-in-place Zephyr image at `0x80400000`:

| Address range | Size | Contents |
| --- | ---: | --- |
| `0x80008000`-`0x8035816F` | 3,473,776 bytes | Ethos-U85 MobileNetV2 PTE |
| `0x80358170`-`0x803A1ACF` | 301,408 bytes | Ethos-U55 SSD-Slim PTE |
| `0x803A1AD0`-`0x803BCB05` | 110,646 bytes | Grace Hopper startup image |
| `0x803BCB06`-`0x803BF3FD` | 10,488 bytes | ImageNet class labels |
| From `0x80400000` | Build-dependent | RTSS-HP Zephyr firmware |

The combined `model_assets.bin` payload is 3,896,318 bytes. CMake packs both PTE files first, followed by the startup image and the labels. CMake then generates a header containing the artifact sizes. Changing a model causes CMake to reconfigure so the compiled offsets can't silently disagree with the payload.

### HP DTCM

The 1 MiB HP DTCM region starts at `0x20000000`. It contains the following:

- 640 KiB U55 method pool
- Both 4 KiB metadata pools
- The fast-scratch arrays
- Zephyr worker stacks
- Semaphores
- Driver objects
- ISP library state

The larger U55 temporary arena is placed in SRAM0. The linker can move individual DTCM symbols as code changes, so the application fixes their sizes rather than their exact addresses.

### Shared SRAM0

SRAM0 spans from `0x02000000` to `0x023FFFFF`. The validated build dedicates most of it to the U55 delegate scratch arena:

| Address range | Reserved size | Use |
| --- | ---: | --- |
| `0x02000000`-`0x02383FFF` | 3,686,400 bytes | U55 temporary allocator pool |

SSD-Slim requires a larger delegated scratch plan than the earlier face detector. Keeping this arena outside HP DTCM leaves enough private memory for the method pool and Zephyr runtime.

### Shared SRAM1

SRAM1 spans from `0x02400000` to `0x027FFFFF` and holds the display, U85-visible working set, and camera buffers:

| Address range | Size | Use |
| --- | ---: | --- |
| `0x02400000`-`0x024BB7FF` | 768,000 bytes | CDC200 480 x 800 RGB565 framebuffer |
| `0x024BB800`-`0x025437FF` | 557,056 bytes | U85 command and weight mirror reservation |
| `0x02543800`-`0x026B424F` | 1,509,968 bytes | U85 temporary allocator pool |
| `0x026B4250`-`0x026F024F` | 304 KiB | U85 ExecuTorch method pool |
| `0x02700250`-`0x0278C24F` | 560 KiB | Five-buffer Zephyr video heap |

The active ISP output uses five 192 x 192 x 3-byte RGB888 buffers. Each buffer is 110,592 bytes. The heap allows up to 114,688 bytes per buffer. When its original address isn't directly usable by U85, the backend copies delegated command or weight data into the mirror reservation. Shared SRAM also avoids consuming the limited HP DTCM with the U85 working set.

---
id: "intr-reproducible-firmware-builds-why-does-only-one-of-the-builds-crash"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible / Why does only one of the builds crash?!"
summary: "A full discussion of how to debug the crash is outside the scope of this article but can be found in this post."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#why-does-only-one-of-the-builds-crash"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Making a Build Reproducible_

A full discussion of how to debug the crash is outside the scope of this article but can be found in [this post](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#debugger-plugins).

We examine the Configurable Fault Status Register (CFSR) and can see that a UsageFault has taken place:

```bash
(gdb) svd SCB CFSR_UFSR_BFSR_MMFSR
Fields in SCB CFSR_UFSR_BFSR_MMFSR:
[...]
    UNALIGNED:    1  Unaligned access usage fault
[...]
```

We can examine the frame captured in the `my_fault_handler_c` handler and see that the UsageFault was triggered by an unaligned store to a 64 bit pointer.

```bash
(gdb) p/a *frame
$5 = {
  r0 = 0x200001ca <s_heap>,
  r1 = 0x1 <g_pfnVectors+1>,
  r2 = 0x200001ca <s_heap>,
  r3 = 0x0 <g_pfnVectors>,
  r12 = 0x0 <g_pfnVectors>,
  lr = 0x89 <prvQueuePingTask+24>,
  return_address = 0x8c <prvQueuePingTask+28>,
  xpsr = 0x81000000
}
(gdb) list *frame->return_address
0x8c is in prvQueuePingTask (/private/tmp/dev/interrupt/example/reproducible-build/main.c:33).
28    xNextWakeTime = xTaskGetTickCount();
29
30    uint64_t *total_queue_sends = minimal_heap_malloc(sizeof(uint64_t));
31
32    while (1) {
==> CRASH WAS HERE:
33      (*total_queue_sends)++;
34      vTaskDelayUntil(&xNextWakeTime, mainQUEUE_SEND_FREQUENCY_MS);
35      xQueueSend(xQueue, total_queue_sends, 0U);
36    }
```

The pointer which caused the bad store comes from the call to `minimal_heap_malloc()`. Let's take a look at that C file:

```c
#include "minimal_heap.h"

#include <stdbool.h>
#include <stdint.h>

#define MINIMAL_HEAP_TOTAL_SIZE 16

typedef struct {
  uint8_t heap[MINIMAL_HEAP_TOTAL_SIZE];
  bool space_free;
} sMinimalHeapContext;

static sMinimalHeapContext s_heap = {
  .space_free = true,
};

void *minimal_heap_malloc(size_t size) {
  if (!s_heap.space_free || size > MINIMAL_HEAP_TOTAL_SIZE) {
    return NULL;
  }
  s_heap.space_free = false;
  return &s_heap.heap[0];
}

void minimal_heap_free(void) {
  s_heap.space_free = true;
}
```

So allocations are always from the address of `s_heap.heap[0]`. We can take a look at where that address is in GDB:

```
(gdb) p &s_heap.heap
$6 = (uint8_t (*)[16]) 0x200001ca <s_heap>
```

We'll that's a bug! Our minimal malloc implementation is handing out pointers that are not 8 byte aligned. We can fix the issue by either making `heap` a `uint64_t` or leveraging the aligned attribute (`__attribute__((aligned(8)))`) to ensure our structure is always aligned on a 8 byte boundary. Let's at least apply a fix for the bug we encountered:

```bash
$ cd /private/tmp/dev/interrupt/example/reproducible-build/
$ git apply 01-fix-alignment.patch
$ cd /private/tmp/repos/interrupt/example/reproducible-build/
$ git apply 01-fix-alignment.patch
```

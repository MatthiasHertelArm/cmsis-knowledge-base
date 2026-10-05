---
id: "intr-step-through-debugging-with-no-deb-a-minimal-debugmonitor-handler"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: A minimal DebugMonitor Handler"
summary: "We can use the same handler we put together in our post about fault handling to dump register state about the code which caused the DebugMonitor exception to be invoked:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#a-minimal-debugmonitor-handler"
license: "CC-BY-SA-4.0"
mode: "V"
---

We can use the same handler we put together in [our post about fault handling](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#halting--determining-core-register-state) to dump register state
about the code which caused the DebugMonitor exception to be invoked:

```c
typedef struct __attribute__((packed)) ContextStateFrame {
  uint32_t r0;
  uint32_t r1;
  uint32_t r2;
  uint32_t r3;
  uint32_t r12;
  uint32_t lr;
  uint32_t return_address;
  uint32_t xpsr;
} sContextStateFrame;


void debug_monitor_handler_c(sContextStateFrame *frame) {
  // DebugMonitor Exception Logic
  // ...
}

__attribute__((naked))
void DebugMon_Handler(void) {
  __asm volatile(
      "tst lr, #4 \n"
      "ite eq \n"
      "mrseq r0, msp \n"
      "mrsne r0, psp \n"
      "b debug_monitor_handler_c \n");
}
```

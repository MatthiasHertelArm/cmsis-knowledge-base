---
id: "intr-mcuboot-walkthrough-and-porting-gu-launching-an-application"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Launching an Application"
summary: "The boot_go() routine returns a struct populated with information about the image to boot. It's the bootloader applications responsibility to actually launch the application from the information:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#launching-an-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `boot_go()` routine returns a struct populated with information about the image to boot. It's
the bootloader applications responsibility to actually launch the application from the
information:

```c
static void start_app(uint32_t pc, uint32_t sp) {
  __asm volatile ("MSR msp, %0" : : "r" (sp) : );
  void (*application_reset_handler)(void) = (void *)pc;
  application_reset_handler();
}

static void do_boot(struct boot_rsp *rsp) {
  EXAMPLE_LOG("Starting Main Application");
  EXAMPLE_LOG("  Image Start Offset: 0x%x", (int)rsp->br_image_off);

  // We run from internal flash. Base address of this medium is 0x0
  uint32_t vector_table = 0x0 + rsp->br_image_off + rsp->br_hdr->ih_hdr_size;

  uint32_t *app_code = (uint32_t *)vector_table;
  uint32_t app_sp = app_code[0];
  uint32_t app_start = app_code[1];

  EXAMPLE_LOG("  Vector Table Start Address: 0x%x. PC=0x%x, SP=0x%x",
    (int)vector_table, app_start, app_sp);

  // We need to move the vector table to reflect the location of the main application
  volatile uint32_t *vtor = (uint32_t *)0xE000ED08;
  *vtor = (vector_table & 0xFFFFFFF8);

  start_app(app_start, app_sp);
}
```

---
id: "alp-bare-metal-retarget-retarget-fputc-to-use-the-uart"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Modify the example to use the UART for printf output: Retarget fputc to use the UART"
summary: "Many library functions depend on semihosting. You must retarget these functions to use the hardware of the target instead of the host system."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/retarget.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/retarget/#retarget-fputc-to-use-the-uart"
license: "CC-BY-SA-4.0"
mode: "V"
---

Many library functions depend on semihosting. You must retarget these functions to use the hardware of the target instead of the host system.

Copy and paste the following code into a new file `uart.c`.

This contains code to initialize the UART (`uartInit()`), and a retargeted version of `fputc()` (which is called by `printf()` and other functions) to write to the UART directly, not via the semihosted `_ttywrch()` function.

#### uart.c
```C
#include <stdio.h>
#include "uart.h"

/* FILE is typedef’d in stdio.h. */
struct __FILE {
  int handle;
};
FILE __stdout;


struct pl011_uart* uart;

void uartInit(void* addr) {
  uart = (struct pl011_uart*) addr;

  // Ensure UART is disabled
  uart->UARTCR  = 0x0;

  // Set UART 0 Registers
  uart->UARTECR   = 0x0;  // Clear the recieve status (i.e. error) register
  uart->UARTLCR_H = 0x0 | PL011_LCR_WORD_LENGTH_8 | PL011_LCR_FIFO_DISABLE | PL011_LCR_ONE_STOP_BIT | PL011_LCR_PARITY_DISABLE | PL011_LCR_BREAK_DISABLE;

  uart->UARTIBRD = PL011_IBRD_DIV_38400;
  uart->UARTFBRD = PL011_FBRD_DIV_38400;

  uart->UARTIMSC = 0x0;                     // Mask out all UART interrupts
  uart->UARTICR  = PL011_ICR_CLR_ALL_IRQS;  // Clear interrupts

  uart->UARTCR  = 0x0 | PL011_CR_UART_ENABLE | PL011_CR_TX_ENABLE | PL011_CR_RX_ENABLE;
  
  return;
}

int fputc(int c, FILE *f) {
  // Wait until FIFO or TX register has space
  while ((uart->UARTFR & PL011_FR_TXFF_FLAG) != 0x0) {}

  // Write packet into FIFO/tx register
  uart->UARTDR = c;

  // Model requires us to manually send a carriage return
  if ((char)c == '\n') {
    while ((uart->UARTFR & PL011_FR_TXFF_FLAG) != 0x0) {}
    uart->UARTDR = '\r';
  }
  return 0;
}

void  __attribute__ ((noreturn)) _sys_exit(int x){
	printf("In _sys_exit. Use Ctrl+C to quit.\n");
	while(1);
}
```
**__sys_exit:**
The source also retargets `__sys_exit()` as an infinite while loop.

Typically an embedded application will never return.


Create `uart.h` containing various macros used above. This code is taken from extended examples supplied with Arm Development Studio.
#### uart.h
```C
#ifndef __uart_h
#define __uart_h

void uartInit(void* addr);
// void uartSendString(const char*);

// Useful defines for control/status registes
#define PL011_LCR_WORD_LENGTH_8   (0x60)
#define PL011_LCR_WORD_LENGTH_7   (0x40)
#define PL011_LCR_WORD_LENGTH_6   (0x20)
#define PL011_LCR_WORD_LENGTH_5   (0x00)

#define PL011_LCR_FIFO_ENABLE     (0x10)
#define PL011_LCR_FIFO_DISABLE    (0x00)

#define PL011_LCR_TWO_STOP_BITS   (0x08)
#define PL011_LCR_ONE_STOP_BIT    (0x00)

#define PL011_LCR_PARITY_ENABLE   (0x02)
#define PL011_LCR_PARITY_DISABLE  (0x00)

#define PL011_LCR_BREAK_ENABLE    (0x01)
#define PL011_LCR_BREAK_DISABLE   (0x00)

#define PL011_IBRD_DIV_38400      (0x27)
#define PL011_FBRD_DIV_38400      (0x09)

#define PL011_ICR_CLR_ALL_IRQS    (0x07FF)

#define PL011_FR_TXFF_FLAG        (0x20)
#define PL011_FR_RXFF_FLAG        (0x40)

#define PL011_CR_UART_ENABLE      (0x01)
#define PL011_CR_TX_ENABLE        (0x0100)
#define PL011_CR_RX_ENABLE        (0x0200)


struct pl011_uart {
        volatile unsigned int UARTDR;        // +0x00
        volatile unsigned int UARTECR;       // +0x04
  const volatile unsigned int unused0[4];    // +0x08 to +0x14 reserved
  const volatile unsigned int UARTFR;        // +0x18 - RO
  const volatile unsigned int unused1;       // +0x1C reserved
        volatile unsigned int UARTILPR;      // +0x20
        volatile unsigned int UARTIBRD;      // +0x24
        volatile unsigned int UARTFBRD;      // +0x28
        volatile unsigned int UARTLCR_H;     // +0x2C
        volatile unsigned int UARTCR;        // +0x30
        volatile unsigned int UARTIFLS;      // +0x34
        volatile unsigned int UARTIMSC;      // +0x38
  const volatile unsigned int UARTRIS;       // +0x3C - RO
  const volatile unsigned int UARTMIS;       // +0x40 - RO
        volatile unsigned int UARTICR;       // +0x44 - WO
        volatile unsigned int UARTDMACR;     // +0x48
};

#endif
```
### Modify hello.c

Modify `hello.c` to initialize the UART before any messages are printed. From the [memory map](https://developer.arm.com/documentation/100964/latest/Base-Platform/Base---memory/Base-Platform-memory-map), `UART0` is located at `0x1C090000`.

#### hello.c
```C
#include <stdio.h>
#include "uart.h"

__asm(".global __use_no_semihosting\n\t");

int main (void) {
  uartInit((void*)(0x1C090000));
  printf("Hello World!\n");
  return 0;
}
```
No changes are needed to the scatter file. The additional code will be placed by the catch-all `* (+RO)` line.

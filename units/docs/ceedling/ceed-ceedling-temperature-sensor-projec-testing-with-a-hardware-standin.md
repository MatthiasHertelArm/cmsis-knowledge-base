---
id: "ceed-ceedling-temperature-sensor-projec-testing-with-a-hardware-standin"
type: "concept"
domain: "test"
title: "Ceedling Temperature Sensor Project: Testing with a Hardware Standin"
summary: "Embedded source files that drive hardware peripherals typically rely on creative linkage from C to the actual hardware through vendor-defined symbols and chip features (e.g. memory mapped registers):"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/snapshot/examples/temp_sensor/README.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/snapshot/examples/temp_sensor/#testing-with-a-hardware-standin"
license: "MIT"
mode: "V"
---

### The Problem

Embedded source files that drive hardware peripherals typically rely on creative linkage 
from C to the actual hardware through vendor-defined symbols and chip features (e.g. 
memory mapped registers):

```c
/* AdcHardwareConfigurator.c */
void Adc_Reset(void)
{
  AT91C_BASE_ADC->ADC_CR = AT91C_ADC_SWRST;
}
```
(Once upon a time it was fairly common for vendors to add C language extensions for
their hardware access in code.)

`AT91C_BASE_ADC`, `AT91C_ADC_SWRST`, and the `ADC_CR` field all come from
the chip vendor’s SDK (_at91sam7s256.h_ for this imagined AT91SAM7S256 
project). These vendor source files are non-portable.

Further, and more importantly, the underlying peripherals doe not exist 
apart from the target hardware or an emulator. On the surface, you might think this 
prevents testing. But, oh no, it does not. There is a way.

### The Standin Approach

A platform standin provides a host-compilable substitute for the vendor
bridge from C to hardware. The magic of C is that it does not care what is behind a symbol
so long as the defined symbol meets expectations.

The platform standin approach simply recreates the symbols used to access
hardware peripherals and points them at a generic block of memory. Reads
and writes through those symbols to that memory can be tested. The source
code depending on these symbols remains unchanged.

Two files in _test/platform/_ cover everything the `temp_sensor` hardware 
source files need:

**_test/platform/at91sam7s256.h_** declares:

1. **Peripheral register structs** — Plain C `typedef struct` types with one
   field per register used by this project (e.g. `AT91S_ADC`, `AT91S_TC`,
   `AT91S_US`). Fields match the vendor register names exactly.

2. **Global standin instances** — One `extern` instance per peripheral
   (`AdcStandin`, `TimerStandin`, `UsartStandin`, …), defined in the
   accompanying `.c` file and allocated in ordinary program memory.

3. **Base-address macros** — The `AT91C_BASE_*` macros, which in the real
   SDK expand to hardware addresses, are redefined here to point to the
   corresponding standin instances:
   ```c
   #define AT91C_BASE_ADC  (&AdcStandin)
   #define AT91C_BASE_TC0  (&TimerStandin)
   ```

4. **Bit-mask constants** — All `AT91C_*` register bit-field constants
   (`AT91C_ADC_SWRST`, `AT91C_TC_CPCS`, `AT91C_US_TXRDY`, …) defined with
   their real AT91SAM7S256 datasheet values.

**_test/platform/at91sam7s256.c_** defines the global structs (i.e. memory)
that the accessors in _test/platform/at91sam7s256.h_ point to.

Each hardware source file adds `#include "at91sam7s256.h"` — exactly what it
would include in a real embedded build where the vendor header lives in the
toolchain’s system include path. Ceedling’s support path (_test/platform/_)
makes this header resolvable during test builds.

By carefully segmenting include paths between release and test builds and
selectively swapping in certain symbol definitions in a testing-only C source 
file, we can cleanly create a portable hardware stand-in suitable for test purposes.

NOTE: This technique only validates what is read and written to the stand-in
peripherals. It cannot validate that the correct functionality is triggered.
That requires on-hardware validation.

### What This Enables

Production code runs on the host unchanged. A test calls the real
hardware-layer function and then inspects the standin struct to verify the
correct register bits were written:

```c
void testResetWritesSwrstBitToControlRegister(void)
{
  Adc_Reset();
  TEST_ASSERT_EQUAL_UINT32(AT91C_ADC_SWRST, AdcStandin.ADC_CR);
}
```

This catches logic bugs that mocking the hardware function interfaces cannot —
all without touching real hardware:

* Wrong bit positions
* Missing enable steps
* Off-by-one prescaler values
* Incorrect bitmask combinations
* Etc.

### The Role of setUp()

Each standin test file’s `setUp()` calls `memset()` to zero all standin structs
before every test (below). Alternatively, as needed you can also initialize with
non-zero values to represent hardware specific behaviors.

```c
void setUp(void)
{
  memset(&AdcStandin, 0, sizeof(AdcStandin));
}
```

This guarantees a clean slate. If a test finds a non-zero register field, it
was written there by the code under test during that test — not left over from
a previous run or from C’s zero-initialization of global storage.

For read-dependent behavior (such as `Usart_PutChar()`, which spins on
`Usart_ReadyToTransmit()` before transmitting), the test sets the relevant
standin field to a known value so the production code sees the expected
hardware state:

```c
void testPutCharWritesByteToTransmitHoldingRegisterWhenReady(void)
{
  UsartStandin.US_CSR = AT91C_US_TXRDY; // Make the ready-check pass
  Usart_PutChar('Z');
  TEST_ASSERT_EQUAL_UINT32('Z', UsartStandin.US_THR);
}
```

### Where This Fits

A platform standin is not a replacement for on-hardware integration testing.
It cannot exercise timing, DMA, real interrupt delivery, or silicon errata.
What it does well:

- **Register configuration logic** — verifies the exact bit patterns written
  during peripheral initialization sequences.
- **Status-flag branching** — exercises the code paths that read status
  registers (e.g. `TC_SR & AT91C_TC_CPCS`) by pre-loading the standin field.
- **Math and conversion code** — any calculation layered on top of a hardware
  read (ADC counts → millivolts) is fully exercisable.

Used alongside CMock-based unit tests for the higher architectural layers, the
standin tests give you meaningful coverage of the hardware-touching code
without requiring the target board to be present.

### Running the Standin Tests

```sh
# Run only the platform standin tests
ceedling test:pattern[PlatformStandin]
```
---

---
id: "mlek-timing-adapter-building-timing-adapter-with-custom-opti"
type: "concept"
domain: "edge-ai"
title: "Timing adapter: Building timing adapter with custom options"
summary: "The CMake build framework allows the parameters to control the behavior of each bus with following parameters:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/timing_adapters.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/timing_adapters.md#building-timing-adapter-with-custom-options"
license: "Apache-2.0"
mode: "V"
---

The CMake build framework allows the parameters to control the behavior of each bus with following parameters:

- `MAXR`: Maximum number of pending read operations allowed. `0` is inferred as infinite and the default value is `4`.

- `MAXW`: Maximum number of pending write operations allowed. `0` is inferred as infinite and the default value is `4`.

- `MAXRW`: Maximum number of pending read and write operations allowed. `0` is inferred as infinite and the default
  value is `8`.

- `RLATENCY`: Minimum latency, in cycle counts, for a read operation. This is the duration between `ARVALID` and
  `RVALID` signals. The default value is `50`.

- `WLATENCY`: Minimum latency, in cycle counts, for a write operation. This is the duration between `WVALID` and
  `WLAST`, with `BVALID` being deasserted. The default value is `50`.

- `PULSE_ON`: The number of cycles where addresses are let through. The default value is `5100`.

- `PULSE_OFF`: The number of cycles where addresses are blocked. The default value is `5100`.

- `BWCAP`: Maximum number of bus-width words (beats) transferred per pulse cycle. A pulse cycle is defined by
  `PULSE_ON` and `PULSE_OFF`. `0` is inferred as infinite and the default value is `625`.

  The bus-width word size depends on the *Arm Ethos-U* NPU AXI bus width:

  - `U55`: 64-bit words
  - `U65`: 128-bit words
  - `U85`: 128-bit words

  > **Note:** The bandwidth cap `BWCAP` operates on the transaction level and, because of its simple implementation,
  > the accuracy is limited.
  > When set to a small value it allows only a small number of transactions for each pulse cycle.
  > Once the counter has reached or exceeded the configured cap, no transactions will be allowed before the next pulse
  > cycle. In order to minimize this effect some possible solutions are:
  >
  > - scale up all the parameters to a reasonably large value.
  > - scale up `BWCAP` as a multiple of the burst length (in this case bulk traffic will not face rounding errors in
  >   the bandwidth cap).

- `MODE`: Timing adapter operation mode. Default value is `0`.

  - `Bit 0`: `0`=simple, `1`=latency-deadline QoS throttling of read versus write,

  - `Bit 1`: `1`=enable random AR reordering (`0`=default),

  - `Bit 2`: `1`=enable random R reordering (`0`=default),

  - `Bit 3`: `1`=enable random B reordering (`0`=default)

For the CMake build configuration of the timing adapter, the SRAM AXI is assigned `index 0` and the flash, or DRAM, AXI
bus has `index 1`.

To change the bus parameter for the build an "***SRAM***" or "***EXT***" prefix should be added to the above. For example,
**SRAM_MAXR=10** sets the maximum pending reads to 10 on the SRAM AXI bus.

As an example, if we have the following parameters for the flash, or DRAM, region:

- `EXT_MAXR` = "2"

- `EXT_MAXW` = "0"

- `EXT_MAXRW` = "0"

- `EXT_RLATENCY` = "64"

- `EXT_WLATENCY` = "32"

- `EXT_PULSE_ON` = "320"

- `EXT_PULSE_OFF` = "80"

- `EXT_BWCAP` = "50"

For a clock rate of 500MHz, this would translate to:

- The maximum duty cycle for any operation is:\
  (figure: Maximum duty cycle formula)

- Maximum bit rate for this bus is based on the AXI bus width
  (`64-bit` for `U55`; `128-bit` for `U65` and `U85`):\
  (figure: Maximum bit rate formula)

- With a read latency of 64 cycles, and maximum pending reads as 2, each read could be a maximum of 64 or 128 bytes. As
  defined for the *Ethos-U* NPU AXI bus attribute.

  The bandwidth is calculated solely by read parameters:

  (figure: Bandwidth formula)

  This is higher than the overall bandwidth dictated by the bus parameters of:

  (figure: Overall bandwidth formula)

This suggests that the read operation is only limited by the overall bus bandwidth.

Timing adapter requires recompilation to change parameters. Default timing adapter configuration file pointed to by
`TA_CONFIG_FILE` build parameter is located in the `scripts/cmake folder` and contains all options for `SRAM` and `EXT`
as previously described.

here is an example of `scripts/cmake/timing_adapter/ta_config_u55_high_end.cmake`:

```cmake
# Timing adapter settings for SRAM
set(SRAM_MAXR       "8")
set(SRAM_MAXW       "8")
set(SRAM_MAXRW      "0")
set(SRAM_RLATENCY   "32")
set(SRAM_WLATENCY   "32")
set(SRAM_PULSE_ON   "3999")
set(SRAM_PULSE_OFF  "1")
set(SRAM_BWCAP      "4000")
...
```

An example of the build with a custom timing adapter configuration:

```commandline
cmake .. -DTA_CONFIG_FILE=scripts/cmake/timing_adapter/my_ta_config.cmake
```

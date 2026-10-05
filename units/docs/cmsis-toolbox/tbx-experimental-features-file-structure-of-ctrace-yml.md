---
id: "tbx-experimental-features-file-structure-of-ctrace-yml"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / File Structure of `*.ctrace.yml`"
summary: "The .ctrace.yml file starts with the node ctrace: and contains the trace capture settings for one solution-set."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#file-structure-of-ctrace-yml"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

The `*.ctrace.yml` file starts with the node `ctrace:` and contains the trace capture settings for one solution-set.

!!! Note
    Cortex-M processors and the DWT, ITM, ETM, MTB, and PMU implementations differ in ways that affect the available configuration options. The pyTS tool uses the `*.cbuild-run.yml` file to discover the processor and implemented capabilities and rejects incompatible settings.

`ctrace:`                                               |             | Content
:-------------------------------------------------------|:------------|:------------------------------------
    `generated-by:`                      |  Optional   | Tool and version that generated or last updated the file.
    `setup:`                             |  Required   | Setup for each processor.

`setup:`                                                  |             | Content
:---------------------------------------------------------|:------------|:---------------------------------------                                      
`- pname:`                                                |  Optional   | Section applies to a processor name (required for multi-processor systems).
    `disable:`                             |  Optional   | When set, this list node is ignored; useful for testing.
    [`timestamps:`](#timestamps)           |  Optional   | Enables timestamps in the emitted trace streams.
    [`timesync:`](#timesync)               |  Optional   | Enables time synchronization between trace streams.
    [`data:`](#data)                       |  Optional   | DWT data trace configuration.
    [`exceptions:`](#exceptions)           |  Optional   | DWT exception trace configuration.
    [`events:`](#events)                   |  Optional   | DWT or PMU event trace configuration.
    [`itm:`](#itm)                         |  Optional   | ITM channel configuration.
    [`instructions:`](#instructions)       |  Optional   | ETM or MTB instruction trace configuration.
    [`pcsampling:`](#pcsampling)           |  Optional   | DWT PC sampling configuration.
    [`synchronization:`](#synchronization) |  Optional   | Trace synchronization packet period configuration.
    [`tracehalt:`](#tracehalt)             |  Future     | Trace sink or formatter halt trigger configuration.

**Example:**

```yml
ctrace:
  created-by: CMSIS-Debugger v1.4.0
  setup:
    - pname: 
#     disable:    # disables trace without need to remove settings
      timestamps:
        clock: 24000000
      timesync:

      data:
        - location: mysimple

        - location: App|0x20001000
          access: RW
          size: 0x100
          output: PC

        - location: App|"main.c"::sample_counter
          access: R
          output: PC
          match:
            value: 0x00001234
            size: 4

      exceptions:
      events:
        - event: CPICNT
        - event: LSUCNT

      itm:
        enable: 0x0000000F
        privileged: 0x0
```

#### `timestamps:`

When `timestamps:` is present, timestamp generation is enabled in the trace stream. ITM uses local timestamps with a synchronous timestamp source.

`timestamps:`                                            |             | Content
:--------------------------------------------------------|:------------|:------------------------------------
    `clock:`                              |  Optional   | Timestamp clock frequency in Hz.
    `itm-prescaler:`                      |  Optional   | ITM timestamp prescaler: `1` (default), `4`, `16`, `64`.

The timestamp `clock` typically is the processor clock.

#### `timesync:`

When `timesync:` is present, time synchronization between streams is enabled, for example between ITM and ETM by global timestamps.

#### `data:`

The `data:` node configures DWT data trace. DWT comparator resources are limited and shared with data access breakpoints, trigger conditions, and trace start/stop logic.

`data:`                                                  |             | Content
:--------------------------------------------------------|:------------|:------------------------------------
`- location:`                                            |**Required** | Symbol or numeric address [location](#location) to trace.
    `label:`                              |  Optional   | User-defined short label for Trace Compass.
    `access:`                             |  Optional   | Access type: `W`, `R`, or `RW`. Default: `W`.
    `size:`                               |  Optional   | Number of bytes in the traced range. Default: `sizeof(symbol)`, `4` for numeric addresses.
    `output:`                             |  Optional   | Trace output mode (see table below). Default: `value`.
    `match:`                              |  Optional   | Value match condition. When present, trace is emitted only for matching accesses.

`match:`                                                 |             | Content
:--------------------------------------------------------|:------------|:------------------------------------
       `value:`            |**Required** | Value to match.
       `size:`             |  Optional   | Number of bytes to compare. Allowed values: `1`, `2`, `4`. Default: `4`.

`output:`       | Description
:---------------|:------------------------------------
`value`         | Emits the value of the access.
`offset`        | Emits the address offset. This is useful when tracing an address range.
`PC`            | Emits the PC value that caused the access.
`match`         | Emits only the comparator ID of a match. This requires Armv8-M and saves trace bandwidth.
`PC+value`      | Emits PC and value.
`offset+value`  | Emits address offset and value.
`PC+offset`     | Emits PC and address offset. This requires Armv8-M.

!!! Note
    `size:` values greater than `4` may require two DWT comparators, depending on the DWT architecture. A `match:` condition can also require two DWT comparators.

#### `exceptions:`

The `exceptions:` node enables DWT exception trace. This does not enable ETM exception trace.

#### `events:`

The `events:` node enables DWT or PMU event trace for all processors or for a specific processor.

`events:`                             |             | Content
:-------------------------------------|:------------|:------------------------------------
`- event:`                            |**Required** | Event selector.

Supported DWT event selectors include `CYCCNT`, `CPICNT`, `EXCCNT`, `SLEEPCNT`, `LSUCNT`, and `FOLDCNT`.

**Example:**

```yml
events:
  - event: CPICNT
  - event: FOLDCNT
  - event: LSUCNT
```

#### `itm:`

The `itm:` node enables ITM channels.

`itm:`                                |             | Content
:-------------------------------------|:------------|:------------------------------------
`- enable:`                           |**Required** | ITM channel bit mask.
    `privileged:`      |  Optional   | Privileged access only mask by blocks of eight channels. Default: `0`.

Each bit in `enable:` represents one ITM channel.  
Each bit in `privileged:` represents a block of eight channels, i.e. value `0x2` configures that access to ITM channles 8-15 must be privileged.

!!! Note
    ITM channel 0 is often used for `printf` output. This output should be routed to an output window or debug console instead of the trace analysis components.

#### `pcsampling:`

The `pcsampling:` node enables DWT PC sampling.

`pcsampling:`                         |             | Content
:-------------------------------------|:------------|:------------------------------------
`period:`                             |  Optional   | Sampling period in CPU cycles.

Supported values for `period:` `0` (off), `64`, `128`, `256`, ..., `16384`. Default: `0`.

#### `synchronization:`

The `synchronization:` node specifies behavior and frequency of synchronization packet generation.

`synchronization:`                    |             | Content
:-------------------------------------|:------------|:------------------------------------
`DWT:`                                |  Optional   | Frequency `off`, `16M`, `64M`, `256M` processor cycles. Default: `16M`.
`sync-on-run:`                        |  Optional   | Explicitly request synchronization packets at start of a step or run. Supported values: `true` (default) and `false`.

`sync-on-run:` is preserved in `*.ctrace-run.yml` under `ctrace-setup:` so that pyOCD can apply the requested synchronization behavior. It only applies to trace sources with enabled synchronization and that do not always insert synchronization packets at start of a step or run. A debugger must request the packets as follows:

Architecture | DWT/ITM Request
:---------------------|:--------
Armv7-M | Debugger toggles bits 24, 26, and 28 of DWT_CYCCNT twice between setting up trace capture and start of processor step/run. These are the bits selectable by DWT_CTRL.SYNCTAP. The second toggle restores the original cycle counter value. Do not toggle other bits to avoid side effects.
Armv8-M | N/A, processor always automatically inserts at start of step/run

**Example:**

```yml
synchronization:
  DWT: 256M
  sync-on-run: false  # Skip manual DWT synchronization at start of run
```

#### `instructions:`

The `instructions:` node is reserved for ETM and MTB instruction trace. It is not required for the initial implementation.

`instructions:`                       |             | Content
:-------------------------------------|:------------|:------------------------------------
    `start:`           |  Optional   | Conditions that start instruction trace.
    `stop:`            |  Optional   | Conditions that stop instruction trace.

`start:` and `stop:` contain [condition](#conditions) entries. These entries define when instruction trace starts or stops; they do not define trace output.

#### `tracehalt:`

The `tracehalt:` node contains [condition](#conditions) entries that halt a trace sink or formatter by a trace trigger. It affects all trace streams that use the sink. Support to combine two conditions by logic operators may be added in the future.

#### Conditions

The nodes `start:`, `stop:`, and `tracehalt:` may contain a condition list that is logically OR-combined. They have the following form.

`start:`, `stop:`, `tracehalt:`                        |             | Content
:------------------------------------------------------|:------------|:------------------------------------
`- location:`                                          |**Required** | Code symbol, data symbol, or numeric address [location](#location) used as the trace condition.
    `access:`                           |  Optional   | Access type: `X`, `R`, `W`, or `RW`. Defaults to `X` for code symbols, and to `W` for data symbols or numeric addresses
    `size:`                             |  Optional   | Number of bytes in the condition range. Defaults to `sizeof(symbol)` for symbols and `4` for numeric addresses.
    `match:`                            |  Optional   | Value match condition for data symbols or numeric addresses.

`match:`                                               |             | Content
:------------------------------------------------------|:------------|:------------------------------------
       `value:`          |**Required** | Value to match.
       `size:`           |  Optional   | Number of bytes to compare. Allowed values: `1`, `2`, `4`. Default: `4`.

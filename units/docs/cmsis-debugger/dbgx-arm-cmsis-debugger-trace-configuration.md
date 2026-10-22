---
id: "dbgx-arm-cmsis-debugger-trace-configuration"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Using Trace / Trace configuration"
summary: "Trace configuration consists of these parts:"
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#trace-configuration"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using Trace_

Trace configuration consists of these parts:

1. The CMSIS solution file (`csolution.yml`) configures the trace transport and capture method, including the SWO input and output clocks.
2. The `./cmsis/<target>.dbgconf` file configures trace pins, clocks, and other device specific trace communication components.
3. The **Trace Generation** view configures the trace sources in the processor, such as exception trace, instrumentation trace, DWT data trace, event counters, and PC sampling. The trace source configuration is stored separately in a target-specific `.cmsis/<target>.ctrace.yml` file.

This separation allows the trace transport, such as SWO, to be configured independently from the processor trace sources that produce the data.

#### Configure SWO trace in the CMSIS solution

Before configuring individual trace sources, enable SWO trace for the target.

1. Select the debug adapter

    - Open **Manage Solution** and select the debug adapter to use with the target.
    - **Save** the solution configuration before continuing.

    For example, you can use an onboard ST-Link debug adapter with pyOCD.

2. Enable SWO

    From **Manage Solution**, select **Edit csolution.yml** and add a `trace` section to the debugger configuration.

    For example:

    ```yaml
      debugger:
        name: ST-Link@pyOCD
        clock: 4000000
        protocol: swd
        trace:
          - swo-uart:
            mode: file
            input-clock: 84000000
            output-clock: 1500000
    ```

    |  Key  | Description |
    |-------|-------------|
    | `swo-uart` | Selects SWO as the trace output. |
    | `mode: file` | Captures the trace to a file for subsequent analysis |
    | `input-clock` | Specifies the clock used by the target trace hardware. It must correspond to the actual processor or trace clock used by the application. |
    | `output-clock` | Specifies the SWO communication rate used to transfer trace data to the debug adapter. |

    In the example above, the trace input clock is 84 MHz and the SWO output clock is 1.5 MHz.

    > ⚠ **Important:**
    >
    > The appropriate clock values depend on the target and application configuration. An incorrect `input-clock` can prevent SWO trace from being decoded correctly. Verify the processor clock used by your application.

    Save `csolution.yml`. The [**Trace Generation**](#configure-trace-sources) view now shows the trace capabilities of the selected processor.

#### Configure trace communication in .dbgconf

Depending on the hardware target, a `.cmsis/<target>.dbgconf` file might exist that lets you configure the trace pin and clock
settings using **Configuration Wizard** view. For example, if you are switching from an off-the-shelf development board
to custom hardware, don't forget to adapt these settings.

#### Configure trace sources

Open the **Trace And Live View** and scroll down to **Trace Generation**.

(figure: Trace Generation)

By default, the start processor is enabled as a trace source. Select the information that you want to capture. The
available options depend on the trace capabilities of the processor.

##### Timestamps

Enable **Timestamps** for timing information. Timestamps contribute to the cycle information in the decoded
trace. They are normally not displayed as individual trace records.

- **Clock**: reserved for future use.
- **ITM Prescaler**: defines the granularity and hence the number of generated timestamps. A higher value reduces the generated data but also means less accurate timestamps.

##### Exceptions

Enable **Exceptions** to record exception activity.

In the decoded trace, **index** identifies the exception number and **value** identifies the exception event (0x1 - Enter Exception, 0x2 - Exit Exception, 0x3 - Return to Exception/Thread mode).

##### Event Counters

Enable **Event Counters** to include supported processor events in the trace.

Each bit in the decoded **value** indicates that a specific counter wrapped around (0x01 - DWT_CPICNT, 0x02 - DWT_EXCCNT, 0x04 - DWT_SLEEPCNT, 0x08 - DWT_LSUNCT, 0x10 - DWT_FOLDCNT, 0x11 - POSTCNT).

##### Instrumentation Trace

Enable **Instrumentation Trace** to capture information generated through ITM stimulus channels.

- Select the required channels (0 - 31).
- **Privileged** sets group access rights (eight channels at a time). Ports that are used by an operating system can be protected from being
accessed through user-code. When unchecked, accessing ports in **User Mode** is not allowed. Ports are always
accessible when the device is in **Privileged Mode**.

##### DWT Data Trace

Use **DWT Data Trace** to monitor accesses to a variable or memory location without stopping program execution:

- Specify the **Location** to monitor (variable name or memory location).
- Select the required **Access** type (`Read`, `Write`, `Read Write`).
- Set the **Size** of the variable/memory location (`<Auto>` determines the size by symbol information).
- Select the generated **Output** packets (`value`, `offset`, `PC`, `match`, `PC+value`, `offset+value`, `PC+offset`).
- Select **Match** to only trigger recording when a certain value is matched.
- Set the **Size** of the match (`<Auto>` determines the size by symbol information).

Depending on the processor,
combinations of settings may bot be supported. The validation clearly flags unsupported combinations.

For example, configuring a variable for write access generates a trace record whenever the processor writes to that
variable. The captured value is included in the decoded trace.

A data trace point can also be made sensitive to a particular value (**Match**). Value-dependent configurations can
require additional DWT hardware resources and should therefore only be used when required.

> 📝 **Note:**
>
> DWT data trace and data access breakpoints use the same underlying hardware resources. Enabling data trace can reduce
> the number of data access breakpoints available to the debugger.

##### PC Sampling

Select a suitable **PC Sampling** frequency to periodically record the program counter.

The available sampling configuration depends on the processor.

##### Advanced Settings

- **Time Synchronization**: reserved for future use.
- **Stream Synchronization** determines how often a synchronization packet is generated to allow a decoder to synchronize into a captured trace stream. Default for ITM/DWT is every 16 M cycles.

#### Validate the trace configuration

CMSIS Debugger automatically validates changes made in the **Trace Generation** view.

An invalid or unsupported setting is indicated by an error icon:
(figure: Error icon). Errors are
propagated through the configuration hierarchy so that an error remains visible even when the affected section is
collapsed.

Hover over the error indicator to display additional information.

Some validation requires information from the application image. If validation reports that the application image does
not exist, build the solution and allow the trace configuration to be validated again.

Validation also detects configurations that are not supported by the target trace hardware. For example, a processor
might support PC information for some DWT access types but not for others.

#### Save the trace configuration

After configuring the required trace sources and successful validation, press the save button
(figure: Save trace button).

CMSIS Debugger stores the trace source configuration in `.cmsis/<solution-set>.ctrace.yml`. The filename corresponds to the
active target and target-set.

Use (figure: Revert) to discard
unsaved changes and restore the previously saved trace configuration.

> 📝 **Note:**
>
> You normally do not need to edit the `<solution-set>.ctrace.yml` file directly. Configure the required trace sources using
> the **Trace Generation** view.

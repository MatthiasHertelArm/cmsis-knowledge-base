---
id: "cc-use-cmsis-compiler-resolve-dependencies"
type: "concept"
domain: "core"
title: "Use CMSIS-Compiler: Resolve Dependencies"
summary: "The Event Recorder subcomponent requires the CMSIS-View::Event Recorder component from the CMSIS-View pack."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/usage.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/usage.md#resolve-dependencies"
license: "Apache-2.0"
mode: "V"
---

### Using Event Recorder

The **Event Recorder** subcomponent requires the `CMSIS-View::Event Recorder` component from the [CMSIS-View](https://www.keil.arm.com/packs/cmsis-view-arm/) pack.

1) Install the **CMSIS-View** pack:

   ```sh
   cpackget add ARM::CMSIS-View
   ```

2) In the **Manage Software Components** dialog, select **Software Pack**, then choose **All installed packs** and find and select **ARM::CMSIS-View**.

   (figure: Select CMSIS-View Pack)

3) Select the **CMSIS-View::Event Recorder** component.

   (figure: Select CMSIS-View::Event Recorder Component)

The project yml file should contain:

```yml
packs:
   - pack: ARM::CMSIS-Compiler
   - pack: ARM::CMSIS-View
```

```yml
components:
   - component: CMSIS-Compiler:CORE
   - component: CMSIS-Compiler:STDOUT:Event Recorder
   - component: CMSIS-View:Event Recorder&DAP
```

### Using RTT

The **RTT** subcomponent requires the `SEGGER::RTT` component from the [SEGGER RTT](https://www.keil.arm.com/packs/rtt-segger/) pack.

1) Install the **SEGGER RTT** pack:

   ```sh
   cpackget add SEGGER::RTT
   ```

2) In the **Manage Software Components** dialog, select **Software Pack**, then choose **All installed packs** and find and select **SEGGER::RTT**.

   (figure: Select SEGGER Pack)

3) Select the **SEGGER::RTT** component.

   (figure: Select SEGGER::RTT Component)

The project yml file should contain:

```yml
packs:
   - pack: ARM::CMSIS-Compiler
   - pack: SEGGER::RTT
```

```yml
components:
   - component: CMSIS-Compiler:CORE
   - component: CMSIS-Compiler:STDOUT:RTT
   - component: SEGGER:RTT
```

### Using UART

The **UART** subcomponent provides default implementation variant **CMSIS** which requires the `CMSIS Driver::USART` implementation, typically provided by a Board Support Pack (BSP) or Device Family Pack (DFP) for the target hardware.

> **Note**
>
> Use the [CMSIS Packs catalog](https://www.keil.arm.com/packs/) to find the appropriate pack for your target hardware.

1) Install the Board Support Pack (BSP) or Device Family Pack (DFP):

   ```sh
   cpackget add Vendor::Pack
   ```

2) In the **Manage Software Components** dialog, select **Software Pack**, then choose **All installed packs** and find and select installed BSP or DFP.

3) Select the **CMSIS Driver::USART** component.

   (figure: Select CMSIS Driver::USART Component)

The project yml file should contain:

```yml
packs:
   - pack: ARM::CMSIS-Compiler
   - pack: Vendor::Pack
```

```yml
components:
   - component: CMSIS-Compiler:CORE
   - component: CMSIS-Compiler:STDOUT:UART&CMSIS
   - component: CMSIS Driver:USART
```

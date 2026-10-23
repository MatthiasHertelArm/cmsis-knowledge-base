---
id: "tbx-pyocd-debugger-debug-access-sequence-usage-for-pyocd-co"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Debug Access Sequence Usage for pyOCD Commands"
summary: "The sequence diagrams below show the usage of the debug access sequences for pyOCD commands. The specification Open-CMSIS-Pack: Usage of debug access sequences describes the following sequence blocks. pyOCD uses these concepts, but implements these deviations:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#debug-access-sequence-usage-for-pyocd-commands"
license: "Apache-2.0"
mode: "V"
---

The sequence diagrams below show the usage of the debug access sequences for pyOCD commands. The specification [Open-CMSIS-Pack: Usage of debug access sequences](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences) describes the following sequence blocks. pyOCD uses these concepts, but implements these deviations:

- **Connect Debugger to Device**:  
    - For the [`connect:`](#connect) mode `attach`, no reset or halt operations are issued.
    - For multi-processor systems, only the following blocks are executed once per processor core: **Read Target Features**, **DebugCoreStart**, **Stop Processor** / **ResetCatchSet**,
    **Wait for Processor to Stop**, and **Initialize Debug Components**. The remaining diagram elements run once for the device as a whole. This distinction is important for multi-core targets, where some blocks run once per core and others run once for the device.

!!! Info
    Sequence Blocks in the diagrams below link to the [Open-CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences) specification that provides further details.

---

### Command: pyOCD erase

```mermaid
flowchart TD
  classDef seq fill:#c7d6ea,stroke:#333;

  B0(Sequence Block:<br>Connect Debugger to Device):::seq
  click B0 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
  B0 -.-> B1
  B1[Set reset catch on all cores] --> B2
  B2[Reset device with<br>primary core using<br>selected reset type] --> B3
  B3[Clear reset catch on all cores] --> loop
  subgraph loop[Loop over algorithms for primary core]
    B4(Sequence Block:<br>Flash Erase):::seq
    click B4 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
    B4 --> B5
    B5[Put primary core in deadloop]
  end
  loop -.-> B6
  B6(Sequence Block:<br>Disconnect Debugger):::seq
  click B6 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
```

---

### Command: pyOCD load

```mermaid
flowchart TD
  classDef seq fill:#c7d6ea,stroke:#333;

  B0(Sequence Block:<br>Connect Debugger to Device):::seq
  click B0 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
  B0 -.-> B1
  B1([Evaluate pre-reset type])
  B1 --> B2
  B2[Set reset catch on all cores] --> B3
  B3[Reset device with<br>primary core using<br>selected pre-reset type] --> B4
  B4[Clear reset catch on all cores] --> loop
  B1 -- off --> loop
  subgraph loop[Loop over algorithms for primary core]
    B5(Sequence Block:<br>Flash Program):::seq
    click B5 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
    B5 --> B6
    B6[Put primary core in deadloop] 
  end
  loop -.-> B7
  B7([Evaluate post-reset type])
  B7 --> B8
  B8[Reset device with<br>primary core using<br>selected post-reset type] --> B9
  B7 -- off --> B9
  B9(Sequence Block:<br>Disconnect Debugger):::seq
  click B9 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
```

---

### Command: pyOCD gdbserver

```mermaid
flowchart TD
  classDef seq fill:#c7d6ea,stroke:#333;

  B0(Sequence Block:<br>Connect Debugger to Device):::seq
  click B0 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
  B0 -.-> B1
  B1{Is reset-run<br>option set?}
  B1 -- Yes --> B2
  B2[Reset device with<br>primary core using<br>selected reset type] --> B3
  B1 -- No --> B3
  B3[Create GDB servers for all cores] --> gdbserver
  subgraph gdbserver[Core's GDB server]
    B4([Wait for GDB client<br>connection to server])
  end
  gdbserver -.-> gdbclient
  subgraph gdbclient[GDB client connection]
    B5[GDB client connected] --> B6
    B6[Halt core] --> loop
    subgraph loop[Loop]
      B7([Process GDB<br>commands]) -.-> B8
      B8[Client detached<br>or disconnected]
    end
    B8 --> B9
    B9[Close GDB client connection]
  end
  gdbclient -.-> gdbserver2
  subgraph gdbserver2[Core's GDB server]
    B10([Wait for all GDB client<br>connections to close]) -.-> B11
    B11[Resume core] --> B12
    B12[Close core's GDB server]
  end
  gdbserver2 -.-> B13
  B13([Wait for all servers to close]) --> B14
  B14(Sequence Block:<br>Disconnect Debugger):::seq
  click B14 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
```

---

### Command: pyOCD run

```mermaid
flowchart TD
  classDef seq fill:#c7d6ea,stroke:#333;

  B0(Sequence Block:<br>Connect Debugger to Device):::seq
  click B0 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
  B0 -.-> B1
  B1[Halt all cores] --> B2
  B2[Create Run servers for all cores] --> B3
  B3[Reset device with<br>primary core using<br>selected reset type]
  B3 ---> runserver
  subgraph runserver[Core's Run server loop]
    B4([Process<br>Semihosting + RTT]) -.-> B6
    B6{EOT<br>received?}
  end
  B3 --> loop
  subgraph loop[Loop]
    B7{Timelimit<br>reached?}
    B8{User terminated<br>pyOCD instance?}
  end
  B6 -- Yes ---> B9
  B7 -- Yes ---> B9
  B8 -- Yes ---> B9
  B9[Close all servers] --> B10
  B10(Sequence Block:<br>Disconnect Debugger):::seq
  click B10 "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#usage_of_sequences"
```

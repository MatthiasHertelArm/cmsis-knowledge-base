---
id: "intr-diving-into-jtag-overview-part-1-state-machine"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): State Machine"
summary: "The JTAG protocol’s finite state automaton comprises a set of states that the TAP can assume, depending on the signals received at its inputs. Each state corresponds to a specific combination of signal values for the TMS and TDI inputs."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#state-machine"
license: "CC-BY-SA-4.0"
mode: "V"
---

The JTAG protocol’s finite state automaton comprises a set of states that the TAP can assume, depending on the signals received at its inputs. Each state corresponds to a specific combination of signal values for the `TMS` and `TDI` inputs.

The transitions between states depend on the `TMS` signal at the moment of rising level of `TCK`.

The initial state after resetting is Test Logic-Reset. As defined by the standard the LSB is pushed in and pulled out first for all shift registers.

The State Machine is quite simple and has two ways of working:

- Instruction register selection (blue blocks) is used to select the current command.
- Data register selection (green blocks) is used to read/write data into the data registers.



  


All states have two outputs, and transitions are arranged so that any state can be reached by controlling the dispenser with a single `TMS` signal (synchronized by `TCK`). There are two distinct sequences of states: one for reading or writing to the data register and one for working with the instruction register.

Let's describe the most important states. But since `IR` path and DR path have identical states, I will describe these states for both paths at once specifying the differences if necessary.

- **Test-Logic-Reset** — all test logic is disabled, chip behaves normally.
- **Run-Test/Idle** — first state to initialize test logic and default idling state
- **Select-DR/IR-Scan** — this state is necessary to select the current path: data or instruction. I think this can be visualized as the operation of the switches: SW1, SW1, SW3, SW4. When the Select-DR-Scan the state is hit, the switches SW1, SW1, SW3, SW4 are switched to the corresponding DR register. When the Select-IR-Scan state is reached - switches SW1, SW1 are switched to the `IR` register.



  


- **Capture-DR** — In this state, there is a parallel loading of the value stored in the selected DR register into the shift register if you follow the Select-DR-Scan state branch and loading of a special pattern if we follow the Select-IR-Scan state path, the value 0x01 is usually selected as the pattern.



  


- **Shift-DR** — register shifts data from `TDI` one step forward `TDO`. The Shift-DR and Shift-IR states are the main states for serial-loading data into either data registers or the instruction register.



  


- **Update-DR** — the state in which the data in the shift register is written to the corresponding register in the chip. The Update-DR and Update-IR states latch the data into the registers, setting the data in the instruction register as the current instruction



  



- **Pause-DR/IR** — temporarily halt data shifting from `TDI` to `TDO`

The state machine progresses on the test clock (`TCK`) edge, with the value of the test mode select (`TMS`) pin controlling the behavior.

>**Note**: Regardless of the initial state of the TAP controller,
>the Test-Logic-Reset state can always be entered by holding the TMS logic 1 for 5 clock cycles of TCK.

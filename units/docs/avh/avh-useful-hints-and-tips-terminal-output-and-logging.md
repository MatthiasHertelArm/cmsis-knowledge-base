---
id: "avh-useful-hints-and-tips-terminal-output-and-logging"
type: "concept"
domain: "test"
title: "Useful Hints and Tips: Terminal output and logging"
summary: "Application can use following options for printing information to a console:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/simulation/src/hints_and_tips.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/simulation/src/hints_and_tips.md#terminal-output-and-logging"
license: "Apache-2.0"
mode: "V"
---

Application can use following options for printing information to a console:

- uart
- semihosting

### UART I/O

The application firmware can use UART channels available in the FVP model to print out information, with data being
forwarded to a Telnet terminal on the PC via a local TCP/IP connection.

This approach is especially beneficial for full-stack applications that also run on real hardware with UART
communication and so can keep uniform structure for virtual and real targets.

Below is useful information for using UART I/O on FVP targets:

- **Concept**: [Using-a-terminal-with-an-FVP](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/Using-a-terminal-with-an-FVP)
  and [TelnetTerminal](https://developer.arm.com/documentation/100964/1126/Fast-Models-components/Peripheral-components/TelnetTerminal)
  explain the concept in details.
- **UART Drivers**: CMSIS BSP packs listed in avh_fvp_cmsis contain drivers for UART access on corresponding FVP
  targets.
- **Retarget to UART**: [CMSIS-Compiler component](https://arm-software.github.io/CMSIS_6/latest/Compiler/index.html)
  implements retargeting of standard output functions, such as `printf()`.
- **FVP parameters**: the default values of FVP configuration parameters related to UART and Telnet should already work
  correctly. Refer to the FVP and Fast Models documentation as well as reference examples for additional information.
- **Windows setup** : On Windows you need to enable Telnet, as follows:
    - Open **Start > Settings**.
    - In the search box, type **Turn Windows features on or off** and click on the suggested item. The
      **Windows Features** dialog opens.
    - Select the **Telnet Client** check box and click **OK**. The installation might take several minutes to complete.
- **Linux setup** : on Linux both `xterm` and `telnet` must be installed and be specified in your PATH.
- **Logging** : If a UART output needs to be saved as a log file (for example in CI tests), you can use FVP parameter
  `<board>.<uart>.out_file` to specify the log file. For example for UART0 on Corstone-315:
  `mps4_board.UART0.out_file=./log.txt`.
    - If displaying the information in an output terminal is not required (for example in CI jobs), you can disable it
      with the configuration parameter `<board>.<telnetterminal>.start_telnet`. For example for Corsone-315 and UART0:
      `mps4_board.telnetterminal0.start_telnet=0`. In this case, the output will not be displayed in any terminal, but
      will be stored into a log file if this is configured accordingly with the `out_file` parameter.
- **Multiple channels**: in complex systems and applications it can be beneficial to separate output into different
  UART channels and hence terminals, to avoid cluttered messages in a single terminal.
- **Example** : [AVH-Hello](https://github.com/Arm-Examples/AVH-Hello) provides a universal example with UART output,
  covering all Arm FVP targets.

### Semihosting I/O

Applications can also rely on the semihosting mechanism that enables the code running on an FVP model to directly use
the input/output facilities of the host computer. With semihosting, we can enable standard C I/O functions, such as
`printf()` and `scanf()`, to use the host terminal from where the model is started.

This approach can be useful to quickly enable terminal communication and bypass the complexity of using UART and I/O
retargeting. It also helps to  achieve a simpler implementation for rather CPU-centric test suites with unit testing,
module testings and API testing that need to be run on various CPUs and with different compilers.

Below is useful information for using semihosting for terminal output on FVP targets:

- **Concept**: [Using semihosting](https://developer.arm.com/documentation/101470/2024-0/Controlling-Target-Execution/Using-semihosting-to-access-resources-on-the-host-computer)
  gives a good overview and references about semihosting on Arm targets. It is a part of Arm Development Studio
  documentation, and contains additional details for that environment.
- **FVP parameters**: by default, semihosting is disabled in FVPs and needs to be enabled with `semihosting-enable`
  configuration parameter on the CPU instance. For example for FVP_Corstone_SSE-3xx as `cpu0.semihosting-enable=1` and
  for FVP_MPS2_Cortex-M4 as  `armcortexm4ct.semihosting-enable=1`.
- **GCC support**: special considerations are required when using firmware built with GCC toolchain:
    - you need to set the spec strings file in Linker options as `--specs=rdimon.specs` to use the semihosted version
      of the syscalls.
    - when running a project built using GCC and CMSIS, the semihosting implementation can overwrite the memory
      configuration. To avoid this problem, configure the required values for stack and heap using model parameters, as
      described in
      [How do I Avoid Stack Pointer Corruption When Semihosting is Enabled on a GCC Toolchain?](https://developer.arm.com/documentation/ka005824/).
- **Logging**: to store the semihosted output, simply redirect the terminal output of the FVP execution to a log file,
  using standard mechanisms provided by corresponding console, such as `tee` in Linux or `>` in bash.
- **Examples**:
    - [CMSIS-Core Validation](https://github.com/ARM-software/CMSIS_6/tree/main/CMSIS/CoreValidation) project
      implements tests suite for CMSIS-Core using semihosting-based print outs. FVP configuration file can be found in
      [/Layer/Target](https://github.com/ARM-software/CMSIS_6/tree/main/CMSIS/CoreValidation/Layer/Target) folder for
      respective target, as `model-config.txt`.
    - [CMSIS-FreeRTOS Examples](https://github.com/ARM-software/CMSIS-FreeRTOS/tree/main/CMSIS/RTOS2/FreeRTOS/Examples)
      contain simple "hello world" style applications that use semihosting for print-outs.

Semihosting is also required for the following use cases:

- With [CMSIS-View](https://github.com/ARM-software/CMSIS-View) component to store the events and execution times into
  a log file on the host machine. See more in
  [Event Recorder semihosting](https://arm-software.github.io/CMSIS-View/main/er_use.html#er_semihosting).
- With arm_vsocket for using the internet connectivity of the host machine.

---
id: "avh-useful-hints-and-tips-execution-stop"
type: "concept"
domain: "test"
title: "Useful Hints and Tips: Execution stop"
summary: "Embedded applications typically run with an infinite loop that ensures continuous program execution."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/simulation/src/hints_and_tips.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/simulation/src/hints_and_tips.md#execution-stop"
license: "Apache-2.0"
mode: "V"
---

Embedded applications typically run with an infinite loop that ensures continuous program execution. But for executing
regression tests as part of Continuous Integration (CI) workflows it is often required that program execution is
stopped after a test is completed, so that the next test can be started.

FVP command line options `--cpulimit`, `--cyclelimit`, `--timelimit` and `--simlimit` can be used to stop execution
after specified activity time, for example, for 20 wall-clock seconds, use `--timelimit 20`. See
[FVP command line options](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/FVP-command-line-options)
for more details.

FVP models have a `shutdown_on_eot` parameter that enables simple implementation of program exit. The parameter should
be set in the Config, for example for FPV_Corstone_SSE-300:

```sh
mps3_board.uart0.shutdown_on_eot=1   # (bool, init-time) default = '0'
```

To trigger the shutdown, an `EOT` (ASCII 4) symbol can be transmitted to the corresponding serial interface from
the program. The code below demonstrates an example, where the execution is stopped after target execution count is
achieved. In this implementation the STDIO is assumed to be retargeted to the UART0:

```c
  while (1)  {
    printf ("Hello World %d\r\n", count);
    if (count > 100) printf ("\x04");  // EOT (0x04) stops simulation
    count++;
    osDelay (1000);
  }
```

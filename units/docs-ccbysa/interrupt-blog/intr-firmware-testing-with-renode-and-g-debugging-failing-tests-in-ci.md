---
id: "intr-firmware-testing-with-renode-and-g-debugging-failing-tests-in-ci"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: Debugging Failing Tests in CI"
summary: "Tests are going to fail in CI, and it's probably a good thing, as that's what CI is for. But, it would be a pain to guess and check how to fix issues that only occur in CI."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#debugging-failing-tests-in-ci"
license: "CC-BY-SA-4.0"
mode: "V"
---

Tests are going to fail in CI, and it's probably a good thing, as that's what CI
is for. But, it would be a pain to guess and check how to fix issues that only
occur in CI. Thankfully, Renode can capture the state of the system, save it to
a file, and load it after-the-fact[^renode_state_save] for postmortem debugging.

It does this using the monitor commands `Save` and `Load`. Wouldn't it be cool
if we could call the `Save` command in CI for failing tests and then locally run
`Load` in Renode to get the exact state of the device at the time of failure?
Yes, it would be.

Renode has part of this
[built-in](https://github.com/renode/renode/blob/05377ef375daa3d5ea0de12633d27bf26e20b3b3/src/Renode/RobotFrameworkEngine/renode-keywords.robot#L77-L86).
Unfortunately, this is yet another piece of functionality that doesn't exist in
the current public release, so I've
[copied and modified the code slightly](https://github.com/memfault/interrupt-renode-test-automation/blob/master/tests/common.robot).
Recall that GitHub Actions gobbles up the artifacts in the output folder
`/test_results` so as long as we place the snapshots in this directory, they
should be automatically included in our final ZIP.

In the example project, I've added a test that always fails. The C code
generates a fault which crashes the device:

```c
int cli_command_fault(int argc, char *argv[]) {
    // Bad function call!!
    void (*g_bad_func_call)(void) = (void (*)(void))0x20000002;
    g_bad_func_call();
    return 0;
}
```

The Robot Framework test fails after it doesn't get a response from the device.

```robot
*** Test Cases ***
Trigger Fault
    [Documentation]             Should fail, but fine since non_critical
    [Tags]                      non_critical  uart  input

    Start Test

    Wait For Prompt On Uart         ${SHELL_PROMPT}
    Write Line To Uart              fault

    # By now we've crashed
    Wait For Line On Uart           Nope     timeout=2
```

By adding the hooks above, every failing test should capture a Renode snapshot.

I've done a few commits into the example project repo with this test in place,
which means there is a ZIP with a Renode snapshot in it. Let's download one of
the ZIP archives and extract it.

```
$ tree .
test_results
├── log.html
├── logs.txt
├── report.html
├── robot_output.xml
├── snapshots
│   └── test-basic-Trigger_Fault.fail.save
└── test-basic.xml
```

The `test-basic-Trigger_Fault.fail.save` file is a snapshot from a test and
shell command that forces a crash.

Let's load it up into Renode & GDB and see what it looks like. I've created
another script in the project repo to help with loading these save files into
Renode, `load-save.sh`.

```bash
#!/bin/sh

sh /Applications/Renode.app/Contents/MacOS/macos_run.command --disable-xwt \
  -e "Load @$1" \
  -e 'mach set 0' \
  -e 'machine StartGdbServer 3333'
```

This script starts Renode in headless mode, loads the save file passed in as an
argument with the `Load` command, and starts a GDB server.

```
$ ./load-save.sh test_results/snapshots/test-basic-Trigger_Fault.fail.save
Loaded monitor commands from: ./scripts/monitor.py
Monitor available in telnet mode on port 1234
machine-0: GDB server with all CPUs started on port :3333
```

We see that the GDB port on 3333 is up and running, so let's attach to that
port. Don't forget to include the ELF file (which is also saved in the GitHub
build artifacts).

```
$ arm-none-eabi-gdb-py --eval-command="target remote :3333" --se renode-example.elf
[...]
(gdb) bt
#0  blocking_handler () at ../../cm3/vector.c:104
#1  <signal handler called>
#2  0x20000002 in rcc_ahb_frequency ()
#3  0x08000252 in cli_command_fault (argc=1, argv=0x2000ff74) at src/app_shell_commands.c:24
#4  0x08000528 in prv_process () at src/shell/src/shell.c:113
#5  0x080005ec in shell_receive_char (c=13 '\r') at src/shell/src/shell.c:147
#6  0x080001e0 in main () at src/app.c:29
```

That looks right! `0x20000002` was the bogus address I used which caused a
UsageFault, and we can tell it came from the CLI command `fault`.

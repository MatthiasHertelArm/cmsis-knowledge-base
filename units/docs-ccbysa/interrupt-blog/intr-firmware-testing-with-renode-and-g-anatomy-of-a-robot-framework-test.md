---
id: "intr-firmware-testing-with-renode-and-g-anatomy-of-a-robot-framework-test"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: Anatomy of a Robot Framework Test"
summary: "Now that we've verified that the firmware works within Renode, it's time to think about how we are going to test our firmware."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#anatomy-of-a-robot-framework-test"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we've verified that the firmware works within Renode, it's time to
think about how we are going to test our firmware. We have two shell commands,
`help` and `ping` which are probably useful "sanity" checks that we can test, so
let's start with those.

If we write `ping` as a command into our shell, the following is printed:

```
shell> ping
PONG
```

It makes logical sense to test that this exact text is printed. Although
incredibly basic, this is the code that we are testing within our firmware:

```c
int cli_command_ping(int argc, char *argv[]) {
    shell_put_line("PONG");
    return 0;
}
```

The following is a Robot Framework test file that calls the `ping` shell command
and expects that `PONG` is printed.

```robot
# test-basic.robot

*** Settings ***
# Boilerplate
Suite Setup       Setup
Suite Teardown    Teardown
Test Setup        Reset Emulation
Resource          ${RENODEKEYWORDS}

*** Variables ***
# Our shell prompt to expect
${SHELL_PROMPT}    shell>

*** Keywords ***
Start Test
    # Create the Machine
    Execute Command             mach create
    # Load the stm32f4 board definitions
    Execute Command             machine LoadPlatformDescription @platforms/boards/stm32f4_discovery-kit.repl
    Execute Command             machine LoadPlatformDescription @${PWD_PATH}/add-ccm.repl
    # Load the ELF file
    Execute Command             sysbus LoadELF @${PWD_PATH}/build/renode-example.elf
    # Connect the UART
    Create Terminal Tester      sysbus.uart2
    Start Emulation

*** Test Cases ***
Ping
    [Documentation]             Prints help menu of the command prompt
    [Tags]                      non_critical

    Start Test

    Wait For Prompt On Uart     ${SHELL_PROMPT}
    Write Line To Uart          ping
    Wait For Line On Uart       PONG        timeout=2
```

To help run this test locally, I've created a few extra helpers. First is a
script, `run_tests.sh`, which contains the following:

```
#!/bin/bash -e

RENODE_CHECKOUT=${RENODE_CHECKOUT:-~/code/renode}

${RENODE_CHECKOUT}/test.sh -t "${PWD}/tests/tests.yaml" --variable PWD_PATH:"${PWD}" -r "${PWD}/test_results"
```

`RENODE_CHECKOUT` is the Renode repo that we cloned (with all submodules
initialized!). The second line calls Renode's `test.sh` helper with the test
manifest file and tells it where to output the results.

The test manifest file, `tests.yaml` contains a list of tests that `test.sh`
should iterate over, and it can be used if we want to add more than a single
Robot test file.

```
# tests.yaml
- robot:
    - tests/test-basic.robot
```

If we run our `run_tests.sh` script and see what we get!

```
# Ensure our Python2.7 environment is activated
$ conda activate renode

# Go!
$ ./run_tests.sh
Preparing suites
Started Renode instance on port 9999; pid 82717
Starting suites
Running tests/test-basic.robot
+++++ Starting test 'test-basic.Ping'
+++++ Finished test 'test-basic.Ping' in 1.55 seconds with status OK
Cleaning up suites
Closing Renode pid 82717
Aggregating all robot results
Output:  /Users/tyler/dev/interrupt-renode-test-automation/test_results/robot_output.xml
Log:     /Users/tyler/dev/interrupt-renode-test-automation/test_results/log.html
Report:  /Users/tyler/dev/interrupt-renode-test-automation/test_results/report.html
Tests finished successfully :)
```

Awesome. Our simple test was able to launch the firmware, execute the `ping`
command, receive a `PONG` response, and generate a report.

We can also add another test to this same file to test our `help` command, and
we can use multiple `Wait For Line On Uart`, one after the other. We can append
the following to the end of `test_basic.robot`:

```robot
*** Test Cases ***
Help Menu
    Start Test

    Wait For Prompt On Uart     ${SHELL_PROMPT}
    Write Line To Uart          help

    # Expect two lines
    Wait For Line On Uart       help: Lists all commands      timeout=2
    Wait For Line On Uart       ping: Prints PONG             timeout=2
```

This covers the basic functionality for tests, but there is **so much more**
that can be done with this infrastructure.

---
id: "intr-cortex-m-mcu-emulation-with-renode-renode-integration-tests"
type: "concept"
domain: "debug"
title: "Cortex-M MCU Emulation with Renode: Renode & Integration Tests"
summary: "Another area where emulation really shines is the ability to run automated tests without hardware. Renode integrates with the Robot Framework[^3] to enable this uses case."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-23-intro-to-renode.md"
doc_source: "https://interrupt.memfault.com/blog/intro-to-renode#renode-integration-tests"
license: "CC-BY-SA-4.0"
mode: "V"
---

Another area where emulation really shines is the ability to run automated tests
without hardware. Renode integrates with the Robot Framework[^3] to enable this
uses case.

A full tutorial on the Robot Framework is outside of the scope of this post, but
it is already quite useful.

To make the test more interesting, let's add a button to our firmware. The STM32
discovery board we are emulating has one on Port A pin 0, which we can enable
with a few lines of code:

```c
static void button_setup(void)
{
    /* Enable GPIOA clock. */
    rcc_periph_clock_enable(RCC_GPIOA);

    /* Set GPIOA0 to 'input floating'. */
    gpio_mode_setup(GPIOA, GPIO_MODE_INPUT, GPIO_PUPD_NONE, GPIO0);
}
```

We then modify our main function to test the state of the button

```c
    bool button_is_pressed = false;

    while (1) {
        if (!button_is_pressed && gpio_get(GPIOA, GPIO0)) {
            button_is_pressed = true;
        } else if (button_is_pressed && !gpio_get(GPIOA, GPIO0)) {
            printf("button pressed\n");
            button_is_pressed = false;
        }
    }
```

Not how we'd do it in production, but it works!

We can then write a simple Robot Framework script to exercise our firmware:

```robot
# Filename: test-button.robot
*** Settings ***
Suite Setup                   Setup
Suite Teardown                Teardown
Test Setup                    Reset Emulation
Resource                      ${RENODEKEYWORDS}

*** Test Cases ***
Should Handle Button Press
    Execute Command         mach create
    Execute Command         machine LoadPlatformDescription @platforms/boards/stm32f4_discovery-kit.repl
    Execute Command         machine LoadPlatformDescription @${PATH}/add-ccm.repl
    Execute Command         sysbus LoadELF @${PATH}/renode-example.elf

    Create Terminal Tester  sysbus.uart2

    Start Emulation

    Wait For Line On Uart   hello world
    Test If Uart Is Idle    3
    Execute Command         sysbus.gpioPortA.UserButton Press
    Test If Uart Is Idle    3
    Execute Command         sysbus.gpioPortA.UserButton Release
    Wait For Line On Uart   button pressed
```

This test will wait for the "hello world" string to print, then press and
release the button and wait for "button pressed" to print.

To run the test, we need to checkout and build the Renode codebase. You can find
step by step instructions on their website[^4]. We can then use the
`run_tests.py` script to execute our test.

```
python -u <path-to-renode>/tests/run_tests.py tests/test-button.robot -r test_results --variable PATH:$PWD
```

You'll notice a few things:

1. We passed a "test_results" folder to the script, which is a location that
   HTML test results will be written
2. We must pass the path to our working directory in a variable, as it is not
   propagated automatically

To make life easier, I wrapped this command in a shell script here as well:

```bash
#!/bin/sh

RC=${RENODE_CHECKOUT:-~/code/renode}

python -u $RC/tests/run_tests.py tests/test-button.robot -r test_results --variable PATH:$PWD
```

Running this shell script, we observe the test running!

```
$ ./test.sh
Preparing suites
Starting suites
Running tests/test-button.robot
+++++ Starting test 'test-button.Should Handle Button Press'
+++++ Finished test 'test-button.Should Handle Button Press' in 8.35 seconds with status OK
Cleaning up suites
Aggregating all robot results
Output:  /Users/francois/code/interrupt/example/renode/test_results/robot_output.xml
Log:     /Users/francois/code/interrupt/example/renode/test_results/log.html
Report:  /Users/francois/code/interrupt/example/renode/test_results/report.html
Tests finished successfully :)
```

Success! As a bonus, the robot framework generates some pretty HTML reports:



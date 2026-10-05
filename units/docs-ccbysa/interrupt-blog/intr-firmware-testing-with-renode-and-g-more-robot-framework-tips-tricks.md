---
id: "intr-firmware-testing-with-renode-and-g-more-robot-framework-tips-tricks"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: More Robot Framework Tips & Tricks"
summary: "The best place to start for inspiration for the various features of Renode's integration with Robot Framework is to search around the Internet. I've searched for \"Create Terminal Tester\" on GitHub and grep.app and found great examples."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#more-robot-framework-tips-tricks"
license: "CC-BY-SA-4.0"
mode: "V"
---

The best place to start for inspiration for the various features of Renode's
integration with Robot Framework is to search around the Internet. I've searched
for "Create Terminal Tester" on
[GitHub](https://github.com/search?q=%22Create+Terminal+Tester%22&type=Code) and
[grep.app](https://grep.app/search?q=Create%20Terminal%20Tester) and found great
examples.

### Built-In Libraries

The official
[Robot Framework documentation](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
is the best reference to learn what commands come built-in. To use these
commands, you may need to include the library. For instance, if you wanted to
use the `DateTime` library[^rf_datetime], you'd have to import it at the top of
your test suite.

```robot
*** Settings ***
Library           DateTime
```

### UART Timeouts

To keep tests failing quickly, make sure not to forget adding
`timeout=<seconds>` to UART expectations.

```
    Wait For Line On Uart       help: Lists all commands      timeout=2
```

If you are building Renode from source or have a release greater than 1.9.0, you
can also set this globally by overriding the `${DEFAULT_UART_TIMEOUT}` variable
in your suite.

```robot
*** Variables ***
${DEFAULT_UART_TIMEOUT}     2
```

### Regular Expressions on UART

You can expect and validate strings from the UART by using regular expressions,
which allows developers to read in values that change between invocations of the
test. For example, we can test the following shell command:

```c
int cli_command_greet(int argc, char *argv[]) {
    char buf[64];
    snprintf(buf, sizeof(buf), "Hello %s!", argv[1]);
    shell_put_line(buf);
    return 0;
}
```

By using `treatAsRegex=True` and saving this value to `p`, we can then read it
out by using `p.groups[0]` and comparing it to the name provided in the test.

```robot
*** Test Cases ***
Greet
    Start Test

    Wait For Prompt On Uart         ${SHELL_PROMPT}
    Write Line To Uart              greet Tyler

    ${p}=  Wait For Line On Uart    Hello (\\w+)!     treatAsRegex=true     timeout=2
    Should Be True                  'Tyler' == """${p.groups[0]}"""
```

### Comparison Operations

At Pebble, we used dynamic memory allocations. To help us sleep at night and
confirm that we always had enough heap available on every build we shipped, we
added tests ensuring our high-water-marks were within acceptable limits. A test
we might have written at the time would measure the available heap space after
all of the tests had finished.

```robot
*** Test Cases ***
High Water Mark
    Start Test

    Wait For Prompt On Uart         ${SHELL_PROMPT}
    Write Line To Uart              heap_free

    ${p}=  Wait For Line On Uart    (\\d+)     treatAsRegex=true  timeout=2
    ${i}=  Convert To Integer       ${p.groups[0]}

    # Ensure we have 5000 bytes free at the end of the tests
    Should Be True                  5000 < ${i}
```

In our automated tests, we did similar checks to make sure that our performance,
power usage, stack, and heap usage were always within acceptable limits.

### Line Endings

If your shell uses carriage returns as line endings, make sure to add the
following option when creating the tester:

```
    Create Terminal Tester    ${UART}  endLineOption=TreatCarriageReturnAsEndLine
```

### Tags & Documentation

You can add a **Tags** and **Documentation** attribute to each test, which will
help bucket your tests up into logical groups and help developers know what each
test is doing.

```robot
*** Test Cases ***
Command
    [Documentation]             Some command
    [Tags]                      critical  uart  factory
```



  


> Adding the tag `non_critical` or `skipped` on a test will allow the test to
> fail but not mark the entire test run as a failure. You can use this for
> work-in-progress or flaky tests.

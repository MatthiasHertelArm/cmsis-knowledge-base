---
id: "intr-building-a-tiny-cli-shell-for-tiny-building-a-basic-shell"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware: Building a Basic Shell"
summary: "It's now time to build up a basic shell implementation, which we will expand upon to cover the features that are most important for a good developer and QA experience."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell#building-a-basic-shell"
license: "CC-BY-SA-4.0"
mode: "V"
---

It's now time to build up a basic shell implementation, which we will expand
upon to cover the features that are most important for a good developer and QA
experience.

### Setup

For this setup we will use:

- a nRF52840-DK[^nrf5_sdk] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^jlink] as our GDB Server
- GCC 8.3.1 / GNU Arm Embedded Toolchain as our compiler[^gnu_toolchain]
- GNU make as our build system

To keep things simpler in the blog post, we'll be modifying an example of the
nRF52 SDK, and will be using the soft device SDK. We will be modifying the
`nrf5_sdk/examples/peripheral/uart` example.

The only thing we need from the SDK is a `putc` and `getc` implementation, which
the nRF52 SDK provides as `app_uart_get` and `app_uart_put`[^sdk_uart]. As long
as you have the equivalent in your firmware project, the examples should easily
apply.

All the code can be found on the
[Interrupt Github page](https://github.com/memfault/interrupt/tree/master/example/firmware-shell)
with more details in the `README` in the directory linked.

To download the code yourself:

```
$ git clone https://github.com/memfault/interrupt.git
$ cd examples/firmware-shell

# Build and flash device
$ make part1_flash
```

### Input and Output

The first thing we need to figure out is how to receive and print characters to
the serial port. In the nRF52 SDK, the two functions `app_uart_get` and
`app_uart_put` are given to us. Let's wrap these so they are easier to use for
our use case.

```c
#include "app_error.h"
#include "app_uart.h"

void console_putc(char c) {
  app_uart_put(c);
}

char console_getc(void) {
  // Blocks until a character is captured from the UART
  uint8_t cr;
  while (app_uart_get(&cr) != NRF_SUCCESS);
  return (char)cr;
}
```

We can now easily get and put characters from the serial port. Let's now build a
way to capture full lines more easily. We take the implementation from
libopencm3's uart_console example[^libopencm3_uart_console], which provides a
clean `console_gets` implementation.

```c
void console_puts(char *s) {
  while (*s != '\0') {
    if (*s == '\r') {
      console_putc('\n');
    } else {
      console_putc(*s);
    }
    s++;
  }
}

int console_gets(char *s, int len) {
  char *t = s;
  char c;

  *t = '\000';
  /* read until a <LF> is received */
  while ((c = console_getc()) != '\n') {
    *t = c;
    console_putc(c);
    if ((t - s) < len) {
      t++;
    }
    /* update end of string with NUL */
    *t = '\000';
  }
  return t - s;
}
```

> NOTE: We are using newlines instead of carriage returns. Make sure to
> configure the console as such!

With these two functions implemented, we now can build our main loop that
constantly consumes input from the shell and outputs it to the user.

```c
int main(void) {
  [...]

  char buf[128];
  int len;
  while (true) {
    console_puts("$ ");
    len = console_gets(buf, 128);
    console_putc('\n');
    if (len) {
      console_puts("\n");
      console_puts("OK");
      console_puts("\n");
    }
  }
}
```

To view the entire file, including the base nRF52 required initialization,
please check out the
[`main.c` on Github](https://github.com/memfault/interrupt/tree/master/example/firmware-shell/part1/main.c).

We can launch PySerial's `miniterm.py`[^miniterm] to connect to my nRF52. When I
initialized the UART, I used 115200 as the baud rate, so we'll make sure to pass
it as an argument.

```
$ make part1_flash
[...]

$ miniterm.py "/dev/cu.usbmodem*" 115200 --eol LF
--- Miniterm on /dev/cu.usbmodem0006839616591  115200,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
$ test
> OK
$ another
> OK
```

And that's a bare-bones console! What remains now is parsing the command name
and arguments. However, instead of building upon this example, we are going to
take the software engineering approach and use what already is out there and
open-sourced.

### Integrating Memfault's CLI Shell

I have pulled in an example of the command-line shell we use at Memfault for
tiny embedded devices and copied it into the example repository for this post,
This is what we'll use going forward.

This CLI was chosen primarily for its simplicity, ease of use of arguments, and
registering new commands, and because, frankly, there aren't many open-source
shells with firmware in mind.

Our goal in this section is to build a simple Hello World example with this new
shell implementation.

#### Build System Integration

Let's first go through what you would need to do to copy the Memfault CLI
implementation into your own project's build system.

```
$ cd example/firmware-shell/part2/
```

Next, you would copy the following directory and files into your project.

```
part2/shell
├── include
│   └── shell
│       └── shell.h
└── src
    └── shell.c
```

Last, add the following paths to your build system.

```
SRC_FILES += \
    shell/src/shell.c \
    shell_commands.c  \   # Doesn't exist yet!

INC_FOLDERS += \
    shell/include
```

#### Main Loop Integration

Now that the project is integrated into our build system, let's initialize the
shell in our `main.c` file. Thankfully, it's very simple since we already have
`console_getc` and `console_putc` built already.

We replace our previous `while ()` loop with one that passes all characters
consumed from the UART to the shell implementation.

```c
int main(void) {
  [...]

  // Configure shell
  sShellImpl shell_impl = {
    .send_char = console_putc,
  };
  shell_boot(&shell_impl);

  // Consume and send characters to shell...forever
  char c;
  while (true) {
    c = console_getc();
    shell_receive_char(c);
  }
}
```

> TIP: It's worthwhile to look at the source code to
> [`shell_receive_char`](https://github.com/memfault/interrupt/blob/master/example/firmware-shell/part2/shell/src/shell.c#L126-L140).

#### Creating and Registering Commands

The last piece of our Hello World example is to create and register a command
with the shell. To do this, create a file called `shell_commands.c` (which we've
already added to our build system) and paste in the following code:

```c
#include "shell/shell.h"

#include <stddef.h>
#include <stdio.h>

#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

// A simple Hello World command which prints "Hello World!"
int cli_cmd_hello(int argc, char *argv[]) {
  shell_put_line("Hello World!");
  return 0;
}

static const sShellCommand s_shell_commands[] = {
  {"hello", cli_cmd_hello, "Say hello"},
  {"help", shell_help_handler, "Lists all commands"},
};

const sShellCommand *const g_shell_commands = s_shell_commands;
const size_t g_num_shell_commands = ARRAY_SIZE(s_shell_commands);
```

Let's break this down.

```c
int cli_cmd_hello(int argc, char *argv[]) {
  shell_put_line("Hello World!");
  return 0;
}
```

Each command registered into the shell needs to accept two arguments, `int argc`
and `char *argv[]`. The two arguments contain arguments specific to the command,
but we'll cover this in the next section.

Within the command, we call `shell_put_line` with a string, which our shell will
then print on our behalf, with a newline after. Behind the scenes, it will use
our `console_putc` which we configured the shell with earlier.

The latter part of the larger code snippet above can be understood better by
looking at the
[`include/shell/shell.h`](https://github.com/memfault/interrupt/tree/master/example/firmware-shell/part2/shell/include/shell/shell.h)
file.

```c
typedef struct ShellCommand {
  const char *command;
  int (*handler)(int argc, char *argv[]);
  const char *help;
} sShellCommand;

extern const sShellCommand *const g_shell_commands;
extern const size_t g_num_shell_commands;
```

This tells us that we need to define a `g_shell_commands` global variable, which
is a list of `sShellCommand`, each of which contains a command name, a function
pointer, and a help string, which we do in the snippet below.

```c
static const sShellCommand s_shell_commands[] = {
  {"hello", cli_cmd_hello, "Say hello"},
  {"help", shell_help_handler, "Lists all commands"},
};

const sShellCommand *const g_shell_commands = s_shell_commands;
const size_t g_num_shell_commands = ARRAY_SIZE(s_shell_commands);
```

#### Testing Our Hello World Command

And that's it! All of the code above is available
[here](https://github.com/memfault/interrupt/tree/master/example/firmware-shell/part2)
on Interrupt's Github, so be sure to check it out there for a deeper analysis.

If we compile and run this example, we can see that our simple shell works!

```
$ miniterm.py "/dev/cu.usbmodem*" 115200 --eol LF
--- Miniterm on /dev/cu.usbmodem0006839616591  115200,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---

shell> hello
Hello World!
shell> test
Unknown command: test
Type 'help' to list all commands
```

With the use of the basic shell provided, we were able to get up and running
very quickly. If you don't already have a command-line shell to your device, I
hope this inspires you to at least get this minimal amount running.

#### Help Command

You may have noticed there is a `help` command in our shell. This allows the
user to type `help` into the shell and get a list of all the commands that are
available, along with the `char *help` string that was passed into the
registration table.

```
shell> help
hello: Say hello
help: Lists all commands
```

You can find the full source of the help command
[on Github](https://github.com/memfault/interrupt/blob/master/example/firmware-shell/part2/shell/src/shell.c#L148-L156)

### Command Arguments

In our Hello World command, there were two arguments, `int argc` and
`char *argv[]`, which we skimmed over.

```c
int cli_cmd_hello(int argc, char *argv[]) {
  shell_put_line("Hello World!");
  return 0;
}
```

These might seem cryptic at first, but this is the standard way to pass
command-line arguments to C/C++ programs.[^command_line_args]

**argc** - number of strings pointed to by `argv`
 **argv** - 1 plus the
number of arguments passed to the function. The first argument is the command
name.


To further understand how these two arguments work together in our shell, let's
build a command called `kv_write` that could hook into the Key/Value Store from
a previous Interrupt post, [Unit Testing
Basics](https://interrupt.memfault.com/blog/unit-testing-basics#basic-implementation-of-keyvalue-store).
This command will take two arguments from the user, a key and value, and work in
the following way:

```
$ kv_write device_name "Device ABCD"
> OK
```

We need to write a function for the command now, which will call
`kv_store_write()` with our key and value.

```c
int cli_cmd_kv_write(int argc, char *argv[]) {
  // We expect 3 arguments:
  // 1. Command name
  // 2. Key
  // 3. Value
  if (argc != 3) {
    shell_put_line("> FAIL,1");
    return;
  }

  const char *key = argv[1];
  const char *value = argv[2];

  bool result = kv_store_write(key, value, strlen(value));
  if (!result) {
    shell_put_line("> FAIL,2");
    return;
  }
  shell_put_line("> OK");
  return 0;
}
```

> NOTE: Notice that we use a different FAIL code for each failure case. This is
> to assist in debugging when a failure is hit.

The final part would be to add it to the list within `shell_commands.c`.

```c
static const sShellCommand s_shell_commands[] = {
  {"kv_write", cli_cmd_kv_write, "Write a Key/Value pair"},  // Added!
  {"hello", cli_cmd_hello, "Say hello"},
  {"help", shell_help_handler, "Lists all commands"},
};
```

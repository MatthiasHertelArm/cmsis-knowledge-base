---
id: "intr-building-a-tiny-cli-shell-for-tiny-tips-and-considerations"
type: "concept"
domain: "debug"
title: "Building a Tiny CLI Shell for Tiny Firmware: Tips and Considerations"
summary: "There are two consumers of a device's shell: a developer and a machine hooked up to the device through serial. Therefore, an output format should be both human and machine-readable."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-09-firmware-shell.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-shell#tips-and-considerations"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Formatted Output

There are two consumers of a device's shell: a developer and a machine hooked up
to the device through serial. Therefore, an output format should be both human
and machine-readable.

I suggest that all commands succeed or fail in the same way, either printing
`OK` or `FAIL,<code>`. It might help to build helper functions that do this for
you:

```c
void shell_result_success(void) {
  shell_put_line("> OK");
}

void shell_result_fail(int code) {
  char buf[32];
  snprint(buf, sizeof(buf), "> FAIL,%d", code);
  shell_put_line(buf);
}

```

One common format that is used is CSV, which is mostly readable depending on
what is being output. Below, we show an example of a `dump_heap` command which
would spit out a CSV, which a developer could then copy into Excel or Google
Sheets and do further inspections.

```
$ dump_heap
addr,size
0x00200000,64
0x00200040,128
...
```

If you are trying to output files or raw binary buffers into the shell, I
recommend using base64 or hexdump encoding, which will make it easier for
automated systems to ingest and convert the output.

### Extra Shell Features

Every developer loves a full-featured shell. These features might include being
able to backspace and delete keys, use the left and right arrow keys for
in-place editing, Emacs shortcuts, command history and completion, argument
parsing, and help menus.

To learn how to add some of these features to your project's shell, it's best to
look at a few open-source projects. Unfortunately, there aren't many _great_
shell's publicly available for tiny firmware.

- [Zephyr Shell](https://github.com/zephyrproject-rtos/zephyr/blob/master/subsys/shell)
- [Skip Scooters Anchor Console](https://github.com/rideskip/anchor/tree/master/console)
- [ESP-IDF Console](https://github.com/espressif/esp-idf/tree/master/components/console)

I would say the Zephyr shell is the opposite of small and lightweight, but that
is because it can be run through the RTT console, telnet, UART, and likely
arbitrary transports. It contains every shell feature you have come to love on
your UNIX shell, such as history, wildcard support, hexdumps, and support for
many keyboard shortcuts. If you are looking for _how_ to implement a certain
shell feature, I'd check out this repo.

If you are looking for something a bit more featured than the shell built
earlier, I'd give Anchor a look. It provides history, completion support, and
has an API built on top of macros for easier registering of commands and
arguments.

If you want to take inspiration from my favorite solution, check out the
ESP-IDF's
[`idf_monitor.py`](https://github.com/espressif/esp-idf/blob/master/tools/idf_monitor.py#L3-L10).
It is based upon PySerial's miniterm but adds convenient features host-side such
as automatically `addr2line` address lookups and rebuild-and-flash in one step.

There is no one-size-fits-all shell, as every project has different requirements
based upon memory, functionality, and code space.

### Stable Automated & Factory Tests

For a suite of factory verifications and automated tests to function 100% of the
time, the command arguments, behavior, and output (including formatting!) **can
not** change between builds. This is because these systems have parsers on the
output and those would break if the responses weren't in the correct format.

The simplest way to verify that the input and output do not change between
builds is to invest in a suite of unit tests with [proper
mocks](https://interrupt.memfault.com/blog/unit-test-mocking) that assert that every
character being output remains the same. These should then be run within CI for
every pull request and master branch commit.

### Slimming Down Shell Commands

Every command that you add to the shell will take up a non-trivial amount of
code space. The command implementations usually contain a lot of strings and
formatting code, which doesn't optimize well. When the firmware is out of space
([don't let it](https://interrupt.memfault.com/blog/code-size-deltas)), these shell
features are usually some of the first to go.

You usually want to perform automated tests on a production-like build. These
builds will have fewer developer-facing bells and whistles and only contain the
bare minimum set of commands to successfully and completely run through the set
of automated tests that your team has built.

To make sure that the tests that need to be stable do remain stable, I advise
heavy usage of comments and also tests to confirm the outputs don't change.

```c
static const sShellCommand s_shell_commands[] = {

#if !PRODUCTION_BUILD
  {"help", shell_help_handler, "Lists all commands"},
  {"history", shell_cmd_shell_history, "Show last 10 shell commands"},
  {"heap_dump", shell_cmd_heap_dump, "Parses and pretty-prints the heap"},
#endif

// ==========================================================
// DON'T CHANGE THESE COMMANDS. YOU'LL BREAK AUTOMATED TESTS!
// ==========================================================
  {"get_device_info", shell_cmd_get_device_info, "Get device info"},
  {"reboot", shell_cmd_system_reboot, "Reboot system"},
  {"resets", shell_cmd_system_reset, "Factory resets system"},
};
```

```c
// ==========================================================
// DON'T CHANGE THIS COMMAND. YOU'LL BREAK AUTOMATED TESTS!
// ==========================================================
// Output Format:
// > OK
void shell_cmd_system_reset(void) {
  [...]
}
```

### Securing the Shell

Before the device leaves the factory and goes out to the end customer, you'll
likely want to secure the serial port and shell in some way. This is to ensure
bad actors do not gain access to the system. I'll quickly go over a few ways
that you can lock down the shell to limit access to approved developers or
technicians.

#### Password Verification

This is the simplest approach to locking down the serial port. If the
verification process is successful, the shell will unlock itself!

Although its security is questionable, it is a good base-line I would put in
place to restrict a chunk of hobby hackers from gaining access to the system.

Note that this would be easily thwarted by anyone running
[`strings`](https://interrupt.memfault.com/blog/gnu-binutils#strings) on the firmware, as
the password will be seen in plain text. So you might want to add a basic cipher
to the password, such as the following:

```c
bool validate_password(const char *attempt) {
  // UNLOCK with each char rotated by 1 character
  // U + 1 = V, etc
  const char *password = "VOMPDL"

  for (int i = 0; i < sizeof(password) - 1; i++) {
    // Apply simple cipher, compare character
    if ((password[i] - 1) != attempt[i]) {
      return false;
    }
  }

  return true;
}
```

Still not great security, but it is better than nothing.

#### Knock Pattern

This method using timing and logic to send a pattern to the device that it will
verify. If the verification process is successful, the shell will unlock itself.

This method can be compared to
[this knocking sequence (video)](https://www.youtube.com/watch?v=1BB6wj6RyKo)
that GE Lighting built into their light bulbs to place them into "firmware
update" mode.

#### Signed Verification

Most devices today include a public or private key baked in to allow for secure
communication with remote servers. If this system is in place, it wouldn't take
much more effort to use this system to help unlock the shell.

A basic approach would be for the central server to sign the phrase "UNLOCK"
with the device's key. This payload can then be sent over the UART, and, if the
device verifies the authenticity of the payload, it will unlock the shell.

This is all the detail I'll give about this process for now, as the topic is
worthy of a blog post itself.

#### Different Firmware

The most secure way to lock down the shell is to not include the shell at all.
Simple, but it will severely limit your ability to debug a faulty production
device should you receive one from customer support.

---
id: "zep-shell-reading-user-input"
type: "concept"
domain: "debug"
title: "Shell: Reading User Input"
summary: "The shell provides a shell_readline function that allows command handlers to interactively read a line of input from the user."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

The shell provides a `shell_readline` function that allows command handlers
to interactively read a line of input from the user. This is useful for implementing
commands that need to prompt the user for additional information, such as confirmation
dialogs, multi-step wizards, or interactive data entry.

The function reads from the shell transport until a newline character is received,
storing the data in a provided buffer. The newline character itself is not included
in the buffer. The buffer is automatically null-terminated on success.

Use `shell_readline_prompt_set` before calling `shell_readline` to
display a prompt string (e.g. `"Proceed? [y/N]: "`). The prompt is printed
automatically at the start of readline and restored after any log messages that
interrupt the input line. It is cleared when `shell_readline` returns.


**Note:** The `shell_readline` function should be called from the shell thread in a shell command handler and blocks the thread until a result is returned.

Example usage:

```c

static int cmd_read_secret(const struct shell *sh, size_t argc, char **argv)
{
        uint8_t input_buf[256];
        int ret;

        shell_obscure_set(sh, true);
        shell_readline_prompt_set(sh, "Enter your secret: ");
        ret = shell_readline(sh, input_buf, sizeof(input_buf), K_SECONDS(10));
        shell_obscure_set(sh, false);

        if (ret < 0) {
                if (ret == -ETIMEDOUT) {
                        shell_error(sh, "Timeout waiting for input");
                } else if (ret == -ECANCELED) {
                        shell_error(sh, "Input canceled");
                } else if (ret == -ENOBUFS) {
                        shell_error(sh, "Input too long");
                }
                return ret;
        }

        shell_print(sh, "Secret input received (%d bytes)", ret);
        return 0;
}
```

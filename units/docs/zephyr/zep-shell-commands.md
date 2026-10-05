---
id: "zep-shell-commands"
type: "concept"
domain: "debug"
title: "Shell: Commands"
summary: "Shell commands are organized in a tree structure and grouped into the following types:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/shell/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/shell/index.rst"
license: "Apache-2.0"
mode: "V"
---

Shell commands are organized in a tree structure and grouped into the following
types:

* Root command (level 0): Gathered and alphabetically sorted in a dedicated
  memory section.
* Static subcommand (level > 0): Number and syntax must be known during compile
  time. Created in the software module.
* Dynamic subcommand (level > 0): Number and syntax does not need to be known
  during compile time. Created in the software module.



### Commonly-used command groups


The following list is a set of useful command groups and how to enable them:


#### GPIO


- `CONFIG_GPIO`
- `CONFIG_GPIO_SHELL`


#### I2C


- `CONFIG_I2C`
- `CONFIG_I2C_SHELL`


#### Sensor


- `CONFIG_SENSOR`
- `CONFIG_SENSOR_SHELL`


#### Flash


- `CONFIG_FLASH`
- `CONFIG_FLASH_SHELL`


#### File-System


- `CONFIG_FILE_SYSTEM`
- `CONFIG_FILE_SYSTEM_SHELL`


#### ADC


- `CONFIG_ADC`
- `CONFIG_ADC_SHELL`
- `CONFIG_ADC_EMUL_SHELL` (requires `CONFIG_ADC_EMUL`)


### Creating commands


Use the following macros for adding shell commands:

* `SHELL_CMD_REGISTER` - Create root command. All root commands must
  have different name.
* `SHELL_COND_CMD_REGISTER` - Conditionally (if compile time flag is
  set) create root command. All root commands must have different name.
* `SHELL_CMD_ARG_REGISTER` - Create root command with arguments.
  All root commands must have different name.
* `SHELL_COND_CMD_ARG_REGISTER` - Conditionally (if compile time flag
  is set) create root command with arguments. All root commands must have
  different name.
* `SHELL_CMD` - Initialize a command.
* `SHELL_COND_CMD` - Initialize a command if compile time flag is set.
* `SHELL_EXPR_CMD` - Initialize a command if compile time expression is
  non-zero.
* `SHELL_CMD_ARG` - Initialize a command with arguments.
* `SHELL_COND_CMD_ARG` - Initialize a command with arguments if compile
  time flag is set.
* `SHELL_EXPR_CMD_ARG` - Initialize a command with arguments if compile
  time expression is non-zero.
* `SHELL_STATIC_SUBCMD_SET_CREATE` - Create a static subcommands
  array.
* `SHELL_SUBCMD_DICT_SET_CREATE` - Create a dictionary subcommands
  array.
* `SHELL_DYNAMIC_CMD_CREATE` - Create a dynamic subcommands array.

Commands can be created in any file in the system that includes
`include/zephyr/shell/shell.h`. All created commands are available for all
shell instances.


#### Static commands


Example code demonstrating how to create a root command with static
subcommands.

```c

/* Creating subcommands (level 1 command) array for command "demo". */
SHELL_STATIC_SUBCMD_SET_CREATE(sub_demo,
    SHELL_CMD(params, NULL, "Print params command.",
                           cmd_demo_params),
    SHELL_CMD(ping,   NULL, "Ping command.", cmd_demo_ping),
    SHELL_SUBCMD_SET_END
);
/* Creating root (level 0) command "demo" */
SHELL_CMD_REGISTER(demo, &sub_demo, "Demo commands", NULL);
```
Example implementation can be found under following location:
`samples/subsys/shell/shell_module/src/main.c`.


### Dictionary commands

This is a special kind of static commands. Dictionary commands can be used
every time you want to use a pair: (string <-> corresponding data) in
a command handler. The string is usually a verbal description of a given data.
The idea is to use the string as a command syntax that can be prompted by the
shell and corresponding data can be used to process the command.

Let's use an example. Suppose you created a command to set an ADC gain.
It is a perfect place where a dictionary can be used. The dictionary would
be a set of pairs: (string: gain_value, int: value) where int value could
be used with the ADC driver API.

Abstract code for this task would look like this:

```c

static int gain_cmd_handler(const struct shell *sh,
                size_t argc, char **argv, void *data)
{
    int gain;

    /* data is a value corresponding to called command syntax */
    gain = (int)data;
    adc_set_gain(gain);

    shell_print(sh, "ADC gain set to: %s\n"
               "Value send to ADC driver: %d",
               argv[0],
               gain);

    return 0;
}

SHELL_SUBCMD_DICT_SET_CREATE(sub_gain, gain_cmd_handler,
    (gain_1, 1, "gain 1"), (gain_2, 2, "gain 2"),
    (gain_1_2, 3, "gain 1/2"), (gain_1_4, 4, "gain 1/4")
);
SHELL_CMD_REGISTER(gain, &sub_gain, "Set ADC gain", NULL);
```
This is how it would look like in the shell:


#### Dynamic commands


Example code demonstrating how to create a root command with static and dynamic
subcommands. At the beginning dynamic command list is empty. New commands
can be added by typing:

```none

dynamic add <new_dynamic_command>
```
Newly added commands can be prompted or autocompleted with the `Tab` key.

```c

/* Buffer for 10 dynamic commands */
static char dynamic_cmd_buffer[10][50];

/* commands counter */
static uint8_t dynamic_cmd_cnt;

/* Function returning command dynamically created
 * in  dynamic_cmd_buffer.
 */
static void dynamic_cmd_get(size_t idx,
                struct shell_static_entry *entry)
{
    if (idx < dynamic_cmd_cnt) {
        entry->syntax = dynamic_cmd_buffer[idx];
        entry->handler  = NULL;
        entry->subcmd = NULL;
        entry->help = "Show dynamic command name.";
    } else {
        /* if there are no more dynamic commands available
         * syntax must be set to NULL.
         */
        entry->syntax = NULL;
    }
}

SHELL_DYNAMIC_CMD_CREATE(m_sub_dynamic_set, dynamic_cmd_get);
SHELL_STATIC_SUBCMD_SET_CREATE(m_sub_dynamic,
    SHELL_CMD(add, NULL,"Add new command to dynamic_cmd_buffer and"
          " sort them alphabetically.",
          cmd_dynamic_add),
    SHELL_CMD(execute, &m_sub_dynamic_set,
          "Execute a command.", cmd_dynamic_execute),
    SHELL_CMD(remove, &m_sub_dynamic_set,
          "Remove a command from dynamic_cmd_buffer.",
          cmd_dynamic_remove),
    SHELL_CMD(show, NULL,
          "Show all commands in dynamic_cmd_buffer.",
          cmd_dynamic_show),
    SHELL_SUBCMD_SET_END
);
SHELL_CMD_REGISTER(dynamic, &m_sub_dynamic,
       "Demonstrate dynamic command usage.", cmd_dynamic);
```
Example implementation can be found under following location:
`samples/subsys/shell/shell_module/src/dynamic_cmd.c`.


### Commands execution


Each command or subcommand may have a handler. The shell executes the handler
that is found deepest in the command tree and further subcommands (without a
handler) are passed as arguments. Characters within parentheses are treated
as one argument. If shell won't find a handler it will display an error message.

Commands can be also executed from a user application using any active backend
and a function `shell_execute_cmd`, as shown in this example:

```c

int main(void)
{
    /* Below code will execute "clear" command on a DUMMY backend */
    shell_execute_cmd(NULL, "clear");

    /* Below code will execute "shell colors off" command on
     * an UART backend
     */
    shell_execute_cmd(shell_backend_uart_get_ptr(),
              "shell colors off");
}
```
Enable the DUMMY backend by setting the Kconfig
`CONFIG_SHELL_BACKEND_DUMMY` option.


#### Commands execution example


Let's assume a command structure as in the following figure, where:

* `root_cmd` - root command without a handler
* `cmd_xxx_h` - command has a handler
* `cmd_xxx` - command does not have a handler


##### Example 1

Sequence: `root_cmd` `cmd_1_h` `cmd_12_h`
`cmd_121_h` `parameter` will execute command
`cmd_121_h` and `parameter` will be passed as an argument.


##### Example 2

Sequence: `root_cmd` `cmd_2` `cmd_22_h`
`parameter1` `parameter2` will execute command
`cmd_22_h` and `parameter1` `parameter2`
will be passed as an arguments.


##### Example 3

Sequence: `root_cmd` `cmd_1_h` `parameter1`
`cmd_121_h` `parameter2` will execute command
`cmd_1_h` and `parameter1`, `cmd_121_h` and
`parameter2` will be passed as an arguments.


##### Example 4

Sequence: `root_cmd` `parameter` `cmd_121_h`
`parameter2` will not execute any command.



#### Command handler


Simple command handler implementation:

```c

static int cmd_handler(const struct shell *sh, size_t argc,
            char **argv)
{
    ARG_UNUSED(argc);
    ARG_UNUSED(argv);

    shell_fprintf(sh, SHELL_INFO, "Print info message\n");

    shell_print(sh, "Print simple text.");

    shell_warn(sh, "Print warning text.");

    shell_error(sh, "Print error text.");

    return 0;
}
```
Function `shell_fprintf` or the shell print macros:
`shell_print`, `shell_info`, `shell_warn` and
`shell_error` can be used from the command handler or from threads,
but not from an interrupt context. Instead, interrupt handlers should use
logging_api for printing.


#### Command help


Every user-defined command or subcommand can have its own help description.
The help for commands and subcommands can be created with respective macros:
`SHELL_CMD_REGISTER`, `SHELL_CMD_ARG_REGISTER`,
`SHELL_CMD`, and `SHELL_CMD_ARG`.

Shell prints this help message when you call a command
or subcommand with `-h` or `--help` parameter.


#### Parent commands


In the subcommand handler, you can access both the parameters passed to
commands or the parent commands, depending on how you index `argv`.

* When indexing `argv` with positive numbers, you can access the parameters.
* When indexing `argv` with negative numbers, you can access the parent
  commands.
* The subcommand to which the handler belongs has the `argv` index of 0.

```c

static int cmd_handler(const struct shell *sh, size_t argc,
               char **argv)
{
    ARG_UNUSED(argc);

    /* If it is a subcommand handler parent command syntax
     * can be found using argv[-1].
     */
    shell_print(sh, "This command has a parent command: %s",
              argv[-1]);

    /* Print this command syntax */
    shell_print(sh, "This command syntax is: %s", argv[0]);

    /* Print first argument */
    shell_print(sh, "%s", argv[1]);

    return 0;
}
```

### Built-in commands


These commands are activated by `CONFIG_SHELL_CMDS` set to `y`.

* `aliases` - Shows currently configured aliases. This command needs
  extra activation: `CONFIG_SHELL_CMDS_ALIASES` set to `y`.
* `clear` - Clears the screen.
* `history` - Shows the recently entered commands.
* `resize` - Must be executed when terminal width is different than 80
  characters or after each change of terminal width. It ensures proper
  multiline text display and `←`, `→`, `End`, `Home` keys
  handling. Currently this command works only with UART flow control switched
  on. It can be also called with a subcommand:

    * `default` - Shell will send terminal width = 80 to the
      terminal and assume successful delivery.

  These command needs extra activation:
  `CONFIG_SHELL_CMDS_RESIZE` set to `y`.
* `select` - It can be used to set new root command. Exit to main
  command tree is with alt+r. This command needs extra activation:
  `CONFIG_SHELL_CMDS_SELECT` set to `y`.
* `shell` - Root command with useful shell-related subcommands like:

    * `echo` - Toggles shell echo.
        * `colors` - Toggles colored syntax. This might be helpful in
          case of Bluetooth shell to limit the amount of transferred bytes.
    * `stats` - Shows shell statistics.

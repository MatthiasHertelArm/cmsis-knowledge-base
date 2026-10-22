---
id: "pyocd-user-scripts-user-defined-commands"
type: "concept"
domain: "debug"
title: "User scripts: User-defined commands"
summary: "New commands accessible from the commander subcommand or gdbserver monitor commands can be easily created in a user script."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/user_scripts.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/user_scripts.md#user-defined-commands"
license: "Apache-2.0"
mode: "V"
---

New commands accessible from the commander subcommand or gdbserver monitor commands can be easily created in a user
script.

User defined commands are created by using the `@command()` decorator on a function. The name of the new command can
either be the same as the name of the decorated function, or can be set explicitly with a `name` (or first positional)
argument to the decorator. For instance, either `@command('mycmd')` or `@command(name='anothercmd')`. Note that the
decorator requires parentheses (it must be called as a function) even if there are no parameters.

Parameters for the new command are automatically determined using introspection and type annotations. Arguments for
parameters of these types are converted to the appropriate type before the function is called as a command.

Supported parameter types:
- `int`
- `float`
- `str`
- Variable arguments, e.g. `*args`.

Keyword parameters are not allowed.

An `int` parameter is converted using the same method as for other pyOCD commands. Hexadecimal and binary numbers are
allowed, digits can be separated by underscores, and so on. For variable arguments, type annotations are ignored and the
tuple passed to the function will contain strings as entered in the command invocation.

The decorated function remains accessible as a regular function in the user script namespace, and is therefore callable
from other functions within the user script. This is true even if the function definition is not compatible with the
command decorator, for instance if it has invalid parameter types.

Help for the new command can be specified by passing a `help` argument to the `@command` decorator.

Example:

```py
@command(help="Decode and print the first few vectors")
def vectable(base: int):
    vecs = target.read_memory_block32(base, 4)
    print(f"Initial SP:     {vecs[0]:#010x}")
    print(f"ResetHandler:   {vecs[1]:#010x}")
    print(f"NMI:            {vecs[2]:#010x}")
    print(f"HardFault:      {vecs[3]:#010x}")
```

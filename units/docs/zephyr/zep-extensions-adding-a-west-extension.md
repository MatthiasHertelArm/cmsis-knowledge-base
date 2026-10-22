---
id: "zep-extensions-adding-a-west-extension"
type: "concept"
domain: "project"
title: "Extensions: Adding a West Extension"
summary: "There are three steps to adding your own extension:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/extensions.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/extensions.rst"
license: "Apache-2.0"
mode: "V"
---

There are three steps to adding your own extension:

#. Write the code implementing the command.
#. Add information about it to a `west-commands.yml` file.
#. Make sure the `west-commands.yml` file is referenced in the
   `west manifest`.

Note that west ignores extension commands whose names are the same as a
built-in command.


### Step 1: Implement Your Command


Create a Python file to contain your command implementation (see the west
project metadata on the west PyPI page for details on the currently
supported versions of Python). You can put it in anywhere in any project
tracked by your `west manifest`, or the manifest repository itself.
This file must contain a subclass of the `west.commands.WestCommand` class.
This class will be instantiated and used when your extension is run.

Here is a basic skeleton you can use to get started. It contains a subclass of
`WestCommand`, with implementations for all the abstract methods. For more
details on the west APIs you can use, see west-apis.

```py

'''my_west_extension.py

Basic example of a west extension.'''

from textwrap import dedent            # just for nicer code indentation

from west.commands import WestCommand  # your extension must subclass this

class MyCommand(WestCommand):

    def __init__(self):
        super().__init__(
            'my-command-name',  # gets stored as self.name
            '', # ignored self.help, will not be required by future west versions
            # self.description:
            description=dedent('''
            A multi-line description of my-command.

            You can split this up into multiple paragraphs and they'll get
            reflowed for you. You can also pass
            formatter_class=argparse.RawDescriptionHelpFormatter when calling
            parser_adder.add_parser() below if you want to keep your line
            endings.'''))

    def do_add_parser(self, parser_adder):
        # This is a bit of boilerplate, which allows you full control over the
        # type of argparse handling you want. The "parser_adder" argument is
        # the return value of an argparse.ArgumentParser.add_subparsers() call.
        parser = parser_adder.add_parser(self.name,
                                         description=self.description)

        # Add some example options using the standard argparse module API.
        parser.add_argument('-o', '--optional', help='an optional argument')
        parser.add_argument('required', help='a required argument')

        return parser           # gets stored as self.parser

    def do_run(self, args, unknown):
        # This gets called when the user runs the command, e.g.:
        #
        #   $ west my-command-name -o FOO BAR
        #   --optional is FOO
        #   required is BAR
        self.inf('--optional is', args.optional)
        self.inf('required is', args.required)
```
You can ignore the second argument to `do_run()` (`unknown` above), as
`WestCommand` will reject unknown arguments by default. If you want to be
passed a list of unknown arguments instead, add `accepts_unknown_args=True`
to the `super().__init__()` arguments.


### Step 2: Add or Update Your `west-commands.yml`


You now need to add a `west-commands.yml` file to your project which
describes your extension to west.

Here is an example for the above class definition, assuming it's in
`my_west_extension.py` at the project root directory:

```yaml

west-commands:
  - file: my_west_extension.py
    commands:
      - name: my-command-name
        class: MyCommand
        help: one-line help for what my-command-name does
```
The top level of this YAML file is a map with a `west-commands` key.  The
key's value is a sequence of "command descriptors".  Each command descriptor
gives the location of a file implementing west extensions, along with the names
of those extensions, and optionally the names of the classes which define them
(if not given, the `class` value defaults to the same thing as `name`).

Some information in this file is redundant with definitions in the Python code.
This is because west won't import `my_west_extension.py` until the user
runs `west my-command-name`, since:

- It allows users to run `west update` with a manifest from an untrusted
  source, then use other west commands without your code being imported along
  the way. Since importing a Python module is shell-equivalent, this provides
  some peace of mind.

- It's a small optimization, since your code will only be imported if it is
  needed.

So, unless your command is explicitly run, west will just load the
`west-commands.yml` file to get the basic information it needs to display
information about your extension to the user in `west --help` output, etc.

If you have multiple extensions, or want to split your extensions across
multiple files, your `west-commands.yml` will look something like this:

```yaml

west-commands:
  - file: my_west_extension.py
    commands:
      - name: my-command-name
        class: MyCommand
        help: one-line help for what my-command-name does
  - file: another_file.py
    commands:
      - name: command2
        help: another cool west extension
      - name: a-third-command
        class: ThirdCommand
        help: a third command in the same file as command2
```
Above:

- `my_west_extension.py` defines extension `my-command-name`
  with class `MyCommand`
- `another_file.py` defines two extensions:

  #. `command2` with class `command2`
  #. `a-third-command` with class `ThirdCommand`

See the file `west-commands-schema.yml` in the west repository for a
schema describing the contents of a `west-commands.yml`.


### Step 3: Update Your Manifest


Finally, you need to specify the location of the `west-commands.yml` you
just edited in your west manifest. If your extension is in a project, add it
like this:

```yaml

manifest:
   # [... other contents ...]

   projects:
     - name: your-project
       west-commands: path/to/west-commands.yml
     # [... other projects ...]
```
Where `path/to/west-commands.yml` is relative to the root of the project.
Note that the name `west-commands.yml`, while encouraged, is just a
convention; you can name the file something else if you need to.

Alternatively, if your extension is in the manifest repository, just do the
same thing in the manifest's `self` section, like this:

```yaml

manifest:
  # [... other contents ...]

  self:
    west-commands: path/to/west-commands.yml
```
That's it; you can now run `west my-command-name`. Your command's name, help,
and the project which contains its code will now also show up in the ``west
--help`` output.  If you share the updated repositories with others, they'll be
able to use it, too.

---
id: "intr-zephyr-west-tips-and-tricks-west-extensions"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: West extensions"
summary: "West extensions let projects (or your own local tooling) add custom subcommands to west."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#west-extensions"
license: "CC-BY-SA-4.0"
mode: "V"
---

West extensions let projects (or your own local tooling) add custom subcommands
to west. This is useful when you want project-specific tooling to feel like a
first-class citizen in your workflow rather than a separate script (it's
especially nice for discoverability, since everything is available from
`west --help`).

It's useful when the commands you need don't fit into the normal
build/flash/debug/attach workflow provided by the Zephyr SDK's own extension
commands, and aliases are insufficient.

A quick example: we add the following files/snippets to our manifest repo:

**`west.yml`:**

```yaml
manifest:
  self:
    # register this repo's west extensions
    west-commands: scripts/west-commands.yml
```

**`scripts/west-commands.yml`:**

```yaml
west-commands:
  - file: scripts/west_extensions.py
    commands:
      - name: project-hello
        class: ProjectHello
        help: sample Project west extension command
```

**`scripts/west_extensions.py`:**

```python
from textwrap import dedent

from west.commands import WestCommand


class ProjectHello(WestCommand):
    def __init__(self):
        super().__init__(
            "project-hello",  # gets stored as self.name
            "",  # ignored self.help, will not be required by future west versions
            description=dedent(
                """
            Sample Project west extension command.
            """
            ),
        )

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(self.name, description=self.description)

        levels = ["dbg", "inf", "wrn", "err"]
        parser.add_argument(
            "-l",
            "--level",
            default="inf",
            choices=levels,
            help="log level for the message (default: %(default)s)",
        )
        parser.add_argument("message", help="message to print")

        return parser  # gets stored as self.parser

    def do_run(self, args, unknown):
        log_fn = {
            "dbg": self.dbg,
            "inf": self.inf,
            "wrn": self.wrn,
            "err": self.err,
        }[args.level]

        self.inf(f"[{self.name}] log level: {args.level}")
        log_fn(f"[{self.name}] message: {args.message}")
```

Now the new extension shows up in `west --help`:

```plaintext
extension commands from project manifest (path: blahblah):
  project-hello:        sample Project west extension command
```

And we can run it:

```bash
❯ west project-hello --level err 'Hello!'
[project-hello] log level: err
ERROR: [project-hello] message: Hello!
```

The Zephyr reference goes through the details of how to do this:
<https://docs.zephyrproject.org/latest/develop/west/extensions.html#west-extensions>

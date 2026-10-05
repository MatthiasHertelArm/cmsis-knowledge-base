---
id: "intr-firmware-testing-with-renode-and-g-using-renode-in-headless-mode"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: Using Renode in Headless Mode"
summary: "To improve my workflow with Renode, I needed to do something about the Mono-emulated terminal windows that were spawned with Renode."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#using-renode-in-headless-mode"
license: "CC-BY-SA-4.0"
mode: "V"
---

To improve my workflow with Renode, I needed to do something about the
Mono-emulated terminal windows that were spawned with Renode. Although not
entirely documented, it's quite easy to never have to use these terminal windows
directly and you can instead attach to Renode using Telnet. This enables you to
have use iTerm2, your native clipboard, tmux, etc.

To do so, we need to make a few modifications to the way we launch Renode. We'll
pass in the argument `--disable-xwt` to disable the GUI entirely, and
`--port <port>` to make the Renode Monitor available through Telnet on that
port.

I've included another script, `start-headless.sh` in the example project which
can be used to more easily launch Renode in headless mode.

```bash
#!/bin/sh
sh /Applications/Renode.app/Contents/MacOS/macos_run.command \
    --disable-xwt renode-config.resc --port 33334
```

After launching this, a user should be able to use `telnet` to connect to that
open port.

```
$ telnet 127.0.0.1 33334
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Renode, version 1.9.0.28176 (169a3c85-202003101417)

(monitor) i $CWD/renode-config.resc
(STM32F4_Discovery)
```

That solves the problem of the Monitor window, but we also want to connect to
the UART without a GUI too. The answer on how to do this was found in a
[GitHub Issue on the PlatformIO repo](https://github.com/platformio/platformio-core/issues/3401#issuecomment-597768021).

We needed to add the following lines to `renode-config.resc`, which is the
Renode script that is run every time we launch it.

```
# Publish a Telnet connection to the UART
emulation CreateServerSocketTerminal 33335 "externalUART"

# Connect that connection to our UART
connector Connect sysbus.uart2 externalUART
```

Now all we need to do is `telnet` again to that port, and we'll have our shell.

```
$ telnet 127.0.0.1 33335
shell>
shell> help
...
```

Taking inspiration from my previous post, [Building a CLI for Firmware
Projects](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects), I
wrote a quick and hacky `tasks.py` Invoke file to improve this flow.

```python
import time
from datetime import datetime, timedelta
from telnetlib import Telnet

from invoke import Collection, Context, task


@task()
def renode(ctx):
    """Spawn Renode and attach to its monitor"""
    ctx.run("./start-headless.sh", asynchronous=True)

    print("Letting Renode boot...")
    time.sleep(3)

    retry_until = datetime.now() + timedelta(seconds=3)
    while datetime.now() < retry_until:
        try:
            ctx.run('telnet 127.0.0.1 33334', pty=True)
        except Exception as e:
            time.sleep(0.5)

@task()
def console(ctx):
    """Connect to Renode's UART"""
    ctx.run('telnet 127.0.0.1 33335', pty=True)

@task()
def gdb(ctx):
    """Connect to Renode's GDB connection"""
    ctx.run("arm-none-eabi-gdb-py "
            "--eval-command=\"target remote :3333\" "
            "--se build/renode-example.elf",
            pty=True)

@task()
def test(ctx):
    """Run tests locally"""
    ctx.run("./run_tests.sh", pty=True)
```

Now, all I need to do is install Invoke into my Conda environment, and I'll be
able to more easily do everything I want!

```
$ pip install invoke
```

I can start Renode and get access to its monitor:

```
$ invoke renode
[...]
Renode, version 1.9.0.28176 (169a3c85-202003101417)

(monitor) i $CWD/renode-config.resc
Starting emulation...
(STM32F4_Discovery)
```

I can get it's shell:

```
$ inv console
[...]
shell>
```

And I can launch GDB and connect to the instance:

```
$ inv gdb
GNU gdb (GNU Tools for Arm Embedded Processors 8-2019-q3-update) 8.3.0.20190703-git

Reading symbols from build/renode-example.elf...
Remote debugging using :3333
0x08003fd4 in usart_wait_recv_ready (usart=usart@entry=1073759232) at ../common/usart_common_f124.c:96
96    while ((USART_SR(usart) & USART_SR_RXNE) == 0);
```

Much, much better. For those who know me or have read my previous posts, you
know this makes me very happy.

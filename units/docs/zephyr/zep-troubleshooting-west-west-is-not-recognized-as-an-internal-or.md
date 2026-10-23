---
id: "zep-troubleshooting-west-west-is-not-recognized-as-an-internal-or"
type: "concept"
domain: "project"
title: "Troubleshooting West: \"'west' is not recognized as an internal or external command, operable program or batch file.'"
summary: "On Windows, this means that either west is not installed, or your PATH environment variable does not contain the directory where pip installed west.exe."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/troubleshooting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/troubleshooting.rst"
license: "Apache-2.0"
mode: "V"
---

On Windows, this means that either west is not installed, or your `PATH`
environment variable does not contain the directory where pip installed
`west.exe`.

First, make sure you've installed west; see west-install. Then try
running `west` from a new `cmd.exe` window. If that still doesn't work,
keep reading.

You need to find the directory containing `west.exe`, then add it to your
`PATH`. (This `PATH` change should have been done for you when
you installed Python and pip, so ordinarily you should not need to follow these
steps.)

Run this command in `cmd.exe`::
```
pip3 show west
```
Then:

#. Look for a line in the output that looks like ``Location:
   C:\foo\python\python38\lib\site-packages``. The exact location
   will be different on your computer.
#. Look for a file named `west.exe` in the `scripts` directory
   `C:\foo\python\python38\scripts`.


**Important:** Notice how `lib\site-packages` in the `pip3 show` output was changed to `scripts`!

#. If you see `west.exe` in the `scripts` directory, add the full path to
   `scripts` to your `PATH` using a command like this::
```
setx PATH "%PATH%;C:\foo\python\python38\scripts"
```
   **Do not just copy/paste this command**. The `scripts` directory location
   will be different on your system.
#. Close your `cmd.exe` window and open a new one. You should be able to run
   `west`.

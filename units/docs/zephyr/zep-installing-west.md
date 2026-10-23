---
id: "zep-installing-west"
type: "concept"
domain: "project"
title: "Installing west"
summary: "West is written in Python 3 and distributed through PyPI. Use pip3 to install or upgrade west:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/install.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/install.rst"
license: "Apache-2.0"
mode: "V"
---

West is written in Python 3 and distributed through PyPI.
Use `pip3` to install or upgrade west:

On Linux::
```
pip3 install --user -U west
```
On Windows and macOS::
```
pip3 install -U west
```

**Note:** See python-pip for additional clarification on using the `--user` switch.

Afterwards, you can run `pip3 show -f west` for information on where the west
binary and related files were installed.

Once west is installed, you can use it to :ref:`clone the Zephyr repositories
<clone-zephyr>`.

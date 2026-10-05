---
id: "intr-tracking-firmware-code-size-building-the-firmware"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size / Building the Firmware"
summary: "After getting the Zephyr project building with the hello world example, this is the following command to build the example firmware."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#building-the-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How to Track Code Size_

After getting the Zephyr project building with the hello world example, this is
the following command to build the example firmware.

```
$ cd zephyrproject/zephyr
$ west build -b cc3220sf_launchxl samples/net/lwm2m_client --pristine
...
Memory region         Used Size  Region Size  %age Used
           FLASH:      149936 B         1 MB     14.30%
            SRAM:       44544 B       256 KB     16.99%
        IDT_LIST:          56 B         2 KB      2.73%
[...]
[188/188] Linking C executable zephyr/zephyr.elf
```

Zephyr already has some code size statistics at the end of their build, which is
great! However, there is room for improvement.

To help generate data for me to work with, I spun up an AWS Spot EC2 instance
and built the most recent 2,500 commits of Zephyr from the master branch as of
March 14th. I would have built more but there was an issue with the CMake build
system and dependencies unfortunately.

The process for this was quite simple. Using `git rev-list --first-parent`, we
can get all the revisions that were committed into the master branch
chronological order.

```
$ git rev-list --first-parent master
22b9167acb52386c13be6d22223fd3d585d57a3d
7cb8f5c61e6081475223586349b88c5a34eb7f38
[...]
```

Once we have all the commits, we can run a Python script that builds every
commit.

```python
for commit in commits:
    try:
        os.system("git checkout {}".format(commit))
        os.system("west update")
        os.system("west build -b cc3220sf_launchxl samples/net/lwm2m_client --pristine")
        # Here, we calculate and update the code size.
    except:
        continue
```

> To whomever it concerns: I _love_ the `--pristine` option in the `west` tool.

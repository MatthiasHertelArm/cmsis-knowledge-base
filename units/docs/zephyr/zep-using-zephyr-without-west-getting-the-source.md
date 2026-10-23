---
id: "zep-using-zephyr-without-west-getting-the-source"
type: "concept"
domain: "project"
title: "Using Zephyr without west: Getting the Source"
summary: "In addition to downloading the zephyr source code repository itself, you will need to manually clone the additional projects listed in the west manifest file inside that repository."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/without-west.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/without-west.rst"
license: "Apache-2.0"
mode: "V"
---

In addition to downloading the zephyr source code repository itself,
you will need to manually clone the additional projects listed in the
`west manifest` file inside that repository.

```console

mkdir zephyrproject
cd zephyrproject
git clone https://github.com/zephyrproject-rtos/zephyr
# clone additional repositories listed in zephyr/west.yml,
# and check out the specified revisions as well.
```
As you pull changes in the zephyr repository, you will also need to
maintain those additional repositories, adding new ones as necessary
and keeping existing ones up to date at the latest revisions.

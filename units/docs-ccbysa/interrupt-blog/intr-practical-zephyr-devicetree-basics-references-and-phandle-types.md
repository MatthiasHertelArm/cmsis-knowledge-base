---
id: "intr-practical-zephyr-devicetree-basics-references-and-phandle-types"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): References and `phandle` types"
summary: "We've already seen how we can create node labels as shorthand forms of a node's full path, but haven't really seen how such labels are used within the Devicetree. Tired of all the theory? I thought so."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#references-and-phandle-types"
license: "CC-BY-SA-4.0"
mode: "V"
---

We've already seen how we can create _node labels_ as shorthand forms of a node's full path, but haven't really seen how such labels are used within the Devicetree. Tired of all the theory? I thought so. Now that we're familiar with a good part of the Devicetree source file syntax, it's time for _a little_ hands-on, so let's dive back into the command line.

We'll practice using a Devicetree _overlay_ file. In the next article, we'll go more into detail about what an overlay is. For now, it is enough to know that an overlay file is simply an additional DTS file on top of the hierarchy of files that is included starting with the board's Devicetree source file. We can [specify an extra Devicetree overlay file using the CMake variable `EXTRA_DTC_OVERLAY_FILE`](https://docs.zephyrproject.org/latest/build/dts/howtos.html#set-devicetree-overlays), and we'll use a newly created `props-phandles.overlay` file for that:

```bash
$ mkdir -p dts/playground
$ touch dts/playground/props-phandles.overlay
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build -- \
  -DEXTRA_DTC_OVERLAY_FILE=dts/playground/props-phandles.overlay
```

The build system's output now announces that it encountered the newly created overlay file with the message `Found devicetree overlay`:

```
-- Found Dtc: /opt/nordic/ncs/toolchains/322ac893fe/bin/dtc (found suitable version "1.6.1", minimum required is "1.4.6")
-- Found BOARD.dts: /opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts
-- Found devicetree overlay: playground/test.overlay
-- Generated zephyr.dts: /path/to/build/zephyr/zephyr.dts
```

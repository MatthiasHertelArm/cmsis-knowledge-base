---
id: "intr-practical-zephyr-devicetree-semant-extending-the-example-application"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Towards bindings / Extending the example application"
summary: "We start by creating our own overlay file dts/playground/props-basics.overlay:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#extending-the-example-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Towards bindings_

We start by creating our own overlay file `dts/playground/props-basics.overlay`:

```bash
$ tree --charset=utf-8 --dirsfirst .
├── dts
│   └── playground
│       └── props-basics.overlay
├── src
│   └── main.c
├── CMakeLists.txt
└── prj.conf
```

In the development kit's Devicetree source file `nrf52840dk_nrf52840.dts`, the `&uart0` node has two properties: A property `current-speed` of type `int`, and the property `status` of type `string`. We've seen that Zephyr creates some output in `devicetree_generated.h` for the UART node, so let's try the same with a custom node:

`dts/playground/props-basics.overlay`
```dts
/ {
  node_with_props {
    int = <1>;
    string = "foo";
  };
};
```

When running a build whilst specifying the path to the overlay using the CMake variable `EXTRA_DTC_OVERLAY_FILE`, we can verify that the overlay is indeed picked up by the build system, since it informs us about the overlays it found using the output `Found devicetree overlay`:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build -- \
  -DEXTRA_DTC_OVERLAY_FILE="dts/playground/props-basics.overlay"
```
```
-- Found Dtc: /opt/nordic/ncs/toolchains/322ac893fe/bin/dtc (found suitable version "1.6.1", minimum required is "1.4.6")
-- Found BOARD.dts: /opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts
-- Found devicetree overlay: dts/playground/props-basics.overlay
-- Generated zephyr.dts: /path/to/build/zephyr/zephyr.dts
-- Generated devicetree_generated.h: /path/to/build/zephyr/include/generated/devicetree_generated.h
-- Including generated dts.cmake file: /path/to/build/zephyr/dts.cmake
```

Checking the output file `build/zephyr/zephyr.dts` we also see that our `node_with_props` can be found in the Devicetree that Zephyr is using as input for its generator script, that in turn produces `devicetree_generated.h`:

`build/zephyr/zephyr.dts`
```dts
/ {
  /* ... */
  node_with_props {
    int = < 0x1 >;
    string = "foo";
  };
};
```

Let's see if we can find anything in `devicetree_generated.h` by searching for the quite unique value `foo` of our `string` property:

```bash
$ grep foo ../build/zephyr/include/generated/devicetree_generated.h
$
```

The search yields no results! Did we miss something? One thing that we can easily verify, is that the `devicetree_generated.h` at least contains our node: We can search using the node's full path `/node_with_props`. You should find a large comment, separating the macros generated for our node, containing a list of definitions:

`build/zephyr/include/generated/devicetree_generated.h`
```c
/*
 * Devicetree node: /node_with_props
 *
 * Node identifier: DT_N_S_node_with_props
 */

/* Node's full path: */
#define DT_N_S_node_with_props_PATH "/node_with_props"
// ---snip ---
/* (No generic property macros) */
```

The omitted lines contain lots of generic macros for our node. Don't worry, we'll skim through these soon enough. However, we won't find anything that is even remotely related to the two properties that we defined for our node. In fact, the comment _"(No generic property macros)"_ seems to hint that the generator did not encounter the properties `int` and `string` in our node `/node_with_props`.

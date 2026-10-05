---
id: "intr-practical-zephyr-devicetree-semant-devicetree-overlays"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Devicetree overlays"
summary: "Overlays are used to extend or modify the board's Devicetree source file. Even though by convention overlay files use the .overlay file extension, they're just plain old Devicetree source (DTS) files."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#devicetree-overlays"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Overlays_ are used to extend or modify the board's Devicetree source file. Even though by convention overlay files use the `.overlay` file extension, they're just plain old Devicetree source (DTS) files. The build system combines the board's `.dts` file and any `.overlay` files by concatenating them, with the overlays put last. Thus, the contents of the `.overlay` file have priority over any definitions in the board's `.dts` file or its includes.

### Automatic overlays

The Zephyr build system automatically picks up additional _overlays_ based on their location and file name. The following repeats the steps [in Zephyr's official documentation](https://docs.zephyrproject.org/latest/build/dts/howtos.html#set-devicetree-overlays) used by the build system to detect _overlay_ files.

Before we have a look at the steps, there's one detail that we haven't seen yet. So far, we've specified the board as a command-line argument in the format `--board <board>`. Zephyr also supports [building for a board revision](https://docs.zephyrproject.org/latest/develop/application/index.html#application-board-version) in case you have multiple _revisions_ or versions of a specific board. In such a case, you can use the format `--board <board>@<revision>`.

> **Note:** As we've seen in previous articles, there are several ways to specify the board, but for the sake of simplicity we're only using `west` and its `--board` argument here. You can specify the board in your path using the variable `BOARD`, you can provide it directly in your `CMakeLists.txt` file, or even pass it to an explicit `cmake` call.

With this detail out of the way, here's the search performed by the CMake module `zephyr/cmake/modules/dts.cmake`:

- In case the CMake variable `DTC_OVERLAY_FILE` is set, the build system uses the specified file(s) and stops the search.
- If the file `boards/<BOARD>.overlay` exists in the application's root directory, the build system selects the provided file as overlay and proceeds with the following step.
- If a specific revision has been specified for the `BOARD` in the format `<board>@<revision>` and `boards/<BOARD>_<revision>.overlay` exists in the application's root directory, this file is used in _addition_ to `boards/<BOARD>.overlay`, if both exist.
- If _overlays_ have been encountered in any of the previous steps, the search stops.
- If no files have been found and `<BOARD>.overlay` exists in the application's root directory, the build system uses the overlay and stops the search.
- Finally, if none of the above overlay files exist but `app.overlay` exists in the application's root directory, the build system uses the overlay.

On top of the _overlay_ files that have or haven't been discovered by the build process, the CMake variable `EXTRA_DTC_OVERLAY_FILE` allows to specify additional _overlay_ files that are added regardless of the outcome of the overlay search.

The important thing to remember is, that the Devicetree overlay files that were detected _last_ have the _highest_ precedence, since they may overwrite anything in the previously added overlay files. The precedence is always visible in the build output, where Zephr lists all overlay files using the output `Found devicetree overlay: <name>.overlay` in the order that they are detected and thus added. The precedence _increases_ with the given list.

### Overlays by example

Let's try and visualize this list using an imaginary file tree and board "dummy_board". I've annotated the files with precedence numbers, even though - as we've learned before - not all files will be used by the build:

```bash
$ tree --charset=utf-8 --dirsfirst.
.
├── boards
│   ├── dummy_board_123.overlay -- #3
│   └── dummy_board.overlay     -- #4
├── dts
│   └── extra
│       ├── extra_0.overlay -- #2
│       └── extra_1.overlay -- #1
├── src
│   └── main.c
├── CMakeLists.txt
├── app.overlay         -- #6
├── dummy_board.overlay -- #5
└── prj.conf
```

Let's assume we would use the following command that doesn't include the CMake variable `DTC_OVERLAY_FILE`:

```bash
$ west build --no-sysbuild --board dummy_board@123 -- \
  -DEXTRA_DTC_OVERLAY_FILE="dts/extra/extra_0.overlay;dts/extra/extra_1.overlay"
```

The overlay files would be detected and added as follows, depending on whether or not they exist. As mentioned, the precedence _increases_ and thus the files listed _last_ have the _highest_ precedence:

- `boards/dummy_board.overlay`
- `boards/dummy_board_123.overlay`
- if none of the previous files exist, `dummy_board.overlay`
- if none of the previous files exist, `app.overlay`
- `dts/extra/extra_0.overlay`
- `dts/extra/extra_1.overlay`

> **Note:** It is recommended to use the `boards` directory for board overlay files. You should no longer place your board's overlay files in the application's root directory.

If, instead, we specify the CMake variable `DTC_OVERLAY_FILE` as `app.overlay` in our command as follows, the automatic detection is skipped and the build process only picks the selected DTC overlay files:

```bash
$ west build --no-sysbuild --board dummy_board@123 -- \
  -DTC_OVERLAY_FILE="app.overlay" \
  -DEXTRA_DTC_OVERLAY_FILE="dts/extra/extra_0.overlay;dts/extra/extra_1.overlay"
```

The overlay files would thus be added as follows and with _increasing_ precedence:
- `app.overlay`
- `dts/extra/extra_0.overlay`
- `dts/extra/extra_1.overlay`

What does that mean in practice? If you provide the CMake variable `DTC_OVERLAY_FILE` in your build, the board overlays will no longer be picked up automatically. For quick builds that might be helpful, but in case you're building an application that should run on multiple boards, you should **not** use `DTC_OVERLAY_FILE` but maybe rather list additional overlays using `EXTRA_DTC_OVERLAY_FILE`.

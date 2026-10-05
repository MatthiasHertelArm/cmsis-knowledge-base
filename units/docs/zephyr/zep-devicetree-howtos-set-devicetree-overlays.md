---
id: "zep-devicetree-howtos-set-devicetree-overlays"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Set devicetree overlays"
summary: "Devicetree overlays are explained in devicetree-intro. The CMake variable DTC_OVERLAY_FILE contains a space- or semicolon-separated list of overlay files to use. If DTC_OVERLAY_FILE specifies multiple files, they are included in that order by the C preprocessor."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

Devicetree overlays are explained in devicetree-intro. The CMake
variable `DTC_OVERLAY_FILE` contains a space- or semicolon-separated
list of overlay files to use. If `DTC_OVERLAY_FILE` specifies multiple
files, they are included in that order by the C preprocessor.  A file in a
Zephyr module can be referred to by escaping the Zephyr module dir variable
like `\${ZEPHYR_<module>_MODULE_DIR}/<path-to>/dts.overlay`
when setting the DTC_OVERLAY_FILE variable.

You can set `DTC_OVERLAY_FILE` to contain exactly the files you want
to use. Here is an example using
`west build`.

If you don't set `DTC_OVERLAY_FILE`, the build system will follow
these steps, looking for files in your application configuration directory to
use as devicetree overlays:

#. If the file `socs/<SOC>_<BOARD_QUALIFIERS>.overlay` exists, it will be used.
#. If the file `boards/<BOARD>.overlay` exists, it will be used in addition to the above.
#. If the current board has multiple revisions
   and `boards/<BOARD>_<revision>.overlay` exists, it will be used in addition to the above.
#. If one or more files have been found in the previous steps, the build system
   stops looking and just uses those files.
#. Otherwise, if `<BOARD>.overlay` exists, it will be used, and the build
   system will stop looking for more files.
#. Otherwise, if `app.overlay` exists, it will be used.

Extra devicetree overlays may be provided using `EXTRA_DTC_OVERLAY_FILE` which
will still allow the build system to automatically use devicetree overlays
described in the above steps.

The build system appends overlays specified in `EXTRA_DTC_OVERLAY_FILE`
to the overlays in `DTC_OVERLAY_FILE` when processing devicetree overlays.
This means that changes made via `EXTRA_DTC_OVERLAY_FILE` have higher
precedence than those made via `DTC_OVERLAY_FILE`.

All configuration files will be taken from the application's configuration
directory except for files with an absolute path that are given with the
`DTC_OVERLAY_FILE` or `EXTRA_DTC_OVERLAY_FILE` argument.

See Application Configuration Directory
on how the application configuration directory is defined.

Using shields will also add devicetree overlay files.

The `DTC_OVERLAY_FILE` value is stored in the CMake cache and used
in successive builds.

The build system prints all the devicetree overlays it
finds in the configuration phase, like this:

```none

-- Found devicetree overlay: .../some/file.overlay
```

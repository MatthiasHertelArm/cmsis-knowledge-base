---
id: "pyocd-target-support-target-support-sources"
type: "concept"
domain: "debug"
title: "Target support: Target support sources"
summary: "PyOCD has built-in support for over 70 popular MCUs from various vendors."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/target_support.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/target_support.md#target-support-sources"
license: "Apache-2.0"
mode: "V"
---

### Built-in

PyOCD has built-in support for over 70 popular MCUs from various vendors.

The best way to see the available built-in targets is
by running `pyocd list --targets`. This command will print a table of supported target types.
Built-in targets will be identified as such in the "SOURCE" column.
New built-in targets are added relatively infrequently since the addition of CMSIS-Pack based targets.


### CMSIS-Packs

The [Open-CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec) specification defines the
Device Family Pack (DFP) standard for
distributing device support files. PyOCD uses DFPs as a means to add support for devices that do
not have support built in. This allows pyOCD to support nearly every Cortex-M MCU on the market. It
also means that pyOCD can immediately support newly released devices as soon as the silicon vendor
makes a DFP available.

The [CMSIS-Pack list](http://www.keil.com/dd2/pack/) web page is the official list of all available
packs. You can choose to download individual packs.

There are two methods to use a DFP within pyOCD. First, you can let pyOCD fully manage packs for
you, where all you have to do is tell it the part number(s) for which you wish to install support.
Alternatively, you can manually download packs and tell pyOCD which pack files to use.

*Note:* As with any software release, CMSIS-Packs may be buggy and have incorrect or missing
information about a device. Sometimes memory regions will be missing, attributes of a memory region
or flash algorithm might be wrong, or the flash algorithm itself might be buggy. If you encounter an
issue with a pack, you can report the issue on the [pyOCD GitHub
site](https://www.github.com/pyocd/pyOCD/issues) to let other users know about the problem. You
should also report the issue to the pack vendor so it can be fixed.


#### Managed packs

The `pyocd` tool's `pack` subcommand provides completely automated management of CMSIS-Packs. It
allows you to install new device support with a single command line invocation.

As part of the pack management, pyOCD keeps an index of all available DFPs. The pack index is a two-
level hierarchy of pack lists, with the top level pointing to individual vendor indexes. Once the
index is downloaded, pyOCD can very quickly locate the DFP that provides support for a given
MCU part number. To learn more about the index, see the [Open-CMSIS-Pack index
files](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/packIndexFile.html) documentation.

The two most useful subcommands of the `pack` subcommand are `find` and `install`. The options accept a glob-style
pattern that is matched against MCU part numbers in the index. If the index has not been downloaded yet, that will be
done first, or you can run `pyocd pack update` yourself. The `find` subcommand will print out a list of matching part
numbers and the names of the containing DFPs. `install` performs the same match, but downloads and installs the matching
DFPs. The part number patterns are matched case-insensitively and as a contains comparison.

For instance, if you know the specific part number of the device you are using, say STM32L073, you
can run this command to install support:

    $ pyocd pack install stm32l073

This will download the index if required, then download the STM32L0xx_DFP pack. The

As another example, to find which pack(s) support the NXP MK26F family, you could run:

    $ pyocd pack find k26

This will print a table similar to:

      Part             Vendor   Pack          Version
    ---------------------------------------------------
      MK26FN2M0CAC18   NXP      MK26F18_DFP   11.0.1
      MK26FN2M0VLQ18   NXP      MK26F18_DFP   11.0.1
      MK26FN2M0VMD18   NXP      MK26F18_DFP   11.0.1
      MK26FN2M0VMI18   NXP      MK26F18_DFP   11.0.1

Once a DFP is installed, the `pyocd list --targets` command will show the new targets in its output,
and you can immediately begin using the target support with the other `pyocd` subcommands.

To get a list of all installed packs, use the `pack show` subcommand.


#### Manual pack usage

If you prefer to manually manage packs, or if the managed pack system cannot access online packs
from your network, you can download them yourself from the [official CMSIS-Pack
list](http://www.keil.com/dd2/pack/). The downloaded pack files can be stored wherever you like.
Typically you would group them in a single common directory. Another good option is to place the
pack file used with a project in a project-relative location.

There are two ways to use a manually downloaded pack.

The simplest option is to pass the `--pack` option to the `pyocd` tool, specifying the path to the
.pack file. PyOCD does not cache any information about packs used this way, so this argument must be
passed for every invocation in addition to the other arguments. For instance, to run the GDB server,
you might execute `pyocd gdbserver --pack=Keil.STM32L4xx_DFP.2.2.0.pack`. Note that you can pass
multiple `--pack` arguments to pyOCD, which might be useful in a scripted execution of pyOCD.

For a more permanent solution, use a [`pyocd.yaml` configuration file]({% link _docs/configuration.md %}). In the
config file, set the `pack` session option to either a single .pack file path or a list of paths. Now
when you run the `pyocd` tool, it will automatically pick up the pack file(s) to use.

Here is an example config file that lists two packs.
```yaml
pack:
  - /Users/admin/CMSIS-Packs/Keil.STM32L0xx_DFP.2.0.0.pack
  - /Users/admin/CMSIS-Packs/NXP.MKV58F24_DFP.11.0.0.pack
```

To see the targets provided by a .pack file, run `pyocd list --targets` and pass the approprate
`--pack` option or use a config file, as described above.

_Note:_ .pack files are simply zip archives with a different extension. To examine the contents of
a pack, change the extension to .zip and extract.

_Note:_ PyOCD can work with expanded packs just like zipped .pack files. Pass the path to the root directory
of the pack using the `--pack` argument, as above. This is very useful for cases such as development or
debugging of a pack, or for working with other CMSIS-Pack managers that store packs in decompressed form.

#### CMSIS-Toolbox Run and Debug Management

Run and Debug Management is a part of the [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox) build
information files when working with CSolution projects. Each `*.cbuild-run.yml` file contains relevant run and
debug information for a single `target-type` defined in a CSolution project. The tool gathers and filters the
target information from the BSP and DFP.

To use the `cbuild-run` target information in PyOCD, pass the `--cbuild-run` option followed by the path to
desired `*.cbuild-run.yml` file. The target information is not cached in PyOCD, which means the command-line
option should always be passed when launching the debugger.

Because a single `target-type` is described in the YAML file, the `--target`
command-line argument is not needed, as the target is automatically selected.

More information on CMSIS-Toolbox and the CSolution project format for Run and Debug Management can be found in the
[CMSIS-Toolbox Documentation](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#run-and-debug-management).

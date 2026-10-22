---
id: "pyocd-installing-development-versions"
type: "concept"
domain: "debug"
title: "Installing: Development versions"
summary: "To install the latest prerelease version from the HEAD of the develop branch, you can do the following:"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/installing.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/installing.md#development-versions"
license: "Apache-2.0"
mode: "V"
---

To install the latest prerelease version from the HEAD of the `develop` branch, you can do
the following:

```
$ python3 -m pip install --pre -U git+https://github.com/pyocd/pyOCD.git@develop
```

You can also install directly from the source by cloning the [git repository](https://github.com/pyocd/pyOCD) and
running this command from the working copy root directory:

```
$ python3 -m pip install .
```

See the [developer's guide]({% link _docs/developers_guide.md %}) for more about setting up a development
environment for pyOCD.

(Note: Installing by running `setup.py` directly is deprecated since pyOCD migrated to PEP 517 based packaging.
In many cases it will not work at all. Installing with pip or another standards-compliant tool is the only
supported method.)


udev rules on Linux
-------------------

On Linux, particularly Ubuntu 16.04+, you must configure udev rules to allow pyOCD to access debug
probes from user space. Otherwise you will need to run pyOCD as root, using sudo, which is very
highly discouraged. (You should _never_ run pyOCD as root on any OS.)

To help with this, example udev rules files are included with pyOCD in the
[udev](https://github.com/pyocd/pyOCD/tree/main/udev) folder. The
[readme](https://github.com/pyocd/pyOCD/tree/main/udev/README.md) in this folder has detailed
instructions.


Target support
--------------

See the [target support documentation]({% link _docs/target_support.md %}) for information on how to check if
the MCU(s) you are using have built-in support, and how to install support for additional MCUs via
CMSIS-Packs.

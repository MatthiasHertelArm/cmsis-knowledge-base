---
id: "zep-install-linux-host-dependencies-install-requirements-and-dependencies"
type: "concept"
domain: "project"
title: "Install Linux Host Dependencies: Install Requirements and Dependencies"
summary: ".. NOTE FOR DOCS AUTHORS: DO NOT PUT DOCUMENTATION BUILD DEPENDENCIES HERE."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/getting_started/installation_linux.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/getting_started/installation_linux.rst"
license: "Apache-2.0"
mode: "V"
---

.. NOTE FOR DOCS AUTHORS: DO NOT PUT DOCUMENTATION BUILD DEPENDENCIES HERE.

   This section is for dependencies to build Zephyr binaries, *NOT* this
   documentation. If you need to add a dependency only required for building
   the docs, add it to doc/README.rst. (This change was made following the
   introduction of LaTeX->PDF support for the docs, as the texlive footprint is
   massive and not needed by users not building PDF documentation.)

Note that both Ninja and Make are installed with these instructions; you only
need one.


### CMake


A recent CMake version is required. Check what
version you have by using `cmake --version`. If you have an older version,
there are several ways of obtaining a more recent one:

* On Ubuntu, you can follow the instructions for adding the
  [kitware third-party apt repository](https://apt.kitware.com/)
  to get an updated version of cmake using apt.

* Download and install a packaged cmake from the CMake project site.
  (Note this won't uninstall the previous version of cmake.)

```console

cd ~
wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-Linux-x86_64.sh
chmod +x cmake-3.21.1-Linux-x86_64.sh
sudo ./cmake-3.21.1-Linux-x86_64.sh --skip-license --prefix=/usr/local
hash -r
```
  The `hash -r` command may be necessary if the installation script
  put cmake into a new location on your PATH.

* Download and install from the pre-built binaries provided by the CMake
  project itself in the CMake Downloads page.
  For example, to install version 3.21.1 in `~/bin/cmake`:

```console

mkdir $HOME/bin/cmake && cd $HOME/bin/cmake
wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-Linux-x86_64.sh
yes | sh cmake-3.21.1-Linux-x86_64.sh | cat
echo "export PATH=$PWD/cmake-3.21.1-Linux-x86_64/bin:\$PATH" >> $HOME/.zephyrrc
```
* Use `pip3`:

```console

pip3 install --user cmake
```
  Note this won't uninstall the previous version of cmake and will
  install the new cmake into your ~/.local/bin folder so
  you'll need to add ~/.local/bin to your PATH.  (See python-pip
  for details.)

* Check your distribution's beta or unstable release package library for an
  update.

* On Ubuntu you can also use snap to get the latest version available:

```console

sudo snap install cmake
```
After updating cmake, verify that the newly installed cmake is found
using `cmake --version`.
You might also want to uninstall the CMake provided by your package manager to
avoid conflicts.  (Use `whereis cmake` to find other installed
versions.)


### DTC (Device Tree Compiler)


A recent DTC version is required. Check what
version you have by using `dtc --version`. If you have an older version,
either install a more recent one by building from source, or use the one that is
bundled in the Zephyr SDK by installing it.


### Python


A modern Python 3 version is required. Check
what version you have by using `python3 --version`.

If you have an older version, you will need to install a more recent Python 3.
You can build from source, or use a backport from your distribution's package
manager channels if one is available. Isolating this Python in a virtual
environment is recommended to avoid interfering with your system Python.

---
id: "ethu-vela-installation"
type: "concept"
domain: "edge-ai"
title: "Vela: Installation"
summary: "The Vela compiler runs on Linux, macOS, and Windows. The released package requires Python 3.10 or newer:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/vela/src/main.md#installation"
license: "Apache-2.0"
mode: "V"
---

The Vela compiler runs on Linux, macOS, and Windows. The released package
requires Python 3.10 or newer:

```console
python -m pip install ethos-u-vela
vela --version
```

### Update an existing installation

Plain `pip install` considers an already installed version satisfactory and
does not necessarily install a newer release. Request an upgrade explicitly:

```console
python -m pip install --upgrade ethos-u-vela
python -m pip show ethos-u-vela
vela --version
```

#### Troubleshooting installation

If PyPI reports a newer package but `vela --version` still shows the old
version, the `pip` command and the `vela` executable usually belong to different
Python environments. Locate both and compare them:

```console
python -c "import sys; print(sys.executable)"
python -m pip --version
python -m pip show ethos-u-vela
```

On Windows use `where vela`; on Linux or macOS use `command -v vela`. Activate
the intended virtual environment, remove the stale executable from `PATH`, or
upgrade through the Python interpreter associated with that executable. A clean
reinstallation in the selected environment is the final fallback:

```console
python -m pip install --upgrade --force-reinstall ethos-u-vela
vela --version
```

Use `py -m pip ...` instead of `python -m pip ...` on Windows when the Python
launcher is how the intended interpreter is selected. Avoid `pip` without
`python -m`: it is easier for that command to address a different environment.

PyPI supplies wheels for supported host combinations. If no matching wheel is
available, `pip` builds from source and requires Python development headers,
CMake, a C99 compiler, and a C++17 compiler. The package depends on FlatBuffers
and NumPy 1.23 or newer.

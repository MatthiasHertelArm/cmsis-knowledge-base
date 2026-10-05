---
id: "pyocd-installing"
type: "concept"
domain: "debug"
title: "Installing"
summary: "PyOCD requires Python 3.9 or later. It runs on macOS, Linux, FreeBSD, and Windows platforms."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/installing.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/installing.md"
license: "Apache-2.0"
mode: "V"
---

PyOCD requires [Python](https://python.org/) 3.9 or later. It runs on macOS,
Linux, FreeBSD, and Windows platforms.

The latest pyOCD package is available [on PyPI](https://pypi.python.org/pypi/pyOCD/). The
[GitHub releases](https://github.com/pyocd/pyOCD/releases) page details changes between versions.

The latest stable version of pyOCD may be installed or upgraded via [pip](https://pip.pypa.io/en/stable/index.html)
as follows:

```
$ python3 -m pip install -U pyocd
```

_Note: depending on your system, you may need to use `python` instead of `python3`._

We also recommend using [pipx](https://pypa.github.io/pipx/) as an excellent method to install pyOCD in an isolated
virtual Python environment.

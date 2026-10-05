---
id: "mlek-troubleshooting-problem-installing-vela"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: Problem installing Vela"
summary: "During Vela installation, part of the package is compiled and requires libpython3. If the system lacks this dependency the following error will occur:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/troubleshooting.md#problem-installing-vela"
license: "Apache-2.0"
mode: "V"
---

During Vela installation, part of the package is compiled and requires libpython3.
If the system lacks this dependency the following error will occur:

```log
 x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g
  -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong
  -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DNPY_NO_DEPRECATED_API=NPY_1_9_API_VERSION
  -I/venv/include -I/usr/include/python3.7 -I/venv/lib/python3.7/site-packages/numpy/core/include
  -c ethosu/mlw_codec/mlw_codecmodule.c -o build/temp.linux-x86_64-3.7/ethosu/mlw_codec/mlw_codecmodule.o
    ethosu/mlw_codec/mlw_codecmodule.c:20:10: fatal error: Python.h: No such file or directory
       20 | #include <Python.h>
          |          ^~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /venv/bin/python -u -c
'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-4rmoh7va/ethos-u-vela/setup.py'"'"'
; __file__='"'"'/tmp/pip-install-4rmoh7va/ethos-u-vela/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)
(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))'
install --record /tmp/pip-record-jidxiokn/install-record.txt --single-version-externally-managed
--compile --install-headers
/venv/include/site/python3.7/ethos-u-vela Check the logs for full command output.
```

To solve this issue install libpython3 on the system.

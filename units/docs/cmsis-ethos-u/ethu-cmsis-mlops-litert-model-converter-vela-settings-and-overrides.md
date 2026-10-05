---
id: "ethu-cmsis-mlops-litert-model-converter-vela-settings-and-overrides"
type: "concept"
domain: "edge-ai"
title: "CMSIS MLOps LiteRT model converter specification: Vela settings and overrides"
summary: "By default, the complete Vela configuration comes from cbuild-mlops.vela.options, cbuild-mlops.vela.misc, and cbuild-mlops.vela.ini."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/script/model-converter-specification.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/script/model-converter-specification.md#vela-settings-and-overrides"
license: "Apache-2.0"
mode: "V"
---

By default, the complete Vela configuration comes from
`cbuild-mlops.vela.options`, `cbuild-mlops.vela.misc`, and
`cbuild-mlops.vela.ini`.

The script tokenizes `vela.options` and `vela.misc` with `shlex.split` and
invokes Vela with a subprocess argument list and `shell=False`. Miscellaneous
Vela options are passed through unchanged and in their specified order.

`--system` replaces the value of `--system-config` in `vela.options`.
`--memory` replaces the value of `--memory-mode`. Both `--option value` and
`--option=value` forms are supported. If an overridden option is absent, the
script appends it in this form:

```text
--system-config <value>
--memory-mode <value>
```

`--misc` replaces the complete value of `cbuild-mlops.vela.misc` for the
current invocation; it does not append to it. An explicitly empty value removes
all miscellaneous options:

```console
python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml --misc=""
```

A miscellaneous option string shall not contain `--system-config` or
`--memory-mode`; these settings belong to their dedicated fields and command
line options.

Overrides affect only the current invocation. The script never modifies the
generated `*.cbuild-mlops.yml` file.

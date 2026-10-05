---
id: "genpack-bash-library-for-gen-pack-scripts-usage"
type: "concept"
domain: "pack"
title: "Bash library for gen-pack scripts: Usage"
summary: "A genpack.sh script accepts the following command line flags and arguments:"
status: "draft"
collection: "gen-pack"
source: "Open-CMSIS-Pack/gen-pack@2fc9447:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/gen-pack/blob/2fc9447/README.md#usage"
license: "Apache-2.0"
mode: "V"
---

A `gen_pack.sh` script accepts the following command line flags and arguments:

- `-h, --help`: Prints below usage message end exits with error level 1.
- `-k, --keep`: Prevents the temporary build directory from being automatically deleted.
- `-c, --[no-]changelog <prefix>`: Update the `<releases>` section in the `.pdsc` file with a generated history. The
                                   versions, dates and descriptions are inferred from Git tags. The `<prefix>` can be
                                   used to filter tags for release tags by the given string.
- `--[no-]preprocess`: Run custom preprocess function if implemented.
- `--[no-]postproces`: Run custom postprocess function if implemented.
- `-v, --verbose`: Enable verbose log output such as full sub-commands being issues.

```sh
$ ./gen_pack.sh -h

Usage: gen_pack.sh [-h] [-k] [-c <prefix>] [<pdsc>]

Arguments:
  -h, --help                      Print this usage message and exit.
  -k, --keep                      Keep build directory.
  -c, --[no-]changelog <prefix>   Generate changelog. Tags are filtered for <prefix>.
  --[no-]preprocess               Run the preprocess function if implemented in the enclosing script.
  --[no-]postproces               Run the postprocess function if implemented in the enclosing script.
  -v, --verbose                   Print verbose log output.
  <pdsc>                          The pack description to generate the pack for.
```

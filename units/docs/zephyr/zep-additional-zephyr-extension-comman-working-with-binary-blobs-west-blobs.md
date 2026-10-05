---
id: "zep-additional-zephyr-extension-comman-working-with-binary-blobs-west-blobs"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Working with binary blobs: `west blobs`"
summary: "The blobs command allows users to interact with :ref:binary blobs <bin-blobs> declared in one or more modules via their module.yml file."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

The `blobs` command allows users to interact with :ref:`binary blobs
<bin-blobs>` declared in one or more modules via their
module.yml file.

The `blobs` command has three sub-commands, used to list, fetch or clean (i.e.
delete) the binary blobs themselves.

You can list binary blobs while specifying the format of the output::
```
west blobs list -f '{module}: {type} {path}'
```
For the full set of variables available in `-f/--format` run
`west blobs -h`.

Fetching blobs works in a similar manner::
```
west blobs fetch
```
Note that, as described in the modules section,
fetched blobs are stored in a `zephyr/blobs/` folder relative to the root
of the corresponding module repository.

As does deleting them::
```
west blobs clean
```
Additionally the tool allows you to specify the modules you want to list,
fetch or clean blobs for by typing the module names as a command-line
parameter.

The argument `--allow-regex` can be passed `west blobs fetch` to restrict
the specific blobs that are fetched, by passing a regular expression::
```
# For example, only download esp32 blobs, skip the other variants
west blobs fetch hal_espressif --allow-regex 'lib/esp32/.*'
```
An auto-cache directory can be provided via the `--auto-cache` cli argument
or via the `blobs.auto-cache` config option. When enabled, the auto-cache
directory is automatically populated whenever a blob is missing and downloaded.

One or more additional cache directories (separated by `;`) can be provided
in `--cache-dirs` cli argument or `blobs.cache-dirs` config option.

`west blobs fetch` searches all configured cache directories (including the
auto-cache) for a matching blob filename. Cached files may be stored either
under their original filename or with a SHA-256 suffix (`<filename>.<sha>`).
If found, the blob is copied from the cache to the blob path; otherwise
it is downloaded from its URL(s) to the blob path.

One or more download mirrors can be configured via the `blobs.mirrors`
config option. Its value is a JSON object that contains one or more
key-value pairs, where each key is a remote URL prefix (a string) and each
value is either a single mirror URL prefix (a string) or a list of mirror
URL prefixes (an array of strings).

A single mirror for a remote URL prefix::
```
west config blobs.mirrors '{"https://github.com/": "https://example.com/github-mirror/"}'
```
More than one mirror for the same remote URL prefix, tried in list order::
```
west config blobs.mirrors '{
  "https://github.com/": [
    "https://example.com/github1-mirror/",
    "https://example.com/github2-mirror/"
  ]
}'
```
For each blob URL, every mirror whose remote URL prefix matches is tried,
ordered so that the *longest* (most specific) matching remote URL prefix is
tried first (like git's `insteadOf`); mirrors for shorter, less specific
matches are tried afterward. Mirrors configured for the same remote URL
prefix are tried in the order they are listed. The original URL is tried
last, as a fallback if every mirror fails.

---
id: "pyocd-configuration-config-file"
type: "concept"
domain: "debug"
title: "configuration: Config file"
summary: "pyOCD supports a YAML configuration file that lets you set session options that either apply to all probes or to a single probe, based on the probe's unique ID."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/configuration.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/configuration.md#config-file"
license: "Apache-2.0"
mode: "V"
---

pyOCD supports a YAML configuration file that lets you set session options that either apply to
all probes or to a single probe, based on the probe's unique ID.

The easiest way to use a config file is to place a `pyocd.yaml` file in the project directory.
An alternate `.yml` extension and
optional dot prefix on the config file name are allowed. Alternatively, you can use the
`--config` command line option, for instance `--config=myconfig.yaml`. Finally, you can set the
`config_file` option. If there is a need to prevent reading a config file, use the `--no-config`
argument.

The top level of the YAML file is a dictionary. The keys in the top-level dictionary must be names
of session options, or the key `probes`. Session options are set to the value corresponding to the
dictionary entry. Unrecognized option names are ignored.

If there is a top-level `probes` key, its value must be a dictionary with keys that match a
substring of debug probe unique IDs. Usually you would just use the complete unique ID shown by
listing connected boards (i.e., `pyocd list`). The values for the unique ID entries are
dictionaries containing session options, just like the top level of the YAML file. Of course, these
options are only applied when connecting with the given probe. If the probe unique ID
substring listed in the config file matches more than one probe, the corresponding options
will be applied to all matching probes.

Options set in the config file will override any options set via the command line.

Example config file:
````yaml
probes:
  066EFF555051897267233656: # Probe's unique ID.
    target_override:  stm32l475xg
    test_binary:      stm32l475vg_iot01a.bin

# Global options
auto_unlock: false
frequency: 8000000 # Set 8 MHz SWD default for all probes
````

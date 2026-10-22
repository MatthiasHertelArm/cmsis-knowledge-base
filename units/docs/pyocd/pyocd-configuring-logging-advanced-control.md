---
id: "pyocd-configuring-logging-advanced-control"
type: "concept"
domain: "debug"
title: "Configuring logging: Advanced control"
summary: "Fine-grained control of pyOCD log output is available through logging configuration. The logging package supports loading a configuration dictionary to control almost all aspects of log output."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/configuring_logging.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/configuring_logging.md#advanced-control"
license: "Apache-2.0"
mode: "V"
---

Fine-grained control of pyOCD log output is available through logging configuration. The logging
package supports loading a configuration dictionary to control almost all aspects of log output.

The `logging` session option is used to specify the logging configuration. It can be set to either a
logging configuration dictionary or the path to a YAML file containing a configuration dictionary.
Usually it is easiest to include the configuration directly in a `pyocd.yaml` config file. See the
[configuration documentation]({% link _docs/configuration.md %}) for more on config files. The file path is most
useful when passing the `logging` option via the command line, since you can't provide a dictionary
this way.


### Controlling module log levels

A basic logging configuration to control verbosity at the module level looks like this, as shown
in a `pyocd.yaml` config file:

```yaml
logging:
  loggers:
    pyocd.flash.loader:
      level: DEBUG
    pyocd.flash.flash_builder:
      level: DEBUG
```

The top level `logging` key is the session option. Under it must be a `loggers` key, which has the
name of each module you wish to configure as a child key. Then, under each module name, the `level`
key specifies the log level for that module. Due to the way logging propagation works, you do not
need to set the level of parent loggers to match the child levels. In fact, setting the level of a
parent logger
such as `pyocd` will set the level for all children—this is an easy way to control the log level
for all of pyOCD.

Note that because the `logging` option is passed to and handled by the Python logging module, it does not support
wildcard matching against loggers like the `--log-level` argument.


### Full control

The full schema for the logging configuration dictionary is documented in the
[logging.config module documentation](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema).
The logging module's
[advanced tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
has a good introduction to the features and log output flow, so you can better understand the
configuration schema.

The `version` key described in the schema is optional in pyOCD's logging configuration. If not
present, pyOCD will set the schema version to 1 (currently the only version). In addition, pyOCD
will set the `disabled_existing_loggers` key to false unless it is specified in the configuration
(the default is true).

Note that if you change the configuration for the root logger, you will need to define a handler
and formatter in the configuration (see the example below).

Here is a much more complex example configuration that sets a custom formatter and changes several log
levels:

```yaml
logging:
  formatters:
    brief:
      format: '%(relativeCreated)07d - %(levelname)s - %(name)s - %(message)s'
  handlers:
    console:
      class: logging.StreamHandler
      formatter: brief   # reference to "brief" formatter above
      level: DEBUG
      stream: ext://sys.stdout
  root:
    level: INFO
    handlers:
      - console          # reference to "console" handler above
  loggers:
    pyocd:
      level: INFO        # set all pyocd loggers to INFO level
    pyocd.probe:
      level: DEBUG       # set this logger to DEBUG level
```

This example shows how to direct log output to a log file called `pyocd_log.txt`:

```yaml
logging:
  root:
    handlers: [logfile]
  formatters:
    precise:
      format: "[%(relativeCreated)07d:%(levelname)s:%(module)s] %(message)s"
  handlers:
    logfile:
      class: logging.FileHandler
      formatter: precise
      filename: pyocd_log.txt
      mode: w
      delay: false
```

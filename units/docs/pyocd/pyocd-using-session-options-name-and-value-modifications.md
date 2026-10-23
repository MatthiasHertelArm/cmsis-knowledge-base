---
id: "pyocd-using-session-options-name-and-value-modifications"
type: "concept"
domain: "debug"
title: "Using session options: Name and value modifications"
summary: "Several changes are applied to option names and values when they are set. First, the names are normalised."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/api/using_session_options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/api/using_session_options.md#name-and-value-modifications"
license: "Apache-2.0"
mode: "V"
---

Several changes are applied to option names and values when they are set. First, the names are normalised.

1. Convert all occurrences of double-underscores to a dot, e.g., `__` changes to a `.` character. Doing this makes it possible to set options with dots in the name using keyword arguments.
2. Change to lower case.

Then, any option set with a value of `None` is ignored. In that case, the option's value from a lower priority layer will take precedence.

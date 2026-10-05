---
id: "pyocd-using-session-options-accessing-options"
type: "concept"
domain: "debug"
title: "using session options: Accessing options"
summary: "Options are quite easy to use from within Python code. The Session object has an options property which returns a dict-like OptionsManager object that is used to access options for that session."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/api/using_session_options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/api/using_session_options.md#accessing-options"
license: "Apache-2.0"
mode: "V"
---

Options are quite easy to use from within Python code. The `Session` object has an `options` property which returns a dict-like `OptionsManager` object that is used to access options for that session. The `OptionsManager` object supports either slicing or `.get()`/`.set()` methods for reading and writing options.

```py
# Reading an option from the session using two techniques.
value = session.options['reset_type']
value = session.options.get('reset_type')

# Changing the value of an option
session.options['reset_type'] = 'system'
session.options.set('reset_type') = 'system'
```

Note that `.get()` does not take an optional second parameter for a default value if the session option is unset. Instead, this default value is determined from the session option's definition.

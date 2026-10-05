---
id: "pyocd-api-examples-alternative-ways-to-create-a-session"
type: "concept"
domain: "debug"
title: "api examples: Alternative ways to create a session"
summary: "It's important to understand that the ConnectHelper.session_with_chosen_probe() method doesn't itself open the session for you. Instead, it's using the session object as a context manager that does this."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/api_examples.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/api_examples.md#alternative-ways-to-create-a-session"
license: "Apache-2.0"
mode: "V"
---

It's important to understand that the `ConnectHelper.session_with_chosen_probe()` method doesn't
itself open the session for you. Instead, it's using the session object as a context manager that
does this.

Here is an example where the `with` statement is separated from the creation of the session.

```python
# Connect to the target.
session = ConnectHelper.session_with_chosen_probe()

# Manually open the session. When the 'with' statement exits, the session is closed.
with session:
    # ... control the target
```

This example demonstrates complete manual control of session opening and closing.

```python
# Connect to the target.
session = ConnectHelper.session_with_chosen_probe()

# Manually open the session.
session.open()

# ... control the target

# Close the session and connection.
session.close()
```

In reality you might want to put the call to `close()` in a `finally` clause of an exception handler.

The example here shows how the `auto_open` parameter can be used to achieve a combination of the
above approaches. When set to False, the session will _not_ be opened upon entry into a `with`
statement. This allows using a `with` statement to ensure the session is properly closed, but with
manual opening so you could, perhaps, further configure the session before it is opened.

```python
# Here we set auto_open to False, so the 'with' statement won't open the session.
session = ConnectHelper.session_with_chosen_probe(auto_open=False)

# When the 'with' statement exits, the session is closed.
with session:
    # ... modify the session

    # Manually open the session.
    session.open()

    # ... control the target
```

Selecting a probe and configuring the target connection is done as follows:

```python
# Connect to the target with some options.
session = ConnectHelper.session_with_chosen_probe(unique_id = "E6616407E3646B29", options = {"frequency": 4000000, "target_override": "nrf52840"})

with session:
    # ...
```

More options can be found [here](https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md).

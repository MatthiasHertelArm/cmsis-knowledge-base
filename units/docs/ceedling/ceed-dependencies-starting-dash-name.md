---
id: "ceed-dependencies-starting-dash-name"
type: "concept"
domain: "test"
title: "Dependencies: Starting Dash & Name"
summary: "Yes, that opening dash tells the dependencies plugin that the rest of these fields belong to our first dependency."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#starting-dash-name"
license: "MIT"
mode: "V"
---

Yes, that opening dash tells the dependencies plugin that the rest of these fields
belong to our first dependency. If we had a second dependency, we’d have another
dash, lined up with the first, and followed by all the fields indented again.

By convention, we use the `:name` field as the first field for each tool. Ceedling
honestly doesn't care which order the fields are given... but as humans, it makes
it easier for us to see the name of each dependency with starting dash.

The name field is only used to print progress while we're running Ceedling. You may
call the name of the field whatever you wish.

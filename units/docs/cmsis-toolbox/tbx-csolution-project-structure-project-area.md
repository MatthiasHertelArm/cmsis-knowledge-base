---
id: "tbx-csolution-project-structure-project-area"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Directory Structure / Project Area"
summary: "There are no strict rules on how to organize the project area that stores the user source code. However, the following guidelines apply:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#project-area"
license: "Apache-2.0"
mode: "V"
---

_Part of: Directory Structure_

There are no strict rules on how to organize the project area that stores the user source code. However, the following guidelines apply:

- Each [solution](#project-examples) should have a distinct base directory. This directory contains the file `*.csolution.yml` which refers to the independent projects defined with `*.cproject.yml` files.

Each project should have a distinct base directory. This directory contains the file `*.cproject.yml`, which defines the project's content. The project's source code might be grouped in subdirectories that are typically stored in this base directory. The [configuration files](#rte-directory-structure) of the software components are typically stored in a subdirectory with the name `./RTE`.

- A `*.cproject.yml` may refer to one or more [software layers](#software-layers) with `*.clayer.yml` files. Each software layer should have a distinct base directory with a similar structure as a project. This base directory contains the file `*.clayer.yml` that defines the content of the software layer. It also contains the user source code (optionally organized in sub-directories) and the [configuration​ files](#rte-directory-structure) of software components that belong to this layer, typically stored in a sub-directory with the name `./RTE`.

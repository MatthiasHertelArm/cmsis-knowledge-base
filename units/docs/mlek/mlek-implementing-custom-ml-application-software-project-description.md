---
id: "mlek-implementing-custom-ml-application-software-project-description"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Software project description"
summary: "See Repository structure section for the outline of the repo."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md#software-project-description"
license: "Apache-2.0"
mode: "V"
---

See [Repository structure](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../documentation.md#repository-structure) section for the outline of the repo.

> **Convention**: Separate use-cases must be organized in sub-folders under the `source/app/use_case` folder. The name of
> the directory is used as a name for this use-case and can be provided as a `USE_CASE_BUILD` parameter value. The build
> system expects that sources for the use-case are structured as follows: Headers in an `include` directory and C/C++
> sources in a `src` directory. For example:
>
> ```tree
> source/app/use_case
>   └── img_class
>         ├── include
>         └── src
> ```
>
> It is important to note that each use case example has at least one associated API that it uses from
> `source/lib/mlek/use_case`. These are reusable ML use-case libraries so the use case example
> implementations can re-use one or more of these components across targets. However, it
> is not mandatory to use an API, or to implement one if you are adding a use-case.

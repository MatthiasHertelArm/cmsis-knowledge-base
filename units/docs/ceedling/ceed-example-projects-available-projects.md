---
id: "ceed-example-projects-available-projects"
type: "concept"
domain: "test"
title: "Example projects: Available projects"
summary: "Once you’ve exported a project you can inspect the project.yml file and source & test code. Run ceedling help from the root of an example project to see what you can do, or just go nuts with ceedling test:all."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/getting-started/example-projects/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/#available-projects"
license: "MIT"
mode: "V"
---

Once you’ve exported a project you can inspect the _project.yml_ file and 
source & test code. Run `ceedling help` from the root of an example project
to see what you can do, or just go nuts with `ceedling test:all`.




-   :material-memory: **[`temp_sensor`](https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/temp-sensor.md)**

    ---

    An imagined temperature sensor project containing assertions, 
    mocks, and code techniques representative of testing in embedded 
    development. Test suite only.

-   :material-forest-outline: **[`wondrous_forest`](https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/wondrous-forest.md)**

    ---

    An imagined forest monitoring system project illustrating the
    use of [Partials](https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/../../testing-guide/partials/index.md) in a test suite.
    Test suite only.

-   :material-incognito: **[`cipher_quest`](https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/cipher-quest.md)**

    ---

    An imagined spy’s command line string manipulation toolkit. This
    project can be run both as a test suite and as a release build. It
    demonstrates build options around conditional compilation (`ifdef`) 
    and defining symbols with Ceedling including with Mixins.

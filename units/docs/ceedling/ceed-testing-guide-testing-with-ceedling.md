---
id: "ceed-testing-guide-testing-with-ceedling"
type: "concept"
domain: "test"
title: "Testing Guide: Testing with Ceedling"
summary: "Much of what Ceedling accomplishes is by convention. Code and file structures and naming trigger sophisticated test build features. Also covers search paths, file extensions, preprocessing, and more."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/#testing-with-ceedling"
license: "MIT"
mode: "V"
---

-   :material-book-open-page-variant: **[Important Conventions & Behaviors][conventions]**

    ---

    Much of what Ceedling accomplishes is by convention. Code and file structures 
    and naming trigger sophisticated test build features. Also covers search paths, 
    file extensions, preprocessing, and more.

-   :material-link-variant: **[Using Unity & CMock][frameworks]**

    ---

    Ceedling connects the Unity and CMock frameworks — each of which 
    can require configuration of its own. Ceedling facilitates this.

-   :material-content-cut: **[Partials][partials]**

    ---

    Partials are like a scalpel for your source code. A generated partial allows 
    you to test and mock parts of your code you could not otherwise access
    without rewriting it first.

-   :material-pound: **[Build Directive Macros][build-directives]**

    ---

    In-test macros to accomplish build goals when Ceedling’s conventions aren’t
    quite enough — adding source files, handling include paths, and more.



[test-cases]:         test-cases.md
[test-sample]:        test-sample.md
[test-suite-anatomy]: test-suite-anatomy.md
[conventions]:        conventions.md
[frameworks]:         frameworks.md
[build-directives]:   build-directives.md
[partials]:           partials/index.md

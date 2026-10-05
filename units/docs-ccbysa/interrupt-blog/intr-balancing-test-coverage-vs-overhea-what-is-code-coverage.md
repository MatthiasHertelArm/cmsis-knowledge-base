---
id: "intr-balancing-test-coverage-vs-overhea-what-is-code-coverage"
type: "concept"
domain: "debug"
title: "Balancing Test Coverage vs. Overhead: What is Code Coverage"
summary: "Code coverage refers to how much of a codebase is covered by tests. Below is an example output from LCOV[^lcov], a popular tool for testing code coverage."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-03-23-testing-vs-overhead.md"
doc_source: "https://interrupt.memfault.com/blog/testing-vs-overhead#what-is-code-coverage"
license: "CC-BY-SA-4.0"
mode: "V"
---

Code coverage refers to how much of a codebase is covered by tests. Below is an example output from LCOV[^lcov], a popular tool for testing code coverage.



    


A code coverage report will provide you with information about the number of units of code (and percentage of total units) that have been run by the tests as well as point out exactly which units haven't been tested. This makes it easy to find the branches of code that have not been tested at all.

[Unit testing](https://interrupt.memfault.com/blog/unit-testing-basics) is the most common method developers use to test code. Unit tests are tests that are written to instrument a single unit of code, such as a collection of methods inside a class or module. Each method in a class will have several tests written against it, which provide a series of different inputs and assert an expected output. How many units of code are covered by tests determines the percentage of code coverage.

> To learn how to add code coverage reporting to your embedded projects, you can check out the instructions [here](https://interrupt.memfault.com/blog/unit-testing-basics#code-coverage).

Certain programming paradigms are easier to test than others. Functional programming is particularly easy to test, as each function is intended to be idempotent and can be called in isolation. However, many other times, code is not as clean and easy to test. Certain functions may expect certain environmental configurations or dependency functions to be compiled in. They may be tightly coupled to other modules or methods and may expect to be passed results from external sources, such as a database connection, API result, file on the filesystem, or external sensor.

These expected inputs need to be [mocked](https://interrupt.memfault.com/blog/unit-test-mocking) and other special conditions must be taken into consideration, all of which take up valuable developer's time and company resources.

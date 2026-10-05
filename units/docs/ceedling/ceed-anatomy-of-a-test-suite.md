---
id: "ceed-anatomy-of-a-test-suite"
type: "concept"
domain: "test"
title: "Anatomy of a Test Suite"
summary: "A Ceedling test suite is composed of one or more individual test executables."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/test-suite-anatomy.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/test-suite-anatomy/"
license: "MIT"
mode: "V"
---

A Ceedling test suite is composed of one or more individual test executables.

The [Unity] project provides the actual framework for test case assertions 
and unit test sucess/failure accounting. If mocks are enabled, [CMock] builds 
on Unity to generate mock functions from source header files with expectation
test accounting. Ceedling is the glue that combines these frameworks, your
project's toolchain, and your source code into a collection of test 
executables you can run as a singular suite.

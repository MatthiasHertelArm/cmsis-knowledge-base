---
id: "ceed-partials-walk-through-example-testing-mocking-a-static-helper"
type: "concept"
domain: "test"
title: "Partials Walk-Through Example: Testing & mocking a `static` helper"
summary: "Partials allows you to accomplish both of these goals with no changes to sensor.c even though ConvertRawToMilliCelsius() is static."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/partials/example.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/example/#testing-mocking-a-static-helper"
license: "MIT"
mode: "V"
---

!!! tip
    Ceedling comes with example projects. The example project `wondrous_forest`
    demonstrates the use of Partials in realistic code.
    Use [`ceedling example`](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/example/../../getting-started/command-line.md#application-commands)
    to export the `wondrous_forest` project.

You as a test author want to:

1. Test the `static` helper `_ConvertRawToMilliCelsius()` directly
2. Mock the `static` helper `_ConvertRawToMilliCelsius()` while testing `Sensor_ReadCelsius()`

Partials allows you to accomplish both of these goals with no changes to
_sensor.c_ even though `_ConvertRawToMilliCelsius()` is static.

!!! warning "A function cannot be both tested and mocked in the same test file"
    A core restriction of the C language remains here! `_ConvertRawToMilliCelsius()`
    cannot be both tested and mocked in the same test. Attempting to do so would
    duplicate the function and cause a doubly-defined symbol failure during linking.

    We solve this by simply creating two peer test files for the different Partials
    usage scenarios.

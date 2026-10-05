---
id: "ceed-fake-function-framework-for-ceedli"
type: "concept"
domain: "test"
title: "Fake Function Framework for Ceedling"
summary: "This plugin causes Ceedling to use the Fake Function Framework for mocking instead of CMock, the default mocking framework packaged with Ceedling."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/fff.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/fff/"
license: "MIT"
mode: "V"
---

This plugin causes Ceedling to use the [Fake Function Framework](https://github.com/meekrosoft/fff) for mocking instead of CMock, the default mocking framework packaged with Ceedling.

Using _FFF_ provides less strict mocking than CMock and affords more loosely-coupled tests.

This Ceedling 1.x plugin incorporates a snapshot of _FFF_ version 0.1.1 and supersedes a separately available [FFF Ceedling plugin project](https://github.com/ElectronVector/fake_function_framework). The built-in _FFF_ plugin that now comes with Ceedling was derived from the ElectronVector project and is now maintained along with Ceedling and tracks its updates.

!!! note "Special thanks to Matt Chernosky"
    [Matt Chernosky](http://www.electronvector.com) originally developed this plugin 
    as an adapter for _FFF_. It's a well-loved piece of the Ceedling ecosystem,
    and we really appreciate his support through the years.

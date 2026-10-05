---
id: "unity-unity-fixtures-dependency-notification"
type: "concept"
domain: "test"
title: "Unity Fixtures: Dependency Notification"
summary: "Fixtures, by default, uses the Memory addon as well. This is to make it simple for those trying to follow along with James' book. Using them together is completely optional."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:extras/fixture/readme.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/extras/fixture/readme.md#dependency-notification"
license: "MIT"
mode: "V"
---

Fixtures, by default, uses the Memory addon as well.
This is to make it simple for those trying to follow along with James' book.
Using them together is completely optional.
You may choose to use Fixtures without Memory handling by defining `UNITY_FIXTURE_NO_EXTRAS`.
It will then stop automatically pulling in extras and leave you to do it as desired.

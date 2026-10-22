---
id: "unity-unity-fixtures"
type: "concept"
domain: "test"
title: "Unity Fixtures"
summary: "This Framework is an optional add-on to Unity. By including unity_fixture.h in place of unity.h, you may now work with Unity in a manner similar to CppUTest."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:extras/fixture/readme.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/extras/fixture/readme.md"
license: "MIT"
mode: "V"
---

This Framework is an optional add-on to Unity.
By including unity_fixture.h in place of unity.h, you may now work with Unity in a manner similar to CppUTest.
This framework adds the concepts of test groups and gives finer control of your tests over the command line.

This framework is primarily supplied for those working through James Grenning's book on Embedded Test Driven Development, or those coming to Unity from CppUTest.
We should note that using this framework glosses over some of the features of Unity, and makes it more difficult to integrate with other testing tools like Ceedling and CMock.

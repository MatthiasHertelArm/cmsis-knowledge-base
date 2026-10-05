---
id: "intr-embedded-c-c-unit-testing-with-moc"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks"
summary: "Writing a unit test from scratch for an embedded software project is almost always an exercise in frustration, patience, and determination. This is because of the constraints, as well as breadth, of embedded software."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking"
license: "CC-BY-SA-4.0"
mode: "V"
---

Writing a unit test from scratch for an embedded software project is almost
always an exercise in frustration, patience, and determination. This is because
of the constraints, as well as breadth, of embedded software. It combines
hardware drivers, operating systems, high-level software, and communication
protocols and stacks all within one software package and is usually managed by a
single team. Due to these complexities, the number of dependencies of a single
file can quickly grow out of control.

One paradigm that we can use to our advantage as embedded developers when
writing unit tests is _mocks_. They serve as a replacement for a module
dependency, are quick and easy to write, and make it easy to test your code in a
white-box fashion.



In this article, we do a deep-dive into unit testing with mocks. We'll go over
where they fit into your unit testing infrastructure, how to write them in
C/C++, and finally run through some real-world examples. At the end, we'll
briefly talk about integration tests.



This post builds upon [Unit Testing Basics
post](https://interrupt.memfault.com/blog/unit-testing-basics), where we covered
everything you would need to know to get started writing unit tests for your
embedded software project in C or C++ using CppUTest. We are going to jump
quickly into the content so it's best to have read that post first.

---
id: "tflm-porting-reference-ops-from-lite-to"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro"
summary: "This is a guide to porting reference ops from Lite to Micro. It explains, step-by-step, the recommended code changes and the process for submitting them for review and acceptance. The process results in multiple pull requests, or PRs."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/porting_reference_ops.md"
license: "Apache-2.0"
mode: "V"
---

This is a guide to porting reference ops from Lite to Micro. It explains,
step-by-step, the recommended code changes and the process for submitting them
for review and acceptance.  The process results in multiple pull requests, or
PRs. Multiple, [small PRs][] are easier for the project to review and merge.

The [Micro Contributing Guidelines][] are prerequisite reading. They cover
general code health, maintainability, style, and submission, as well as how to
setup a development environment. This guide contains step-by-step instructions
for the specific task of porting reference ops from Lite to Micro.

<!--
Semi-automated TOC generation with instructions from
https://github.com/ekalinin/github-markdown-toc#auto-insert-and-update-toc
-->
<!--ts-->
   * [Porting Reference Ops from Lite to Micro](#porting-reference-ops-from-lite-to-micro)
      * [1. Look for a port already in progress](#1-look-for-a-port-already-in-progress)
      * [2. Open a GitHub issue to track the port](#2-open-a-github-issue-to-track-the-port)
      * [3. Extract Lite's code for parsing op parameters to a function (PR1)](#3-extract-lites-code-for-parsing-op-parameters-to-a-function-pr1)
      * [4. Extract the reference for the op to a standalone header (PR2)](#4-extract-the-reference-for-the-op-to-a-standalone-header-pr2)
      * [5. Port the op from Lite to Micro (PR3)](#5-port-the-op-from-lite-to-micro-pr3)
   * [General Guidelines](#general-guidelines)
      * [Check each commit for formatting, lint, and unit-test passage](#check-each-commit-for-formatting-lint-and-unit-test-passage)
      * [Maintain a 1:1 correspondence between Micro and Lite versions of unit tests](#maintain-a-11-correspondence-between-micro-and-lite-versions-of-unit-tests)
   * [Notes](#notes)
   * [Frequently Asked Questions](#frequently-asked-questions)
      * [Can I use malloc/free or new/delete in my operator code?](#can-i-use-mallocfree-or-newdelete-in-my-operator-code)
      * [Can I use global/static variable constructors in my operator code](#can-i-use-globalstatic-variable-constructors-in-my-operator-code)
      * [How do I allocate persistent memory?](#how-do-i-allocate-persistent-memory)
      * [When am I allowed to allocate persistent memory?](#when-am-i-allowed-to-allocate-persistent-memory)
      * [How do I allocate/use temporary memory?](#how-do-i-allocateuse-temporary-memory)
      * [When can I allocate/use temporary memory?](#when-can-i-allocateuse-temporary-memory)
      * [Can I resize the tensors of my model?](#can-i-resize-the-tensors-of-my-model)
      * [Can I change the shape of tensors in my operator code?](#can-i-change-the-shape-of-tensors-in-my-operator-code)
      * [When can I change the shape of tensors in my operator code?](#when-can-i-change-the-shape-of-tensors-in-my-operator-code)
      * [Can I modify a TfLiteTensor or TfLiteEvalTensor?](#can-i-modify-a-tflitetensor-or-tfliteevaltensor)
      * [When can I inspect tensor data?](#when-can-i-inspect-tensor-data)
      * [How do I fix optimized kernel unit test failures?](#how-do-i-fix-optimized-kernel-unit-test-failures)

<!-- Added by: advaitjain, at: Thu 16 Sep 2021 11:49:51 AM PDT -->

<!--te-->

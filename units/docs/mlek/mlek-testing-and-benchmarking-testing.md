---
id: "mlek-testing-and-benchmarking-testing"
type: "concept"
domain: "edge-ai"
title: "Testing and benchmarking: Testing"
summary: "The tests folder uses the following structure:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/testing_benchmarking.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/testing_benchmarking.md#testing"
license: "Apache-2.0"
mode: "V"
---

The `tests` folder uses the following structure:

```tree
.
├── common
│   └── ...
├── use_case
│   ├── <usecase1>
│   │   └── ...
│   ├── <usecase2>
│   │   └── ...
└── utils
    └── ...
```

The folders contain the following information:

- `common`: The tests for generic and common application functions.
- `use_case`: Every use-case specific test in their respective folders.
- `utils`: Utility sources that are only used within the tests.

When [configuring](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-native-unit_test-build) and
[building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-the-configured-project) for your `native` target platform, the results of the build is
placed under `<build folder>/bin/` folder. For example:

```tree
.
├── arm_ml_embedded_evaluation_kit-<usecase1>-tests
├── arm_ml_embedded_evaluation_kit-<usecase2>-tests
├── ethos-u-<usecase1>
└── ethos-u-<usecase1>
```

To view all the available tests to run, use the following command in the `<build folder>`:

```commandline
ctest -N
```

Sample output:

```commandline
Test #1: ad-tests
Test #2: asr-tests
Test #3: img_class-tests
Test #4: kws-tests
Test #5: kws_asr-tests
Test #6: noise_reduction-tests
Test #7: object_detection-tests
Test #8: vww-tests

Total Tests: 8
```

To execute a specific unit-test from the above list, in addition to the common tests, run the following command in the `<build folder>`:

```commandline
ctest -R <test_name>
```

To run every test that has been built, run the following command in the `<build folder>`:

```commandline
ctest
```

Sample output:

```log
Start 1: ad-tests
1/8 Test #1: ad-tests .........................   Passed    0.17 sec
    Start 2: asr-tests
2/8 Test #2: asr-tests ........................   Passed    3.04 sec
    Start 3: img_class-tests
3/8 Test #3: img_class-tests ..................   Passed    0.49 sec
    Start 4: kws-tests
4/8 Test #4: kws-tests ........................   Passed    7.52 sec
    Start 5: kws_asr-tests
5/8 Test #5: kws_asr-tests ....................   Passed    2.85 sec
    Start 6: noise_reduction-tests
6/8 Test #6: noise_reduction-tests ............   Passed   16.41 sec
    Start 7: object_detection-tests
7/8 Test #7: object_detection-tests ...........   Passed    0.58 sec
    Start 8: vww-tests
8/8 Test #8: vww-tests ........................   Passed    0.07 sec


Total Test time (real) =  34.71 sec

```

> **Note:** Test outputs could contain `[ERROR]` messages. This is OK as they are coming from negative scenarios tests.

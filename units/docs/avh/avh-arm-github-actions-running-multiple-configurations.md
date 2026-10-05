---
id: "avh-arm-github-actions-running-multiple-configurations"
type: "concept"
domain: "test"
title: "Arm GitHub Actions: Running multiple configurations"
summary: "Software often needs to be tested in multiple configurations, with different toolchains and on different platforms. To simplify job definition for such variations, you can use a matrix strategy in GitHub Actions."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_gh_actions.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_gh_actions.md#running-multiple-configurations"
license: "Apache-2.0"
mode: "V"
---

Software often needs to be tested in multiple configurations, with different toolchains and on different platforms. To
simplify job definition for such variations, you can use a
[matrix strategy in GitHub Actions](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs).

For example, the code snapshot below defines a two-dimensional matrix for Corstone-320/315/310/300 targets with Arm
Compiler 6, GCC and Clang:

```yml
matrix:
  target: [CS320, CS315, CS310, CS300]
  compiler: [AC6, GCC, Clang]
```

Then, you can use in your job descriptions `${{ matrix.target }}` and  `${{ matrix.compiler }}` variables, that GitHub
Actions will automatically iterate over for you.

See [AVH-Hello](https://github.com/Arm-Examples/AVH-Hello) as a simple example where such matrix strategy is
implemented for building the program with different toolchains and for different Arm FVP targets.

Note that use of the
[csolution project format](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/YML-Input-Format.md) greatly
simplifies project definition and build for different target types and build configurations. It well integrates with
the GitHub Actions matrix for CI jobs.

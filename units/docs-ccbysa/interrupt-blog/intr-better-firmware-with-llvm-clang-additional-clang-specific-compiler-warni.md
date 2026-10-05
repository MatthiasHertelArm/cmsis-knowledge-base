---
id: "intr-better-firmware-with-llvm-clang-additional-clang-specific-compiler-warni"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Static Analysis With Clang and scan-build / Additional Clang Specific Compiler Warnings"
summary: "Part of: Static Analysis With Clang and scan-build"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#additional-clang-specific-compiler-warnings"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Static Analysis With Clang and scan-build_

Once you can compile your project with Clang, there are other compiler warnings not
supported by other compilers that you can enable. These can be helpful for catching potential bugs or issues.

The exhaustive list of "Diagnostic Warnings" supported by Clang can be found in the official documentation online[^5]. However, I find it easiest to run a build with all the possible Clang warnings enabled by using `-Weverything`, disabling all errors (`-Wno-error`) and piping the compilation output to a file I can grep after the fact. Let's try it out on the example project:

```bash
$ make clean && CLI_CFLAG_OVERRIDES="-Weverything -Wno-error" \
  COMPILER=clang make &> compilation_results.txt
$ grep -o "\[\-W.*\].*" compilation_results.txt | sort -u
[-Wcovered-switch-default]
[-Wdocumentation-html]
[-Wdocumentation-unknown-command]
[-Wdocumentation]
[-Wextra-semi-stmt]
[-Wimplicit-int-conversion]
[-Wmissing-noreturn]
[-Wmissing-prototypes]
[-Wmissing-variable-declarations]
[-Wpadded]
[-Wpedantic]
[-Wunused-macros]
[-Wunused-parameter]
```

Sweet! We have discovered quite a few warnings we can go and investigate as to whether we want to enable or not.

> Tip: For a production project, I actually like to leave
> `-Weverything` enabled. You can use a tool such as [Conda](https://interrupt.memfault.com/blog/conda-developer-environments) to ensure all developers are on the same version of
> LLVM/Clang and see the exact same errors and `-Wno-<warning>` (i.e `-Wno-pedantic`) to disable
> any warnings that are not useful for your application.

> Note: I haven't had a chance to try it out yet but it's worth noting that GCC is catching up on
> the static analysis front. In GCC 10, a bunch of new static analyzers
> were added via the `-fanalyzer` option.[^13]

{: #porting-gcc-to-clang}

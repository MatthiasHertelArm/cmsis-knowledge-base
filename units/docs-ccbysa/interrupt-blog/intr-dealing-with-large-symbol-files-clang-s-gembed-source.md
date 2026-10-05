---
id: "intr-dealing-with-large-symbol-files-clang-s-gembed-source"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: Clang's `-gembed-source`"
summary: "This is a very interesting feature that Clang provides (alas, it's not present in GCC, at least as of GCC 11):"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#clang-s-gembed-source"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is a very interesting feature that Clang provides (alas, it's not present
in GCC, at least as of GCC 11):

<https://releases.llvm.org/15.0.0/tools/clang/docs/ClangCommandLineReference.html#cmdoption-clang-gembed-source>

Using it goes something like this:

```bash
# build with clang, with -gembed-source.
# also strip the current working directory from the debug prefixes:
# https://interrupt.memfault.com/blog/reproducible-firmware-builds#fdebug-prefix-map
❯ clang -gdwarf-5 -gembed-source -fdebug-prefix-map=$(pwd)=. hello.c -o hello.embedsource
```

(This actually increases the size of the binary, unlike the other tools in this
article, but it's such a nice feature I couldn't resist including it here).

You can access the source data using llvm-dwarfdump or llvm-objcopy:

```bash
❯ llvm-dwarfdump-20 --color --debug-line-str hello.embedsource
hello.embedsource:      file format elf64-x86-64

.debug_line_str contents:
0x00000000: "."
0x00000002: "hello.c"
0x0000000a: "#include <stdio.h>\n\nint main(int argc, char **argv) {\n  printf(\"hello!\\n\");\n  return 0;\n}\n"
```

```bash
❯ llvm-objdump-20 --disassemble-symbols=main --source hello.embedsource

hello.embedsource:      file format elf64-x86-64

Disassembly of section .text:

0000000000401130 <main>:
; int main(int argc, char **argv) {
  401130: 55                            pushq   %rbp
  401131: 48 89 e5                      movq    %rsp, %rbp
  401134: 48 83 ec 10                   subq    $16, %rsp
  401138: c7 45 fc 00 00 00 00          movl    $0, -4(%rbp)
  40113f: 89 7d f8                      movl    %edi, -8(%rbp)
  401142: 48 89 75 f0                   movq    %rsi, -16(%rbp)
;   printf("hello!\n");
  401146: 48 bf 04 20 40 00 00 00 00 00 movabsq $4202500, %rdi          # imm = 0x402004
  401150: b0 00                         movb    $0, %al
  401152: e8 d9 fe ff ff                callq   0x401030 <printf@plt>
;   return 0;
  401157: 31 c0                         xorl    %eax, %eax
  401159: 48 83 c4 10                   addq    $16, %rsp
  40115d: 5d                            popq    %rbp
  40115e: c3                            retq
```

(Unfortunately I couldn't convince `lldb` to show this information
automatically, but hopefully that will be available eventually!)

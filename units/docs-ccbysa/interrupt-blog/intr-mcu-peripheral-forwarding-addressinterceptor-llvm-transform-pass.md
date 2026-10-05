---
id: "intr-mcu-peripheral-forwarding-addressinterceptor-llvm-transform-pass"
type: "concept"
domain: "debug"
title: "MCU Peripheral Forwarding: Option 2: Compile-Time Instrumentation / AddressInterceptor LLVM Transform pass"
summary: "Part of: Option 2: Compile-Time Instrumentation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-10-11-mcu-peripheral-forwarding.md"
doc_source: "https://interrupt.memfault.com/blog/mcu-peripheral-forwarding#addressinterceptor-llvm-transform-pass"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Option 2: Compile-Time Instrumentation_

I have developed an [LLVM Transform pass](https://llvm.org/docs/WritingAnLLVMPass.html#introduction-what-is-a-pass) (plugin) called AddressInterceptor (ADIN) to address the challenge of distinguishing between PC application addresses and peripheral addresses during instrumentation. ADIN checks all memory operations, assessing whether each operation involves global or local variables of the application. If an operation does not involve these types, ADIN proceeds to instrument the subsequent routines:

```cpp
extern "C" void __adin_store_(llvm_pass_addr pointer, llvm_value_type value, llvm_pass_arg TypeSizeArg, llvm_pass_arg AlignmentArg)
extern "C" llvm_value_type __adin_load_(const llvm_pass_addr pointer, llvm_pass_arg TypeSizeArg, llvm_pass_arg AlignmentArg)
extern "C" void __adin_memcpy_(llvm_pass_addr dest, const llvm_pass_addr src, const llvm_pass_arg size)
extern "C" void __adin_memset_(llvm_pass_addr dest, const llvm_pass_arg val, const llvm_pass_arg size)
```

The plugin works with LLVM IR code. It analyzes and modifies the LLVM IR representation of the source code to perform the necessary checks and instrumentation. For example, we have a simple C code file named `example.c`.

```c
int var = 0;

void f(){
  *(int*)0x100 = 1;
  var = *(int*)0x100;
}
```

To compile it into LLVM IR code using Clang, execute the following command:

```bash
clang -S -emit-llvm example.c -o example.ll
```

This command will generate the LLVM IR code file `example.ll` based on our C code above.

```llvm
; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @f() #0 {
  store i32 1, i32* inttoptr (i64 256 to i32*), align 4
  %1 = load i32, i32* inttoptr (i64 256 to i32*), align 4
  store i32 %1, i32* @b, align 4
  ret void
}
```

To utilize the AddressInterceptor (ADIN) plugin with the `opt` utility of LLVM, you would typically invoke `opt` with the `-adin` flag. This flag indicates that you want to apply the ADIN plugin during the optimization process

```bash
opt -adin -S example.ll-o adin_modified_example.ll
```

The modified LLVM IR code will be written to the `modified.ll` file.

```llvm
define dso_local void @f() #0 {
  call void @__adin_store_(i8* inttoptr (i64 256 to i8*), i64 1, i32 32, i32 4)
  %load_i32_ = call i64 @__adin_load_(i8* inttoptr (i64 256 to i8*), i32 32, i32 4)
  %truncated_i32_ = trunc i64 %load_i32_ to i32
  store i32 %truncated_i32_, i32* @b, align 4
  ret void
}
```

To obtain detailed instructions on building and using the **AddressInterceptor** (ADIN) plugin, refer to the documentation provided in the [ADIN LLVM fork repository](https://github.com/remotemcu/adin-llvm#usage).

Once you have modified the LLVM IR code using the ADIN plugin and obtained the transformed IR code from the MCU's SDK, you can proceed to compile the IR code into object files.

```bash
clang -c modified.ll -o modified.o
```

 However, to successfully link these object files and create an executable file or library, we may need to implement certain functions that the plugin instrumented before it.

```cpp
extern "C" void __adin_store_(llvm_pass_addr pointer, llvm_value_type value, llvm_pass_arg TypeSizeArg, llvm_pass_arg AlignmentArg)
extern "C" llvm_value_type __adin_load_(const llvm_pass_addr pointer, llvm_pass_arg TypeSizeArg, llvm_pass_arg AlignmentArg)
extern "C" void __adin_memcpy_(llvm_pass_addr dest, const llvm_pass_addr src, const llvm_pass_arg size)
extern "C" void __adin_memset_(llvm_pass_addr dest, const llvm_pass_arg val, const llvm_pass_arg size)
```

In the functions inserted by the ADIN plugin, you must perform address checks to verify if the accessed address falls within the defined peripheral address intervals. If a match is found, you can execute the corresponding operation on the MCU chip.

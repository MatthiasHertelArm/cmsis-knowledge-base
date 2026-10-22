---
id: "cda-troubleshooting-c-and-c-debug-sess-c"
type: "concept"
domain: "debug"
title: "Troubleshooting C and C++ debug sessions: C++"
summary: "Troubleshooting C and C++ debug sessions: C++"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@29d444c:docs/agent-resources/troubleshooting/cpp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/29d444c/docs/agent-resources/troubleshooting/cpp.md#c"
license: "Apache-2.0"
mode: "V"
---

- Name template instances and overloads in full: `Buffer<int>::size`; quote a name that contains parentheses, `'ns::parse(char const*)'`.
- In a member function the fields hang under `this` in the variable listing. Read them as `this->count`, or print the object with `-exec print *this`.
- Through a base-class pointer you see the static type. `-exec set print object on` followed by `-exec print *p` shows the dynamic type, and `-exec info vtbl p` its virtual table; `step_into` on a virtual call enters the override that really runs. `__cxa_pure_virtual` in `get_call_stack` means a virtual call from a constructor or destructor, or on a destroyed object.
- An uncaught exception ends in `std::terminate` and `abort`, with the throwing frame still on the stack; to see every throw, set the catchpoint described above.
- Static initialisation order: a global's constructor that reads a global from another file can find it still zero-filled. Break in the constructor: below it `get_call_stack` shows `__static_initialization_and_destruction_0` (GCC) or `__cxx_global_var_init` (Clang) and `_GLOBAL__sub_I_…`, and evaluating the other global shows whether it is built yet. On firmware these constructors run from the C library's start-up (`__libc_init_array` with GCC and newlib); start-up code that skips it leaves every global unconstructed.
- STL containers on the host: `-exec print v` prints the elements through the debugger's pretty-printers. `v[0]` in an expression can fail with "Cannot evaluate function -- may be inlined"; read the fields instead, `v._M_impl._M_start[0]` with libstdc++ or `v.__begin_[0]` with libc++.

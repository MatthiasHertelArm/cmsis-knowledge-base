---
id: "mlek-coding-standards-and-guidelines-naming-conventions"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: Naming Conventions"
summary: "The following examples of Hungarian notation are one possible set of uses:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/coding_guidelines.md#naming-conventions"
license: "Apache-2.0"
mode: "V"
---

### CPP language naming conventions

- Type (class, struct, enum) names must be `PascalCase`:

  ```C++
  class SomeClass
  {
      // [...]
  };
  void SomeFunction()
  {
      // [...]
  }
  ```

- Variables and parameter names must be `camelCase`:

  ```C++
  int someVariable;

  void SomeFunction(int someParameter) {}
  ```

- Use uppercase names for macros, pre-processor definitions, and enumeration values:

  ```C++
  #define SOME_DEFINE

  enum class SomeEnum
  {
      ENUM_VALUE_1,
      ENUM_VALUE_2
  };
  ```

- Namespace names must be lowercase

  ```C++
  namespace nspace
  {
  void FunctionInNamespace();
  }
  ```

- Source code must use Hungarian notation to annotate the name of a variable with information about its meaning.

  | Prefix | Class | Description |
  | ------ | ----- | ----------- |
  | `p` | Type      | Pointer to any other type |
  | `k` | Qualifier | Constant |
  | `v` | Qualifier | Volatile |
  | `m` | Scope     | Member of a class or struct |
  | `s` | Scope     | Static |
  | `g` | Scope     | Used to indicate variable has scope beyond the current function: file-scope or externally visible scope. |

The following examples of Hungarian notation are one possible set of uses:

  ```C++
  int g_GlobalInt=123;
  char* m_pNameOfMemberPointer=nullptr;
  const float g_kSomeGlobalConstant = 1.234f;
  static float ms_MyStaticMember =  4.321f;
  bool myLocalVariable=true;
  ```

### C language naming conventions

For C sources, we follow the Linux variant of the K&R style wherever possible.

- For function and variable names, we use the `snake_case` convention:

  ```C
  int some_variable;

  void some_function(int some_parameter) {}
  ```

- Use uppercase names for macros, pre-processor definitions, and enumeration values:

  ```C
  #define SOME_DEFINE

  enum some_enum
  {
      ENUM_VALUE_1,
      ENUM_VALUE_2
  };
  ```

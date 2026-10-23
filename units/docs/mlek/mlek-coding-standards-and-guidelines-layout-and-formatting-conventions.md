---
id: "mlek-coding-standards-and-guidelines-layout-and-formatting-conventions"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: Layout and formatting conventions"
summary: "Coding standards and guidelines: Layout and formatting conventions"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/coding_guidelines.md#layout-and-formatting-conventions"
license: "Apache-2.0"
mode: "V"
---

- C++ class code layout: Public function definitions must be at the top of a class definition, since they are most
  likely to be used. Private functions and member variables are left to last. Lay out class functions and member
  variables logically in blocks of related functionality.

- Class inheritance keywords are not indented. For example:

  ```C++
  class MyClass
  {
  public:
    int m_PublicMember;
  protected:
    int m_ProtectedMember;
  private:
    int m_PrivateMember;
  };
  ```

- Do not leave trailing spaces at the end of lines.

- Empty lines do not have trailing spaces.

- For pointers and references, the symbols `*` and `&` must be next to the name of the type - *not* the name of the
  variable.

  ```C++
  char* someText = "abc";

  void SomeFunction(const SomeObject& someObject) {}
  ```

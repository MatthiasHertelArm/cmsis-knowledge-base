---
id: "mlek-coding-standards-and-guidelines-block-management"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: Block Management"
summary: "Coding standards and guidelines: Block Management"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/coding_guidelines.md#block-management"
license: "Apache-2.0"
mode: "V"
---

- Blocks must use braces and the brace location must be consistent throughout.
  - Therefore, each function has its opening brace at the next line on the same indentation level as its header. The
    code within the braces is indented and the closing brace at the end is on the same level as the opening. For
    compactness, if the class, or function, body is empty, then braces on the same line are acceptable.

  - Conditional statements and loops, even if they are just single-statement body, must be surrounded by braces. The
    opening brace is at the same line. For non-empty blocks, the closing brace is on the next line and on the same
    indentation level as its header. Empty or short blocks may be kept on a single line where permitted by the
    formatter. The same rule is applied to classes.

    ```C++
    class Class1 {
    public:
        Class1();
    private:
        int element;
    };

    void NotEmptyFunction()
    {
        if (condition) {
            // [...]
        } else {
            // [...]
        }
        // [...]
        for(start_cond; end_cond; step_cond) {
            // [...]
        }
    }

    void EmptyFunction() {}
    ```

  - Cases within switch are indented and enclosed in brackets:

    ```C++
    switch (option)
    {
        case 1:
        {
            // handle option 1
            break;
        }
        case 2:
        {
            // handle option 2
            break;
        }
        default:
        {
            break;
        }
    }
    ```

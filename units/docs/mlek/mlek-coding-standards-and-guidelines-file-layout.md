---
id: "mlek-coding-standards-and-guidelines-file-layout"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: File layout"
summary: "Coding standards and guidelines: File layout"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/coding_guidelines.md#file-layout"
license: "Apache-2.0"
mode: "V"
---

- The standard copyright notice must be included in all files:

  ```copyright
  /*
  * SPDX-FileCopyrightText: Copyright <years additions were made to project> <your name>, Arm Limited and/or its
  * affiliates <open-source-office@arm.com>
  * SPDX-License-Identifier: Apache-2.0
  *
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  *
  *     http://www.apache.org/licenses/LICENSE-2.0
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  */
  ```

- Source lines must be no longer than 100 characters. You can spread the code out vertically, rather than horizontally,
  if required. For example:

  ```C++
  # This is significantly easier to read
  enum class SomeEnum1
  {
      ENUM_VALUE_1,
      ENUM_VALUE_2,
      ENUM_VALUE_3
  };

  # than this
  enum class SomeEnum2 { ENUM_VALUE_1, ENUM_VALUE_2, ENUM_VALUE_3 };
  ```

- Block indentation must use 4 characters and not use tabs.

- Each statement must be on a separate line. For example:

  ```C++
  int a, b; // Error prone
  int c, *d;

  int e = 0; // GOOD
  int *p = nullptr; // GOOD
  ```

- Also, the source code must not contain code that has been commented out or is unreachable.

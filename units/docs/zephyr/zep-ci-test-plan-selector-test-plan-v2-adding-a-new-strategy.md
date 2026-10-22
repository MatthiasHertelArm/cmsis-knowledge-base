---
id: "zep-ci-test-plan-selector-test-plan-v2-adding-a-new-strategy"
type: "concept"
domain: "test"
title: "CI Test Plan Selector (test_plan_v2): Adding a new strategy"
summary: "2. Decide consume vs. additive. Ask: \"If a downstream strategy also sees this file, will it produce useful additional coverage, or redundant/wrong results?\" If redundant/wrong: consumes = True."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ci_test_plan.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ci_test_plan.rst"
license: "Apache-2.0"
mode: "V"
---

1. **Subclass** `SelectionStrategy` and implement the two abstract
   members:

```python

class MyStrategy(SelectionStrategy):

    consumes: bool = False  # or True if authoritative

    @property
    def name(self):
        return "MyStrategy"

    def analyze(self, changed_files):
        # inspect changed_files
        calls = [...]       # list of TwisterCall
        handled = {...}     # subset of changed_files this strategy owns
        return calls, handled
```
2. **Decide consume vs. additive.**  Ask: "If a downstream strategy also sees
   this file, will it produce useful additional coverage, or redundant/wrong
   results?"  If redundant/wrong: `consumes = True`.

3. **Insert in the correct position** in `build_strategies`.  As a rule
   of thumb:

   * Consuming strategies belong before all additive strategies.
   * More-specific strategies belong before less-specific ones.
   * Strategies with no side-effects on the file pool (additive) can be
     ordered by cost — cheapest first.

4. **Guard optional dependencies** with a late import inside `analyze` and
   return `[], set()` gracefully when the dependency is missing.  Use the
   `# noqa: PLC0415` comment to silence the late-import warning.

5. **Write unit tests** in `scripts/tests/ci/test_test_plan_v2.py` covering:

   * The happy path (files correctly identified and routed).
   * The no-op path (irrelevant files produce no calls and no handled set).
   * Edge cases (missing files on disk, malformed YAML, empty inputs).

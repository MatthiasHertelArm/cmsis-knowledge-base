---
id: "avh-useful-hints-and-tips-execution-in-ci-frameworks"
type: "concept"
domain: "test"
title: "Useful Hints and Tips: Execution in CI frameworks"
summary: "The Infrastructure chapter explains how Arm FVPs and other related tools can be programmatically installed into various Continuous Integration (CI) frameworks, such as GitHub. To execute your programs on Arm FVPs in such workflows, the following is important:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:DoxyGen/simulation/src/hints_and_tips.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/simulation/src/hints_and_tips.md#execution-in-ci-frameworks"
license: "Apache-2.0"
mode: "V"
---

The [Infrastructure](https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/simulation/src/./../../infrastructure/html/index.html) chapter explains how Arm FVPs and other related tools can
be programmatically installed into various Continuous Integration (CI) frameworks, such as GitHub. To execute your
programs on Arm FVPs in such workflows, the following is important:

- Disable GUI visualization, as it often is not supported by a host and not needed in CI testing:
    - Set FVP configuration parameter `<board>.visualisation.disable-visualisation=1` for the board instance on the
      target FVP. For example, for Corstone-315 FVP it should be `mps4_board.visualisation.disable-visualisation=1`.
    - For targets with HDLCD, such as Corstone-315 FVP, additionally disable the visualization for HDLCD using
      `vis_hdlcd.disable_visualisation=1`.
- Redirect the console outputs to a log file as explained in console.
- Ensure the program execution is exited when required by the test. stop explains options for such exit.
- For simpler implementation a matrix-style job configuration configuration can be used. See for example
  [Running multiple configurations with GitHub Actions](https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/simulation/src/./../../infrastructure/html/avh_gh_actions.html#avh_gh_matrix).

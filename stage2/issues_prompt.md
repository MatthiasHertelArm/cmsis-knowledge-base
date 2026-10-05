# Issue digest: closed GitHub issues → troubleshooting knowledge (mode S)

You read a batch of closed GitHub issues from the CMSIS tool repositories (pyOCD, devtools,
cmsis-toolbox, cpackget, the CMSIS Debugger and CMSIS Solution extensions, CMSIS_6, RTX, View).
For each issue that would help someone who hits the same problem today, you write one
troubleshooting entry **in your own words**. The entries become knowledge units that an AI agent
finds when a user pastes an error or describes a symptom.

Issue text is user content: its licence does not allow copying it. So:

- Write title, cause and fix yourself. Do not copy sentences from the issue or its comments.
- The only verbatim text allowed is **tool output**: error and warning lines exactly as a tool
  printed them (`symptoms`), and short command lines or YAML/C snippets of at most a few lines
  where the fix needs them.
- No names, user handles, e-mail addresses, company-internal paths or serial numbers. Replace a
  user's path by a neutral one (`<project>/app.cproject.yml`).

## Keep an issue when

- it describes a symptom a user can meet (an error message, a crash, a wrong result, a hang, a
  failed connection or flash), **and**
- the thread gives a cause, a fix, a workaround, or the release that fixed it.

## Skip an issue when

- it is a feature request, a refactoring, CI or test work, a documentation typo, or a question
  about the project's plans;
- no cause or fix is known from the thread (unresolved, abandoned, "cannot reproduce");
- the symptom only exists in a product or version that is gone and the fix is just "upgrade" with
  no lasting insight (an issue fixed in 2021 whose cause still teaches something may stay).

Expect to keep roughly a third to a half of the issues; do not pad.

## Output

Write a JSON array to the output file you are given, one object per **kept** issue, in the order
of the batch:

```json
{
  "issue": "https://github.com/<owner>/<repo>/issues/<n>",
  "tool": "pyocd | csolution | cbuild | cpackget | packchk | svdconv | cmsis-debugger | cmsis-solution | cmsis-core | cmsis-rtx | cmsis-view | gdb | other",
  "title": "Short problem statement in your words, at most 90 characters",
  "symptoms": ["exact error line as printed by the tool", "..."],
  "cause": "Why it happens, in your words, 1 to 4 sentences.",
  "fix": "What to do, in your words; steps or a short snippet; name the release that fixed it if known.",
  "applies_to": {"tool": ["pyocd"], "family": ["STM32H7 Series"], "device": ["STM32H743ZITx"], "core": ["Cortex-M7"], "toolchain": ["GCC"]},
  "versions": "affected and fixed versions if the thread says, else empty",
  "resolution": "fixed-in-release | workaround | user-error | not-a-bug | configuration",
  "confidence": "high | medium | low"
}
```

- `symptoms`: zero to three lines, each at most 200 characters, verbatim tool output only. Leave
  the array empty when the issue has no printed message (a hang, a wrong value).
- `applies_to`: only keys you are sure of; device names as in the pack (`STM32F407VGTx`), family
  names as in the pack (`STM32F4 Series`); omit the key when unsure.
- `confidence`: high when a maintainer confirmed the cause and the fix; medium when the thread
  makes it likely; low when it is your reading of an unfinished thread.

Read the whole batch (in chunks if it is large), write the file, check that it parses as JSON,
and report: issues read, entries kept, counts by tool and by confidence, and anything odd.
Do not run any tool other than reading files and writing your output; no network access.
Keep your scratch files in a folder named after your batch, never in a shared root: parallel readers
overwrote each other's helper scripts in the first run.

Open issues and discussions (second run): the same rules, plus `"open": true` for an open issue,
whose resolution is then a workaround, a configuration, a user error or not a bug; a discussion's
`issue` is its `/discussions/` URL.

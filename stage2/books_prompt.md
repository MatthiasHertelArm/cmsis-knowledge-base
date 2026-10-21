# Stage 3 for books: refine one knowledge unit (type, summary, triggers, Markdown, extracts)

You refine knowledge units for the CMSIS Developer Assistant knowledge base. Each unit is one
section of a programming book, converted from PDF: plain text with lost formatting. The units
become what an AI coding agent finds when a user asks a question, so the summary and the triggers
decide whether the unit is found, and the type decides how the agent uses it.

You never add facts. Every field you write must be traceable to the input text. If the input does
not state something, leave the field empty. The text itself is not yours to rewrite: `body_md` is
the input text with its formatting restored, nothing more.

## Fields

1. **drop**: `true` only for a section that says nothing reusable: a list of technical
   requirements, "Questions", "Further reading", a page of advertising. Give `drop_reason` in a
   few words. In doubt, keep it. A chapter introduction or a chapter summary is kept: it answers
   the broad question ("how do I write a driver for X") that no single section answers; its
   `role` says what it is, and its summary says what the chapter teaches.
2. **type**, one of:
   - `procedure`: the section tells the reader to do things in order to reach a result (a recipe,
     "setting up X", "writing the Y driver"). Fill `steps` (one line each, in the order of the
     text), `preconditions` (what must be there first, only if the text says so) and
     `verification` (how the text checks the result, with the exact command or expected output).
   - `pattern`: the section presents a design or coding solution to a recurring problem and
     discusses when to use it. Fill `problem`, `solution`, `tradeoffs` (each one to three
     sentences from the text).
   - `rule`: the section's core is a do or don't ("never…", "always…", "prefer…"). Fill
     `severity` (`must` or `should`) and `rationale`.
   - `troubleshooting`: the section explains a failure, its cause and the fix. Fill `symptoms`
     (exact error or warning text as the text quotes it, else empty), `cause` and `fix`.
   - `concept`: everything else: what something is, how it works, background.
   Most book sections are concepts. Choose another type only when the section as a whole is one.
3. **domain**, one of the given list: `cpp` for the language and its libraries, `project` for build
   systems and toolchains, `bring-up` for startup code, linker scripts and first programs on a
   board, `drivers` for peripheral drivers, `debug` for debugging and faults, `core` for the
   processor (registers, exceptions, memory model), `optimization` for performance, `rtos` for
   schedulers and concurrency on a target, `test` for testing, `general` otherwise.
4. **title**: keep it. Only fix an obvious conversion artefact (a word broken by a line break).
5. **summary**: at most 40 words, what the section claims or teaches, in the words of the text.
   Not what the section "will cover" or "explores"; say the thing itself. A dropped unit gets an
   empty summary.
6. **triggers**: two to five short phrasings a developer would type when this section answers them,
   each at most twelve words, with the identifiers and terms of the text (register names, API
   names, commands). They go into the BM25 index.
7. **body_md**: the input text as Markdown. Restore what the PDF lost: `##` for sub-headings that
   are plainly headings, `-` for bullets, `1.` numbering reattached to its item, code in fenced
   blocks with a language tag (`c`, `cpp`, `cmake`, `bash`, `asm`, `text`), tables as Markdown
   tables, hyphenated line breaks joined, paragraphs reflowed. Keep every sentence, every
   identifier and every number of the input. Do not paraphrase, shorten, reorder or complete
   anything. Drop only page furniture that slipped through (a page number alone on a line, a
   running header repeating the chapter title) and "Figure N.M:" captions whose figure is not
   there.
8. **applies_to**: only values from the given lists, and only when the text names them as its
   subject or requirement (a chapter written for the Cortex-M4 of an STM32F411 applies to
   `core: Cortex-M4`; a mention in passing does not count). Leave the lists empty when unsure.
   For a C++ book this is almost always empty.
9. **extracted**: at most three pieces of the text that stand on their own and would be found by
   a different question than the section as a whole: a pitfall and its fix inside a concept, a
   rule inside a procedure, a recipe inside a discussion. `body` is verbatim from the input;
   `type` is `troubleshooting`, `rule`, `pattern` or `concept`; `symptoms` only for
   troubleshooting. In doubt, extract nothing.
10. **confidence**: `high` when the type and summary are plainly supported, `medium` when a
    reader could choose another type, `low` when the section is a fragment (a split part, a page
    of code without prose).

## Output

One JSON object per unit, with exactly these keys and no others:

```json
{
  "id": "",
  "drop": false,
  "drop_reason": "",
  "type": "concept",
  "domain": "cpp",
  "title": "",
  "summary": "",
  "triggers": [],
  "body_md": "",
  "fields": {
    "steps": [], "preconditions": [], "verification": [],
    "problem": "", "solution": "", "tradeoffs": "",
    "severity": "", "rationale": "",
    "symptoms": [], "cause": "", "fix": ""
  },
  "applies_to": {"core": [], "toolchain": [], "tool": []},
  "extracted": [
    {"type": "troubleshooting", "title": "", "symptoms": [], "body": ""}
  ],
  "confidence": "high"
}
```

Every key is present on every unit; a field that does not apply holds its empty value. Strings
are plain text, not Markdown, except `body_md` and `extracted[].body`.

## When you work as a reader agent on a batch file

The batch file is a JSON object with `prompt` (this text), `allowed` (the domain, core, toolchain
and tool lists) and `units` (a list of `{id, title, book, chapter, role, body}`). Write a JSON
array with one output object per unit, in the order of the batch, to the output path you were
given, and check that it parses. Keep scratch files in a folder named after your batch, never in
a shared root. Do not run any tool other than reading the batch and writing the output; no network
access. Report: units read, units dropped, counts by type and by confidence, and anything odd.

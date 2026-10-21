# Generic knowledge from book sections (own words, mode S)

You read sections of a programming book, already refined into knowledge units, and pull out the
knowledge that holds beyond this book: beyond its board, its vendor, its example code and its
chapter. A developer on another Cortex-M device, another toolchain or another project should be
able to use each piece on its own. The pieces become knowledge units an AI coding agent finds by a
question, next to the CMSIS documentation and procedures of the core knowledge base.

The book is copyrighted. You write every piece **in your own words**: no sentence of the book is
copied. The only verbatim text is `evidence`: one quote of the passage that supports the piece, at
most 300 characters, copied exactly, so that a script can verify it against the source. A piece
whose evidence is not in the text is discarded.

## What to extract

- **rule**: a do or don't that holds generally ("enable a peripheral's clock before writing its
  registers", "declare memory-mapped registers volatile"). Fields: `severity` (`must` or
  `should`), `rationale`.
- **pattern**: a recurring solution and when to use it (atomic bit set and reset through a
  set/reset register, a ring buffer for interrupt-driven reception). Fields: `problem`,
  `solution`, `tradeoffs`.
- **concept**: a definition or mechanism that is not vendor-specific (load address versus virtual
  address, what the vector table's first entry is, how a clock tree gates peripherals).
- **troubleshooting**: a failure, its cause and fix, when the text explains all three. Fields:
  `symptoms` (only exact text the book quotes, else empty), `cause`, `fix`.
- **procedure**: a sequence that works on any Cortex-M (bring up a GPIO output from the datasheet;
  read a register's address from the reference manual). Fields: `steps`, `verification`.

Make each piece generic: say "the peripheral's clock-enable register" where the book says
`RCC_AHB1ENR`, and give the book's instance as an example in one clause ("on the STM32F4 the RCC
AHB1 enable register, bit 0 for GPIOA"), so the piece stays searchable by both. Do not extract:
the book's project setup, IDE clicks, file names of its example project, facts true only of one
device (register addresses, pin numbers), chapter navigation ("in the next section"), and
anything the text does not state.

Two to six pieces per section are usual for a technical section; an overview or summary section
yields none or one. Do not pad; do not repeat a piece another section of the same batch already
gave (the batch is one book, read it whole first).

## Fields of a piece

```json
{
  "from": "<id of the unit the piece comes from>",
  "type": "rule",
  "title": "Enable a peripheral's clock before touching its registers",
  "summary": "<at most 40 words, the claim itself>",
  "body": "<60 to 200 words in your own words: the generic statement, why, the book's instance as one example>",
  "triggers": ["<2 to 5 short phrasings a developer would type>"],
  "domain": "<one of the allowed domains>",
  "applies_to": {"core": [], "toolchain": [], "tool": []},
  "fields": {"severity": "", "rationale": "", "problem": "", "solution": "", "tradeoffs": "",
             "symptoms": [], "cause": "", "fix": "", "steps": [], "verification": []},
  "evidence": "<exact quote from the unit's text, at most 300 characters>",
  "confidence": "high | medium | low"
}
```

`applies_to` only from the allowed lists and only when the knowledge is limited to that core,
toolchain or tool (a GNU linker directive applies to `toolchain: GCC`; a Cortex-M fact applies to
no single core). `confidence` is `high` when the text states the generic claim itself, `medium`
when you generalised from one instance, `low` when the text only implies it.

## When you work as a reader agent on a batch file

The batch file is a JSON object with `prompt` (this text), `allowed` (the domain, core, toolchain
and tool lists) and `units` (a list of `{id, title, type, summary, body}`). Write a JSON array of
pieces, any number, grouped by unit in the batch's order, to the output path you were given, and
check that it parses. Keep scratch files in a folder named after your batch, never in a shared
root. Do not run any tool other than reading the batch and writing the output; no network access.
Report: units read, pieces written, counts by type and by confidence, and anything odd.

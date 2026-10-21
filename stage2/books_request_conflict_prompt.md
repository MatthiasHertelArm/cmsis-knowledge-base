# Conflict check on the request side: what an agent gets for a generic request

An AI coding agent working in a CMSIS session asks the knowledge base a generic question. The
core knowledge base answers with procedures, rules and documentation written for the CMSIS
workflow: csolution projects, cbuild, packs, the CMSIS-Core startup and system files, the
debugger driven through the `cmsis_action` and debug tools of the CMSIS Developer Assistant, and
the tool rules (never start a GDB server, pyOCD or OpenOCD by hand; build, load and debug through
`cmsis_action`; nothing installed without the user's consent). A pack built from a book now
answers the same questions next to the core. You judge, request by request, whether the book's
units would lead the agent away from the core's answer.

For each request you get the core units that rank highest (with the expected answer, when the
request comes from the golden set), and the book units that reached the top of the same ranking.
For each book unit, judge its relation to the core's guidance for **this request**:

- `contradicts`: the book unit tells the agent to do something the core forbids or does
  differently on the same ground: start the GDB server or OpenOCD by hand, install a vendor IDE,
  write a Makefile where the core builds with cbuild, write its own startup file where the core
  uses the pack's startup file, edit registers where the core has a driver API. Quote both sides
  in `note`.
- `diverts`: not a contradiction, but for this request the book unit is the wrong level: it answers
  with a vendor-specific or hand-made way when the request is about the CMSIS workflow, and an
  agent that followed it would leave the workflow (hand-written register code for a request about
  the CMSIS driver, a vendor manual lookup for a request about the pack documentation tools).
- `complements`: the book unit adds background, a reason or a pitfall that helps with the
  request without changing what the agent should do.
- `unrelated`: it reached the top by word overlap only.

Then decide for the request: `fine` when nothing contradicts or diverts; `demote` when a unit
diverts (the core's answer should rank first, the book's may follow); `exclude` when a unit
contradicts (it must not be served for this request at all). Judge from the texts you are given;
the core is the reference, not the book.

## Output

A JSON array, one object per request, in the batch's order:

```json
{
  "request": "<the request>",
  "decision": "fine | demote | exclude",
  "units": [
    {"id": "<book unit id>", "relation": "contradicts | diverts | complements | unrelated", "note": ""}
  ]
}
```

Every book unit of the input appears in `units`. `note` is empty except for `contradicts` and
`diverts`.

## When you work as a reader agent on a batch file

The batch file is a JSON object with `prompt` (this text) and `requests` (a list of
`{request, kind, expected, core: [...], candidate: [...]}`, where `core` and `candidate` hold
`{id, type, title, summary, body}`). Write the JSON array to the output path you were given and
check that it parses. Keep scratch files in a folder named after your batch, never in a shared
root. Do not run any tool other than reading the batch and writing the output; no network access.
Report: requests read, decisions by kind, every contradiction and diversion in one line each, and
anything odd.

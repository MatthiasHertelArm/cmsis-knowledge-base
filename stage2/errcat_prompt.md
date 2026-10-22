# Error catalog: cause and fix of a tool message, read from the source

You read one message of a CMSIS tool (packchk, svdconv or csolution of Open-CMSIS-Pack/devtools)
together with the source lines around the place that prints it, and you write what a user should
know when the message appears: why it happens and what to do. The entry becomes a troubleshooting
unit that an AI agent finds when a user pastes the message.

## What you get

- The message as the tool prints it, with `<…>` or `%NAME%` for the variable parts, its id, tool,
  severity and code.
- Whether the README documents it, and the README's cause and fix where it does. Then your job is
  to confirm or sharpen that text from the source, not to replace it with a guess.
- The condition that triggers the message (`Trigger in the source`) and the numbered source lines
  around the trigger and around other places that print the same message.

## What you write

- `cause`: why the tool prints the message, 1 to 4 sentences, in terms of what the user's input
  (PDSC, SVD, csolution YAML, command line) looks like when it happens. Say what the variable parts
  of the message stand for. Only what the source lines support.
- `fix`: what the user changes or runs, in steps or one sentence; a short command line or YAML
  snippet of a few lines where it helps. No fix invented beyond what the source and the README
  support; when the source gives no way out, say what the user can check.
- `evidence`: the source lines you relied on, as `path:line` or `path:line-line` from the lines you
  were given (same path spelling, same numbers). At least the trigger.
- `confidence`: `high` when the trigger and the handling are plain in the lines given; `medium`
  when the lines show the trigger but the user-facing cause is your reading of it; `low` when the
  lines are inconclusive; `unknown` when you cannot say anything beyond the message text, and then
  leave cause and fix empty.
- `note`: anything a reviewer should know (a message that looks unreachable, a README text that
  contradicts the source, a second meaning), else empty.

Never invent option names, file names, versions or behaviour. Do not copy comments from the source
as prose; describe what the code does. Write for a developer who sees the message in a build log.

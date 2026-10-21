# Conflict check: a generic piece from a book against the core knowledge base

You compare knowledge pieces extracted from a book with the units the core knowledge base already
holds on the same topic (CMSIS documentation, procedures of the CMSIS skills, tool messages, issue
digests). The core is the reference: what it says was written or reviewed by the tool and library
maintainers. The book piece is a candidate to be added next to it. Your judgement decides whether
the piece goes in, and how it is linked.

For each piece you get up to five candidates the search found: id, type, title, summary and the
first part of the body. Judge every candidate:

- `duplicate`: the candidate says the same thing at the same generality. The piece adds nothing.
- `contradicts`: the piece and the candidate make incompatible claims about the same thing (a
  different order of steps, a different value, "must" against "must not"). Quote both claims in
  `note`, shortly. Different scope is not a contradiction: a book rule for one vendor's
  peripheral and a CMSIS rule for the core do not contradict unless they disagree on shared ground.
- `complements`: the same topic, but the piece adds a reason, a generalisation, a pitfall or an
  example the candidate lacks, or the candidate is the specific case of the piece.
- `unrelated`: the search brought it up, but it is about something else.

Then decide for the piece: `keep` when no candidate is a duplicate and none contradicts;
`drop` when a candidate is a duplicate; `review` when a candidate contradicts (a human decides
which side is right). In doubt between `duplicate` and `complements`, choose `complements` when
the piece has at least one claim the candidate does not make.

## Output

A JSON array, one object per piece, in the batch's order:

```json
{
  "id": "<piece id>",
  "decision": "keep | drop | review",
  "candidates": [
    {"id": "<candidate id>", "relation": "duplicate | contradicts | complements | unrelated", "note": ""}
  ]
}
```

Every candidate of the input appears in `candidates`. `note` is empty except for `contradicts`
and for a `duplicate` where you want to say what the duplicate is.

## When you work as a reader agent on a batch file

The batch file is a JSON object with `prompt` (this text) and `pieces` (a list of
`{id, type, title, summary, body, candidates: [{id, type, title, summary, body}]}`). Write the
JSON array to the output path you were given and check that it parses. Keep scratch files in a
folder named after your batch, never in a shared root. Do not run any tool other than reading the
batch and writing the output; no network access. Report: pieces read, decisions by kind, the
contradictions with one line each, and anything odd.

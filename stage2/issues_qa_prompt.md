# Issue digest check: does the digest say only what the thread supports?

Each item of your batch holds a `digest` (written by another reader from a GitHub thread, in its own
words, for a knowledge base that AI agents use to fix CMSIS tool problems) and the `thread` it was
written from (title, body, comments; truncated to 4000/1500 characters when the digest was
written, so judge against exactly this text).

A first check of 80 digests found these faults, most common first: invented versions, dates or
releases; extra workarounds or steps the thread never mentions; "fixed in release" where the thread
only shows a pull request, a nightly or a guess; mechanisms the thread does not give; guesses stated
as fact; a few claims that contradict the thread; symptom lines that are not in the thread text.

For each item write:

- `verdict`: `supported` (cause, fix, versions and resolution follow from the thread), `partly` (the
  core is right but some claim is not in the thread), or `unsupported` (cause or fix is not what the
  thread says, or the thread has no resolution).
- `problems`: short list of the claims that go beyond or against the thread; empty when supported.
- `symptoms_ok`: true when every symptom line appears in the thread as tool output (redacted paths or
  serial numbers are fine).
- For `partly` and `unsupported` only:
  - `cause_fixed`, `fix_fixed`: the digest's cause and fix rewritten to say only what the thread
    supports, keeping the digest's own wording where it is right (never copy the thread's prose);
    both `""` when the thread supports no usable cause or fix, and the entry will be dropped.
  - `versions_fixed`: the versions the thread names, or `""`.
  - `resolution_fixed`: one of fixed-in-release, workaround, user-error, not-a-bug, configuration,
    unresolved — what the thread supports.
- For `supported`, leave the four `*_fixed` fields out.

Write a JSON array, one object per item in input order, each starting with `issue` (the digest's URL),
to the output file you are given, and check that it parses. Read the batch in chunks. Keep helper
files only in your own scratch folder. No network, no tools other than reading and writing files.
Report the counts per verdict and the kinds of problems found.

---
id: "intr-tracking-firmware-code-size-determining-the-storage"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size / Determining the Storage"
summary: "In my opinion, storing the code size data somewhere useful is the most difficult problem to solve. This is because firmware teams are comprised of firmware engineers with a firmware background and limited web or devops experience."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#determining-the-storage"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How to Track Code Size_

In my opinion, storing the code size data somewhere useful is the most difficult
problem to solve. This is because firmware teams are comprised of firmware
engineers with a firmware background and limited web or devops experience. It is
also a difficult problem because we'll be calculating and storing code sizes in
a continuous integration system and the system needs to be reliable.

I investigated some options and have listed my opinions and conclusions below.

- Persist data within a CI system (CircleCI, Jenkins, etc).
  - Storing metadata alongside builds isn't supported in most CI systems. It's
    also unreasonable to keep build metadata for every build around forever.
- Append code sizes into a Google Sheet or Airtable spreadsheet.
  - It's clever, but I imagine getting a Google "App" and authentication
    approved for use within a company organization would prove to be difficult.
    Airtable is nice, but their pricing becomes quite high after storing large
    amounts of data.
- Keep the data in the git repo using `git notes`[^git_notes] [^git_notes_post].
  - I created a prototype of this. It worked, but the complexity increased when
    storing metadata about more than one "build". Also, parallel CI machines
    could cause note merge-conflicts by pushing the notes.
  - The beautiful thing with `git notes` is that you can see the code size
    information when running `git log`, which was a nice bonus.
- Push the code size data into a proper database, such as PostgreSQL.
  - This is the approach I ultimately took. Databases are great about data
    integrity and being able to logically group the code sizes by "builds". They
    are also fast.

Regardless of what approach is taken, you likely want the ability to quickly
list or export all the historical code sizes, query for a single build (for
pull-request deltas), and be able to ensure that no duplicates exist.

If you go with the hosted database approach, which I do suggest, either ask the
devops/software team for an isolated database or check out
[ElephantSQL](https://www.elephantsql.com/) or
[Heroku Postgres](https://www.heroku.com/postgres). They both have a free
database tier and their pricing is reasonable.

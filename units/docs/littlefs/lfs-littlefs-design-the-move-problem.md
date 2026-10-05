---
id: "lfs-littlefs-design-the-move-problem"
type: "concept"
domain: "project"
title: "littlefs DESIGN: The move problem"
summary: "We have one last challenge: the move problem. Phrasing the problem is simple:"
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#the-move-problem"
license: "BSD-3-Clause"
mode: "V"
---

We have one last challenge: the move problem. Phrasing the problem is simple:

How do you atomically move a file between two directories?

In littlefs we can atomically commit to directories, but we can't create
an atomic commit that spans multiple directories. The filesystem must go
through a minimum of two distinct states to complete a move.

To make matters worse, file moves are a common form of synchronization for
filesystems. As a filesystem designed for power-loss, it's important we get
atomic moves right.

So what can we do?

- We definitely can't just let power-loss result in duplicated or lost files.
  This could easily break users' code and would only reveal itself in extreme
  cases. We were only able to be lazy about the threaded linked-list because
  it isn't user facing and we can handle the corner cases internally.

- Some filesystems propagate COW operations up the tree until a common parent
  is found. Unfortunately this interacts poorly with our threaded tree and
  brings back the issue of upward propagation of wear.

- In a previous version of littlefs we tried to solve this problem by going
  back and forth between the source and destination, marking and unmarking the
  file as moving in order to make the move atomic from the user perspective.
  This worked, but not well. Finding failed moves was expensive and required
  a unique identifier for each file.

In the end, solving the move problem required creating a new mechanism for
sharing knowledge between multiple metadata pairs. In littlefs this led to the
introduction of a mechanism called "global state".

---

Global state is a small set of state that can be updated from _any_ metadata
pair. Combining global state with metadata pairs' ability to update multiple
entries in one commit gives us a powerful tool for crafting complex atomic
operations.

How does global state work?

Global state exists as a set of deltas that are distributed across the metadata
pairs in the filesystem. The actual global state can be built out of these
deltas by xoring together all of the deltas in the filesystem.

```
 .--------.  .--------.  .--------.  .--------.  .--------.
.|        |->| gdelta |->|        |->| gdelta |->| gdelta |
||        | || 0x23   | ||        | || 0xff   | || 0xce   |
||        | ||        | ||        | ||        | ||        |
|'--------' |'--------' |'--------' |'--------' |'--------'
'--------'  '----|---'  '--------'  '----|---'  '----|---'
                 v                       v           v
       0x00 --> xor ------------------> xor ------> xor --> gstate 0x12
```

To update the global state from a metadata pair, we take the global state we
know and xor it with both our changes and any existing delta in the metadata
pair. Committing this new delta to the metadata pair commits the changes to
the filesystem's global state.

```
 .--------.  .--------.  .--------.  .--------.  .--------.
.|        |->| gdelta |->|        |->| gdelta |->| gdelta |
||        | || 0x23   | ||        | || 0xff   | || 0xce   |
||        | ||        | ||        | ||        | ||        |
|'--------' |'--------' |'--------' |'--------' |'--------'
'--------'  '----|---'  '--------'  '--|---|-'  '----|---'
                 v                     v   |         v
       0x00 --> xor ----------------> xor -|------> xor --> gstate = 0x12
                                           |                          |
                                           |                          |
change gstate to 0xab --> xor <------------|--------------------------'
=>                         |               v
                           '------------> xor
                                           |
                                           v
 .--------.  .--------.  .--------.  .--------.  .--------.
.|        |->| gdelta |->|        |->| gdelta |->| gdelta |
||        | || 0x23   | ||        | || 0x46   | || 0xce   |
||        | ||        | ||        | ||        | ||        |
|'--------' |'--------' |'--------' |'--------' |'--------'
'--------'  '----|---'  '--------'  '----|---'  '----|---'
                 v                       v           v
       0x00 --> xor ------------------> xor ------> xor --> gstate = 0xab
```

To make this efficient, we always keep a copy of the global state in RAM. We
only need to iterate over our metadata pairs and build the global state when
the filesystem is mounted.

You may have noticed that global state is very expensive. We keep a copy in
RAM and a delta in an unbounded number of metadata pairs. Even if we reset
the global state to its initial value, we can't easily clean up the deltas on
disk. For this reason, it's very important that we keep the size of global
state bounded and extremely small. But, even with a strict budget, global
state is incredibly valuable.

---

Now we can solve the move problem. We can create global state describing our
move atomically with the creation of the new file, and we can clear this move
state atomically with the removal of the old file.

```
               .--------.    gstate = no move
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | ||        | ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '----|---'  '--------'  '--------'
       v
   .--------.
   | file D |
   |        |
   |        |
   '--------'

begin move, add reference in dir C, change gstate to have move
=>
               .--------.    gstate = moving file D in dir A (m1)
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | ||        | || gdelta |
  ||        | ||        | || =m1    |
  |'--------' |'--------' |'--------'
  '----|---'  '--------'  '----|---'
       |     .----------------'
       v    v
     .--------.
     | file D |
     |        |
     |        |
     '--------'

complete move, remove reference in dir A, change gstate to no move
=>
               .--------.    gstate = no move (m1^~m1)
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  || gdelta | ||        | || gdelta |
  || =~m1   | ||        | || =m1    |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '----|---'
                               v
                           .--------.
                           | file D |
                           |        |
                           |        |
                           '--------'
```


If, after building our global state during mount, we find information
describing an ongoing move, we know we lost power during a move and the file
is duplicated in both the source and destination directories. If this happens,
we can resolve the move using the information in the global state to remove
one of the files.

```
                 .--------.    gstate = moving file D in dir A (m1)
                .| root   |-.             ^
                ||        |------------> xor
.---------------||        |-'             ^
|               |'--------'               |
|               '--|-|-|-'                |
|        .--------'  |  '---------.       |
|       |            |             |      |
|       |     .----------> xor --------> xor
|       v     |      v      ^      v      ^
|  .--------. |  .--------. |  .--------. |
'->| dir A  |-|->| dir B  |-|->| dir C  | |
  ||        |-' ||        |-' || gdelta |-'
  ||        |   ||        |   || =m1    |
  |'--------'   |'--------'   |'--------'
  '----|---'    '--------'    '----|---'
       |     .---------------------'
       v    v
     .--------.
     | file D |
     |        |
     |        |
     '--------'
```

We can also move directories the same way we move files. There is the threaded
linked-list to consider, but leaving the threaded linked-list unchanged works
fine as the order doesn't really matter.

```
               .--------.    gstate = no move (m1^~m1)
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  || gdelta | ||        | || gdelta |
  || =~m1   | ||        | || =m1    |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '----|---'
                               v
                           .--------.
                           | file D |
                           |        |
                           |        |
                           '--------'

begin move, add reference in dir C, change gstate to have move
=>
                .--------.    gstate = moving dir B in root (m1^~m1^m2)
               .| root   |-.
               ||        | |
.--------------||        |-'
|              |'--------'
|              '--|-|-|-'
|        .-------'  |  '----------.
|       v           |              v
|  .--------.       |          .--------.
'->| dir A  |-.     |       .->| dir C  |
  || gdelta | |     |       | || gdelta |
  || =~m1   | |     |       | || =m1^m2 |
  |'--------' |     |       | |'--------'
  '--------'  |     |       | '---|--|-'
              |     |    .-------'   |
              |     v   v   |        v
              |  .--------. |    .--------.
              '->| dir B  |-'    | file D |
                ||        |      |        |
                ||        |      |        |
                |'--------'      '--------'
                '--------'

complete move, remove reference in root, change gstate to no move
=>
             .--------.    gstate = no move (m1^~m1^m2^~m2)
            .| root   |-.
            || gdelta | |
.-----------|| =~m2   |-'
|           |'--------'
|           '---|--|-'
|        .-----'    '-----.
|       v                  v
|  .--------.          .--------.
'->| dir A  |-.     .->| dir C  |
  || gdelta | |     | || gdelta |
  || =~m1   | |     '-|| =m1^m2 |-------.
  |'--------' |       |'--------'       |
  '--------'  |       '---|--|-'        |
              |        .-'    '-.       |
              |       v          v      |
              |  .--------.  .--------. |
              '->| dir B  |--| file D |-'
                ||        |  |        |
                ||        |  |        |
                |'--------'  '--------'
                '--------'
```

Global state gives us a powerful tool we can use to solve the move problem.
And the result is surprisingly performant, only needing the minimum number
of states and using the same number of commits as a naive move. Additionally,
global state gives us a bit of persistent state we can use for some other
small improvements.

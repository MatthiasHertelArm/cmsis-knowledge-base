---
id: "lfs-littlefs-design-ctz-skip-lists"
type: "concept"
domain: "project"
title: "littlefs DESIGN: CTZ skip-lists"
summary: "Metadata pairs provide efficient atomic updates but unfortunately have a large storage cost. But we can work around this storage cost by only using the metadata pairs to store references to more dense, copy-on-write (COW) data structures."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#ctz-skip-lists"
license: "BSD-3-Clause"
mode: "V"
---

Metadata pairs provide efficient atomic updates but unfortunately have a large
storage cost. But we can work around this storage cost by only using the
metadata pairs to store references to more dense, copy-on-write (COW) data
structures.

[Copy-on-write data structures][wikipedia-cow], also called purely functional
data structures, are a category of data structures where the underlying
elements are immutable.  Making changes to the data requires creating new
elements containing a copy of the updated data and replacing any references
with references to the new elements. Generally, the performance of a COW data
structure depends on how many old elements can be reused after replacing parts
of the data.

littlefs has several requirements of its COW structures. They need to be
efficient to read and write, but most frustrating, they need to be traversable
with a constant amount of RAM. Notably this rules out
[B-trees][wikipedia-B-tree], which can not be traversed with constant RAM, and
[B+-trees][wikipedia-B+-tree], which are not possible to update with COW
operations.

---

So, what can we do? First let's consider storing files in a simple COW
linked-list. Appending a block, which is the basis for writing files, means we
have to update the last block to point to our new block. This requires a COW
operation, which means we need to update the second-to-last block, and then the
third-to-last, and so on until we've copied out the entire file.

```
A linked-list
.--------.  .--------.  .--------.  .--------.  .--------.  .--------.
| data 0 |->| data 1 |->| data 2 |->| data 4 |->| data 5 |->| data 6 |
|        |  |        |  |        |  |        |  |        |  |        |
|        |  |        |  |        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'  '--------'
```

To avoid a full copy during appends, we can store the data backwards. Appending
blocks just requires adding the new block and no other blocks need to be
updated. If we update a block in the middle, we still need to copy the
following blocks, but can reuse any blocks before it. Since most file writes
are linear, this design gambles that appends are the most common type of data
update.

```
A backwards linked-list
.--------.  .--------.  .--------.  .--------.  .--------.  .--------.
| data 0 |<-| data 1 |<-| data 2 |<-| data 4 |<-| data 5 |<-| data 6 |
|        |  |        |  |        |  |        |  |        |  |        |
|        |  |        |  |        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'  '--------'
```

However, a backwards linked-list does have a rather glaring problem. Iterating
over a file _in order_ has a runtime cost of _O(n²)_. A quadratic runtime
just to read a file! That's awful.

Fortunately we can do better. Instead of a singly linked list, littlefs
uses a multilayered linked-list often called a
[skip-list][wikipedia-skip-list]. However, unlike the most common type of
skip-list, littlefs's skip-lists are strictly deterministic built around some
interesting properties of the count-trailing-zeros (CTZ) instruction.

The rules CTZ skip-lists follow are that for every _n_‍th block where _n_
is divisible by 2‍_ˣ_, that block contains a pointer to block
_n_-2‍_ˣ_. This means that each block contains anywhere from 1 to
log₂_n_ pointers that skip to different preceding elements of the
skip-list.

The name comes from heavy use of the [CTZ instruction][wikipedia-ctz], which
lets us calculate the power-of-two factors efficiently. For a given block _n_,
that block contains ctz(_n_)+1 pointers.

```
A backwards CTZ skip-list
.--------.  .--------.  .--------.  .--------.  .--------.  .--------.
| data 0 |<-| data 1 |<-| data 2 |<-| data 3 |<-| data 4 |<-| data 5 |
|        |<-|        |--|        |<-|        |--|        |  |        |
|        |<-|        |--|        |--|        |--|        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'  '--------'
```

The additional pointers let us navigate the data-structure on disk much more
efficiently than in a singly linked list.

Consider a path from data block 5 to data block 1. You can see how data block 3
was completely skipped:
```
.--------.  .--------.  .--------.  .--------.  .--------.  .--------.
| data 0 |  | data 1 |<-| data 2 |  | data 3 |  | data 4 |<-| data 5 |
|        |  |        |  |        |<-|        |--|        |  |        |
|        |  |        |  |        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'  '--------'
```

The path to data block 0 is even faster, requiring only two jumps:
```
.--------.  .--------.  .--------.  .--------.  .--------.  .--------.
| data 0 |  | data 1 |  | data 2 |  | data 3 |  | data 4 |<-| data 5 |
|        |  |        |  |        |  |        |  |        |  |        |
|        |<-|        |--|        |--|        |--|        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'  '--------'
```

We can find the runtime complexity by looking at the path to any block from
the block containing the most pointers. Every step along the path divides
the search space for the block in half, giving us a runtime of _O(log n)_.
To get _to_ the block with the most pointers, we can perform the same steps
backwards, which puts the runtime at _O(2 log n)_ = _O(log n)_. An interesting
note is that this optimal path occurs naturally if we greedily choose the
pointer that covers the most distance without passing our target.

So now we have a [COW] data structure that is cheap to append with a runtime
of _O(1)_, and can be read with a worst case runtime of _O(n log n)_. Given
that this runtime is also divided by the amount of data we can store in a
block, this cost is fairly reasonable.

---

This is a new data structure, so we still have several questions. What is the
storage overhead? Can the number of pointers exceed the size of a block? How do
we store a CTZ skip-list in our metadata pairs?

To find the storage overhead, we can look at the data structure as multiple
linked-lists. Each linked-list skips twice as many blocks as the previous,
or from another perspective, each linked-list uses half as much storage as
the previous. As we approach infinity, the storage overhead forms a geometric
series. Solving this tells us that on average our storage overhead is only
2 pointers per block.

![lim,n->inf((1/n)sum,i,0->n(ctz(i)+1)) = sum,i,0->inf(1/2^i) = 2][ctz-formula1]

Because our file size is limited the word width we use to store sizes, we can
also solve for the maximum number of pointers we would ever need to store in a
block. If we set the overhead of pointers equal to the block size, we get the
following equation. Note that both a smaller block size (![B][bigB]) and larger
word width (![w]) result in more storage overhead.

![B = (w/8)ceil(log2(2^w / (B-2w/8)))][ctz-formula2]

Solving the equation for ![B][bigB] gives us the minimum block size for some
common word widths:

1. 32-bit CTZ skip-list => minimum block size of 104 bytes
2. 64-bit CTZ skip-list => minimum block size of 448 bytes

littlefs uses a 32-bit word width, so our blocks can only overflow with
pointers if they are smaller than 104 bytes. This is an easy requirement, as
in practice, most block sizes start at 512 bytes. As long as our block size
is larger than 104 bytes, we can avoid the extra logic needed to handle
pointer overflow.

This last question is how do we store CTZ skip-lists? We need a pointer to the
head block, the size of the skip-list, the index of the head block, and our
offset in the head block. But it's worth noting that each size maps to a unique
index + offset pair. So in theory we can store only a single pointer and size.

However, calculating the index + offset pair from the size is a bit
complicated. We can start with a summation that loops through all of the blocks
up until our given size. Let ![B][bigB] be the block size in bytes, ![w] be the
word width in bits, ![n] be the index of the block in the skip-list, and
![N][bigN] be the file size in bytes:

![N = sum,i,0->n(B-(w/8)(ctz(i)+1))][ctz-formula3]

This works quite well, but requires _O(n)_ to compute, which brings the full
runtime of reading a file up to _O(n² log n)_. Fortunately, that summation
doesn't need to touch the disk, so the practical impact is minimal.

However, despite the integration of a bitwise operation, we can actually reduce
this equation to a _O(1)_ form.  While browsing the amazing resource that is
the [On-Line Encyclopedia of Integer Sequences (OEIS)][oeis], I managed to find
[A001511], which matches the iteration of the CTZ instruction,
and [A005187], which matches its partial summation. Much to my
surprise, these both result from simple equations, leading us to a rather
unintuitive property that ties together two seemingly unrelated bitwise
instructions:

![sum,i,0->n(ctz(i)+1) = 2n-popcount(n)][ctz-formula4]

where:

1. ctz(![x]) = the number of trailing bits that are 0 in ![x]
2. popcount(![x]) = the number of bits that are 1 in ![x]

Initial tests of this surprising property seem to hold. As ![n] approaches
infinity, we end up with an average overhead of 2 pointers, which matches our
assumption from earlier. During iteration, the popcount function seems to
handle deviations from this average. Of course, just to make sure I wrote a
quick script that verified this property for all 32-bit integers.

Now we can substitute into our original equation to find a more efficient
equation for file size:

![N = Bn - (w/8)(2n-popcount(n))][ctz-formula5]

Unfortunately, the popcount function is non-injective, so we can't solve this
equation for our index. But what we can do is solve for an ![n'] index that
is greater than ![n] with error bounded by the range of the popcount function.
We can repeatedly substitute ![n'] into the original equation until the error
is smaller than our integer resolution. As it turns out, we only need to
perform this substitution once, which gives us this formula for our index:

![n = floor((N-(w/8)popcount(N/(B-2w/8))) / (B-2w/8))][ctz-formula6]

Now that we have our index ![n], we can just plug it back into the above
equation to find the offset. We run into a bit of a problem with integer
overflow, but we can avoid this by rearranging the equation a bit:

![off = N - (B-2w/8)n - (w/8)popcount(n)][ctz-formula7]

Our solution requires quite a bit of math, but computers are very good at math.
Now we can find both our block index and offset from a size in _O(1)_, letting
us store CTZ skip-lists with only a pointer and size.

CTZ skip-lists give us a COW data structure that is easily traversable in
_O(n)_, can be appended in _O(1)_, and can be read in _O(n log n)_. All of
these operations work in a bounded amount of RAM and require only two words of
storage overhead per block. In combination with metadata pairs, CTZ skip-lists
provide power resilience and compact storage of data.

```
                                    .--------.
                                   .|metadata|
                                   ||        |
                                   ||        |
                                   |'--------'
                                   '----|---'
                                        v
.--------.  .--------.  .--------.  .--------.
| data 0 |<-| data 1 |<-| data 2 |<-| data 3 |
|        |<-|        |--|        |  |        |
|        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'

write data to disk, create copies
=>
                                    .--------.
                                   .|metadata|
                                   ||        |
                                   ||        |
                                   |'--------'
                                   '----|---'
                                        v
.--------.  .--------.  .--------.  .--------.
| data 0 |<-| data 1 |<-| data 2 |<-| data 3 |
|        |<-|        |--|        |  |        |
|        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'
     ^ ^           ^
     | |           |    .--------.  .--------.  .--------.  .--------.
     | |           '----| new    |<-| new    |<-| new    |<-| new    |
     | '----------------| data 2 |<-| data 3 |--| data 4 |  | data 5 |
     '------------------|        |--|        |--|        |  |        |
                        '--------'  '--------'  '--------'  '--------'

commit to metadata pair
=>
                                                            .--------.
                                                           .|new     |
                                                           ||metadata|
                                                           ||        |
                                                           |'--------'
                                                           '----|---'
                                                                |
.--------.  .--------.  .--------.  .--------.                  |
| data 0 |<-| data 1 |<-| data 2 |<-| data 3 |                  |
|        |<-|        |--|        |  |        |                  |
|        |  |        |  |        |  |        |                  |
'--------'  '--------'  '--------'  '--------'                  |
     ^ ^           ^                                            v
     | |           |    .--------.  .--------.  .--------.  .--------.
     | |           '----| new    |<-| new    |<-| new    |<-| new    |
     | '----------------| data 2 |<-| data 3 |--| data 4 |  | data 5 |
     '------------------|        |--|        |--|        |  |        |
                        '--------'  '--------'  '--------'  '--------'
```

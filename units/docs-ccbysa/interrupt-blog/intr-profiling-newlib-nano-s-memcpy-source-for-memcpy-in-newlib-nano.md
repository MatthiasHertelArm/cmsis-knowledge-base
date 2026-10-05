---
id: "intr-profiling-newlib-nano-s-memcpy-source-for-memcpy-in-newlib-nano"
type: "concept"
domain: "debug"
title: "Profiling newlib-nano's memcpy: Source for `memcpy` in Newlib-nano"
summary: "You can find the implementation of the Newlib-nano memcpy function here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-09-07-memcpy-newlib-nano.md"
doc_source: "https://interrupt.memfault.com/blog/memcpy-newlib-nano#source-for-memcpy-in-newlib-nano"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can find the implementation of the Newlib-nano `memcpy` function here:

[https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/string/memcpy.c;h=52f716b9275f5d24cedb7d66c41541945d13bfb6;hb=HEAD#l49](https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/string/memcpy.c;h=52f716b9275f5d24cedb7d66c41541945d13bfb6;hb=HEAD#l49)

If you're using the GNU Arm Embedded Toolchain, you can find the exact source
for the newlib library it ships by downloading the source tarball from the Arm
download page; for example, `gcc-arm-none-eabi-10.3-2021.07-src.tar.bz2` is the
latest at the moment.

Looking at the implementation, we can see that it's conditionally compiled in 2
different ways:

```c
void *
__inhibit_loop_to_libcall
memcpy (void *__restrict dst0,
	const void *__restrict src0,
	size_t len0)
{
#if defined(PREFER_SIZE_OVER_SPEED) || defined(__OPTIMIZE_SIZE__)
  char *dst = (char *) dst0;
  char *src = (char *) src0;

  void *save = dst0;

  while (len0--)
    {
      *dst++ = *src++;
    }

  return save;
#else
  // this section skipped for brevity
...
#endif /* not PREFER_SIZE_OVER_SPEED */
}
```

The default compilation used by the GNU Arm Embedded Toolchain is with `-O2` as
the optimization level; however, newlib is also built with `-Os` for the "nano"
variant (both are provided with the pre-built toolchain). We can check this by
looking at the source tarball, where the build script sets these CFLAGS (see
`build-toolchain.sh` line 382):

```plaintext
    saveenvvar CFLAGS_FOR_TARGET '-g -Os -ffunction-sections -fdata-sections'
```

When compiling with optimization level `-Os`, the GCC compiler will set `#define
__OPTIMIZE_SIZE__ 1` as a built-in define. You can see this by running the
following command, which dumps the built-in preprocessor definitions to stdout:

```bash
arm-none-eabi-gcc -Os -dM -E - < /dev/null

# diff between -O2 and -Os
diff -du1w <(arm-none-eabi-gcc -O2 -dM -E - < /dev/null) <(arm-none-eabi-gcc -Os -dM -E - < /dev/null)
```

```diff
@@ -317,2 +317,3 @@
 #define __UINT64_TYPE__ long long unsigned int
+#define __OPTIMIZE_SIZE__ 1
 #define __LLFRACT_MAX__ 0X7FFFFFFFFFFFFFFFP-63LLR
```

This results in the bytewise `memcpy` implementation we saw above!

```c
  while (len0--)
    {
      *dst++ = *src++;
    }
```

> An interesting side-effect of the bytewise implementation I've encountered: a
> program used structure assignment to initialize a set of 32-bit hardware
> registers. This was problematic when the compiler inserted a bytewise memcpy,
> because the registers would be written in 8-bit chunks, putting the hardware
> in an undefined state!

If we examine the other implementation (the non-size-optimized version), we can
see that it attempts to copy 4-byte words at a time, which is the native word
size on a Cortex-M processor, and should speed things up a lot!

```c
  /* If the size is small, or either SRC or DST is unaligned,
     then punt into the byte copy loop.  This should be rare.  */
  if (!TOO_SMALL(len0) && !UNALIGNED (src, dst))
    {
      aligned_dst = (long*)dst;
      aligned_src = (long*)src;

      /* Copy 4X long words at a time if possible.  */
      while (len0 >= BIGBLOCKSIZE)
        {
          *aligned_dst++ = *aligned_src++;
          *aligned_dst++ = *aligned_src++;
          *aligned_dst++ = *aligned_src++;
          *aligned_dst++ = *aligned_src++;
          len0 -= BIGBLOCKSIZE;
        }

      /* Copy one long word at a time if possible.  */
      while (len0 >= LITTLEBLOCKSIZE)
        {
          *aligned_dst++ = *aligned_src++;
          len0 -= LITTLEBLOCKSIZE;
        }

       /* Pick up any residual with a byte copier.  */
      dst = (char*)aligned_dst;
      src = (char*)aligned_src;
    }

  while (len0--)
    *dst++ = *src++;
```

Note that some chips will have multiple-load-store or other SIMD/vector
instructions that can possibly speed up the loops even more (though it's always
important to profile when playing with compiler optimizations).

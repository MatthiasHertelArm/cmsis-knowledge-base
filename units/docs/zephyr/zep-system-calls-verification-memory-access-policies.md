---
id: "zep-system-calls-verification-memory-access-policies"
type: "concept"
domain: "rtos"
title: "System Calls: Verification Function / Verification Memory Access Policies"
summary: "Parameters passed to system calls by reference require special handling, because the value of these parameters can be changed at any time by any user thread that has access to the memory that parameter points to."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Verification Function_

Parameters passed to system calls by reference require special handling,
because the value of these parameters can be changed at any time by any
user thread that has access to the memory that parameter points to. If the
kernel makes any logical decisions based on the contents of this memory, this
can open up the kernel to attacks even if checking is done. This is a class
of exploits known as TOCTOU (Time Of Check to Time Of Use).

The proper procedure to mitigate these attacks is to make a copies in the
verification function, and only perform parameter checks on the copies, which
user threads will never have access to. The implementation functions get passed
the copy and not the original data sent by the user. The
`k_usermode_to_copy()` and `k_usermode_from_copy()` APIs exist for
this purpose.

C strings passed from user mode need similar care, since their length is not
known in advance and the terminating `NUL` must be located without reading
past memory the caller can access. The `k_usermode_string_copy()` and
`k_usermode_string_alloc_copy()` helpers safely validate and copy a
user-supplied string into kernel-controlled memory before it is used by the
implementation function.

There is one exception in place, with respect to large data buffers which are
only used to provide a memory area that is either only written to, or whose
contents are never used for any validation or control flow. Further
discussion of this later in this section.

As a first example, consider a parameter which is used as an output parameter
for some integral value:


```c

int z_vrfy_some_syscall(int *out_param)
{
    int local_out_param;
    int ret;

    ret = z_impl_some_syscall(&local_out_param);
    K_OOPS(k_usermode_to_copy(out_param, &local_out_param, sizeof(*out_param)));
    return ret;
}
```
Here we have allocated `local_out_param` on the stack, passed its address to
the implementation function, and then used `k_usermode_to_copy()` to fill
in the memory passed in by the caller.

It might be tempting to do something more concise:

```c

int z_vrfy_some_syscall(int *out_param)
{
    K_OOPS(K_SYSCALL_MEMORY_WRITE(out_param, sizeof(*out_param)));
    return z_impl_some_syscall(out_param);
}
```
However, this is unsafe if the implementation ever does any reads to this
memory as part of its logic. For example, it could be used to store some
counter value, and this could be meddled with by user threads that have access
to its memory. It is by far safest for small integral values to do the copying
as shown in the first example.

Some parameters may be input/output. For instance, it's not uncommon to see APIs
which pass in a pointer to some `size_t` which is a maximum allowable size,
which is then updated by the implementation to reflect the actual number of
bytes processed. This too should use a stack copy:

```c

int z_vrfy_in_out_syscall(size_t *size_ptr)
{
    size_t size;
    int ret;

    K_OOPS(k_usermode_from_copy(&size, size_ptr, sizeof(size));
    ret = z_impl_in_out_syscall(&size);
    K_OOPS(k_usermode_to_copy(size_ptr, &size, sizeof(size)));
    return ret;
}
```
Many system calls pass in structures or even linked data structures. All should
be copied. Typically this is done by allocating copies on the stack:

```c

struct bar {
    ...
};

struct foo {
    ...
    struct bar *bar_left;
    struct bar *bar_right;
};

int z_vrfy_must_alloc(struct foo *foo)
{
    int ret;
    struct foo foo_copy;
    struct bar bar_right_copy;
    struct bar bar_left_copy;

    K_OOPS(k_usermode_from_copy(&foo_copy, foo, sizeof(*foo)));
    K_OOPS(k_usermode_from_copy(&bar_right_copy, foo_copy.bar_right,
                            sizeof(struct bar)));
    foo_copy.bar_right = &bar_right_copy;
    K_OOPS(k_usermode_from_copy(&bar_left_copy, foo_copy.bar_left,
                            sizeof(struct bar)));
    foo_copy.bar_left = &bar_left_copy;

    return z_impl_must_alloc(&foo_copy);
}
```
In some cases the amount of data isn't known at compile time or may be too
large to allocate on the stack. In this scenario, it may be necessary to draw
memory from the caller's resource pool via `z_thread_malloc()`. This
should always be considered last resort. Functional safety programming
guidelines heavily discourage usage of heap and the fact that a resource pool is
used must be clearly documented. Any issues with allocation must be
reported, to a caller, with returning the `-ENOMEM` . The `K_OOPS()`
should never be used to verify if resource allocation has been successful.

```c

struct bar {
    ...
};

struct foo {
    size_t count;
    struct bar *bar_list; /* array of struct bar of size count */
};

int z_vrfy_must_alloc(struct foo *foo)
{
    int ret;
    struct foo foo_copy;
    struct bar *bar_list_copy;
    size_t bar_list_bytes;

    /* Safely copy foo into foo_copy */
    K_OOPS(k_usermode_from_copy(&foo_copy, foo, sizeof(*foo)));

    /* Bounds check the count member, in the copy we made */
    if (foo_copy.count > 32) {
        return -EINVAL;
    }

    /* Allocate RAM for the bar_list, replace the pointer in
     * foo_copy */
    bar_list_bytes = foo_copy.count * sizeof(struct_bar);
    bar_list_copy = z_thread_malloc(bar_list_bytes);
    if (bar_list_copy == NULL) {
        return -ENOMEM;
    }
    K_OOPS(k_usermode_from_copy(bar_list_copy, foo_copy.bar_list,
                            bar_list_bytes));
    foo_copy.bar_list = bar_list_copy;

    ret = z_impl_must_alloc(&foo_copy);

    /* All done with the memory, free it and return */
    k_free(foo_copy.bar_list_copy);
    return ret;
}
```
Finally, we must consider large data buffers. These represent areas of user
memory which either have data copied out of, or copied into. It is permitted
to pass these pointers to the implementation function directly. The caller's
access to the buffer still must be validated with `K_SYSCALL_MEMORY` APIs.
The following constraints need to be met:

 * If the buffer is used by the implementation function to write data, such
   as data captured from some MMIO region, the implementation function must
   only write this data, and never read it.

 * If the buffer is used by the implementation function to read data, such
   as a block of memory to write to some hardware destination, this data
   must be read without any processing. No conditional logic can be implemented
   due to the data buffer's contents. If such logic is required a copy must be
   made.

 * The buffer must only be used synchronously with the call. The implementation
   must not ever save the buffer address and use it asynchronously, such as
   when an interrupt fires.

```c

int z_vrfy_get_data_from_kernel(void *buf, size_t size)
{
    K_OOPS(K_SYSCALL_MEMORY_WRITE(buf, size));
    return z_impl_get_data_from_kernel(buf, size);
}
```

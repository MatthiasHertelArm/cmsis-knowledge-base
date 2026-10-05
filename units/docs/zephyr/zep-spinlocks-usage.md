---
id: "zep-spinlocks-usage"
type: "concept"
domain: "rtos"
title: "Spinlocks: Usage"
summary: "Declare a k_spinlock for each independent resource you need to protect. Acquire it with k_spin_lock, which returns a k_spinlock_key_t that must be passed back to k_spin_unlock to release the lock:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/spinlocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/spinlocks.rst"
license: "Apache-2.0"
mode: "V"
---

Declare a `k_spinlock` for each independent resource you need to protect. Acquire it with
`k_spin_lock`, which returns a `k_spinlock_key_t` that must be passed back to
`k_spin_unlock` to release the lock:

```c

static struct k_spinlock lock;

void update_shared_state(void)
{
        k_spinlock_key_t key = k_spin_lock(&lock);

        /* critical section: exclusive access */

        k_spin_unlock(&lock, key);
}
```
The `K_SPINLOCK` helper acquires the lock for the duration of the
enclosed block and releases it automatically on exiting the block.

```c

K_SPINLOCK(&lock) {
        /* critical section: exclusive access */
}
```
The block must either run to its end or be left with `K_SPINLOCK_BREAK`.
Leaving it with a plain `break`, `goto` or `return` skips the release and
leaks the lock:

```c

K_SPINLOCK(&lock) {
        if (nothing_to_do) {
                K_SPINLOCK_BREAK;
        }

        /* critical section: exclusive access */
}
```

### Acquiring without spinning


`k_spin_trylock` makes a single attempt to take the lock and reports
failure instead of waiting, which is useful when the caller has other work to do
or must not stall. On success it stores the key, which is released exactly as for
`k_spin_lock`:

```c

k_spinlock_key_t key;

if (k_spin_trylock(&lock, &key) == 0) {
        /* critical section: exclusive access */
        k_spin_unlock(&lock, key);
} else {
        /* lock is held elsewhere, do something else */
}
```

### Rules


Follow these rules when using a spinlock:

* Keep the critical section as short as possible. Interrupts are masked on the
  local CPU while the lock is held, and other CPUs may be spinning on it.
* Never perform a blocking or sleeping operation while holding a spinlock.
* Do not acquire a spinlock recursively. A context that already holds a lock
  must not try to take it again, or it will deadlock. Nesting **distinct**
  spinlocks is allowed, but must follow a consistent lock ordering to avoid
  deadlock.

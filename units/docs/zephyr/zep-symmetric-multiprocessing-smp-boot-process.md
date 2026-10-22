---
id: "zep-symmetric-multiprocessing-smp-boot-process"
type: "concept"
domain: "rtos"
title: "Symmetric Multiprocessing: SMP Boot Process"
summary: "A Zephyr SMP kernel begins boot identically to a uniprocessor kernel. Auxiliary CPUs begin in a disabled state in the architecture layer. All standard kernel initialization, including device initialization, happens on a single CPU before other CPUs are brought online."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/smp/smp.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/smp/smp.rst"
license: "Apache-2.0"
mode: "V"
---

A Zephyr SMP kernel begins boot identically to a uniprocessor kernel.
Auxiliary CPUs begin in a disabled state in the architecture layer.
All standard kernel initialization, including device initialization,
happens on a single CPU before other CPUs are brought online.

Just before entering the application `main` function, the kernel
calls `z_smp_init` to launch the SMP initialization process.  This
enumerates over the configured CPUs, calling into the architecture
layer using `arch_cpu_start` for each one.  This function is
passed a memory region to use as a stack on the foreign CPU (in
practice it uses the area that will become that CPU's interrupt
stack), the address of a local `smp_init_top` callback function to
run on that CPU, and a pointer to a "start flag" address which will be
used as an atomic signal.

The local SMP initialization (`smp_init_top`) on each CPU is then
invoked by the architecture layer.  Note that interrupts are still
masked at this point.  This routine is responsible for calling
`smp_timer_init` to set up any needed stat in the timer driver.  On
many architectures the timer is a per-CPU device and needs to be
configured specially on auxiliary CPUs.  Then it waits (spinning) for
the atomic "start flag" to be released in the main thread, to
guarantee that all SMP initialization is complete before any Zephyr
application code runs, and finally calls `z_swap` to transfer
control to the appropriate runnable thread via the standard scheduler
API.

By default the kernel brings up every available CPU during this start-up
sequence. A CPU whose devicetree node carries the `zephyr,deferred-start`
flag is skipped and left disabled so that architecture, SoC, board, or
application code can start it later at run time; deferral is per CPU, so a
system may bring up some secondary CPUs at boot and leave others to be
started on demand. A deferred CPU is started with `k_smp_cpu_start`,
which performs full per-CPU initialization; `k_smp_cpu_resume` is the
counterpart used to bring a previously stopped CPU back online without
repeating one-time initialization.

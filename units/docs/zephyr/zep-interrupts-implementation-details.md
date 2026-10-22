---
id: "zep-interrupts-implementation-details"
type: "concept"
domain: "rtos"
title: "Interrupts: Implementation / Implementation Details"
summary: "Interrupt tables are set up at build time using some special build tools. The details laid out here apply to all architectures except x86, which are covered in the x86 Details section below."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

Interrupt tables are set up at build time using some special build tools.  The
details laid out here apply to all architectures except x86, which are
covered in the x86 Details section below.

The invocation of `IRQ_CONNECT` will declare an instance of
struct _isr_list which is placed in a special .intList section.
This section is placed in compiled code on precompilation stages only.
It is meant to be used by Zephyr script to generate interrupt tables
and is removed from the final build.
The script implements different parsers to process the data from .intList section
and produce the required output.

The default parser generates C arrays filled with arguments and interrupt
handlers in a form of addresses directly taken from .intList section entries.
It works with all the architectures and compilers (with the exception mentioned above).
The limitation of this parser is the fact that after the arrays are generated
it is expected for the code not to relocate.
Any relocation on this stage may lead to the situation where the entry in the interrupt array
is no longer pointing to the function that was expected.
It means that this parser, being more compatible, is limiting us from using Link Time Optimization.

The local ISR declaration parser uses a different approach to construct
the same arrays at the binary level.
All the entries to the arrays are declared and defined locally,
directly in the file where `IRQ_CONNECT` is used.
They are placed in a section with a unique, synthesized name.
The name of that section is then placed in the .intList section, which is used to
generate a linker script fragment placing the entry at the right address.
This parser is currently limited to the supported architectures and toolchains,
but in return, it preserves the information about object relations for the linker,
thus enabling Link Time Optimization.


#### Implementation using C arrays


This is the default configuration available for all Zephyr supported architectures.

Any invocation of `IRQ_CONNECT` will declare an instance of
struct _isr_list which is placed in a special .intList section:

```c

struct _isr_list {
    /** IRQ line number */
    int32_t irq;
    /** Flags for this IRQ, see ISR_FLAG_* definitions */
    int32_t flags;
    /** ISR to call */
    void *func;
    /** Parameter for non-direct IRQs */
    void *param;
};
```
Zephyr is built in two phases; the first phase of the build produces
`${ZEPHYR_PREBUILT_EXECUTABLE}`.elf which contains all the entries in
the .intList section preceded by a header:

```c

struct {
    void *spurious_irq_handler;
    void *sw_irq_handler;
    uint32_t num_isrs;
    uint32_t num_vectors;
    struct _isr_list isrs[];  <- of size num_isrs
};
```
This data consisting of the header and instances of struct _isr_list inside
`${ZEPHYR_PREBUILT_EXECUTABLE}`.elf is then used by the
gen_isr_tables.py script to generate a C file defining a vector table and
software ISR table that are then compiled and linked into the final
application.

The priority level of any interrupt is not encoded in these tables, instead
`IRQ_CONNECT` also has a runtime component which programs the desired
priority level of the interrupt to the interrupt controller. Some architectures
do not support the notion of interrupt priority, in which case the priority
argument is ignored.


##### Vector Table

A vector table is generated when `CONFIG_GEN_IRQ_VECTOR_TABLE` is
enabled.  This data structure is used natively by the CPU and is simply an
array of function pointers, where each element n corresponds to the IRQ handler
for IRQ line n, and the function pointers are:

#. For 'direct' interrupts declared with `IRQ_DIRECT_CONNECT`, the
   handler function will be placed here.
#. For regular interrupts declared with `IRQ_CONNECT`, the address
   of the common software IRQ handler is placed here. This code does common
   kernel interrupt bookkeeping and looks up the ISR and parameter from the
   software ISR table.
#. For interrupt lines that are not configured at all, the address of the
   spurious IRQ handler will be placed here. The spurious IRQ handler
   causes a system fatal error if encountered.

Some architectures have a common entry point for all interrupts and do not
support a vector table, in which case the
`CONFIG_GEN_IRQ_VECTOR_TABLE` option should be disabled.

Some architectures may reserve some initial vectors for system exceptions
and declare this in a table elsewhere, in which case
CONFIG_GEN_IRQ_START_VECTOR needs to be set to properly offset the indices
in the table.


##### SW ISR Table

This is an array of struct _isr_table_entry:

```c

struct _isr_table_entry {
    void *arg;
    void (*isr)(void *);
};
```
This is used by the common software IRQ handler to look up the ISR and its
argument and execute it. The active IRQ line is looked up in an interrupt
controller register and used to index this table.


##### Shared SW ISR Table


This is an array of struct z_shared_isr_table_entry:

```c

struct z_shared_isr_table_entry {
    struct _isr_table_entry clients[CONFIG_SHARED_IRQ_MAX_NUM_CLIENTS];
    size_t client_num;
};
```
This table keeps track of the registered clients for each of the interrupt
lines. Whenever an interrupt line becomes shared, `z_shared_isr` will
replace the currently registered ISR in _sw_isr_table. This special ISR will
iterate through the list of registered clients and invoke the ISRs.


#### Implementation using linker script


This way of prepare and parse .isrList section to implement interrupt vectors arrays
is called local ISR declaration.
The name comes from the fact that all the entries to the arrays that would create
interrupt vectors are created locally in place of invocation of `IRQ_CONNECT` macro.
Then automatically generated linker scripts are used to place it in the right place in the memory.

This option requires enabling by the choose of `CONFIG_ISR_TABLES_LOCAL_DECLARATION`.
If this configuration is supported by the used architecture and toolchaing the
`CONFIG_ISR_TABLES_LOCAL_DECLARATION_SUPPORTED` is set.
See details of this option for the information about currently supported configurations.

Any invocation of `IRQ_CONNECT` or `IRQ_DIRECT_CONNECT` will declare an instance
of `struct _isr_list_sname` which is placed in a special .intList section:

```c

struct _isr_list_sname {
    /** IRQ line number */
    int32_t irq;
    /** Flags for this IRQ, see ISR_FLAG_* definitions */
    int32_t flags;
    /** The section name */
    const char sname[];
};
```
Note that the section name is placed in flexible array member.
It means that the size of the initialized structure will vary depending on the
structure name length.
The whole entry is used by the script during the build of the application
and has all the information needed for proper interrupt placement.

Beside of the _isr_list_sname the `IRQ_CONNECT` macro generates an entry
that would be the part of the interrupt array:

```c

struct _isr_table_entry {
    const void *arg;
    void (*isr)(const void *);
};
```
This array is placed in a section with the name saved in _isr_list_sname structure.

The values created by `IRQ_DIRECT_CONNECT` macro depends on the architecture.
It can be changed to variable that points to a interrupt handler:

```c

static uintptr_t <unique name> = ((uintptr_t)func);
```
Or to actually naked function that implements a jump to the interrupt handler:

```c

static void <unique name>(void)
{
    __asm(ARCH_IRQ_VECTOR_JUMP_CODE(func));
}
```
Similar like for `IRQ_CONNECT`, the created variable or function is placed
in a section, saved in _isr_list_sname section.


##### Files generated by the script


The interrupt tables generator script creates 3 files:
`isr_tables.c`, `isr_tables_swi.ld`, and `isr_tables_vt.ld`.

The `isr_tables.c` will contain all the structures for interrupts, direct interrupts and
shared interrupts (if enabled). This file implements only all the structures that
are not implemented by the application, leaving a comment where the interrupt
not implemented here can be found.

Then two linker files are used. The `isr_tables_vt.ld` file is included in place
where the interrupt vectors are required to be placed in the selected architecture.
The `isr_tables_swi.ld` file describes the placement of the software interrupt table
elements. The separated file is required as it might be placed in writable or nonwritable
section, depending on the current configuration.


#### x86 Details


The x86 architecture has a special type of vector table called the Interrupt
Descriptor Table (IDT) which must be laid out in a certain way per the x86
processor documentation.  It is still fundamentally a vector table, and the
gen_idt.py tool uses the .intList section to create it. However, on APIC-based
systems the indexes in the vector table do not correspond to the IRQ line. The
first 32 vectors are reserved for CPU exceptions, and all remaining vectors (up
to index 255) correspond to the priority level, in groups of 16. In this
scheme, interrupts of priority level 0 will be placed in vectors 32-47, level 1
48-63, and so forth. When the gen_idt.py tool is constructing the IDT, when it
configures an interrupt it will look for a free vector in the appropriate range
for the requested priority level and set the handler there.

On x86 when an interrupt or exception vector is executed by the CPU, there is
no foolproof way to determine which vector was fired, so a software ISR table
indexed by IRQ line is not used. Instead, the `IRQ_CONNECT` call
creates a small assembly language function which calls the common interrupt
code in `_interrupt_enter` with the ISR and parameter as arguments.
It is the address of this assembly interrupt stub which gets placed in the IDT.
For interrupts declared with `IRQ_DIRECT_CONNECT` the parameterless
ISR is placed directly in the IDT.

On systems where the position in the vector table corresponds to the
interrupt's priority level, the interrupt controller needs to know at
runtime what vector is associated with an IRQ line. gen_idt.py additionally
creates an _irq_to_interrupt_vector array which maps an IRQ line to its
configured vector in the IDT. This is used at runtime by `IRQ_CONNECT`
to program the IRQ-to-vector association in the interrupt controller.

For dynamic interrupts, the build must generate some 4-byte dynamic interrupt
stubs, one stub per dynamic interrupt in use. The number of stubs is controlled
by the `CONFIG_X86_DYNAMIC_IRQ_STUBS` option. Each stub pushes an
unique identifier which is then used to fetch the appropriate handler function
and parameter out of a table populated when the dynamic interrupt was
connected.


#### Going Beyond the Default Supported Number of Interrupts


When generating interrupts in the multi-level configuration, 8-bits per level is the default
mask used when determining which level a given interrupt code belongs to. This can become
a problem when dealing with CPUs that support more than 255 interrupts per single
aggregator. In this case it may be desirable to override these defaults and use a custom
number of bits per level. Regardless of how many bits used for each level, the sum of
the total bits used between all levels must sum to be less than or equal to 32-bits,
fitting into a single 32-bit integer. To modify the bit total per level, override the
default 8 in `Kconfig.multilevel` by setting `CONFIG_1ST_LEVEL_INTERRUPT_BITS`
for the  first level, `CONFIG_2ND_LEVEL_INTERRUPT_BITS` for the second level and
`CONFIG_3RD_LEVEL_INTERRUPT_BITS` for the third level. These masks control the
length of the bit masks and shift to apply when generating interrupt values, when checking the
interrupts level and converting interrupts to a different level. The logic controlling
this can be found in `irq_multilevel.h`

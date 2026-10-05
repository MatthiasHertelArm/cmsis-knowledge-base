---
id: "pyocd-session-options-list-extended-options-with-multicore-support"
type: "concept"
domain: "debug"
title: "Session options list: Extended options with multicore support"
summary: "These session options offer extended configuration using either a single setting or a per-core setting, using a list with an entry for each core."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#extended-options-with-multicore-support"
license: "Apache-2.0"
mode: "V"
---

These session options offer extended configuration using either a single setting or a per-core setting,
using a list with an entry for each core. When one of the following options is set using a comma separated list
inside square brackets [], the per-core assignment is encoded by the index (position) of the value in
that list. When using a list, all cores must have a corresponding entry.

<table>

<tr><th>Option Name</th><th>Type</th><th>Default</th><th>Description</th></tr>

<tr><td>gdbserver_port</td>
<td>int, list of int</td>
<td>3333</td>
<td>Base TCP port for the GDB Server. For multicore targets the zero-based core number will be added to
the value unless a list is specified.

Examples:
<ul>
<li><tt>3343</tt>, where in case of a multicore target, TCP port 3343 is assigned to
<tt>core0</tt>, TCP port 3344 is assigned to <tt>core1</tt>, and so on.</li>
<li><tt>[3343, 3334]</tt>, where TCP port 3343 is assigned to <tt>core0</tt> and TCP port
3334 is assigned to <tt>core1</tt>.</li>
</ul>
</td></tr>

<tr><td>stdio_mode</td>
<td>str, list of str</td>
<td>'server'</td>
<td>Controls connection to standard I/O. Must be one of 'off', 'console', 'server', or 'file'. For multicore devices
the mode applies to all cores unless it is specified as a list. This session option is preferred over the
<tt>semihost_console_type</tt> option.

Examples:
<ul>
<li><tt>console</tt>, where the standard I/O for all cores is routed to the console.</li>
<li><tt>[console, server]</tt>, where the standard I/O for <tt>core0</tt> is routed to the
console and the standard I/O for <tt>core1</tt> is routed to the Telnet Server.</li>
</ul>
</td></tr>

<tr><td>stdio_port</td>
<td>int, list of int</td>
<td>4444</td>
<td>The option applies only when <tt>stdio_mode</tt> is set to 'server'. Base TCP port for the Telnet Server.
For multicore targets the zero-based core number will be added to the value unless a list is specified.

Examples:
<ul>
<li><tt>4434</tt>, where in case of a multicore target, TCP port 4434 is assigned to
<tt>core0</tt>, TCP port 4435 is assigned to <tt>core1</tt>, and so on.</li>
<li><tt>[4434, 4443]</tt>, where TCP port 4434 is assigned to <tt>core0</tt> and TCP port
4443 is assigned to <tt>core1</tt>.</li>
</ul>
</td></tr>

<tr><td>stdio_file_in</td>
<td>str, list of str</td>
<td><i>&lt;target&gt;.in</i></td>
<td>The option applies only when <tt>stdio_mode</tt> is set to 'file'. Input filename to use as <i>stdin</i>.
When a single string is used, the core number (_&lt;core&gt;) will be appended to the filename
in case of multicore targets.

Examples:
<ul>
<li><tt>mytarget.in</tt>, where in case of a multicore target, the filenames will be
<tt>mytarget_0.in</tt> assigned to <tt>core0</tt>, <tt>mytarget_1.in</tt> assigned to <tt>core1</tt>,
and so on.</li>
<li><tt>[mytarget_cm4.in, mytarget_cm0.in]</tt>, where <tt>mytarget_cm4.in</tt> is
assigned to <tt>core0</tt> and <tt>mytarget_cm0.in</tt> is assigned to <tt>core1</tt>.</li>
</ul>
</td></tr>

<tr><td>stdio_file_out</td>
<td>str, list of str</td>
<td><i>&lt;target&gt;.out</i></td>
<td>The option applies only when <tt>stdio_mode</tt> is set to 'file'. Output filename to use as <i>stdout</i>.
When a single string is used, the core number (_&lt;core&gt;) will be appended to the filename
in case of multicore targets.

Examples:
<ul>
<li><tt>mytarget.out</tt>, where in case of a multicore target, the filenames will be
<tt>mytarget_0.out</tt> assigned to <tt>core0</tt>, <tt>mytarget_1.out</tt> assigned to <tt>core1</tt>,
and so on.</li>
<li><tt>[mytarget_cm4.out, mytarget_cm0.out]</tt>, where <tt>mytarget_cm4.out</tt> is
assigned to <tt>core0</tt> and <tt>mytarget_cm0.out</tt> is assigned to <tt>core1</tt>.</li>
</ul>
</td></tr>

</table>

---
id: "pyocd-session-options-list-rtt-and-systemview-options"
type: "concept"
domain: "debug"
title: "Session options list: RTT and SystemView options"
summary: "Session options list: RTT and SystemView options"
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#rtt-and-systemview-options"
license: "Apache-2.0"
mode: "V"
---

<table>

<tr><th>Option Name</th><th>Type</th><th>Default</th><th>Description</th></tr>

<tr><td>rtt</td>
<td>YAML Node</td>
<td><i>No default</i></td>
<td><p>Configuration for <a href="https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/">SEGGER RTT</a></p>
<pre>
rtt:
  - pname:         # [optional] Processor identifier (required for multicore devices).
    control-block: # [required] RTT control block discovery in target memory.
      address:     # [optional] Explicit address or start of scan range when size is provided.
      size:        # [optional] Size of the memory range to scan.
      auto-detect: # [optional] Scan default RAM regions. Default=false
    channel:       # [required] List of RTT channel configurations.
      - number:    # [required] Channel number.
        mode:      # [required] Channel mode:
                   #   stdio             - Connects channel to standard input/output.
                   #   server            - Exposes channel over a TCP server.
                   #   systemview        - Saves channel data to *.SVDat file for SEGGER SystemView.
                   #   systemview-server - Streams live data to SEGGER SystemView.
                   #   file              - Routes channel data to and from files.
        port:      # [optional] TCP port number (required for 'server' and 'systemview-server').
        file-out:  # [optional] Output file path (only for 'file' mode; default: &lt;target&gt;_core&lt;X&gt;_ch&lt;Y&gt;.out")
        file-in:   # [optional] Input file path (only for 'file' mode;  default: &lt;target&gt;_core&lt;X&gt;_ch&lt;Y&gt;.in")
</pre>
<p>Example:</p>
<ul>
<li>Command line:<br/>
<tt>-O rtt="[{control-block: {address: 0x20000000, size: 0x00020000}, channel: [{number: 0, mode: stdio}, {number: 1, mode: systemview}]}]"</tt></li>
<li>Config file:<br/>
<pre>rtt:
  - control-block:
      address: 0x20000000
      size: 0x00020000
    channel:
      - number: 0
        mode: stdio
      - number: 1
        mode: systemview
</pre></li></ul></td></tr>

<tr><td>systemview_file</td>
<td>str</td>
<td><i>&lt;target&gt;.SVDat</i></td>
<td>Output filename to capture SystemView data.</td></tr>

<tr><td>systemview_auto_start</td>
<td>bool</td>
<td>True</td>
<td>Whether to automatically start SystemView recording.</td></tr>

<tr><td>systemview_auto_stop</td>
<td>bool</td>
<td>True</td>
<td>Whether to automatically stop SystemView recording.</td></tr>

</table>

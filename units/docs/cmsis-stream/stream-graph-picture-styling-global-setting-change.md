---
id: "stream-graph-picture-styling-global-setting-change"
type: "concept"
domain: "cmsis-stream"
title: "Graph picture styling: Global setting change"
summary: "If you want to change some settings, you define a dictionary with new values for those settings and you create a Style object using this dictionary:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Styling.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Styling.md#global-setting-change"
license: "Apache-2.0"
mode: "V"
---

If you want to change some settings, you define a dictionary with new values for those settings and you create a `Style` object using this dictionary:

`myStyle=Style(myDictionary)`

You don't need to define a value for all the settings recognized in a dictionary. You only need to provide values for the global settings you want to change. For instance:

```python
newBackground = {"graph_background"      : "gray"}
```

Any setting not defined in the dictionary will use a value from the default style. And if you don't pass any dictionary, the default global settings will be used.

The list of all global settings is:

```python
_DEFAULT_STYLE = {
    # Graph global settings
     "graph_background"      : "white"       # Color of graph background
    ,"graph_font"            : "Times-Roman" # Font used in the graph

    # Node settings
    ,"node_color"            : "none"        # Fill color of any node
    ,"node_boundary_color"   : "black"       # Boundary color of any node
    ,"node_label_size"       : "14.0"        # Font size of node labels
    ,"node_label_color"      : "black"       # Color of node labels

    # Special node settings (Constant node and delay box)
    ,"special_node_border"   : "1"           # Thickness of node boundary

    # Node port settings (port = input or output of a node)
    ,"port_sample_color"     : "blue"        # Color of number of samples
    ,"port_sample_font_size" : "12.0"        # Font size of number of samples

    ,"port_font_color"       : "black"       # Color of a port
    ,"port_font_size"        : "12.0"        # Font size of a port

    # Edge settings
    ,"edge_color"            : "black"       # Color of any edge
    ,"edge_label_size"       : "12.0"        # Font size of any edge label
    ,"edge_label_color"      : "black"       # Color of any edge label
    ,"edge_style"            : "solid"       # Edge style (dashed, dotted ...)
    ,"arrow_size"            : 0.5           # Arrow size at end of edge
    }
```

Color settings and style settings must be using syntax and names recognized by graphviz.

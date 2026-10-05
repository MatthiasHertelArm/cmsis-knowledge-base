---
id: "stream-graph-picture-styling-global-settings"
type: "concept"
domain: "cmsis-stream"
title: "Graph picture styling: Global settings"
summary: "Controlled with the graph_backround dictionary item:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Styling.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Styling.md#global-settings"
license: "Apache-2.0"
mode: "V"
---

### Graph background color

Controlled with the `graph_backround` dictionary item:

(figure: feature_graph_background)

### Font

Controlled with the `graph_font` dictionary item:

(figure: feature_graph_font)

### Boundary node color

Controlled with the `node_boundary_color` dictionary item:

(figure: feature_node_boundary_color)

### Node filling color

Controlled with the `node_color` dictionary item:

(figure: feature_node_color)

### Node label color

Controlled with the `node_label_color` dictionary item:

(figure: feature_node_label_color)

### Node label size

Controlled with the `node_label_size` dictionary item:

(figure: feature_node_label_size)

### Port color

Controlled with the `port_font_color` dictionary item:

(figure: feature_port_font_color)

The port (like `o1`, `o`, `i`) colors are changes.

### Port font size

Controlled with the `port_font_size` dictionary item:

(figure: feature_port_font_size)

The port (like `o1`, `o`, `i`) font size are changes.

### Port sample color

Controlled with the `port_sample_color` dictionary item:

(figure: feature_port_sample_color)

The color of the number of samples is changed.

### Port sample font size

Controlled with the `port_sample_font_size` dictionary item:

(figure: feature_port_sample_font_size)

The font size of the number of samples is changed.

### Special nodes border thickness

Controlled with the `special_node_border` dictionary item:

(figure: feature_special_node_border)

Special nodes are virtual nodes (they do not exist in the C++ code):

* Constant nodes
* Delay box

Constant nodes are argument of pure functions and just C variables (not real nodes).

Delay box are additional samples in a FIFO.

### Edge color

Controlled with the `edge_color` dictionary item:

(figure: feature_edge_color)

### Edge label color

Controlled with the `edge_label_color` dictionary item:

(figure: feature_edge_label_color)

### Edge label size

Controlled with the `edge_label_size` dictionary item:

(figure: feature_edge_label_size)

### Edge style

Controlled with the `edge_style` dictionary item:

(figure: feature_edge_style)

Edge style is : solid, dashed, dotted ... please refer to the graphviz documentation..

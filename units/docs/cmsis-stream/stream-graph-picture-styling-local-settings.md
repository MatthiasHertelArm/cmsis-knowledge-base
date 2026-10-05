---
id: "stream-graph-picture-styling-local-settings"
type: "concept"
domain: "cmsis-stream"
title: "Graph picture styling: Local settings"
summary: "Settings applied to a specific node, edge or port."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Styling.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Styling.md#local-settings"
license: "Apache-2.0"
mode: "V"
---

Settings applied to a specific node, edge or port.

### Local Edge color

```python
def edge_color(self,edge):
```

(figure: feature_func_edge_color)

In this example, the color of the edges connecting CMSIS-DSP nodes is changed.

### Local edge label

```python
def edge_label(self,edge):
```

(figure: feature_func_edge_label)

In this example, the label of the edges connecting CMSIS-DSP nodes is changed. It is on two lines instead on being on one line.

Those labels are graphviz HTML like labels.

### Local edge label color

```python
def edge_labe_color(self,edge):
```

(figure: feature_func_edge_label_color)

In this example, when the FIFO length >= 320, the edge label is in red.

### Local edge label size

```python
def edge_label_size(self,edge):
```

(figure: feature_func_edge_label_size)

In this example, when the FIFO length >= 320, the edge font size is increased.

### Local edge style

```python
def edge_style(self,edge):
```

(figure: feature_func_edge_style)

In this example, the style of the edges connecting CMSIS-DSP nodes is changed to dashed.

### Local node boundary color

```python
def node_boundary_color(self,node):
```

(figure: feature_func_node_boundary_color)

CMSIS-DSP nodes are colored differently in this example.

### Local node color

```python
def node_color(self,node):
```

(figure: feature_func_node_color)

CMSIS-DSP nodes are colored differently in this example.

### Local node label

```python
def node_label(self,node):
```

(figure: feature_func_node_label)

`arm_scale_f32` nodes are now named `*` in this example. The label has been customized.

### Local node label color

```python
def node_label_color(self,node):
```

(figure: feature_func_node_label_color)

CMSIS-DSP nodes are colored differently in this example.

### Local node label size

```python
def node_label_size(self,node):
```

(figure: feature_func_node_label_size)

CMSIS-DSP nodes have a different label font size.

### Local port color

```python
def port_font_color(self,item,i,input=False):
```

(figure: feature_func_port_font_color)

Output ports of CMSIS-DSP nodes are colored differently in this example.

### Local port font size

```python
def port_font_size(self,item,i,input=False):
```

(figure: feature_func_port_font_size)

Output ports of CMSIS-DSP nodes have a different font size.

### Local port sample color

```python
def port_sample_color(self,nb_sample):
```

(figure: feature_func_port_sample_color)

When number of samples for an IO is >= 320, it is displayed in red in this example.

### Local port sample font size

```python
def port_sample_font_size(self,nb_sample):
```

(figure: feature_func_port_sample_font_size)

When number of samples for an IO is >= 320, the font size is increased

### Const node border

```python
def const_border(self,const_name):
```

(figure: feature_func_const_border)

Border around the `HALF` node is increased.

### Const node boundary color

```python
def const_boundary_color(self,const_name):
```

(figure: feature_func_const_boundary_color)

Color of the `HALF` node is changed.

### Const node filling color

```python
def const_color(self,const_name):
```

(figure: feature_func_const_color)

Color of the `HALF` node is changed.

### Const node edge color

```python
def const_edge_color(self,name,dstPort):
```

(figure: feature_func_const_edge_color)

Color of edges connecting the `HALF` node to the CMSIS-DSP function are changed.

### Const node edge style

```python
def const_edge_style(self,name,dstPort):
```

(figure: feature_func_const_edge_style)

Style of edges connecting the `HALF` node to the CMSIS-DSP function are changed.

### Const node label color

```python
def const_label_color(self,const_name):
```

(figure: feature_func_const_label_color)

### Const node label size

```python
def const_label_size(self,const_name):
```

(figure: feature_func_const_label_size)

### Delay box border thickness

```python
def delay_border(self,delay_value):
```

(figure: feature_func_delay_border)

### Delay box border color

```python
def delay_boundary_color(self,delay_value):
```

(figure: feature_func_delay_boundary_color)

### Delay box filling color

```python
def delay_color(self,delay_value):
```

(figure: feature_func_delay_color)

### Delay box edge color

```python
def delay_edge_color(self,srcPort,nb_samples):
```

(figure: feature_func_delay_edge_color)

### Delay box edge style

```python
def delay_edge_style(self,srcPort,nb_samples):
```

(figure: feature_func_delay_edge_style)

### Delay box label color

```python
def delay_label_color(self,delay_value):
```

(figure: feature_func_delay_label_color)

### Delay box label size

```python
def delay_label_size(self,delay_value):
```

(figure: feature_func_delay_label_size)

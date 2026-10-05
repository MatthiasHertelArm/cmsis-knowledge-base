---
id: "mlek-implementing-custom-ml-application-output-to-mps3-lcd"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Output to MPS3 LCD"
summary: "The HAL exposes LCD functions to print text or an image to the board LCD. For example:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md#output-to-mps3-lcd"
license: "Apache-2.0"
mode: "V"
---

The HAL exposes LCD functions to print text or an image to the board LCD. For example:

- `hal_display_show_text`
- `hal_display_show_image`

Text presentation function has the following signature:

- `const char* str`: the string to print.
- `const uint32_t str_sz`: The string size.
- `const uint32_t pos_x`: The x coordinate of the first letter in pixels.
- `const uint32_t pos_y`: The y coordinate of the first letter in pixels.
- `const uint32_t alow_multiple_lines`: Signals whether the text is allowed to span multiple lines on the screen, or
  must be truncated to the current line.

This function does not wrap text. If the given string cannot fit on the screen, it goes outside the screen boundary.

Here is an example that prints "Hello world" on the LCD screen:

```C++
std::string hello("Hello world");
hal_display_show_text(hello.c_str(), hello.size(), 10, 35, 0);
```

The image presentation function has the following signature:

- `uint8_t* data`: The image data pointer;
- `const uint32_t width`: The image width;
- `const uint32_t height`: The image height;
- `const uint32_t channels`: The number of channels. Only 1 and 3 channels are supported now.
- `const uint32_t pos_x`: The x coordinate of the first pixel.
- `const uint32_t pos_y`: The y coordinate of the first pixel.
- `const uint32_t downsample_factor`: The factor by which the image is to be downsampled.

For example, the following code snippet visualizes an input tensor data for `MobileNet v2 224`, by down-sampling it
by a factor of two:

```C++
hal_display_show_image((uint8_t *) inputTensor->data.data, 224, 224, 3, 10, 35, 2);
```

Please refer to the [Hardware Abstraction Layer API](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#hardware-abstraction-layer-api) section for more
LCD related functions.

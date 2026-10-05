---
id: "armsw-readme-mainpage-omit-from-toc-features"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: Features"
summary: "Since Arm-2D provides Low-Level 2D Image Processing Services that are deeply optimised for both performance and memory footprint, it has been quickly adopted in many Deep Embedded Display systems since it debuted in 2020."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#features"
license: "Apache-2.0"
mode: "V"
---

### In this version (v1.2.6), A Golden Release

Since Arm-2D provides **Low-Level 2D Image Processing Services** that are deeply optimised for both performance and memory footprint, it has been quickly adopted in many Deep Embedded Display systems since it debuted in 2020.  Now you can find its [presence](https://www.linkedin.com/search/results/all/?keywords=%23amazingarm2d&origin=HASH_TAG_FROM_FEED) from the [tiniest Cortex-M0](https://www.linkedin.com/posts/gabriel-wang-554523167_amazingarm2d-activity-7239115506102726658-CKhE?utm_source=share&utm_medium=member_desktop&rcm=ACoAACfEJVABu43psSmn3fAYP2dptCi3QU4o0Yg) to the [Raspberry Pi 5 powerhouse](https://www.linkedin.com/posts/gabriel-wang-554523167_embeddedworld-activity-7305214952544391170-WkLP?utm_source=share&utm_medium=member_desktop&rcm=ACoAACfEJVABu43psSmn3fAYP2dptCi3QU4o0Yg).  The supported features include, but are not limited to:

- **Alpha-Blending** / **Masks**
  - With or without Colour-Keying
  - Filling-Colour with optional mask and opacity
    - For drawing anti-alias icons/texts in a specified colour
    - Supports A1, A2, A4 and A8 masks
    - Supports horizontal and vertical line masks
    - Supports Colour-Filling with Alpha-Gradient defined in 4-points, 3-points, horizontal and vertical mode.
      - Supports Mask
      - Supports an optional Opacity
    - Supports mirroring
  
- **Image Copy (Blit)** 
  - With or without Colour-Keying
  - Supports four mirroring modes: No-mirroring, X-mirroring, Y-mirroring and XY-mirroring
  - Supports **masks** on the source side and/or the target side
  - Provides API variants that accept **Opacity** as arguments.
  -  Implicit colour conversion for **ARGB8888** (**ccca8888**)
  
- **Supported Colour formats**

  - **GRAY8 (8-bit Grayscale)**, **RGB565** and **RGB888**
  - Generic **C8BIT (8bit colour)**, **RGB16** and **RGB32**
  - Converting colour formats among **GRAY8**, **RGB565** and **RGB888**
    - Implicit colour conversion for **ARGB8888** (**ccca8888**)
  - Ready for **monochrome LCD** (the 1bit colour) and **E-ink devices** (the 1bit, 2bits and 4bits colour formats)
    - Using **Gray8** as the internal processing format and converting to target colour format inside the Display Adapter, e.g. `Disp0_DrawBitmap`
    - Provides a dedicated colour solution in the display adapter service for monochrome display devices.
    - Provides a smart **Full-Frame-Refresh** mode for e-ink devices to flush the whole frame for any updates on the screen.

- **Display Adapter Service for connecting LCD**

  - Generic Partial Frame-buffer (PFB)
    - Easy to Use: transparent for applications
    - No limitation on screen resolution under the common sense **(See note 1)**
    - Flexible in PFB size and shape (it could be a line or a rectangular with any size)  **(See note 2)**
    - Supports PFB pixel alignment for both width and height.

> [!NOTE]
>
> 1. As long as the size is smaller than 32767 * 32767. 
> 2. As long as the total pixel numebr is smaller than 16M pixels.

  - Supports **Dirty Regions** for refreshing specified areas only
    - Provides a debug mode for dirty regions
    - Provides optimization for dirty regions to reduce the chances of refreshing overlapped areas.
    - Provides dirty region helper services for ease of use.
  - Supports swapping high and low bytes for RGB16 pixels
  - Provides a **Scene Player** with various scene switching modes (Fade-In-Fade-Out, Slide, Erase etc.)
  - Supports various buffering Modes with a built-in frame buffer pool.
    - Single Buffer/Double-Buffers
    - Provides a helper service for Direct Mode (i.e. 3FB Mode)
    - Provides a helper service for Asynchronous Flushing (i.e. DMA + ISR)
  - Adds an nano-drawing mode as an alternative option of the Scene Player. 
- **Transform** (i.e. rotation and scaling)
  - With/Without Colour-keying
  - Supports an optional **Opacity** ratio
  - Supports Anti-Alias.
    - You can enable it by defining the macro  `__ARM_2D_HAS_ANTI_ALIAS_TRANSFORM__` to `1` at **compile-time**.
  - Supports source masks
  - Supports specifying different scaling ratios for X and Y axes, respectively
  - Supports using floating point numbers (i.e. `float`) to specify the pivot coordinate.
  - Supports using negative scaling ratios for x/y mirroring
  - Supports colour-filling / tile-copy with a transformed mask, optional source mask and target mask.
- **Filters**

  - Generic Anti-alias and Fast IIR-Blur
  - Colour Inversion
- **An Unified and User-Friendly Programmers' Model**
  - APIs can be used in **Synchronous** manner (  **Classic Blocking-code** ) and/or **Asynchronous** manner ( **Event-Driven** )
  - Supports both **bare-metal** and **RTOS** environments
  - Ultra-small memory footprint
- **Helper Services, Tools and Others**

  - **Timer Services**

    - Timeout: `arm_2d_helper_is_time_out`
    - Time-based functions:
      - Liner: `arm_2d_helper_time_liner_slider` and **[new]** `arm_2d_helper_timer_liner_slider_i64`
      - Cosine: `arm_2d_helper_time_cos_slider`
      - S-curve: `arm_2d_helper_time_half_cos_slider`
  - **Virtual Resource**
    - Supports loading resources on-demand from external memories which are not mapped into the Cortex-M memory space.
    - Supports background-image-loading mode that requests **NO** extra PFB block. 
    - **Example Loaders** for loading
      - JPEG images
      - [QOI images](https://qoiformat.org/) (a Lossless image compression format)
      - TrueType fonts via freetype
      - A generic loader for loading user defined image formats, or drawing shapes/masks directly. 
      - **[new]** A loader for losslessly compressed RGB565 images (**zhRGB565**)
      - **[new]** A loader for losslessly compressed masks (**LMSK**). **It is the optimal solution for mid- / large masks.** 
  - **Layout Assistant**
    - Alignments, e.g. `arm_2d_align_centre`, `arm_2d_align_bottom_right` etc.
    - Docking, e.g. `arm_2d_dock_top`,`arm_2d_dock_right`, `arm_2d_dock_vertical`, `__item_line_dock_horizontal` etc.
    - Line Stream Layout, e.g. `__item_line_horizontal` and `__item_line_vertical`
    - Stream Layout (with wrapping), e.g. `__item_horizontal` and `__item_vertical`
    - Users can specify alignment in `arm_2d_layout()` macro: TOP-DOWN, BOTTOM-UP, RIGHT-TO-LEFT etc.
  - RTOS Helper Services for CMSIS-RTOS2 and RT-Thread
  - **Templates**
    - Provides templates for user controls and scenes.
    - Scene templates for Meter, Watch and Fitness trackers
    - Provides a template for adding new RTOS support.
  - **Tools**
    - A `img2c.py` for generating arm-2d resources from user-specified images
    - A `ttf2c.py` for generating user-customized A1, A2, A4 and A8 fonts from an user-specified TrueType Font
  - **Demos**
    - Demos for various scenarios
    - A dedicated demo for Helium-ACI acceleration. 
    - A set of demos for monochrome devices
    - A set of demos for drawing masks, waveform etc. 
  - **Project Templates**
    - A project template for Windows, Linux and MacOS platform
    - A project template for Raspberry Pi Pico
- **CMSIS-Pack is available.**
- **Ready and Welcome 3rd party adoption**

  - Accelerating [LVGL](https://lvgl.io/) as [soft-GPU](https://docs.lvgl.io/master/details/integration/renderers/arm2d.html)
  - Accelerating [CrankSoftware](https://www.cranksoftware.com/) as [soft-GPU](https://info.cranksoftware.com/platforms/demo-images/renesas/ra8d1)
  - Accelerating [emWin](https://www.segger.com/products/user-interface/emwin/technology/about-emwin-technology/) as [soft-GPU](https://doc.segger.com/UM03001_emWin.html#GUI_GPU_Arm2D_Arm_2D_driver)

### New Features Planned in the Future

- Perspective Transform
- Supports DMAC-350
- SVE2 or NEON Acceleration



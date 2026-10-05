---
id: "alp-cmsisdsp-dev-with-python-how-to-2-launch-jupyter-and-set-up-your"
type: "concept"
domain: "project"
title: "Getting started with CMSIS-DSP using Python: Set up environment: Launch Jupyter and set up your notebook"
summary: "You can now launch the Jupyter notebook with the following command:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-2/#launch-jupyter-and-set-up-your-notebook"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can now launch the Jupyter notebook with the following command:

```bash
jupyter notebook
```
A browser window should open, displaying the source tree. 

Create a new Jupyter notebook by clicking **New** and selecting **Python 3 (ipykernel)**. The new notebook is called `Untitled`. Rename it to something descriptive, for example `cmsis-dsp`.

Now import all the required packages by copying and running the following Python code into your notebook and run the cell (Shift+Enter).

**Note:**
All the Python code blocks in this Learning Path are intended to be executed in the same Jupyter notebook.




```python
import cmsisdsp as dsp
import cmsisdsp.fixedpoint as fix
from cmsisdsp import datatype as dt
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

# Package for plotting
import matplotlib.pyplot as plt

# Package to display audio widgets in the notebook and upload sound files
import ipywidgets
from IPython.display import display,Audio

# To convert a sound file to a NumPy array
import io
import soundfile as sf

# To load test patterns from the Arm Virtual Hardware Echo Canceller demo
from urllib.request import urlopen
```

You're now ready to move on and set up the audio files you'll use for processing.

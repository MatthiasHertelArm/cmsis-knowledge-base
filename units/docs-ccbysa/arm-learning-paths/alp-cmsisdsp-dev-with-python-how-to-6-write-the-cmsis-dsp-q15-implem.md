---
id: "alp-cmsisdsp-dev-with-python-how-to-6-write-the-cmsis-dsp-q15-implem"
type: "concept"
domain: "project"
title: "Getting started with CMSIS-DSP using Python: Write the CMSIS-DSP Q15 implementation: Write the CMSIS-DSP Q15 implementation"
summary: "In this section, you will update the code to run with the CMSIS-DSP Python library. The CMSIS-DSP implementation is similar to the reference implementation you just tested, but some things will be different."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-6.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-6/#write-the-cmsis-dsp-q15-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you will update the code to run with the CMSIS-DSP Python library. The CMSIS-DSP implementation is similar to the reference implementation you just tested, but some things will be different.

### Slicing

Since the Q15 representation is less accurate than float and can saturate, it's a good idea to verify the recombination step. This helps ensure the Q15 windowing and recombination logic is sound before plugging it into the full Q15 noise suppression pipeline. With the following code, you'll check that recombining the windowed block samples works correctly.

The Hanning window is converted to Q15 format. Then, the slices are multiplied by the Q15 Hanning window and summed. The final result is converted to float.

```python
offsets = range(0, len(data),winOverlap)
offsets=offsets[0:len(slices_q15)]
res=np.zeros(len(data))
window_q15=fix.toQ15(window)
i=0
for n in offsets:
    w = dsp.arm_mult_q15(slices_q15[i],window_q15)
    res[n:n+winLength] = dsp.arm_add_q15(res[n:n+winLength],w)
    i=i+1
res_q15=fix.Q15toF32(res)
plt.plot(res_q15)
plt.show()
```
You can now listen to the audio to check the result.

```python
audioRecombine=Audio(data=res_q15,rate=samplerate,autoplay=False)
audioRecombine
```
### Utilities

CMSIS-DSP does not have a complex data type. Complex numbers are represented as a float array with alternating real and imaginary parts: `[real, imaginary, real, imaginary, ...]`.

You'll need functions to convert to and from NumPy complex arrays. Define these by pasting into a cell in the notebook and evaluating it.

```python
def imToReal1D(a):
    ar=np.zeros(np.array(a.shape) * 2)
    ar[0::2]=a.real
    ar[1::2]=a.imag
    return(ar)

def realToIm1D(ar):
    return(ar[0::2] + 1j * ar[1::2])
```

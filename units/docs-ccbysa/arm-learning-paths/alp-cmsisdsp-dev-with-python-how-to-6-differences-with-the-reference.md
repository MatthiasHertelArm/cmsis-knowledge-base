---
id: "alp-cmsisdsp-dev-with-python-how-to-6-differences-with-the-reference"
type: "concept"
domain: "project"
title: "Getting started with CMSIS-DSP using Python: Write the CMSIS-DSP Q15 implementation: Differences with the reference implementation"
summary: "In this section, you will walk through the updates needed to transition from float to Q15 implementation. To avoid duplication, the final code to be run is available in the final step on this page."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-6.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-6/#differences-with-the-reference-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you will walk through the updates needed to transition from float to Q15 implementation. To avoid duplication, the final code to be run is available in the final step on this page. Therefore, you should not copy and evaluate the following code snippets.

### Constructor

The constructor for `NoiseSuppressionQ15` is similar and uses Q15 instead of float. The Hanning window is converted to Q15, and Q15 versions of the CFFT objects are created.

### Subnoise

The noise reduction function is more complex:

1. Q15 is not accurate enough for the energy computation, meaning many values would be evaluated to zero. Q31 is used instead. In the code, this can look like:
```python
vq31 = dsp.arm_q15_to_q31(v)
energy = dsp.arm_cmplx_mag_squared_q31(vq31)
```

2. For maximum accuracy, the signal is rescaled before calling this function. Since energy is not a linear function, the scaling factor must be compensated when computing the Wiener gain. The argument `status` is zero when the scaling has been applied. A similar scaling factor is applied to the noise:
```python
if status==0:
    the_max_q31=dsp.arm_q15_to_q31([the_max])[0]
    energy=dsp.arm_scale_q31(energy,the_max_q31,0)
    energy=dsp.arm_scale_q31(energy,the_max_q31,0)
```

3. CMSIS-DSP fixed-point division represents 1 exactly. So in Q31, instead of using `0x7FFFFFFF`, `1` is represented as `0x40000000` with a shift of `1`. This behavior is handled in the algorithm when converting the scaling factor to an approximate Q31 value.

Several safeguards are applied:
* The Wiener gain is capped at 1 to prevent overflow.
* If the energy is zero, the gain is also set to 1 to avoid divide-by-zero errors.
* When energy == noise, the result should be exactly 1. In this case, `arm_divide_q31` will return a quotient of `0x40000000` and shiftVal of 1. The algorithm detects this specific representation and overrides it, setting quotient = `0x7FFFFFFF` and shiftVal = 0, which is a closer approximation to full-scale gain in Q31 without the need for additional shifts.

```python
quotient=0x7FFFFFFF
shiftVal=0
if b!=0 and a!=b:
    # Compute the quotient
    status,quotient,shiftVal = dsp.arm_divide_q31(a,b)
    if shiftVal > 0:
        quotient=0x7FFFFFFF
        shiftVal = 0

```

4. The final scaling is performed using a Q31 multiplication, and the result is converted back to Q15:
```python
res = dsp.arm_cmplx_mult_real_q31(vq31,scalingQ31)
resQ15 = dsp.arm_q31_to_q15(res)
```

### Rescale

To achieve maximum accuracy in Q15, the signal (and noise) is rescaled before computing the energy.
This rescaling function did not exist in the float implementation. The signal is divided by its maximum value to bring it to full scale::

```python
def rescale(self,w):
        the_max,index=dsp.arm_absmax_q15(w)

        quotient=0x7FFF
        the_shift=0
        status = -1
        if the_max != 0:
            status,quotient,the_shift = dsp.arm_divide_q15(0x7FFF,the_max)
            if status == 0:
                w=dsp.arm_scale_q15(w,quotient,the_shift)
        return(w,status,the_max)
```

The scaling must be reversed after the Inverse FFT (IFFT) to allow recombining the slices and reconstructing the signal:

```python
def undo_scale(self,w,the_max):
    w=dsp.arm_scale_q15(w,the_max,0)
    return(w)
```

### Noise suppression

The algorithm closely follows the float implementation. However, there is a small difference because CMSIS-DSP can be built for Cortex-A and Cortex-M. On Cortex-A, there are small differences in the FFT API, as it uses a different implementation.

If the Python package has been built with Neon acceleration, it will use the new API that requires an additional temporary buffer.

If this temporary buffer is not provided, the Python package will allocate it automatically. While you can use the same API, this is less efficient. It is better to detect whether the package has been compiled with Neon acceleration, allocate a temporary buffer and use it in the FFT calls. This approach is closer to how the C API is used.

```python
if dsp.has_neon():
    resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,tmp=self._tmp)
else:
    resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,1)
```

In the Neon version, the FFT's bit-reversal flag is no longer available. It's not possible to disable bit reversal in the Neon version.

A scaling factor must be applied to the IFFT output:

```python
res = dsp.arm_shift_q15(res,self._fftShift)
```

This scaling is unrelated to the signal and noise scaling used for improved accuracy. The output of the Q15 IFFT is not in Q15 format and must be converted. This is typical of fixed-point FFTs, and the same applies to Q31 FFTs.

Finally, the accuracy-related scaling factor is removed at the end of the function:

```python
if status == 0:
   res=self.undo_scale(res,the_max)
```

### Noise estimation

The noise estimation function performs both noise estimation and noise suppression. Noise energy is computed in Q31 for higher accuracy. The FFT functions detect whether the package was built with Neon support.

### Donothing

`donothing` is a debug function. You can disable noise reduction and test only slicing, overlap-add, and the FFT/IFFT in between. This function applies scaling and performs the FFT/IFFT. It's a good way to check for saturation issues (which are common with fixed-point arithmetic) and to ensure proper scaling compensation.

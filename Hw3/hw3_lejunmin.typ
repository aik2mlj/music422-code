#import "@preview/problemst:0.1.0": pset

#show: pset.with(
  class: "MUSIC 422",
  student: "Lejun Min",
  title: "Homework 3",
  date: datetime.today(),
  subproblems: "1.a.i)",
)

=
==
=== Relation between input and aliased MDCT/IMDCT output
Each MDCT block is computed over a windowed segment of the input signal with a length of N, but it only produces N/2 frequency-domain coefficients. This results in time-domain aliasing because adjacent blocks overlap by 50%, and the information is distributed across consecutive blocks.

- The MDCT output contains transformed frequency components from a windowed portion of the input, but due to the transform's properties, adjacent blocks share spectral information.
- The IMDCT output reconstructs an aliased time-domain signal, where each block contains contributions from two overlapping input segments.

=== How overlap-add will recover the input signal
Each IMDCT block has contributions from two adjacent input blocks, overlapping them and summing cancels the aliasing components due to the design of the TDAC principle, ensuring perfect reconstruction.

==
=== How to initialize the first block of input samples?
Extract the first 4 data samples, and prepend them with 4 zeros.

=== What did you need to do to get the last block of samples?
Append 4 zeros for the last block of samples before feeding into MDCT/IMDCT.

=== Is there any delay in your output signal? How much?
Yes. There is a delay of 4 data samples.

==
The execution time of slow/FFT MDCT/IMDCT functions are:
- Slow MDCT: 0.037722503002441954
- FFT MDCT: 0.00025083799846470356
- Slow IMDCT: 0.032007888999942224
- FFT IMDCT: 0.00029606300086015835
Average speedup ratio: 127.50094091703055

#counter(heading).step(level: 2)
#counter(heading).step(level: 2)
==

#figure(
  image("assets/1f-1.png", width: 60%),
  caption: [Windows in the time domain.],
) <fig-1f-1>


#figure(
  image("assets/1f-2.png", width: 60%),
  caption: [SPL with different windows and transforms.],
) <fig-1f-2>

=== Does anything in this graph explain why we choose to use an FFT to do peak detection in the psychoacoustic model stage instead of the MDCT?
This graph clearly shows that FFT has a much steeper curve, i.e., better frequency separation performance than MDCT given the same Sine window. Therefore, FFT is preferred than MDCT in peak detection of the psychoacoustic model.

=== Does anything explain why a Hanning window is often used for FFT analysis in the psychoacoustic stage instead of a Sine window?
The graph shows that the Hanning window achieves a steeper curve, i.e., better frequency separation performance than the Sine window with FFT. Therefore, Hanning window is preferred than Sine window in the FFT analysis of the psychoacoustic model.

=
#counter(heading).step(level: 2)
#counter(heading).step(level: 2)
#counter(heading).step(level: 2)
==
=== Describe the quantization noise you hear for each quantization and block size.
I tested the coding with `spfe.wav` and `oboe.wav`.

- The quantization noise is much *worse* using _uniform quantization_ than using _floating point quantization_ in any scenario. I suppose this is due to the fact that in this implementation, we move a factor of $2/N$ from the inverse transform to the forward transform, making the absolute level of the MDCT-transformed frequency signals low. Therefore, _uniform quantization_ really struggles to record the low-level frequency information, while _floating point quantization_ performs better with its adaptive adjustment.

- For speech recordings, the quantization noise is more noticeable with larger block size. Since the signals are more transient, smaller block size captures more instantaneous information that are crucial for speech reconstruction. However, for instrumental recordings, larger block size seems to perform better with clearer harmonics captured. This is due to the fact that larger block size achieves better frequency-domain resolution.

=== Difference between time-domain and frequency-domain quantization noise
They do have very different characteristics.

- The time-domain quantization noise approximates the impression of a white noise that is universally chaotic in its frequency components. This is due to that the quantization is on the signal level, which treats the frequency components universally bad. The noise does not pose some filtering effect on the original signal. Also, the noise does not contain adjacent signal information (no time aliasing).

- The frequency-domain quantization noise is more harmonic, closely related to the harmonic components of the signal. The noise poses a filtering effect (low-pass, band-pass like) on the original signal, making it sound muffled. Also, the noise contain adjacent signal information (time aliasing), which sounds like a reverberation or a comb filter sometimes.

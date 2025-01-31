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

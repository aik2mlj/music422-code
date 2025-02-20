#import "@preview/problemst:0.1.0": pset

#set par(justify: true)

#show: pset.with(
  class: "MUSIC 422",
  student: "Lejun Min",
  title: "Homework 5",
  date: datetime.today(),
  subproblems: "1.a.i)",
)
#let avg(x) = [$angle.l #x angle.r$]

=
==
===
The data rate per channel of the input sound file is
$
  I_"input" = R_"input" times F_s = 16 times 48 = 768 "kb/s/ch"
$
Thus, the compression ratio is
$
  C = I_"input" : I = 4 : 1
$

===
The average number of bits per frequency line is
$
  avg(R) = I / F_s = 192 / 48 = 4 "bits/line"
$
To encode each block of $N\/2$ spectral lines, we need to spend
$
  R_"block" = avg(R) times N / 2 = 4 times 512 = 2048 "bits"
$

===
In Zwicker's critical band model, there are in total 25 critical bands (sub-blocks). The number of bits they take for storing sub-block scale factor is
$
  R_"sf" = 4 times 25 = 100 "bits"
$
Therefore, the number of bits that remain to encode mantissas is
$
  R_"mt" = R_"block" - R_"sf" = 1948 "bits"
$
The number of bits per frequency line is
$
  R_"line" = R_"mt" / (N\/2) = 3.805 "bits/line"
$

===
In this case, the number of bits remain to encode mantissas is
$
  R_"mt" = R_"block" - R_"sf" - R_"bitalloc" - R_"header" = 2048 - 100 - 4 times 25 - 4 = 1844 "bits"
$
The number of bits per frequency line is
$
  R_"line" = R_"mt" / (N\/2) = 3.602 "bits/line"
$

==
With a data rate of $I = 128 "kb/s/ch"$,
===
The compression ratio
$
  C = I_"input" : I = 6 : 1
$
===
The number of bits per frequency line is
$
  avg(R) = I / F_s = 2.667 "bits/line"
$
The number of bits for each block is
$
  R_"block" = avg(R) times N / 2 = 1365.333 "bits"
$
===
The number of bits remain to encode mantissas is
$
  R_"mt" = R_"block" - R_"sf" = 1365.333 - 4 times 25 = 1265.333 "bits"
$
The number of bits per frequency line is
$
  R_"line" = R_"mt" / (N\/2) = 2.471 "bits/line"
$
===
The number of bits remain to encode mantissas is
$
  R_"mt" = R_"block" - R_"sf" - R_"bitalloc" - R_"header" = 1365.333 - 100 - 100 - 4 = 1161.333 "bits"
$
The number of bits per frequency line is
$
  R_"line" = R_"mt" / (N\/2) = 2.268 "bits/line"
$

==

=== The uniform mantissa bit allocation:
`[3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 2 2 2 2]`\
In total: 1161 bits.

=== The constant noise floor bit allocation:
`[13 16 14 15 15 12 11 14  8  3  2  2  2  0  0  0  0 10 12  0  0 11  0  0 0]`\
In total: 1152 bits.

=== The constant NMR bit allocation:
`[10 11  8  9 10  8  8 10  5  2  3  4  6  7  8  6  0  8 10  0  0 10  0  0 0]`\
In total: 1153 bits.


#figure(
  image("assets/1c.png", width: 90%),
  caption: [The MDCT, masked threshold, and noise floors for different bit allocation strategies.],
) <fig-1c>

==

=== The uniform mantissa bit allocation:
`[4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3]`
\ In total: 1792

=== The constant noise floor bit allocation:
`[16 16 16 16 16 15 14 16 11  6  4  4  5  4  4  3  3 14 16  2  2 14  2  0 0]`
\ In total: 1838

=== The constant NMR bit allocation:
`[13 14 11 13 13 11 12 13  8  5  6  8  9 10 11  9  5 11 13  2  3 12  2  0 0]`
\ In total: 1839


#figure(
  image("assets/1d.png", width: 90%),
  caption: [The MDCT, masked threshold, and noise floors for different bit allocation strategies.],
) <fig-1d>

==
Among the 6 conditions (128 vs 192 kb/s/ch, 3 bit allocation strategies),
- The uniform bit allocation strategy yields pretty bad output result, the one with 192 kb/s/ch better than the one with 128 kb/s/ch. They have a strong time-domain aliasing artifact.
- Both the constant SMR and constant NMR bit allocation strategies nicely reconstructed the original audio. For them, it is hard to tell which one is better psychoacousically in both the data rate.

=
==
See `BitAlloc` in `bitalloc.py`.

I implemented a bisection method that finds the constant distance below the masked threshold, then derives the bit allocation from it. Then, I "sanitize" the bit allocation by removing one bits and allocating the remaining bit budget.

==

- With data rate of 128 kb/s/ch, the bit allocation:
`[11 11  9 10  9  7  9 10  5  2  3  5  6  7  7  7  3  8 10  0  0  9  0  0 0]`
\ In total: 1160.

- With data rate of 192 kb/s/ch, the bit allocation:
`[14 13 11 12 12 10 12 13  7  4  5  8  9 10 10 10  6 10 12  2  3 12  0  2 0]`
\ In total: 1843.

#figure(
  image("assets/2b.png", width: 80%),
  caption: [The MDCT, masked threshold, and noise floors of two data rates.],
) <fig-2b>

$
  "codingParams.targetBitsPerSample" = cases(2.667 quad &I = 128 "kb/s/ch", 4 quad &I = 196 "kb/s/ch")
$
Also, I notice that to align with the setting in Problem 1, the following parameters should be set:
- `codingParams.nMDCTLines = 512`
- `codingParams.nScaleBits = 4`
- `codingParams.nMantSizeBits = 4`

I used `HW_Test_File.wav` for the input audio.
- The initial size is 937.5 KB.
- The compressed size of 128 kb/s/ch is 160.7 KB, which yields a compression ratio of 5.83 : 1 (close to the theoretical 6 : 1).
- The compressed size of 192 kb/s/ch is 238.7 KB, which yields a compression ratio of 3.93 : 1 (close to the theoretical 4 : 1).

==
The main tweaking I tried is to add noise maskers to the SMR calculation. Under the data rate of 128 kb/s/ch (`targetBitsPerSample=2.667`), I tested `castanet.wav`, `harpsichord.wav`, `spgm.wav`.

With `harpsichord.wav`, the difference isn't noticeable. But with `castanet.wav` and `spgm.wav`, adding noise maskers to the SMR calculation yields less artifacts (though subtle). Without noise maskers, the artifacts are more "harmonic", which is especially unnatural with speech.

==

1. *Pre-Echo*
  - Most noticeable in transient-rich sounds, especially the **castanet** and **harpsichord** excerpts.
  - At lower bit rates, the compression algorithm fails to allocate enough bits to short transients, causing a **smearing effect** before the actual attack of the sound.

2. *Aliasing*
  - More prominent in high-frequency content, particularly in **harpsichord** recordings.
  - At lower bit rates, aliasing manifests as an unnatural, harsh distortion in the upper harmonics. This might be due to the aggressive quantization of high-frequency components when using a psychoacoustic model.

3. *"Birdies"*
  - Most evident in sustained harmonic sounds like **the harpsichord**.
  - Appears as artificial, high-frequency warbling or chirping noises that sound unnatural. These arise due to quantization noise and imperfect reconstruction of spectral components.

4. *Speech Reverberation ("Metallic" Sound)*
  - Clearly noticeable in the **German male speaker** recording at low bit rates. Sounds robotic and unnatural, with a metallic or hollow resonance.

5. *Multichannel Artifacts (Stereo Imaging Issues)*
  - Mono sounds become somewhat stereo. Elements shift unnaturally within the stereo field.

#import "@preview/problemst:0.1.0": pset

#set par(justify: true)

#show: pset.with(
  class: "MUSIC 422",
  student: "Lejun Min",
  title: "Homework 4",
  date: datetime.today(),
  subproblems: "1.a.i)",
)

The code for the plots and the tables is in `plots.ipynb`.

=
#counter(heading).step(level: 2)
==

#figure(
  image("assets/1b.png", width: 80%),
  caption: [SPL of a Hanning-windowed signal with different block sizes.],
) <fig-1b>
\

#figure(
  caption: [Peak detection results for each block size.],
  table(
    columns: (auto, auto, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: (x: none),
    table.header([], [*Block Sizes*], table.cell(colspan: 6, [*Peaks*])),
    table.cell(rowspan: 3, [*SPL (dB)*]),
    [512], [ 196.967 ], [], [ 459.899 ], [ 878.499 ], [4400.006 ], [8800.055],
    table.vline(x: 1, start: 1),
    table.vline(x: 2, start: 1),
    [1024], [ 226.025 ], [ 322.289 ], [ 419.419 ], [ 880.109 ], [4400.028 ], [8800.218],
    [2048], [ 219.681 ], [ 330.034], [ 440.079], [ 880.517], [ 4400.109], [ 8799.435],
    table.cell(rowspan: 3, [*Frequency (Hz)*]),
    [512], [92.067], [], [ 84.475], [ 80.045], [ 74.061], [ 68.038],
    [1024], [94.462], [ 90.859], [ 88.705], [ 80.072], [ 74.058], [ 68.025],
    [2048], [94.020], [ 89.618], [ 87.114], [ 80.016], [ 74.046], [ 67.969],
  ),
)

From the table, we can see that block size $N$ influences the peaks detected. The larger the block size, the better and more accurate the peaks are detected. With $N=512$, only 5 peaks are detected, and the first two aren't correct. With $N=1024$, all 6 peaks are detected but with some minor discrepancy. With $N=2048$, all 6 peaks are detected and accurately align with the answer.

==

#figure(
  image("assets/1c.png", width: 80%),
  caption: [The SPL curve of the threshold in quiet and the signal in 1.b.],
) <fig-1c>

==
The obtained Bark values are:
`
0.000  0.987  1.963  2.920  3.847  4.823  5.830  6.920  7.985  9.007
10.080 11.109 12.115 13.104 14.047 14.976 15.888 16.814 17.803 18.878
19.987 21.061 22.178 23.195
`

The obtained values using Bark formula basically match the $z$ as shown in Table 1 on pp. 182-3, though not perfectly.

==

#figure(
  image("assets/1e.png", width: 80%),
  caption: [The signal, threshold in quiet, masking curves, critical band boundaries, and masked threshold.],
) <fig-1e>

In the implementation, I used $alpha=oo$ for the addition of masking (calculating the maximum value across all the masking thresholds and the threshold in quiet).

For all the critical bands (centers at 226, 322, 419, 880, 4400, 8800 Hz), the signal SPL exceeds the masked threshold somewhere in that band.

==
In the `ScaleFactorBands` object,
- `nBands = 25`
- `lowerLine = [  0   3   5   7   9  11  14  17  20  24  28  32  37  43  50  58  68  79 94 114 137 165 203 256 331]`
- `upperLine = [  2   4   6   8  10  13  16  19  23  27  31  36  42  49  57  67  78  93 113 136 164 202 255 330 511]`
- `nLines = [  3   2   2   2   2   3   3   3   4   4   4   5   6   7   8  10  11  15 20  23  28  38  53  75 181]`

==
The obtained `SMR`s are:\
#figure(
  caption: [The obtained SMRs in each critical band.],
  table(
    columns: (auto,) * 8,
    [*Critical Band*], [0], [1], [2], [3], [4], [5], [6],
    [*SMR (dB)*], [ 12.394 ], [ 10.35 ], [ -0.095 ], [ 6.008], [ 8.09], [ -8.031], [ 3.634],
    [*Critical Band*], [7],[8], [9], [10], [11], [12], [13],
    [*SMR (dB)*], [ 10.989], [ -21.815], [ -42.281], [ -33.377], [ -19.488], [ -10.014], [ -5.758],
    [*Critical Band*], [14], [15],[16], [17], [18], [19], [20],
    [*SMR (dB)*] , [ -4.118], [ -4.223], [ -31.227], [ -3.837], [ 8.855], [ -51.302], [ -46.144],
    [*Critical Band*], [21], [22], [23], [24], [], [], [],
    [*SMR (dB)*] , [ 6.508], [ -62.257], [ -57.486], [ -87.364],
  ),
)

I implemented both tonal and noise masker detection according to Chapter 11.5.2 in the textbook (see `indentifyMaskers` in `psychoac.py`). However, the noise masker is turned off during the SMR calculation for the coherence with 1.e.

==
I tested the given `HW_Test_File.wav`, `oboe.wav`, and `spfe.wav` (speech-female-english). My discoveries are:
- The current compression ratio is around 6.2 : 1. The encoding takes most of the time. It roughly takes 3 seconds to encode 1 second of the input audio on my laptop.
- The overall compressed quality for highly tonal audio files is great. I can barely tell the difference. `HW_Test-File` yields near-perfect reconstruction. For `oboe.wav`, the codec mildly muffles the sound of button pressing, but the main part remains identically clear.
- The compressed quality for human speech is not good. I can hear the "metallic" speech reverberation artifact, and sometimes there is a multichannel artifact (stereo imaging). Generally, the current codec isn't good at capturing short-term transient sounds.

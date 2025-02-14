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

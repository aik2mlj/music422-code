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



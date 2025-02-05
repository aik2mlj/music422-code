#import "@preview/problemst:0.1.0": pset

#set par(justify: true)

#show: pset.with(
  class: "MUSIC 422",
  student: "Lejun Min",
  title: "Homework 4",
  date: datetime.today(),
  subproblems: "1.a.i)",
)

=
#counter(heading).step(level: 2)
==
The code for the plot and the table is in `plots.ipynb`.

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
    [512], [ 196.967 ], [], [ 459.899 ],[ 878.499 ],[4400.006 ],[8800.055],
    table.vline(x: 1, start: 1),
    table.vline(x: 2, start: 1),
    [1024], [ 226.025 ],[ 322.289 ],[ 419.419 ],[ 880.109 ],[4400.028 ],[8800.218],
    [2048], [ 219.681 ],[ 330.034],[ 440.079],[ 880.517],[ 4400.109],[ 8799.435],
    table.cell(rowspan: 3, [*Frequency (Hz)*]),
    [512], [92.067], [], [ 84.475],[ 80.045],[ 74.061],[ 68.038],
    [1024], [94.462],[ 90.859],[ 88.705],[ 80.072],[ 74.058],[ 68.025],
    [2048], [94.020],[ 89.618],[ 87.114],[ 80.016],[ 74.046],[ 67.969],
  ),
)

From the table, we can see that block size $N$ influences the peaks detected. The larger the block size, the better and more accurate the peaks are detected. With $N=512$, only 5 peaks are detected, and the first two aren't correct. With $N=1024$, all 6 peaks are detected but with some minor discrepancy. With $N=2048$, all 6 peaks are detected and accurately align with the answer.

==

#figure(
  image("assets/1c.png", width: 80%),
  caption: [The SPL curve of the threshold in quiet and the signal in 1.b.],
) <fig-1c>



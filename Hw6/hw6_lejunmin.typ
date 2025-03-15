#import "@preview/problemst:0.1.0": pset

#set par(justify: true)

#show: pset.with(
  class: "MUSIC 422",
  student: "Lejun Min",
  title: "Homework 6",
  date: datetime.today(),
  subproblems: "1.a.i)",
)
#let avg(x) = [$angle.l #x angle.r$]

=
==
The set I prepared:
`spmg`, `harpsichord`, `castanets`, `glockenspiel`, `oboe`.

==
Done.

==
#figure(
  caption: [ITU-R 5-grade impairment scale of the critical materials.],
  table(
    columns: (auto,) * 6,
    [], [`spmg`], [`harpsichord`], [`castanets`], [`glockenspiel`], [`oboe`],
    [`s3m5`], [4.5], [4.8], [4.8], [4.2], [4],
    [`b1s3m5`], [3], [4.7], [4.7], [3.5], [3],
    [`fb1s3m5`], [3.4], [4.2], [2], [4], [4.2],
    [`128kbps`], [4.8], [4.5], [4.2], [4.7], [4.8],
    [`192kbps`], [5], [5], [4.7], [4.8], [4.7],
  ),
)

Surprisingly, `s3m5` performs comparatively good among the five algorithms. This is probably because it uses 8 bits per sample compared to 2.667 / 4 bits per sample for `128kbps` / `192kbps`, which is good enough for the transient samples. `b1s3m5` always performs slightly worse than `s3m5`. `fb1s3m5` is really bad on transient samples but okay on tonal ones.

`192kbps` definitely outperforms `128kbps`, and they are both pretty good. They does not perform as well as `s3m5` on those transient sounds (`castanets`), but they are much better than `fb1s3m5`.

==

In total, 10 people participated in the listening test, 6 of whom are my classmates in Music 422, and the other 4 are my friends. The test was mainly conducted in the ballroom of CCRMA with headphones, some sessions were conducted in my dorm (also with headphones). The participants were asked to listen to the audio samples and rate them according to the ITU-R 5-grade impairment scale. The results are shown in the table below.

#figure(
  grid(
    columns: (1fr, 1fr),
    image("assets/1d-128.png"), image("assets/1d-192.png"),
  ),
  caption: [ITU-R BS.1116 test result of 128kbps and 192kbps audio samples.],
) <fig-1d>

- We can clearly see that in general, 192kbps performs better than 128kbps. The difference is obvious in `harpsichord`, `oboe`, but minor in `glockenspiel` and `spgm`. The improvement is more significant for tonal sounds (`harpsichord`, `oboe`), and less significant for transient sounds (`castanets`, `glockenspiel`, `spgm`).

- Within the same data rate, `spgm` has the best psychoacoustical quality. The worst is `castanets`. With the data rate of 192kbps, `harpsichord`, `spgm`, and `oboe` achieve nearly imperceptible quality loss.

- The variance of the results is huge! I noticed that some of my friends tend to grade the samples more boldly, e.g., having larger grading gap between the reference and the compressed samples. Some of them mistakenly regarded the compressed one as the reference instead, leading to a pretty large positive SDG value. Comparatively, my classmates are more conservative in grading, and usually correctly discerned the reference and the compressed samples.

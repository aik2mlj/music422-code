#import "@preview/problemst:0.1.0": pset

#show: pset.with(
  class: "MUSIC 422",
  student: "Lejun Min",
  title: "Homework 2",
  date: datetime.today(),
  subproblems: "1.a.i)",
)

#set math.mat(delim: "[")
#set math.vec(delim: "[")
#let phi = [#sym.phi.alt]
#let ww = $omega$
#let w0 = $omega_0$
#let dt = $d t$
#let df = $d f$
#let avg(x) = [$angle.l #x angle.r$]

=
#table(
  // columns: 6 * (1fr,),
  columns: (auto, 1fr, 1fr, 1fr, 1fr, 1fr),
  align: center + horizon,
  table.header(
    table.cell(rowspan: 2, [*Input*], align: center + bottom),
    table.cell(rowspan: 2, [12 bit binary], align: center + bottom),
    table.cell(colspan: 4, [*Output = $Q^(-1)(Q("Input"))$*]),
    [8 bit midtread],
    [12 bit midtread],
    [3s5m FP],
    [3s5m BFP N=1],
  ),
  [-0.99], [111111101011], [-0.98824], [-0.98999], [-0.98462], [-0.96899],
  [-0.38], [101100001010], [-0.37647], [-0.37998], [-0.38291], [-0.39072],
  [-0.10], [100011001101], [-0.10196], [-0.10012], [-0.09963], [-0.09768],
  [-0.01], [100000010100], [-0.00784], [-0.00977], [-0.00977], [-0.01026],
  [-0.001], [100000000010], [0], [-0.00098], [-0.00098], [-0.00098],
  [0.0], [000000000000], [0], [0], [0], [0],
  [0.05], [000001100110], [0.04706], [0.04982], [0.04982], [0.04884],
  [0.28], [001000111101], [0.28235], [0.27985], [0.2735], [0.26569],
  [0.65], [010100110011], [0.65098], [0.65006], [0.64078], [0.65641],
  [0.97], [011111000010], [0.97255], [0.96996], [0.98462], [0.96899],
  [1.0], [011111111111], [0.99608], [0.99976], [0.98462], [0.96899],
)

#counter(heading).step(level: 2)
#counter(heading).step(level: 2)
#counter(heading).step(level: 2)
==
===
The quantization noise in _8-bit midtread uniform quantization_ is universally loud, and especially audible for low-power parts.

The quantization noise in _3 scale bits, 5 mantissa bits midtread floating point quantization_ is much better for low-power parts, but more audible in high-power parts.

===
For low-power parts, _12-bit uniform quantization_ has similar quality to _3
scale bits, 5 mantissa bits floating point quantization_; for high-power parts, _6-bit uniform quantization_ has similar quality.

===
- _Float point quantization_ has less artifacts than _block float point quantization_ given the same number of scale and mantissa bits.
- As $N$ increases for _block float point quantization_, the quality gradually degrades.

===
Given that the uncompressed audio is 16 bits per sample,

====
$
  C = 16 / 8 : 1 = 2:1
$

====
$
  C = 16 / 8 : 1 = 2:1
$

====
Since $N$ samples share one common scale in a block,
$
  "bits per block" = 3 + 5N\
  R_"total" = "bits per block" / N = (3 + 5N) / N
$
Therefore,
$
  C &= 16 / R_"total" : 1 = (16 N) / (3 + 5N) : 1\
  &= cases(2":"1 quad quad &N=1, 2.46":"1 & N=2, 3.08":"1 & N=16)
$

===
I tested the scenario of compression rate $2 : 1$, which can correspond to
- 8 bits for _midtread uniform quantization_.
- 3 scale bits, 5 mantissa bits for _float point quantization_.
- 4 scale bits, 7 mantissa bits for _block float point quantization_ with $N=16$.

In this case, _block point quantization_ clearly offers better quality with less artifacts, followed by _float point quantization_ and _midtread uniform quantization_.

=
==
The average signal power is defined as the mean value of $y^2$ over the duration $T$, i.e.,
$
  avg(y^2) eq.def 1 / N sum_(n=0)^N abs(y[n])^2 = 1 / (T f_s) sum_(n=0)^(T f_s) abs(y[n])^2
$

==
See `plots.ipynb` for the corresponding python code.

#figure(
  image("assets/2b.png", width: 80%),
  caption: [SNR vs input level for different quantization methods],
) <fig-2b>

==
Compared to the results on page 38, this reproduction of the experiment successfully shows similar plots.
/ Similarity: The shape of the curves are the same from low input level to high input level less than -4.771 dB.
/ Difference: The reproduced plots do not drop when the input level is larger than -4.771 dB. Also, the SNR values at the same input level are slightly different. This is due to the different choices of the reference signal level.

==
At very high input power, the _float point quantizer_ has similar performance as the _6 bits uniform quantizer_, and the performance remains unchanged for a wide range of input power. This is because that given a high input power, the scale bits that store the number of leading zeros become useless. Therefore, the equivalent number of uniform quantization bits is the number of mantissa bits plus 1 (the omitted leading 1 after the leading zeros), which is $5+1=6$.

At very low input power, the _float point quantizer_ has the same performance as the _12 bits uniform quantizer_. It drops just like the latter as the input power drops. This is because that now the scale bits perfectly represent $2^("nScaleBits") - 1$ leading zeros. Along with the mantissa bits, the equivalent number of uniform quantization bits is $2^("nScaleBits") - 1 + "nMantissaBits"$, which is $2^3 - 1 + 5 = 12$.

The main difference between the _FP quantizer_ and the _BFP quantizer_ is that the latter performs slightly worse (1 bit difference) than the former when the input signal power is not too low. They perform the same given a very low input power.

=
Yes, I have read the assigned chapters.



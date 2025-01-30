#import "@preview/problemst:0.1.0": pset
#import "@preview/physica:0.9.3": *

#show: pset.with(
  class: "MUSIC 422",
  student: "Lejun Min",
  title: "Homework 1",
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

For all the corresponding codes, please see `plots.ipynb` in the submitted archive file.

=
==
===
$
  I_"CD" = F_"sCD" times "#channel" = 44.1 times 16 times 2 "kb/s" = 1.4112 "Mb/s"
$

===
The size
$
  S_"CD" = I_"CD" times T_"CD" = 1.4112 "Mb/s" times 1800 "s" = 2540.16 "Mb" = 317.52 "MB" = 0.318 "GB"
$
Here we use the disk storage convention ($1 times 10^3$).

===
$
  S'_"CD" = I'_"CD" times T_"CD" = 48 "kb/s/ch" times 2 "ch" times 1800 "s" = 17280 "kb" = 21.6 "MB"
$

===
Compression ratio
$
  C = S_"CD" / S'_"CD":1 = 14.7 : 1.
$
The equivalent number of bits per sample
$
  R = R_"CD" / C = 1.088 "bits/sample"
$


==
===
$
  T_"modem" = T_"CD" times I_"CD" / I_"modem" = 4times 60 "s" times 1411.2 / 9.6 = 35280 "s" = 9.8 "h"
$

===
$
  T_"modem" = T_"CD" times I'_"CD" / I_"modem" = 240s times 48 / 9.6 = 1200s = 0.33h
$

===
$
  C = I_"CD" / I'_"CD" : 1 = 1411.2 / 48 : 1 = 29.4 : 1
$

==
===
$
  T_"net" = T_"CD" times I_"CD" / I_"net" = 60 "min" times 1.4112 / 20 = 4.23 "min"
$

===
$
  T_"net" = T_"CD" times I'_"CD" / I_"net" = 3600s times 0.048 / 20 = 8.64 s
$

===
To reach the same total data rate,
$
  n times I'_"CD, per channel" = I_"CD"
$
Therefore
$
  n = I_"CD" / I'_"CD, per channel" = 1411.2 / 48 "ch" = 29.4 "ch"
$

==
===
For 96 kHz sampling rate,
$
  I_"DVD" = 96 times 24 times 5 "kb/s" = 11.5 "Mb/s"
$
For 192 kHz sampling rate,
$
  I_"DVD" = 192 times 24 times 5 "kb/s" = 23 "Mb/s"
$

===
For 96 kHz sampling rate,
$
  S_"DVD" = I_"DVD" times T_"DVD" = 41400 "Mb/s" = 5.175 "GB"
$
For 192 kHz sampling rate,
$
  S_"DVD" = I_"DVD" times T_"DVD" = 82800 "Mb/s" = 10.35 "GB"
$

===
For 96 kHz sampling rate,
$
  C = I_"DVD" / I_"CD" : 1 = 11.5 / 1.4112 : 1 = 8.15 : 1
$
For 192 kHz sampling rate,
$
  C = I_"DVD" / I_"CD" : 1 = 23 / 1.4112 : 1 = 16.30 : 1
$

===
For 96 kHz sampling rate,
$
  C = I_"DVD" / I_"DVD-Video" : 1 = 11.5 / 6.144 : 1 = 1.87 : 1
$
For 192 kHz sampling rate,
$
  C = I_"DVD" / I_"DVD-Video" : 1 = 23 / 6.144 : 1 = 3.74 : 1
$

===
For 96 kHz sampling rate,
$
  C = I_"DVD" / I_"DVD-Audio" : 1 = 11.5 / 9.6 : 1 = 1.20 : 1
$
For 192 kHz sampling rate,
$
  C = I_"DVD" / I_"DVD-Audio" : 1 = 23 / 6.144 : 1 = 2.40 : 1
$

=
==
#figure(
  image("assets/2a.png", width: 90%),
  caption: [The windowed signal on two different time ranges],
) <fig-2a>

==
The bias
$
  mu = 1 / T integral_0^T x(t) d t = 2 integral_0^(1 / 2) 1 / 2 [cos(1998 pi t) - cos(2002 pi t)] d t = 0
$

The average power
$
  P_"avg" &= 1 / T integral_0^T abs(x(t))^2 d t = 2 integral_0^(1 / 2) sin^2(2000pi t)sin^2(2pi t) d t\
  &= 2 integral_0^(1 / 2) ((1-cos(4000pi t)) / 2)((1-cos(4pi t)) / 2) d t\
  &= 1 / 2 integral_0^(1 / 2) (1- cos(4000pi t) - cos(4pi t) + 1 / 2 cos(4004 pi t) + 1 / 2 cos(3996 pi t)) d t\
  &= 1 / 4
$


The energy
$
  E = integral_0^T abs(x(t))^2 d t = T dot P_"avg" = 1 / 8
$

The standard deviation
$
  sigma = sqrt(1/T integral_0^T abs(x(t) - mu)^2 d t) = sqrt(1/T integral_0^T abs(x(t))^2 d t) = sqrt(P_"avg") = 1 / 2
$

==
Rewrite the signal equation as
$
  x(t) = cases(1/2 (cos(1998 pi t) - cos(2002 pi t)) quad & "for" 0<=t<=1/2, 0 & "elsewhere")
$

// The Fourier Transform of a cosine function is
// $
//   cal(F){cos(w0 t)} = pi[delta(ww - w0) + delta(ww + w0)]
// $
// So,
// $
//   cal(F){x(t)} = pi / 2 [delta(ww-1998pi) + delta(ww+1998pi) - delta(ww-2002pi) - delta(ww+2002pi)]
// $

The Fourier Transform of this signal
$
  X(f) &= integral_(-oo)^oo x(t) e^(-j 2pi f t) d t\
  &= 1 / 2 (integral_0^(1 / 2) cos(2pi dot 999 t) e^(-j 2pi f t) d t - integral_0^(1 / 2) cos(2pi dot 1001 t) e^(-j 2pi f t) d t)\
$

Note that
$
  integral_0^T cos(2pi f_0 t) e^(-2pi f t) dt &= integral_0^T 1 / 2(e^(-j 2pi f_0 t) + e^(j 2pi f_0 t)) e^(-j 2pi f t) dt\
  &= 1 / 2 integral_0^T (e^(-j 2pi (f + f_0)t) + e^(-j 2pi(f-f_0)t)) dt \
  &= 1 / 2 integral_(-1 / 2T)^(1 / 2T) (e^(-j 2pi (f + f_0)(t'+1 / 2 T)) + e^(-j 2pi(f-f_0)(t'+1 / 2T))) dt' \
  &= T / 2[e^(-j pi(f+f_0)T) sinc((f+f_0)T) + e^(-j pi(f-f_0)T) sinc((f-f_0)T)]
$
where $sinc(x) = sin(pi x) / (pi x)$.

Therefore,
$
  X(f) = &1 / 8 [e^(-j pi / 2 (f+999)) sinc(1/2(f+999)) + e^(-j pi / 2 (f-999)) sinc(1/2(f-999)) \
    &- e^(-j pi / 2 (f+1001)) sinc(1/2(f+1001)) - e^(-j pi / 2 (f-1001)) sinc(1/2(f-1001))]
$

The plots are as follows:

#figure(
  image("assets/2c-1.png", width: 80%),
  caption: [Magnitude and phase of $X(f)$ around 1000 Hz.],
) <fig-2c-1>


#figure(
  image("assets/2c-2.png", width: 80%),
  caption: [Magnitude and phase of $X(f)$ around -1000 Hz.],
) <fig-2c-2>


==
The bias
$
  mu = 1 / T X(0) = 0
$

The average power
$
  P_"avg" &= 1 / T integral_0^T abs(X(f))^2 df\
  &approx 2 / 64 integral_0^(1 / 2) [2sinc(1/2(f+1000))]^2 df + integral_0^(12 / 2) [2sinc(1/2(f-1000))]^2 df\
  &approx 2 / 64 times (4+4) = 1 / 4
$

The energy
$
  E = P_"avg" dot T approx 1 / 4 times 1 / 2 = 1 / 8
$

The standard deviation
$
  sigma = P_"avg" - mu^2 approx 1 / 4
$

==

#figure(
  image("assets/2e.png", width: 60%),
  caption: [The sampled signal using scatter plot.],
) <fig-2e>

==

#figure(
  image("assets/2f-1.png", width: 60%),
  caption: [Sinc interpolation of sampled signal along with original signal.],
) <fig-2f-1>


#figure(
  image("assets/2f-2.png", width: 60%),
  caption: [Error between original and interpolated signal.],
) <fig-2f-2>

The interpolated signal matches the original signal well, yet the reconstruction is not perfect. The difference is because the implemented interpolation uses finite sample points $x[n]$ ranging from $t in [-0.005, 0.015]$, instead of infinite sample points from $n in [-oo, oo]$. The difference is more apparent near the bound of the time series, since there aren't enough local sampled values to reconstruct the original signal. (The left bound is not apparent since the value is 0).

=
☑️ Done!

=
==
☑️ Done!

==
The quantization noise is obvious. Generally, when the quantization bit is small (4, 6, 8), there is an audible white noise along with the original audio. The noise is gone when the audio is off. `nBit` above 12 is good enough to reconstruct the original audio.

The high frequency is especially distorted given a small `nBit`. There are audible discrete changing artifacts when the oboe sound fades, like small particles.

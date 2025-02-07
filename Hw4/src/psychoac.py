"""
psychoac.py -- masking models implementation

-----------------------------------------------------------------------
(c) 2011-2025 Marina Bosi & Richard E. Goldberg -- All rights reserved
-----------------------------------------------------------------------
"""

import numpy as np
from window import *


def SPL(intensity):
    """
    Returns the SPL corresponding to intensity
    """
    # This does not take care of the 2/N in MDCT
    return np.maximum(96 + 10.0 * np.log10(intensity), -30.0)


def Intensity(spl):
    """
    Returns the intensity for SPL spl
    """
    # This does not take care of the 2/N in MDCT
    return np.power(10, (spl - 96) / 10.0)


def Thresh(f):
    """Returns the threshold in quiet measured in SPL at frequency f (in Hz)"""

    f_floored = np.maximum(f, 20.0)
    f_khz = f_floored / 1000.0
    return (
        3.64 * np.pow(f_khz, -0.8)
        - 6.5 * np.exp(-0.6 * np.pow(f_khz - 3.3, 2))
        + 0.001 * np.pow(f_khz, 4)
    )


def Bark(f):
    """Returns the bark-scale frequency for input frequency f (in Hz)"""
    f_khz = np.array(f) / 1000.0
    return 13 * np.arctan(0.76 * f_khz) + 3.5 * np.arctan(np.pow(f_khz / 7.5, 2))


class Masker:
    """
    a Masker whose masking curve drops linearly in Bark beyond 0.5 Bark from the
    masker frequency
    """

    def __init__(self, f, SPL, isTonal=True):
        """
        initialized with the frequency and SPL of a masker and whether or not
        it is Tonal
        """
        self.f = f
        self.z = Bark(f)
        self.spl = SPL
        self.isTonal = isTonal
        self.delta = 16 if isTonal else 6

    def IntensityAtFreq(self, freq):
        """The intensity at frequency freq"""
        return self.IntensityAtBark(Bark(freq))

    def vIntensityAtFreq(self, freqVec):
        """The intensity at frequency freq"""
        return self.vIntensityAtBark(Bark(freqVec))

    def IntensityAtBark(self, z):
        """The intensity at Bark location z"""
        spl = self.spl - self.delta
        dz = z - self.z
        if dz < -0.5:
            spl += -27 * (abs(dz) - 0.5)
        elif dz > 0.5:
            spl += (-27 + 0.367 * max(self.spl - 40.0, 0.0)) * (abs(dz) - 0.5)
        return Intensity(spl)

    def vIntensityAtBark(self, zVec):
        """The intensity at vector of Bark locations zVec"""
        splVec = np.zeros_like(zVec)
        splVec += self.spl - self.delta
        dzVec = zVec - self.z
        splVec += np.where(dzVec < -0.5, -27 * (np.abs(dzVec) - 0.5), 0)
        splVec += np.where(
            dzVec > 0.5,
            (-27 + 0.367 * max(self.spl - 40.0, 0.0)) * (np.abs(dzVec) - 0.5),
            0,
        )
        return Intensity(splVec)


# Default data for 25 scale factor bands based on the traditional 25 critical bands
cbFreqLimits = [100, 200, 300, 400, 510, 630, 770, 920, 1080, 1270, 1480,
           1720, 2000, 2320, 2700, 3150, 3700, 4400, 5300, 6400, 7700, 9500, 12000, 15500]  # fmt: skip


def AssignMDCTLinesFromFreqLimits(nMDCTLines, sampleRate, flimit=cbFreqLimits):
    """
    Assigns MDCT lines to scale factor bands for given sample rate and number
    of MDCT lines using predefined frequency band cutoffs passed as an array
    in flimit (in units of Hz). If flimit isn't passed it uses the traditional
    25 Zwicker & Fastl critical bands as scale factor bands.
    """
    freqVec = np.arange(nMDCTLines) * sampleRate / (2 * nMDCTLines)
    indices = np.searchsorted(flimit, freqVec, side="right")  # left-close, right-open
    counts = np.bincount(indices, minlength=len(flimit) + 1)
    return counts


class ScaleFactorBands:
    """
    A set of scale factor bands (each of which will share a scale factor and a
    mantissa bit allocation) and associated MDCT line mappings.

    Instances know the number of bands nBands; the upper and lower limits for
    each band lowerLimit[i in range(nBands)], upperLimit[i in range(nBands)];
    and the number of lines in each band nLines[i in range(nBands)]
    """

    def __init__(self, nLines):
        """
        Assigns MDCT lines to scale factor bands based on a vector of the number
        of lines in each band
        nlines: return value of AssignMDCTLinesFromFreqLimits
        """
        self.nBands = len(nLines)
        self.lowerLine = np.concat(([0], np.cumsum(nLines)[:-1]))
        self.upperLine = np.cumsum(nLines) - 1
        self.nLines = nLines
        assert (self.nLines == self.upperLine - self.lowerLine + 1).any()


def getMaskedThreshold(data, MDCTdata, MDCTscale, sampleRate, sfBands):
    """
    Return Masked Threshold evaluated at MDCT lines.

    Used by CalcSMR, but can also be called from outside this module, which may
    be helpful when debugging the bit allocation code.
    """
    return np.zeros_like(0)  # TO REPLACE WITH YOUR CODE


def CalcSMRs(data, MDCTdata, MDCTscale, sampleRate, sfBands):
    """
    Set SMR for each critical band in sfBands.

    Arguments:
                data:       is an array of N time domain samples
                MDCTdata:   is an array of N/2 MDCT frequency coefficients for the time domain samples
                            in data; note that the MDCT coefficients have been scaled up by a factor
                            of 2^MDCTscale
                MDCTscale:  corresponds to an overall scale factor 2^MDCTscale for the set of MDCT
                            frequency coefficients
                sampleRate: is the sampling rate of the time domain samples
                sfBands:    points to information about which MDCT frequency lines
                            are in which scale factor band

    Returns:
                SMR[sfBands.nBands] is the maximum signal-to-mask ratio in each
                                    scale factor band

    Logic:
                Performs an FFT of data[N] and identifies tonal and noise maskers.
                Combines their relative masking curves and the hearing threshold
                to calculate the overall masked threshold at the MDCT frequency locations.
                                Then determines the maximum signal-to-mask ratio within
                each critical band and returns that result in the SMR[] array.
    """
    return np.zeros_like(0)  # TO REPLACE WITH YOUR CODE


# -----------------------------------------------------------------------------

# Testing code
if __name__ == "__main__":
    # 1.d)
    fls = [0, 100, 200, 300, 400, 510, 630, 770, 920, 1080, 1270, 1480,
           1720, 2000, 2320, 2700, 3150, 3700, 4400, 5300, 6400, 7700, 9500, 12000]  # fmt: skip
    np.set_printoptions(precision=3)
    print(Bark(fls))

    # 1.f)
    nMDCTLines = 512
    sampleRate = 48000
    nLines = AssignMDCTLinesFromFreqLimits(nMDCTLines, sampleRate)
    scaleFactorBands = ScaleFactorBands(nLines)
    print("nBands =", scaleFactorBands.nBands)
    print("lowerLine =", scaleFactorBands.lowerLine)
    print("upperLine =", scaleFactorBands.upperLine)
    print("nLines =", scaleFactorBands.nLines)

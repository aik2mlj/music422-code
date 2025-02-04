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
    return np.maximum(96 + 10.0 * np.log10(intensity), -30.0)


def Intensity(spl):
    """
    Returns the intensity for SPL spl
    """
    return np.power(10, (spl - 96) / 10.0)


def Thresh(f):
    """Returns the threshold in quiet measured in SPL at frequency f (in Hz)"""

    return np.zeros_like(f)  # TO REPLACE WITH YOUR CODE


def Bark(f):
    """Returns the bark-scale frequency for input frequency f (in Hz)"""
    return np.zeros_like(f)  # TO REPLACE WITH YOUR CODE


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
        pass  # TO REPLACE WITH YOUR CODE

    def IntensityAtFreq(self, freq):
        """The intensity at frequency freq"""
        return 0  # TO REPLACE WITH YOUR CODE

    def IntensityAtBark(self, z):
        """The intensity at Bark location z"""
        return 0  # TO REPLACE WITH YOUR CODE

    def vIntensityAtBark(self, zVec):
        """The intensity at vector of Bark locations zVec"""
        return np.zeros_like(zVec)  # TO REPLACE WITH YOUR CODE


# Default data for 25 scale factor bands based on the traditional 25 critical bands
cbFreqLimits = []  # TO REPLACE WITH THE APPROPRIATE VALUES


def AssignMDCTLinesFromFreqLimits(nMDCTLines, sampleRate, flimit=cbFreqLimits):
    """
    Assigns MDCT lines to scale factor bands for given sample rate and number
    of MDCT lines using predefined frequency band cutoffs passed as an array
    in flimit (in units of Hz). If flimit isn't passed it uses the traditional
    25 Zwicker & Fastl critical bands as scale factor bands.
    """
    return np.zeros(len(flimit), dtype=np.int)  # TO REPLACE WITH YOUR CODE


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
        """
        pass  # TO REPLACE WITH YOUR CODE


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
    pass  # TO REPLACE WITH YOUR CODE

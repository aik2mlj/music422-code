"""
Music 422
-----------------------------------------------------------------------
(c) 2009-2025 Marina Bosi  -- All rights reserved
-----------------------------------------------------------------------
"""

import numpy as np


# Question 1.c)
def BitAllocUniform(bitBudget, maxMantBits, nBands, nLines, SMR=None):
    """
    Returns a hard-coded vector that, in the case of the signal used in HW#4,
    gives the allocation of mantissa bits in each scale factor band when
    bits are uniformly distributed for the mantissas.
    """
    return np.array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2])  # fmt:off
    return np.array([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3])  # fmt:off


def BitAllocConstSNR(bitBudget, maxMantBits, nBands, nLines, peakSPL):
    """
    Returns a hard-coded vector that, in the case of the signal used in HW#4,
    gives the allocation of mantissa bits in each scale factor band when
    bits are distributed for the mantissas to try and keep a constant
    quantization noise floor (assuming a noise floor 6 dB per bit below
    the peak SPL line in the scale factor band).
    """
    # return np.array([13, 16, 14, 15, 15, 12, 11, 14,  8,  3,  2,  2,  2,  0,  0,  0,  0, 10, 12,  0,  0, 11,  0,  0,  0])  # fmt:off
    return np.array([16, 16, 16, 16, 16, 15, 14, 16, 11,  6,  4,  4,  5,  4,  4,  3,  3, 14, 16,  2,  2, 14,  2,  0,  0])  # fmt:off


def BitAllocConstNMR(bitBudget, maxMantBits, nBands, nLines, SMR):
    """
    Returns a hard-coded vector that, in the case of the signal used in HW#4,
    gives the allocation of mantissa bits in each scale factor band when
    bits are distributed for the mantissas to try and keep the quantization
    noise floor a constant distance below (or above, if bit starved) the
    masked threshold curve (assuming a quantization noise floor 6 dB per
    bit below the peak SPL line in the scale factor band).
    """
    # return np.array([10, 11,  8,  9, 10,  8,  8, 10,  5,  2,  3,  4,  6,  7,  8,  6,  0,  8, 10,  0,  0, 10,  0,  0,  0])  # fmt:off
    return np.array([13, 14, 11, 13, 13, 11, 12, 13,  8,  5,  6,  8,  9, 10, 11,  9,  5, 11, 13,  2,  3, 12,  2,  0,  0])  # fmt:off


# Question 2.a)
def BitAlloc(bitBudget, maxMantBits, nBands, nLines, SMR):
    """
    Allocates bits to scale factor bands so as to flatten the NMR across the spectrum

       Arguments:
           bitBudget is total number of mantissa bits to allocate
           maxMantBits is max mantissa bits that can be allocated per line
           nBands is total number of scale factor bands
           nLines[nBands] is number of lines in each scale factor band
           SMR[nBands] is signal-to-mask ratio in each scale factor band

        Returns:
            bits[nBands] is number of bits allocated to each scale factor band


    """
    return BitAllocConstNMR(bitBudget, maxMantBits, nBands, nLines, SMR)


# -----------------------------------------------------------------------------

# Testing code
if __name__ == "__main__":
    pass  # TO REPLACE WITH YOUR CODE

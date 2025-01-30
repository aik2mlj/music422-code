"""
Music 422 Marina Bosi

- mdct.py -- Computes a reasonably fast MDCT/IMDCT using the FFT/IFFT

-----------------------------------------------------------------------
© 2009-2025 Marina Bosi & Richard E. Goldberg -- All rights reserved
-----------------------------------------------------------------------

"""

### ADD YOUR CODE AT THE SPECIFIED LOCATIONS ###

import numpy as np


### Problem 1.a ###
def MDCTslow(data, a, b, isInverse=False):
    """
    Slow MDCT algorithm for window length a+b following pp. 130 of
    Bosi & Goldberg, "Introduction to Digital Audio..." book
    and where the 2/N factor is included in the forward transform instead of inverse.
    a: left half-window length
    b: right half-window length
    """

    ### YOUR CODE STARTS HERE ###

    return np.zeros_like(data)  # CHANGE THIS
    ### YOUR CODE ENDS HERE ###


### Problem 1.c ###
def MDCT(data, a, b, isInverse=False):
    """
    Fast MDCT algorithm for window length a+b following pp. 141-143 of
    Bosi & Goldberg, "Introduction to Digital Audio..." book
    and where the 2/N factor is included in forward transform instead of inverse.
    a: left half-window length
    b: right half-window length
    """

    ### YOUR CODE STARTS HERE ###

    return np.zeros_like(data)  # CHANGE THIS
    ### YOUR CODE ENDS HERE ###


def IMDCT(data, a, b):
    ### YOUR CODE STARTS HERE ###

    return np.zeros_like(data)  # CHANGE THIS
    ### YOUR CODE ENDS HERE ###


# -----------------------------------------------------------------------------

# Testing code
if __name__ == "__main__":
    ### YOUR TESTING CODE STARTS HERE ###

    pass  # THIS DOES NOTHING

    ### YOUR TESTING CODE ENDS HERE ###

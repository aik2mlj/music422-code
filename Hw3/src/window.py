"""

Music 422  Marina Bosi

window.py -- Defines functions to window an array of discrete-time data samples

-----------------------------------------------------------------------
© 2009-2025 Marina Bosi & Richard E. Goldberg -- All rights reserved
-----------------------------------------------------------------------


"""

### ADD YOUR CODE AT THE SPECIFIED LOCATIONS ###

import numpy as np


### Problem 1.d ###
def SineWindow(dataSampleArray):
    """
    Returns a copy of the dataSampleArray sine-windowed
    Sine window is defined following pp. 106-107 of
    Bosi & Goldberg, "Introduction to Digital Audio..." book
    """

    ### YOUR CODE STARTS HERE ###

    return np.zeros_like(dataSampleArray)  # CHANGE THIS
    ### YOUR CODE ENDS HERE ###


def HanningWindow(dataSampleArray):
    """
    Returns a copy of the dataSampleArray Hanning-windowed
    Hann window is defined following pp. 106-107 of
    Bosi & Goldberg, "Introduction to Digital Audio..." book
    """

    ### YOUR CODE STARTS HERE ###

    return np.zeros_like(dataSampleArray)  # CHANGE THIS
    ### YOUR CODE ENDS HERE ###


### Problem 1.d - OPTIONAL ###
def KBDWindow(dataSampleArray, alpha=4.0):
    """
    Returns a copy of the dataSampleArray KBD-windowed
    KBD window is defined following the KDB Window handout in the
        Canvas Files/Assignments/HW3 folder
    """

    ### YOUR CODE STARTS HERE ###

    return np.zeros_like(dataSampleArray)  # CHANGE THIS
    ### YOUR CODE ENDS HERE ###


# -----------------------------------------------------------------------------

# Testing code
if __name__ == "__main__":
    ### YOUR TESTING CODE STARTS HERE ###

    pass  # THIS DOES NOTHING

    ### YOUR TESTING CODE ENDS HERE ###

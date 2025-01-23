"""
Music 422 - Marina Bosi

quantize.py -- routines to quantize and dequantize floating point values
between -1.0 and 1.0 ("signed fractions")

-----------------------------------------------------------------------
© 2009-2025 Marina Bosi & Richard E. Goldberg -- All rights reserved
-----------------------------------------------------------------------
"""

### ADD YOUR CODE AT THE SPECIFIED LOCATIONS ###

import quantize
import numpy as np


### Problem 1.a.i ###
def QuantizeUniform(aNum, nBits):
    """
    Uniformly quantize signed fraction aNum with nBits
    """
    # Notes:
    # The overload level of the quantizer should be 1.0

    aQuantizedNum = 0

    ### YOUR CODE STARTS HERE ###
    if aNum < 0:
        aQuantizedNum = 1 << (nBits - 1)  # sign bit

    if abs(aNum) >= 1:
        aQuantizedNum |= (1 << (nBits - 1)) - 1
    else:
        aQuantizedNum |= int((((1 << nBits) - 1) * abs(aNum) + 1) / 2)
    ### YOUR CODE ENDS HERE ###

    return aQuantizedNum


### Problem 1.a.i ###
def DequantizeUniform(aQuantizedNum, nBits):
    """
    Uniformly dequantizes nBits-long number aQuantizedNum into a signed fraction
    """

    aNum = 0.0  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###
    sign = -1 if (aQuantizedNum >> (nBits - 1)) == 1 else 1
    code = aQuantizedNum & ((1 << (nBits - 1)) - 1)
    aNum = sign * 2 * code / ((1 << nBits) - 1)
    ### YOUR CODE ENDS HERE ###

    return aNum


### Problem 1.a.ii ###
def vQuantizeUniform(aNumVec, nBits):
    """
    Uniformly quantize vector aNumberVec of signed fractions with nBits
    """

    aQuantizedNumVec = np.zeros_like(
        aNumVec, dtype=int
    )  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    # Notes:
    # Make sure to vectorize properly your function as specified in the homework instructions

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return aQuantizedNumVec


### Problem 1.a.ii ###
def vDequantizeUniform(aQuantizedNumVec, nBits):
    """
    Uniformly dequantizes vector of nBits-long numbers aQuantizedNumVec into vector of  signed fractions
    """

    aNumVec = np.zeros_like(
        aQuantizedNumVec, dtype=float
    )  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return aNumVec


### Problem 1.b ###
def ScaleFactor(aNum, nScaleBits=3, nMantBits=5):
    """
    Return the floating-point scale factor for a  signed fraction aNum given nScaleBits scale bits and nMantBits mantissa bits
    """
    # Notes:
    # The scale factor should be the number of leading zeros

    scale = 0  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return scale


### Problem 1.b ###
def MantissaFP(aNum, scale, nScaleBits=3, nMantBits=5):
    """
    Return the floating-point mantissa for a  signed fraction aNum given nScaleBits scale bits and nMantBits mantissa bits
    """

    mantissa = 0  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return mantissa


### Problem 1.b ###
def DequantizeFP(scale, mantissa, nScaleBits=3, nMantBits=5):
    """
    Returns a  signed fraction for floating-point scale and mantissa given specified scale and mantissa bits
    """

    aNum = 0.0  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return aNum


### Problem 1.c.i ###
def Mantissa(aNum, scale, nScaleBits=3, nMantBits=5):
    """
    Return the block floating-point mantissa for a  signed fraction aNum given nScaleBits scale bits and nMantBits mantissa bits
    """

    mantissa = 0  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return mantissa


### Problem 1.c.i ###
def Dequantize(scale, mantissa, nScaleBits=3, nMantBits=5):
    """
    Returns a  signed fraction for block floating-point scale and mantissa given specified scale and mantissa bits
    """

    aNum = 0.0  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return aNum


### Problem 1.c.ii ###
def vMantissa(aNumVec, scale, nScaleBits=3, nMantBits=5):
    """
    Return a vector of block floating-point mantissas for a vector of  signed fractions aNum given nScaleBits scale bits and nMantBits mantissa bits
    """

    mantissaVec = np.zeros_like(
        aNumVec, dtype=int
    )  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return mantissaVec


### Problem 1.c.ii ###
def vDequantize(scale, mantissaVec, nScaleBits=3, nMantBits=5):
    """
    Returns a vector of  signed fractions for block floating-point scale and vector of block floating-point mantissas given specified scale and mantissa bits
    """

    aNumVec = np.zeros_like(
        mantissaVec, dtype=float
    )  # REMOVE THIS LINE WHEN YOUR FUNCTION IS DONE

    ### YOUR CODE STARTS HERE ###

    ### YOUR CODE ENDS HERE ###

    return aNumVec


# -----------------------------------------------------------------------------

# Testing code
if __name__ == "__main__":
    ### YOUR TESTING CODE STARTS HERE ###
    pass
    ### YOUR TESTING CODE ENDS HERE ###

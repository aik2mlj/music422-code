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
    N = a + b
    n0 = (b + 1) / 2
    n_plus_n0 = np.arange(0, N) + n0
    k_plus_half = np.arange(0, N // 2) + 0.5
    cos_matrix = np.cos((2 * np.pi / N) * np.outer(n_plus_n0, k_plus_half))  # (N,N/2)

    if isInverse:
        summand = cos_matrix * data
        x = 2 * np.sum(summand, axis=1)
        return x
    else:
        summand = cos_matrix.T * data
        X = (2 / N) * np.sum(summand, axis=1)
        return X
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
    xs = [0, 1, 2, 3, 4, 4, 4, 4, 3, 1, -1, -3]
    a = 4
    b = 4
    N = a + b
    xs_pad = np.concat((xs, np.zeros(b)))
    xs_pad = np.concat((np.zeros(a), xs_pad))
    # print(xs)

    idx = a  # starting from 4
    last_half_recon = np.zeros(N // 2)
    output = []
    while idx + b <= len(xs_pad):
        x = xs_pad[idx - a : idx + b]
        print(x)

        mdct_x = MDCTslow(x, a, b, isInverse=False)
        x_prime = MDCTslow(mdct_x, a, b, isInverse=True)
        x_prime /= 2.0
        x_recon = last_half_recon + x_prime[: N // 2]
        last_half_recon = x_prime[N // 2 :]
        if np.allclose(x_recon, x[: N // 2], atol=1e-10):
            print("reconstruction success!")
        else:
            print("recon:", x_recon)
            print("wrong!")
        output.append(x_recon)
        idx += b
    output = np.concat(output[1:])
    assert np.allclose(output, xs, atol=1e-10)
    ### YOUR TESTING CODE ENDS HERE ###

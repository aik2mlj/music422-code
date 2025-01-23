import numpy as np
import unittest

import quantize
from my_quantize import *


class TestQuantize(unittest.TestCase):
    xs = np.array(
        [
            -0.99,
            -0.38,
            -0.10,
            -0.01,
            -0.001,
            0.0,
            0.05,
            0.28,
            0.65,
            0.97,
            1.0,
        ]
    )

    def test_quantizeUniform(self):
        for x in self.xs:
            self.assertEqual(QuantizeUniform(x, 12), quantize.QuantizeUniform(x, 12))

    def test_dequantizeUniform(self):
        for x in self.xs:
            self.assertEqual(
                DequantizeUniform(QuantizeUniform(x, 12), 12),
                quantize.DequantizeUniform(quantize.QuantizeUniform(x, 12), 12),
            )

    def test_vQuantizeUniform(self):
        np.testing.assert_equal(
            vQuantizeUniform(self.xs, 12), quantize.vQuantizeUniform(self.xs, 12)
        )

    def test_vDequantizeUniform(self):
        np.testing.assert_equal(
            vDequantizeUniform(vQuantizeUniform(self.xs, 12), 12),
            quantize.vDequantizeUniform(quantize.vQuantizeUniform(self.xs, 12), 12),
        )


if __name__ == "__main__":
    unittest.main()

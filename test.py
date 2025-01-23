import unittest

import quantize
from my_quantize import *


class TestQuantize(unittest.TestCase):
    input_series = [
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

    def test_quantizeUniform(self):
        for x in self.input_series:
            self.assertEqual(QuantizeUniform(x, 12), quantize.QuantizeUniform(x, 12))

    def test_dequantizeUniform(self):
        for x in self.input_series:
            self.assertEqual(
                DequantizeUniform(QuantizeUniform(x, 12), 12),
                quantize.DequantizeUniform(quantize.QuantizeUniform(x, 12), 12),
            )


if __name__ == "__main__":
    unittest.main()

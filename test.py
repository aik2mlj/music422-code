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

    def test_QuantizeUniform(self):
        for x in self.xs:
            self.assertEqual(QuantizeUniform(x, 12), quantize.QuantizeUniform(x, 12))

    def test_DequantizeUniform(self):
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

    def test_ScaleFactor(self):
        for x in self.xs:
            self.assertEqual(ScaleFactor(x), quantize.ScaleFactor(x))

    def test_MantissaFP(self):
        for x in self.xs:
            self.assertEqual(
                MantissaFP(x, ScaleFactor(x)),
                quantize.MantissaFP(x, quantize.ScaleFactor(x)),
            )

    def test_DequantizeFP(self):
        for x in self.xs:
            scale = ScaleFactor(x)
            mantissa = MantissaFP(x, scale)
            q_scale = quantize.ScaleFactor(x)
            q_mantissa = quantize.MantissaFP(x, q_scale)
            result = DequantizeFP(scale, mantissa)
            q_result = quantize.DequantizeFP(q_scale, q_mantissa)
            self.assertEqual(result, q_result)

    def test_Mantissa(self):
        for x in self.xs:
            self.assertEqual(
                Mantissa(x, ScaleFactor(x)),
                quantize.Mantissa(x, quantize.ScaleFactor(x)),
            )

    def test_Dequantize(self):
        for x in self.xs:
            scale = ScaleFactor(x)
            mantissa = Mantissa(x, scale)
            q_scale = quantize.ScaleFactor(x)
            q_mantissa = quantize.Mantissa(x, q_scale)
            result = Dequantize(scale, mantissa)
            q_result = quantize.Dequantize(q_scale, q_mantissa)
            self.assertEqual(result, q_result)


if __name__ == "__main__":
    unittest.main()

import unittest

from plot_roc import SensibilityInterpolator

class TestSensibilityInterpolator(unittest.TestCase):
    def test_identity(self):
        fpr = [0.1, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        tpr = [0.1, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

        i = SensibilityInterpolator(fpr, tpr);

        self.assertEqual(i.sensibility(0.3), 0.3)

    def test_square(self):
        fpr = [0.1, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        tpr = [x * 2 for x in fpr]

        i = SensibilityInterpolator(fpr, tpr)

        self.assertAlmostEqual(i.sensibility(0.3), 0.6, 2)

if __name__ == '__main__':
    unittest.main()

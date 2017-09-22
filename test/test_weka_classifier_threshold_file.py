import unittest

from plot_roc import WekaClassifierThresholdFile

class TestWekaClassifierThresholdFile(unittest.TestCase):

    def test_load_file_wth_success(self):
        threshold_file = WekaClassifierThresholdFile(file_location = "test/fixture/test.curve.arff.csv")

        fpr = threshold_file.false_positive_rate()
        tpr = threshold_file.true_positive_rate()

        self.assertEqual(len(fpr), 125)
        self.assertEqual(fpr[1], 0.982759)

        self.assertEqual(len(tpr), 125)
        self.assertEqual(tpr[123], 0.015152)

        self.assertAlmostEquals(threshold_file.aroc(), 0.923, 3)

        interpolator = threshold_file.sensibility_interpolator()
        self.assertAlmostEquals(interpolator.sensibility(0.1), 0.621, 3)
        self.assertAlmostEquals(interpolator.sensibility(0.2), 0.924, 3)

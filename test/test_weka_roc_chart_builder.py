import unittest

from plot_roc import WekaClassifierExecution
from plot_roc import WekaClassifierThresholdFile
from plot_roc import WekaROCChartBuilder

class TestWekaROCChartBuilder(unittest.TestCase):
    def test_roc_chart_creation_with_success(self):
        test_threshold_file = WekaClassifierThresholdFile(file_location = "test/fixture/test.curve.arff.csv")
        test_execution = WekaClassifierExecution(
            classifier_name = "naive-bayes-test",
            threshold_file = test_threshold_file,
            command = "java -cp ...")

        train_threshold_file = WekaClassifierThresholdFile(file_location = "test/fixture/train.curve.arff.csv")
        train_execution = WekaClassifierExecution(
            classifier_name = "naive-bayes-test",
            threshold_file = train_threshold_file,
            command = "java -cp ...")

        roc_builder = WekaROCChartBuilder(title = "ROC for test classifier")
        roc_builder.add_classifier(test_execution)
        roc_builder.add_classifier(train_execution)
        roc_builder.write_to_file(file_location = "test/result_images/naive-bayes.pdf")

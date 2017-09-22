import unittest

from plot_roc import WekaClassifierExecution
from plot_roc import WekaClassifierThresholdFile
from plot_roc import WekaClassifierBuilder

class TestWekaClassifierBuilder(unittest.TestCase):
    def test_classifier_with_success(self):
        config = {
          'name': 'Naive Bayes',
          'token': 'naive-bayes',
          'algorithm': 'weka.classifiers.bayes.NaiveBayes',
          'command-line': 'weka.classifiers.bayes.NaiveBayes'}

        build = WekaClassifierBuilder(experiment_dir = "experiments", classifier = config)

        command = build.train_command(
            weka_lib = "/usr/local/weka/weka.jar",
            train_file = "dataset-a.csv")

        self.assertEqual(command, "java -cp /usr/local/weka/weka.jar weka.Run weka.classifiers.bayes.NaiveBayes"
            + " -t dataset-a.csv -d experiments/naive-bayes/naive-bayes.model"
            + " -threshold-file experiments/naive-bayes/train.curve.arff.csv"
            + " -threshold-label G")

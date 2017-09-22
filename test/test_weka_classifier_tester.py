import unittest

from plot_roc import WekaClassifierExecution
from plot_roc import WekaClassifierThresholdFile
from plot_roc import WekaClassifierTester

class TestWekaClassifierTester(unittest.TestCase):
    def test_classifier_with_success(self):
        config = {
          'name': 'Naive Bayes',
          'token': 'naive-bayes',
          'algorithm': 'weka.classifiers.bayes.NaiveBayes',
          'command-line': 'weka.classifiers.bayes.NaiveBayes'}

        tester = WekaClassifierTester(experiment_dir = "experiments", classifier = config)

        summary_command, per_instance_command = tester.test_command(
            weka_lib = "/usr/local/weka/weka.jar",
            test_file = "dataset-b.csv")

        self.assertEqual(summary_command, "java -cp /usr/local/weka/weka.jar"
            + " weka.Run weka.classifiers.bayes.NaiveBayes"
            + " -l experiments/naive-bayes/naive-bayes.model -T dataset-b.csv")

        self.assertEqual(per_instance_command, "java -cp /usr/local/weka/weka.jar"
            + " weka.Run weka.classifiers.bayes.NaiveBayes"
            + " -l experiments/naive-bayes/naive-bayes.model -T dataset-b.csv"
            + " -classifications weka.classifiers.evaluation.output.prediction.PlainText"
            + " -threshold-file experiments/naive-bayes/test.curve.arff.csv -threshold-label G")

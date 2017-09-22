import unittest
import csv

from plot_roc import WekaClassifiersSummaryCSVWriter
from plot_roc import WekaClassifierFullExecution
from plot_roc import WekaClassifierExecution
from plot_roc import WekaClassifierThresholdFile

class TestWekaClassifiersSummaryCSVWriter(unittest.TestCase):

    def test_summarization_with_one_classifier(self):
        # Load the CSV thread file produced by Weka
        threshold_file = WekaClassifierThresholdFile(file_location = "test/fixture/test.curve.arff.csv")

        # Creates a sample of execution commands returned from the classifier
        full = WekaClassifierFullExecution(
            train = WekaClassifierExecution(classifier_name = "naive-bayes", threshold_file = threshold_file, command = "java -cp ..."),
            test = WekaClassifierExecution(classifier_name = "naive-bayes", threshold_file = threshold_file, command = "java -cp test..."))

        # Creates the summarizer specifying two points of specificity
        csvWriter = WekaClassifiersSummaryCSVWriter(specificity_points = [0.9, 0.8])
        csvWriter.add_classifier(full)

        # Get back the CSV output
        summary_file = csvWriter.get_csv()
        summary_reader = [row for row in csv.reader(summary_file.splitlines())]

        self.assertEqual(summary_reader[0], ['Classificador', 'AROC', '90%', '80%', 'Train Command', 'Test Command'])

        self.assertEqual(summary_reader[1], ['naive-bayes', '0.923', '0.621', '0.924', 'java -cp ...', 'java -cp test...'])

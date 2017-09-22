# Glaucoma Scripts

This repository includes some scripts in python to train and test classifiers
that help to predict Glaucoma based on OCT data. The scripts uses the Weka command line in the trainning process.

The choice of algorithms that are used on the default configuraiton
was based on **Silva, Fabrício R., et al. "Sensitivity and specificity of machine learning classifiers for glaucoma diagnosis using Spectral Domain OCT and standard automated perimetry." Arquivos brasileiros de oftalmologia 76.3 (2013): 170-174.**:

  - AdaBoostM1
  - Bagging
  - Ensemble Selection
  - J48
  - MLP
  - Naive Bayes
  - Random Forest
  - RBF Network
  - SVM Linear (Using LibSVM)
  - SVM Gaussian (Using LibSVM)
  - Simple Logistic
  - SMO with Polykernel
  - SMO with RBF Kernel

## Dependencies

  Some libraries are necessary to be able to run the scripts:

  - sklearn
  - numpy
  - matplotlib
  - pandas

  You can install these libraries using pip:

  ```
  pip install --user numpy scipy matplotlib pandas
  ```

## Usage

```bash
python plot-roc.py -e <experiment_name> \
  -t <train_dataset_file>
  -w <weka_jar_file> \
  -T <test_dataset_file> \
  -c 'naive-bayes'
  -s '0.9,0.8'
```

## Options

Option | Required |Default Value | Description
------------ | ------------- | ------------ | -------------
-e --experiment | [x] | | Set the name of the experiment
-t --train | [x] | | Set the trainning dataset file location
-T --test | [x] | | Set the test dataset file location
-w --weka-jar | [x] | | Set the weka jar file location
-c --classifiers | | | Set which classifiers will be executed. If not specificied, all classifiers are executed.
-s --specificity-points | | 0.9,0.8 | Set a list of specificity points to be used.

## Generated files for each classifier

At each classifier directory, some files are created as result of trainning and testing process:

File | Description
------------ | -------------
{classifier_name}.model | Model generated from the trainning process
comparison_curves.pdf | Both trainning and testing ROC plot
train.curve.arff.csv | Threshold values generated from train dataset
test.curve.arff.csv | Threshold values generated from test dataset
train.statistics.txt | File with the statistic results from train process
test.statistics.txt | File with the statistic results from test process
train.roc.pdf | ROC curve plot generated from train dataset
test.roc.pdf | ROC curve plot generated from test dataset

## Generated files grouping all classifiers

At the root of experiment directory, other files are created to save a comparison between the classifiers.

File | Description
------------ | -------------
train_all_curves.pdf | Plot of all ROC curves generated in trainning process
test_all_curves.pdf | Plot of all ROC curves generated in test process
train_aroc.csv | Area from ROC, Sensibilities and Weka command used for train process
test_aroc.csv | Area from ROC, Sensibilities and Weka command used for testing process

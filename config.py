# Set the default interpolation kind
# Possible values: 'linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic'
interpolation_kind = 'linear'

# Specify a list of values to be used as specificity when calculating sensibilities
specificities_points = [0.9, 0.8]

# List of classifiers that could be used and their parameters
classifiers = [
    { 'name': 'AdaBoostM1',
      'token': 'adaboost-m1',
      'algorithm': 'weka.classifiers.meta.AdaBoostM1',
      'command-line': 'weka.classifiers.meta.AdaBoostM1 -P 100 -S 1 -I 10 -W weka.classifiers.trees.DecisionStump'},

    { 'name': 'Bagging',
      'token': 'bagging',
      'algorithm': 'weka.classifiers.meta.Bagging',
      'command-line': 'weka.classifiers.meta.Bagging -P 100 -S 1 -num-slots 1 -I 10 -W weka.classifiers.trees.REPTree',
      'meta': '-- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0'},

    { 'name': 'Ensemble Selection',
      'token': 'ensemble-selection',
      'algorithm': 'weka.classifiers.meta.EnsembleSelection',
      'command-line': 'weka.classifiers.meta.EnsembleSelection -W ./model_data/ -P rmse -A forward -B 10 -V 0.25 -E 0.5 -H 100 -I 1.0 -X 1 -R -G -S 1'},

    { 'name': 'J48',
      'token': 'j48',
      'algorithm': 'weka.classifiers.trees.J48',
      'command-line': 'weka.classifiers.trees.J48 -C 0.25 -M 2'},

    { 'name': 'MLP',
      'token': 'mlp',
      'algorithm': 'weka.classifiers.functions.MultilayerPerceptron',
      'command-line': 'weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0 -E 20 -H a'},

    { 'name': 'Naive Bayes',
      'token': 'naive-bayes',
      'algorithm': 'weka.classifiers.bayes.NaiveBayes',
      'command-line': 'weka.classifiers.bayes.NaiveBayes'},

    { 'name': 'Random Forest',
      'token': 'random-forest',
      'algorithm': 'weka.classifiers.trees.RandomForest',
      'command-line': 'weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1'},

    { 'name': 'RBF Network',
      'token': 'rbf-network',
      'algorithm': 'weka.classifiers.functions.RBFNetwork',
      'command-line': 'weka.classifiers.functions.RBFNetwork -B 2 -S 1 -R 1.0E-8 -M -1 -W 0.1'},

    { 'name': 'SVM Linear',
      'token': 'libsvm-linear',
      'algorithm': 'weka.classifiers.functions.LibSVM',
      'command-line': 'weka.classifiers.functions.LibSVM -S 0 -K 0 -D 3 -G 0.0 -R 0.0 -N 0.5 -M 40.0 -C 1.0 -E 0.001 -P 0.1 -B -Z -model ./model_data/ -seed 1'},

    { 'name': 'SVM Gaussian',
      'token': 'libsvm-gaussian',
      'algorithm': 'weka.classifiers.functions.LibSVM',
      'command-line': 'weka.classifiers.functions.LibSVM -S 0 -K 2 -D 3 -G 0.0 -R 0.0 -N 0.5 -M 40.0 -C 1.0 -E 0.001 -P 0.1 -B -Z -model ./model_data/ -seed 1' },

    { 'name': 'Simple Logistic',
      'token': 'simple-logistic',
      'algorithm': 'weka.classifiers.functions.SimpleLogistic',
      'command-line': 'weka.classifiers.functions.SimpleLogistic -I 5 -M 500 -H 100 -W 0.0 -A'},

    { 'name': 'SMO Polykernel',
      'token': 'smo-polykernel',
      'algorithm': 'weka.classifiers.functions.SMO',
      'command-line': 'weka.classifiers.functions.SMO -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -M -V -1 -W 1 -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007" -calibrator "weka.classifiers.functions.Logistic -C -R 1.0E-8 -M -1 -num-decimal-places 4"'},

    { 'name': 'SMO RBF Kernel',
      'token': 'smo-rbfkernel',
      'algorithm': 'weka.classifiers.functions.SMO',
      'command-line': 'weka.classifiers.functions.SMO -C 500.0 -L 0.001 -P 1.0E-12 -N 1 -M -V -1 -W 1 -K "weka.classifiers.functions.supportVector.RBFKernel -G 0.001 -C 250007" -calibrator "weka.classifiers.functions.Logistic -R 1.0E-8 -M -1 -num-decimal-places 4"'}]

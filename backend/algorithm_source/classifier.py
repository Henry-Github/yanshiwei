from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from typing import List

names = [
    'LogisticRegression',
    'RidgeClassifier',
    'SGDClassifier',
    'PassiveAggressiveClassifier',
    'KNeighborsClassifier',
    'DecisionTreeClassifier',
    'ExtraTreeClassifier',
    'SVC',
    'GaussianNB',
    'AdaBoostClassifier',
    'BaggingClassifier',
    'RandomForestClassifier',
    'ExtraTreesClassifier',
    'GradientBoostingClassifier'
]


# create a dict of standard models to evaluate {name:object}
def define_models(methods=List):
    models = dict()
    # linear models
    if 'LogisticRegression' in methods:
        models['logistic'] = LogisticRegression()
    if 'RidgeClassifier' in methods:
        alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        for a in alpha:
            models['ridge-' + str(a)] = RidgeClassifier(alpha=a)
    if 'SGDClassifier' in methods:
        models['sgd'] = SGDClassifier(max_iter=1000, tol=1e-3)
    if 'PassiveAggressiveClassifier' in methods:
        models['pa'] = PassiveAggressiveClassifier(max_iter=1000, tol=1e-3)
    # non-linear models
    if 'KNeighborsClassifier' in methods:
        n_neighbors = range(1, 21)
        for k in n_neighbors:
            models['knn-' + str(k)] = KNeighborsClassifier(n_neighbors=k)
    if 'DecisionTreeClassifier' in methods:
        models['cart'] = DecisionTreeClassifier()
    if 'ExtraTreeClassifier' in methods:
        models['extra'] = ExtraTreeClassifier()
    if 'SVC' in methods:
        models['svml'] = SVC(kernel='linear')
        models['svmp'] = SVC(kernel='poly')
        c_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        for c in c_values:
            models['svmr' + str(c)] = SVC(C=c)
    if 'GaussianNB' in models:
        models['bayes'] = GaussianNB()
    # ensemble models
    n_trees = 100
    if 'AdaBoostClassifier' in methods:
        models['ada'] = AdaBoostClassifier(n_estimators=n_trees)
    if 'BaggingClassifier' in methods:
        models['bag'] = BaggingClassifier(n_estimators=n_trees)
    if 'RandomForestClassifier' in methods:
        models['rf'] = RandomForestClassifier(n_estimators=n_trees)
    if 'ExtraTreesClassifier' in methods:
        models['et'] = ExtraTreesClassifier(n_estimators=n_trees)
    if 'GradientBoostingClassifier' in methods:
        models['gbm'] = GradientBoostingClassifier(n_estimators=n_trees)
    print('Defined %d models' % len(models))
    return models

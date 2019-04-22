# binary classification spot check script
import warnings
from numpy import mean
from numpy import std
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
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
import json


# load the dataset, returns X and y elements
def load_dataset():
    return make_classification(n_samples=1000, n_classes=2, random_state=1)


# create a dict of standard models to evaluate {name:object}
def define_models(models=dict()):
    # linear models
    models['logistic'] = LogisticRegression()
    alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for a in alpha:
        models['ridge-' + str(a)] = RidgeClassifier(alpha=a)
    models['sgd'] = SGDClassifier(max_iter=1000, tol=1e-3)
    models['pa'] = PassiveAggressiveClassifier(max_iter=1000, tol=1e-3)
    # non-linear models
    n_neighbors = range(1, 21)
    for k in n_neighbors:
        models['knn-' + str(k)] = KNeighborsClassifier(n_neighbors=k)
    models['cart'] = DecisionTreeClassifier()
    models['extra'] = ExtraTreeClassifier()
    models['svml'] = SVC(kernel='linear')
    models['svmp'] = SVC(kernel='poly')
    c_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for c in c_values:
        models['svmr' + str(c)] = SVC(C=c)
    models['bayes'] = GaussianNB()
    # ensemble models
    n_trees = 100
    models['ada'] = AdaBoostClassifier(n_estimators=n_trees)
    models['bag'] = BaggingClassifier(n_estimators=n_trees)
    models['rf'] = RandomForestClassifier(n_estimators=n_trees)
    models['et'] = ExtraTreesClassifier(n_estimators=n_trees)
    models['gbm'] = GradientBoostingClassifier(n_estimators=n_trees)
    print('Defined %d models' % len(models))
    return models


# create a feature preparation pipeline for a model
def make_pipeline(model):
    steps = list()
    # standardization
    steps.append(('standardize', StandardScaler()))
    # normalization
    steps.append(('normalize', MinMaxScaler()))
    # the model
    steps.append(('model', model))
    # create pipeline
    pipeline = Pipeline(steps=steps)
    return pipeline


# evaluate a single model
def evaluate_model(X, y, model, folds, metric):
    # create the pipeline
    pipeline = make_pipeline(model)
    # evaluate model
    scores = cross_val_score(pipeline, X, y, scoring=metric, cv=folds, n_jobs=-1)
    return scores


# evaluate a model and try to trap errors and and hide warnings
def robust_evaluate_model(X, y, model, folds, metric):
    scores = None
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            scores = evaluate_model(X, y, model, folds, metric)
    except:
        scores = None
    return scores


# evaluate a dict of models {name:object}, returns {name:score}
def evaluate_models(X, y, models, folds=10, metric='accuracy'):
    results = dict()
    for name, model in models.items():
        # evaluate the model
        scores = robust_evaluate_model(X, y, model, folds, metric)
        # show process
        if scores is not None:
            # store a result
            results[name] = scores
            mean_score, std_score = mean(scores), std(scores)
            # print('>%s: %.3f (+/-%.3f)' % (name, mean_score, std_score))
        else:
            # print('>%s: error' % name)
            pass
    return results


# print and plot the top n results
def summarize_results(results, maximize=True, top_n=10):
    # check for no results
    if len(results) == 0:
        print('no results')
        return
    # determine how many results to summarize
    n = min(top_n, len(results))
    # create a list of (name, mean(scores)) tuples
    mean_scores = [(k, mean(v)) for k, v in results.items()]
    # sort tuples by mean score
    mean_scores = sorted(mean_scores, key=lambda x: x[1])
    # reverse for descending order (e.g. for accuracy)
    if maximize:
        mean_scores = list(reversed(mean_scores))
    # retrieve the top n for summarization
    names = [x[0] for x in mean_scores[:n]]
    scores = [results[x[0]] for x in mean_scores[:n]]
    d = []
    for k in scores:
       d.append(k.tolist())
    print(d)

    # # print the top n
    # for i in range(n):
    #     name = names[i]
    #     mean_score, std_score = mean(results[name]), std(results[name])
    #     print('Rank=%d, Name=%s, Score=%.3f (+/- %.3f)' % (i + 1, name, mean_score, std_score))
    # # boxplot for the top n
    # pyplot.boxplot(scores, labels=names)
    # _, labels = pyplot.xticks()
    # pyplot.setp(labels, rotation=90)
    # # pyplot.savefig('spotcheck.png')


if __name__ == '__main__':
    # load dataset
    X, y = load_dataset()
    # get model list
    models = define_models()
    # evaluate models
    results = evaluate_models(X, y, models)
    # summarize results
    summarize_results(results)
    # s = [array([0.86138614, 0.88, 0.97, 0.8, 0.85, 0.84, 0.86, 0.87, 0.82, 0.90909091]),
    #      array([0.86138614, 0.88, 0.95, 0.83, 0.86, 0.84, 0.79, 0.86, 0.86, 0.87878788]),
    #      array([0.87128713, 0.87, 0.94, 0.84, 0.85,0.83, 0.8, 0.86, 0.84, 0.88888889]),
    #      array([0.86138614, 0.85, 0.95, 0.84, 0.85,0.85, 0.83, 0.87, 0.83, 0.85858586]),
    #      array([0.83168317, 0.86, 0.94, 0.81, 0.85,0.85, 0.87, 0.82, 0.83, 0.83838384]),
    #      array([0.84158416, 0.9, 0.93, 0.81, 0.8,0.82, 0.83, 0.84, 0.86, 0.84848485]),
    #      array([0.84158416, 0.9, 0.93, 0.81, 0.8,0.82, 0.83, 0.84, 0.86, 0.84848485]),
    #      array([0.84158416, 0.9, 0.93, 0.81, 0.8, 0.82, 0.83, 0.84, 0.86, 0.84848485]),
    #      array([0.84158416, 0.9, 0.93, 0.81, 0.8,0.82, 0.83, 0.84, 0.86, 0.84848485]),
    #      array([0.84158416, 0.9, 0.93, 0.81, 0.8,0.82, 0.83, 0.84, 0.86, 0.84848485])]

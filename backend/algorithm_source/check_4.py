# 三次重复模型评估的二进制分类
# binary classification spot check script
import warnings
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from .classifier import define_models
from .utils import summarize_results
from typing import List


# load the dataset, returns X and y elements
def load_dataset():
    return make_classification(n_samples=1000, n_classes=2, random_state=1)


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
def evaluate_model(X, y, model, folds, repeats, metric):
    # create the pipeline
    pipeline = make_pipeline(model)
    # evaluate model
    scores = list()
    # repeat model evaluation n times
    for _ in range(repeats):
        # perform run
        scores_r = cross_val_score(pipeline, X, y, scoring=metric, cv=folds, n_jobs=-1)
        # add scores to list
        scores += scores_r.tolist()
    return scores


# evaluate a model and try to trap errors and hide warnings
def robust_evaluate_model(X, y, model, folds, repeats, metric):
    scores = None
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            scores = evaluate_model(X, y, model, folds, repeats, metric)
    except:
        scores = None
    return scores


# evaluate a dict of models {name:object}, returns {name:score}
def evaluate_models(X, y, models, folds=10, repeats=3, metric='accuracy'):
    results = dict()
    for name, model in models.items():
        # evaluate the model
        scores = robust_evaluate_model(X, y, model, folds, repeats, metric)
        # show process
        if scores is not None:
            # store a result
            results[name] = scores
            mean_score, std_score = mean(scores), std(scores)
            print('>%s: %.3f (+/-%.3f)' % (name, mean_score, std_score))
        else:
            print('>%s: error' % name)
    return results


def run(methods=List):
    # load dataset
    X, y = load_dataset()
    # get model list
    models = define_models(methods)
    # evaluate models
    results = evaluate_models(X, y, models)
    # summarize results
    return summarize_results(results)
